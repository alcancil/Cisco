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
"""  # fecha a docstring do modulo, que documenta as 5 decisoes de design

import re  # importa o modulo de expressoes regulares, usado para normalizar interfaces

import networkx as nx  # importa o NetworkX, usado para representar o grafo da arvore STP
import pandas as pd    # importa o Pandas, usado para tipagem e filtragem da tabela consolidada


def _normalizar_interface(valor) -> str:                                        # define a funcao que padroniza o nome de uma interface
    """
    Extrai so a parte numerica (slot/porta) do nome da interface, para
    comparar "Gi0/1" (forma abreviada) com "GigabitEthernet0/1" (forma
    por extenso usada pelo CDP) como sendo a mesma porta.
    """                                                                         # fecha a docstring da funcao, explicando o proposito da normalizacao
    correspondencia = re.search(r"(\d+(?:/\d+)*)$", str(valor).strip())         # procura o padrao numerico de slot/porta no final da string
    return correspondencia.group(1) if correspondencia else str(valor).strip()  # retorna so a parte numerica encontrada, ou o valor original se nao encontrar


def _normalizar_hostname_vizinho(valor) -> str:  # define a funcao que remove o sufixo de dominio do nome de um vizinho CDP
    """
    Remove o sufixo de dominio do nome do vizinho reportado pelo CDP
    (ex: "SW_DST01.cisco.com" -> "SW_DST01"), para bater com o nome
    usado na coluna "Switch" do restante da tabela.
    """                                          # fecha a docstring da funcao, explicando o proposito da normalizacao
    return str(valor).split(".")[0]              # divide a string pelo ponto e retorna so a primeira parte, o hostname puro


def _esta_bloqueado(role: str, state: str) -> bool:  # define a funcao que decide se uma porta esta bloqueada, do ponto de vista de um lado
    """
    Define se uma porta, do ponto de vista de um lado do link, esta
    bloqueada para a VLAN em questao.
    """                                              # fecha a docstring da funcao, explicando seu proposito
    role = str(role).strip()                         # converte o role para string e remove espacos nas pontas
    state = str(state).strip().upper()               # converte o state para string, remove espacos e padroniza em maiusculo
    return role == "Altn" or state != "FWD"          # considera bloqueado se o role for Alternate ou o state nao for Forwarding


def _identificar_root_bridge(linhas_vlan: pd.DataFrame) -> str:                              # define a funcao que descobre qual switch e o Root Bridge desta VLAN
    """
    Identifica qual switch e o Root Bridge desta VLAN: e o unico switch,
    entre os presentes, que nao possui nenhuma porta com Role == "Root".
    """                                                                                      # fecha a docstring da funcao, explicando a regra usada
    switches = linhas_vlan["Switch"].unique()                                                # lista todos os switches distintos presentes nesta VLAN
    tem_porta_root = set(linhas_vlan.loc[linhas_vlan["Role"] == "Root", "Switch"].unique())  # monta o conjunto de switches que possuem pelo menos uma porta com Role Root
    candidatos = [switch for switch in switches if switch not in tem_porta_root]             # filtra os switches que NAO estao nesse conjunto -- o(s) candidato(s) a Root Bridge
    return candidatos[0] if candidatos else ""                                               # retorna o primeiro candidato encontrado, ou string vazia se nenhum for identificado


def construir_arvore(tabela: pd.DataFrame, vlan) -> nx.MultiGraph:  # define a funcao principal que monta o grafo da arvore STP de uma VLAN
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
    """                                                                          # fecha a docstring da funcao, explicando parametros e retorno
    vlan_normalizada = str(int(vlan))                                            # normaliza o identificador da VLAN recebido para uma string numerica sem zeros a esquerda
    linhas_vlan = tabela[tabela["VLAN"].astype(str) == vlan_normalizada].copy()  # filtra da tabela completa so as linhas desta VLAN especifica

    root_bridge = _identificar_root_bridge(linhas_vlan)  # identifica qual switch e o Root Bridge desta VLAN

    grafo = nx.MultiGraph()                                                  # cria o grafo vazio, permitindo arestas paralelas entre o mesmo par de nos
                                                                             # linha em branco com espacos residuais, sem efeito no codigo
    # Adiciona os nós com o atributo de custo (Root Cost) extraído da tabela
    switches = linhas_vlan["Switch"].unique()                                # lista todos os switches distintos presentes nesta VLAN
    for switch in switches:                                                  # percorre cada switch para adiciona-lo como no do grafo
        dados_switch = linhas_vlan[linhas_vlan["Switch"] == switch].iloc[0]  # pega a primeira linha desta VLAN pertencente a este switch, para extrair atributos gerais
        custo = dados_switch.get("Root Cost", "")                            # extrai o Root Cost registrado para este switch nesta VLAN, ou vazio se ausente
        grafo.add_node(switch, root=(switch == root_bridge), cost=custo)     # adiciona o no ao grafo, marcando se e o Root Bridge e guardando o custo

    vizinho_preenchido = linhas_vlan["Neighbor"].fillna("").astype(str) != ""  # monta uma mascara booleana das linhas que tem um vizinho CDP preenchido
    linhas_com_vizinho = linhas_vlan[vizinho_preenchido]                       # filtra so as linhas com vizinho conhecido, usadas para montar os enlaces

    enlaces = {}                                                                      # cria o dicionario vazio que vai acumular os enlaces, agrupados por par de pontas
    for _, linha in linhas_com_vizinho.iterrows():                                    # percorre cada linha com vizinho CDP conhecido
        switch_local = linha["Switch"]                                                # extrai o nome do switch local desta linha
        vizinho = _normalizar_hostname_vizinho(linha["Neighbor"])                     # normaliza o hostname do vizinho, removendo o sufixo de dominio
        ponta_local = (switch_local, _normalizar_interface(linha["Interface"]))       # monta a tupla que identifica esta ponta do link: switch + interface normalizada
        ponta_remota = (vizinho, _normalizar_interface(linha["Neighbor Interface"]))  # monta a tupla que identifica a ponta remota do link
        chave = frozenset({ponta_local, ponta_remota})                                # cria uma chave unica e sem ordem para este link, usada para deduplicar

        enlaces.setdefault(chave, {"pontas": (ponta_local, ponta_remota), "lados": []})  # garante uma entrada no dicionario para esta chave, se ainda nao existir
        enlaces[chave]["lados"].append({                                                 # inicia o registro de mais um lado observado para este link
            "switch": switch_local,                                                      # grava o nome do switch que reportou este lado do link
            "interface": linha["Interface"],                                             # grava a interface local usada por este switch neste link
            "role": linha["Role"],                                                       # grava o papel da porta (Root, Desg, Altn) reportado por este lado
            "state": linha["State"],                                                     # grava o estado da porta (FWD, BLK) reportado por este lado
        })                                                                               # fecha o dicionario do lado e a chamada de append

    for chave, dado in enlaces.items():                                                          # percorre cada link unico ja deduplicado
        (switch_a, _), (switch_b, _) = dado["pontas"]                                            # extrai os nomes dos dois switches envolvidos neste link, ignorando a interface
        bloqueado = any(_esta_bloqueado(lado["role"], lado["state"]) for lado in dado["lados"])  # considera o link bloqueado se qualquer um dos lados reportar bloqueio
        grafo.add_edge(                                                                          # inicia a criacao da aresta entre os dois switches deste link
            switch_a, switch_b,                                                                  # define os dois nos que esta aresta conecta
            vlan=vlan_normalizada,                                                               # grava a VLAN a qual este enlace pertence
            bloqueado=bloqueado,                                                                 # grava se este enlace esta bloqueado, combinando os dois lados
            detalhes=dado["lados"],                                                              # grava a lista completa dos lados observados, para uso no desenho
        )                                                                                        # fecha a chamada de add_edge, criando de fato a aresta no grafo

    return grafo  # retorna o grafo completo desta VLAN, com nos e arestas prontos
