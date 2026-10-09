"""
consolidador.py

Junta os registros estruturados (JSON) gerados pelo Script 03 em uma unica
tabela (lista de dicionarios), com granularidade
switch + VLAN + interface -- uma linha por porta participante de uma
instancia PVST+.

Fontes usadas por linha:
    - show spanning-tree      -> VLAN, Interface, Role, State (base da tabela)
    - show spanning-tree root -> Root Bridge, Root Port, Root Cost, Priority (por VLAN)
    - show processes cpu      -> CPU (por switch, repetido em todas as linhas)
    - show interfaces trunk   -> Vlans permitidas no trunk (por interface, quando aplicavel)

Bridge Priority, Bridge MAC (do proprio switch), Designated Bridge e
Designated Port ainda NAO estao disponiveis -- exigiriam um template
customizado para "show spanning-tree detail", que ainda nao foi criado.
Ficam de fora da tabela por enquanto.
"""

import json
import re
from pathlib import Path

from output_writer import PARSED_OUTPUT_DIR, nome_arquivo_parsed


def _carregar_json(hostname: str, comando: str) -> list[dict]:
    """
    Le o arquivo .json parseado de um comando especifico para um dispositivo.
    Retorna lista vazia se o arquivo nao existir (comando nao coletado
    para este dispositivo), em vez de lancar erro.
    """
    caminho = PARSED_OUTPUT_DIR / hostname / nome_arquivo_parsed(comando)
    if not caminho.exists():
        return []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def _normalizar_vlan(valor) -> str:
    """
    Normaliza o identificador de VLAN para permitir cruzar dados vindos de
    templates diferentes: "show spanning-tree" retorna so o numero
    (ex: "1"), enquanto "show spanning-tree root" retorna o token completo
    da CLI (ex: "VLAN0001"). Aqui os dois viram a mesma coisa: string
    numerica sem zeros a esquerda.
    """
    digitos = re.sub(r"\D", "", str(valor))
    return str(int(digitos)) if digitos else ""


def _normalizar_interface(valor) -> str:
    """
    Normaliza o nome da interface para permitir cruzar dados vindos de
    fontes diferentes: "show spanning-tree" usa a forma abreviada
    (ex: "Gi0/1"), enquanto "show cdp neighbors detail" usa o nome por
    extenso (ex: "GigabitEthernet0/1"). Aqui os dois viram a mesma coisa:
    so a parte numerica (slot/porta), sem o prefixo do tipo de interface.
    """
    correspondencia = re.search(r"(\d+(?:/\d+)*)$", str(valor).strip())
    return correspondencia.group(1) if correspondencia else str(valor).strip()


def _indexar_por_vlan(registros: list[dict], campo_vlan: str) -> dict:
    """
    Transforma uma lista de registros em um dicionario {vlan_normalizada:
    registro}, para permitir busca rapida ao consolidar. Assume um
    registro por VLAN (correto para show spanning-tree root).
    """
    return {
        _normalizar_vlan(registro[campo_vlan]): registro
        for registro in registros
        if registro.get(campo_vlan)
    }


def _indexar_por_interface(registros: list[dict], campo_interface: str) -> dict:
    """
    Transforma uma lista de registros em um dicionario {interface:
    registro}, usado para cruzar dados de show interfaces trunk pela porta.
    Quando ha mais de um registro para a mesma interface (ex: modo +
    vlans permitidas), o ultimo registro sobrescreve o anterior -- por
    isso mesclamos os dois tipos de registro antes de indexar.
    """
    indice = {}
    for registro in registros:
        interface = registro.get(campo_interface)
        if not interface:
            continue
        # Mescla com o que ja existir para essa interface, em vez de
        # sobrescrever -- assim o registro de "modo" e o de "vlans
        # permitidas" (dois registros separados para a mesma porta,
        # vindos do template customizado) se combinam num so.
        indice.setdefault(interface, {}).update(
            {chave: valor for chave, valor in registro.items() if valor}
        )
    return indice


def _indexar_cdp_por_interface(registros: list[dict]) -> dict:
    """
    Transforma a lista de vizinhos CDP em um dicionario
    {interface_local_normalizada: registro}, para cruzar com a interface
    de cada linha da tabela. Usa a interface normalizada (so o numero de
    slot/porta) como chave, ja que o CDP traz o nome por extenso
    (GigabitEthernet0/1) e o restante da tabela usa a forma abreviada
    (Gi0/1).
    """
    return {
        _normalizar_interface(registro["local_interface"]): registro
        for registro in registros
        if registro.get("local_interface")
    }


def consolidar_dispositivo(hostname: str) -> list[dict]:
    """
    Monta as linhas consolidadas de um unico switch, uma linha por
    combinacao VLAN + interface participante do PVST+.

    Observacao sobre maiusculas/minusculas: comandos que passam pelo
    NTC-Templates oficial (parse_output) tem as chaves normalizadas para
    minusculo (ex: "vlan_id"). Os templates customizados que escrevemos
    a mao (trunk) preservam o nome exato definido no .textfsm, em
    maiusculo (ex: "PORT"). Por isso as duas fontes abaixo usam
    convencoes diferentes -- nao e inconsistencia nossa, e assim que
    cada caminho de codigo devolve o dado.
    """
    interfaces_stp = _carregar_json(hostname, "show spanning-tree")
    root_por_vlan = _indexar_por_vlan(
        _carregar_json(hostname, "show spanning-tree root"), campo_vlan="vlan_id"
    )
    cpu_registros = _carregar_json(hostname, "show processes cpu")
    trunk_por_interface = _indexar_por_interface(
        _carregar_json(hostname, "show interfaces trunk"), campo_interface="PORT"
    )
    cdp_por_interface = _indexar_cdp_por_interface(
        _carregar_json(hostname, "show cdp neighbors detail")
    )

    # CPU vem repetido em cada processo listado no comando (Filldown) --
    # todos os registros trazem o mesmo valor global, entao basta o primeiro.
    cpu = cpu_registros[0].get("cpu_usage_5_min", "") if cpu_registros else ""

    linhas = []
    for interface_registro in interfaces_stp:
        vlan_normalizada = _normalizar_vlan(interface_registro.get("vlan_id", ""))
        interface = interface_registro.get("interface", "")
        root = root_por_vlan.get(vlan_normalizada, {})
        trunk = trunk_por_interface.get(interface, {})
        cdp = cdp_por_interface.get(_normalizar_interface(interface), {})

        linhas.append({
            "Switch": hostname,
            "VLAN": vlan_normalizada,
            "Interface": interface,
            "Role": interface_registro.get("role", ""),
            "State": interface_registro.get("status", ""),
            "Root Bridge": root.get("root_id", ""),
            "Root Port": root.get("root_port", ""),
            "Root Cost": root.get("root_cost", ""),
            "Priority": root.get("priority", ""),
            "CPU": cpu,
            "Trunk (Vlans Allowed)": trunk.get("VLANS_ALLOWED", ""),
            "Neighbor": cdp.get("neighbor_name", ""),
            "Neighbor Interface": cdp.get("neighbor_interface", ""),
        })

    return linhas


def consolidar_topologia(hostnames: list[str]) -> list[dict]:
    """
    Percorre todos os hostnames informados e junta as linhas consolidadas
    de cada um em uma unica lista, representando toda a topologia.
    """
    todas_as_linhas = []
    for hostname in hostnames:
        todas_as_linhas.extend(consolidar_dispositivo(hostname))
    return todas_as_linhas
