"""
arvore_stp.py

Constroi, a partir da tabela consolidada (PVST+ + CDP), um grafo NetworkX
representando a arvore STP de uma VLAN especifica.

Decisoes de design (definidas em conversa antes de implementar):
    1. Deduplicacao de aresta: cada link fisico e identificado pelo par de
       pontas (switch, interface normalizada) dos dois lados -- evita
       contar o mesmo link duas vezes (CDP reporta cada lado separado).
    2. Um link e considerado bloqueado se QUALQUER um dos dois lados
       reportar Role=Altn ou State != FWD naquela VLAN.
    3. O switch Root de uma VLAN e aquele que NAO possui nenhuma porta
       com Role == "Root" (o Root Bridge nunca tem porta Root, so Desg).
    4. O campo "Neighbor" traz o hostname com sufixo de dominio
       (ex: "SW_DST01.cisco.com") -- normalizado removendo tudo a partir
       do primeiro ponto, para bater com a coluna "Switch".
    5. Usamos MultiGraph, pois a topologia tem links paralelos confirmados
       entre pelo menos um par de switches.
"""

import re

import networkx as nx
import pandas as pd


def _normalizar_interface(valor) -> str:
    """
    Extrai so a parte numerica (slot/porta) do nome da interface, para
    comparar "Gi0/1" (forma abreviada) com "GigabitEthernet0/1" (forma
    por extenso usada pelo CDP) como sendo a mesma porta.
    """
    correspondencia = re.search(r"(\d+(?:/\d+)*)$", str(valor).strip())
    return correspondencia.group(1) if correspondencia else str(valor).strip()


def _normalizar_hostname_vizinho(valor) -> str:
    """
    Remove o sufixo de dominio do nome do vizinho reportado pelo CDP
    (ex: "SW_DST01.cisco.com" -> "SW_DST01"), para bater com o nome
    usado na coluna "Switch" do restante da tabela.
    """
    return str(valor).split(".")[0]


def _esta_bloqueado(role: str, state: str) -> bool:
    """
    Define se uma porta, do ponto de vista de um lado do link, esta
    bloqueada para a VLAN em questao.
    """
    role = str(role).strip()
    state = str(state).strip().upper()
    return role == "Altn" or state != "FWD"


def _identificar_root_bridge(linhas_vlan: pd.DataFrame) -> str:
    """
    Identifica qual switch e o Root Bridge desta VLAN: e o unico switch,
    entre os presentes, que nao possui nenhuma porta com Role == "Root".
    """
    switches = linhas_vlan["Switch"].unique()
    tem_porta_root = set(linhas_vlan.loc[linhas_vlan["Role"] == "Root", "Switch"].unique())
    candidatos = [switch for switch in switches if switch not in tem_porta_root]
    return candidatos[0] if candidatos else ""


def construir_arvore(tabela: pd.DataFrame, vlan) -> nx.MultiGraph:
    """
    Constroi o grafo da arvore STP de uma VLAN especifica, a partir da
    tabela consolidada (PVST+ + CDP).

    Args:
        tabela (pd.DataFrame): tabela consolidada, ja carregada (ver
                                script_05_reconstrucao_arvore.py).
        vlan: identificador da VLAN (aceita int ou str).

    Returns:
        nx.MultiGraph: nos = switches (com atributos "root": bool e "cost": str),
                        arestas = links fisicos entre switches
                        participantes desta VLAN, com atributos
                        "vlan", "bloqueado" e "detalhes".
    """
    vlan_normalizada = str(int(vlan))
    linhas_vlan = tabela[tabela["VLAN"].astype(str) == vlan_normalizada].copy()

    root_bridge = _identificar_root_bridge(linhas_vlan)

    grafo = nx.MultiGraph()
    
    # Adiciona os nós com o atributo de custo (Root Cost) extraído da tabela
    switches = linhas_vlan["Switch"].unique()
    for switch in switches:
        dados_switch = linhas_vlan[linhas_vlan["Switch"] == switch].iloc[0]
        custo = dados_switch.get("Root Cost", "")
        grafo.add_node(switch, root=(switch == root_bridge), cost=custo)

    vizinho_preenchido = linhas_vlan["Neighbor"].fillna("").astype(str) != ""
    linhas_com_vizinho = linhas_vlan[vizinho_preenchido]

    enlaces = {}
    for _, linha in linhas_com_vizinho.iterrows():
        switch_local = linha["Switch"]
        vizinho = _normalizar_hostname_vizinho(linha["Neighbor"])
        ponta_local = (switch_local, _normalizar_interface(linha["Interface"]))
        ponta_remota = (vizinho, _normalizar_interface(linha["Neighbor Interface"]))
        chave = frozenset({ponta_local, ponta_remota})

        enlaces.setdefault(chave, {"pontas": (ponta_local, ponta_remota), "lados": []})
        enlaces[chave]["lados"].append({
            "switch": switch_local,
            "interface": linha["Interface"],
            "role": linha["Role"],
            "state": linha["State"],
        })

    for chave, dado in enlaces.items():
        (switch_a, _), (switch_b, _) = dado["pontas"]
        bloqueado = any(_esta_bloqueado(lado["role"], lado["state"]) for lado in dado["lados"])
        grafo.add_edge(
            switch_a, switch_b,
            vlan=vlan_normalizada,
            bloqueado=bloqueado,
            detalhes=dado["lados"],
        )

    return grafo