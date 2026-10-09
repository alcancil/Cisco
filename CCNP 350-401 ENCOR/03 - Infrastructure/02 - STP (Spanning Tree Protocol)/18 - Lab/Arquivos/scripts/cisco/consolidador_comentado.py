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
"""  # fecha a docstring do modulo, que documenta fontes de dados e limitacoes conhecidas

import json               # importa o modulo usado para ler os arquivos .json parseados
import re                 # importa o modulo de expressoes regulares, usado para normalizar o identificador de VLAN
from pathlib import Path  # importa Path, usado nas assinaturas de tipo dos caminhos de arquivo

from output_writer import PARSED_OUTPUT_DIR, nome_arquivo_parsed  # importa a pasta dos JSON parseados e a funcao que monta o nome do arquivo de cada comando


def _carregar_json(hostname: str, comando: str) -> list[dict]:             # define a funcao que le o .json parseado de um comando especifico de um dispositivo
    """
    Le o arquivo .json parseado de um comando especifico para um dispositivo.
    Retorna lista vazia se o arquivo nao existir (comando nao coletado
    para este dispositivo), em vez de lancar erro.
    """                                                                    # fecha a docstring da funcao, explicando o comportamento em caso de arquivo ausente
    caminho = PARSED_OUTPUT_DIR / hostname / nome_arquivo_parsed(comando)  # monta o caminho completo do arquivo .json esperado para esse comando e hostname
    if not caminho.exists():                                               # verifica se o arquivo realmente existe em disco
        return []                                                          # retorna lista vazia em vez de erro, caso o comando nao tenha sido coletado para este switch

    with open(caminho, "r", encoding="utf-8") as arquivo:  # abre o arquivo .json encontrado para leitura
        return json.load(arquivo)                          # le e converte o conteudo JSON em lista de dicionarios Python


def _normalizar_vlan(valor) -> str:              # define a funcao que padroniza o identificador de VLAN vindo de fontes diferentes
    """
    Normaliza o identificador de VLAN para permitir cruzar dados vindos de
    templates diferentes: "show spanning-tree" retorna so o numero
    (ex: "1"), enquanto "show spanning-tree root" retorna o token completo
    da CLI (ex: "VLAN0001"). Aqui os dois viram a mesma coisa: string
    numerica sem zeros a esquerda.
    """                                          # fecha a docstring da funcao, explicando por que a normalizacao e necessaria
    digitos = re.sub(r"\D", "", str(valor))      # remove tudo que nao for digito, restando so os numeros (ex: "VLAN0001" -> "0001")
    return str(int(digitos)) if digitos else ""  # converte para inteiro e de volta para string, eliminando zeros a esquerda; retorna vazio se nao houver digitos


def _indexar_por_vlan(registros: list[dict], campo_vlan: str) -> dict:  # define a funcao que transforma uma lista de registros num dicionario indexado por VLAN
    """
    Transforma uma lista de registros em um dicionario {vlan_normalizada:
    registro}, para permitir busca rapida ao consolidar. Assume um
    registro por VLAN (correto para show spanning-tree root).
    """                                                                 # fecha a docstring da funcao, explicando o formato do dicionario retornado
    return {                                                            # inicia a construcao do dicionario via compreensao
        _normalizar_vlan(registro[campo_vlan]): registro                # usa a VLAN normalizada como chave e o registro inteiro como valor
        for registro in registros                                       # percorre cada registro da lista recebida
        if registro.get(campo_vlan)                                     # ignora registros que nao tenham o campo de VLAN preenchido
    }                                                                   # fecha a compreensao de dicionario


def _indexar_por_interface(registros: list[dict], campo_interface: str) -> dict:  # define a funcao que transforma uma lista de registros num dicionario indexado por interface
    """
    Transforma uma lista de registros em um dicionario {interface:
    registro}, usado para cruzar dados de show interfaces trunk pela porta.
    Quando ha mais de um registro para a mesma interface (ex: modo +
    vlans permitidas), o ultimo registro sobrescreve o anterior -- por
    isso mesclamos os dois tipos de registro antes de indexar.
    """                                                                           # fecha a docstring da funcao, explicando a estrategia de mesclagem
    indice = {}                                                                   # cria o dicionario vazio que vai acumular os registros mesclados por interface
    for registro in registros:                                                    # percorre cada registro da lista recebida
        interface = registro.get(campo_interface)                                 # extrai o valor da interface deste registro
        if not interface:                                                         # verifica se o registro realmente tem uma interface identificada
            continue                                                              # pula para o proximo registro se nao houver interface, sem adicionar nada ao indice
        # Mescla com o que ja existir para essa interface, em vez de
        # sobrescrever -- assim o registro de "modo" e o de "vlans
        # permitidas" (dois registros separados para a mesma porta,
        # vindos do template customizado) se combinam num so.
        indice.setdefault(interface, {}).update(                                  # garante uma entrada para essa interface no indice e atualiza seus campos
            {chave: valor for chave, valor in registro.items() if valor}          # monta um dicionario so com os campos que tem valor de fato, ignorando os vazios
        )                                                                         # fecha a chamada de update, completando a mesclagem deste registro
    return indice                                                                 # retorna o dicionario final, com um registro combinado por interface


def consolidar_dispositivo(hostname: str) -> list[dict]:  # define a funcao que monta as linhas consolidadas de um unico switch
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
    """                                                                            # fecha a docstring da funcao, alertando sobre a diferenca de maiusculas/minusculas entre fontes
    interfaces_stp = _carregar_json(hostname, "show spanning-tree")                # carrega os registros de role/state por interface e por VLAN, a base da tabela
    root_por_vlan = _indexar_por_vlan(                                             # inicia o carregamento e indexacao dos dados de root bridge por VLAN
        _carregar_json(hostname, "show spanning-tree root"), campo_vlan="vlan_id"  # carrega o show spanning-tree root e indexa pelo campo vlan_id
    )                                                                              # fecha a chamada de _indexar_por_vlan
    cpu_registros = _carregar_json(hostname, "show processes cpu")                 # carrega a lista de processos com a utilizacao de CPU do switch
    trunk_por_interface = _indexar_por_interface(                                  # inicia o carregamento e indexacao dos dados de trunk por interface
        _carregar_json(hostname, "show interfaces trunk"), campo_interface="PORT"  # carrega o show interfaces trunk e indexa pelo campo PORT
    )                                                                              # fecha a chamada de _indexar_por_interface

    # CPU vem repetido em cada processo listado no comando (Filldown) --
    # todos os registros trazem o mesmo valor global, entao basta o primeiro.
    cpu = cpu_registros[0].get("cpu_usage_5_min", "") if cpu_registros else ""  # pega o valor de CPU do primeiro registro, ou string vazia se nao houver nenhum

    linhas = []                                                                     # cria a lista vazia que vai acumular todas as linhas consolidadas deste switch
    for interface_registro in interfaces_stp:                                       # percorre cada combinacao de VLAN + interface vinda do show spanning-tree
        vlan_normalizada = _normalizar_vlan(interface_registro.get("vlan_id", ""))  # normaliza a VLAN deste registro para poder cruzar com o indice de root bridge
        interface = interface_registro.get("interface", "")                         # extrai o nome da interface deste registro
        root = root_por_vlan.get(vlan_normalizada, {})                              # busca os dados de root bridge desta VLAN; dicionario vazio se nao encontrar
        trunk = trunk_por_interface.get(interface, {})                              # busca os dados de trunk desta interface; dicionario vazio se nao encontrar

        linhas.append({                                               # adiciona uma nova linha consolidada a lista, com todos os campos combinados
            "Switch": hostname,                                       # grava o hostname do switch nesta linha
            "VLAN": vlan_normalizada,                                 # grava a VLAN ja normalizada
            "Interface": interface,                                   # grava a interface participante desta instancia PVST+
            "Role": interface_registro.get("role", ""),               # grava o papel da porta (Root, Desg, Altn, etc.)
            "State": interface_registro.get("status", ""),            # grava o estado operacional da porta (FWD, BLK, etc.)
            "Root Bridge": root.get("root_id", ""),                   # grava o MAC do root bridge desta VLAN, vindo do show spanning-tree root
            "Root Port": root.get("root_port", ""),                   # grava a porta raiz desta VLAN
            "Root Cost": root.get("root_cost", ""),                   # grava o custo acumulado ate o root bridge
            "Priority": root.get("priority", ""),                     # grava a prioridade do root bridge desta VLAN
            "CPU": cpu,                                               # grava a utilizacao de CPU do switch, repetida em todas as linhas dele
            "Trunk (Vlans Allowed)": trunk.get("VLANS_ALLOWED", ""),  # grava as VLANs permitidas no trunk, quando esta interface for uma delas
        })                                                            # fecha o dicionario da linha e a chamada de append

    return linhas  # retorna todas as linhas consolidadas deste switch


def consolidar_topologia(hostnames: list[str]) -> list[dict]:     # define a funcao que consolida todos os switches da topologia de uma vez
    """
    Percorre todos os hostnames informados e junta as linhas consolidadas
    de cada um em uma unica lista, representando toda a topologia.
    """                                                           # fecha a docstring da funcao, explicando seu proposito
    todas_as_linhas = []                                          # cria a lista vazia que vai acumular as linhas de todos os switches
    for hostname in hostnames:                                    # percorre cada hostname informado
        todas_as_linhas.extend(consolidar_dispositivo(hostname))  # consolida este switch e adiciona suas linhas a lista geral
    return todas_as_linhas                                        # retorna a lista completa, representando toda a topologia consolidada
