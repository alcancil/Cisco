"""
gerar_arvore_stp.py

Gera a arvore logica do STP (PVST+) de forma grafica, para uma VLAN especifica.

ARQUITETURA (2 camadas, de proposito):
  1) CAMADA DE DADOS  -> dicionarios Python simples (adjacencia fisica + estado STP por switch)
  2) CAMADA DE RENDERIZACAO -> usa networkx + matplotlib para desenhar o grafo

Por que separado assim:
  Hoje a camada de dados e preenchida manualmente, copiando o que foi coletado
  via "show spanning-tree vlan X" em cada switch (Lab 17).
  Quando o coletar_stp.py (Netmiko + TextFSM/NTC-templates) estiver pronto,
  a CAMADA DE DADOS passa a ser preenchida automaticamente pelo parser.
  A camada de renderizacao (deste arquivo) NAO muda uma linha nesse momento.

Uso:
  python3 gerar_arvore_stp.py
  (gera um arquivo .png com o grafo)
"""

import networkx as nx
import matplotlib.pyplot as plt


# ======================================================================
# CAMADA DE DADOS
# ======================================================================
# Adjacencia fisica entre switches.
# CORRECAO: os links duplos CORE01-DST01 e CORE02-DST02 usam as portas
# Gi0/0 + Gi0/3 (nao Gi0/2 + Gi0/3 como assumido inicialmente a partir do
# diagrama). Isso foi confirmado cruzando os dados reais de "antes" e
# "depois": a Root Port do SW_CORE01 (antes) era Gi0/0, o que so faz
# sentido se Gi0/0 for o link ate o SW_DST01.
TOPOLOGIA_FISICA = [
    ("SW_CORE01", "Gi1/0", "SW_CORE02", "Gi1/0"),
    ("SW_CORE01", "Gi1/1", "SW_CORE02", "Gi1/1"),
    ("SW_CORE01", "Gi0/0", "SW_DST01",  "Gi0/0"),
    ("SW_CORE01", "Gi0/3", "SW_DST01",  "Gi0/3"),
    ("SW_CORE02", "Gi0/0", "SW_DST02",  "Gi0/0"),
    ("SW_CORE02", "Gi0/3", "SW_DST02",  "Gi0/3"),
    ("SW_DST01",  "Gi1/2", "SW_DST02",  "Gi1/2"),
    ("SW_DST01",  "Gi1/3", "SW_DST02",  "Gi1/3"),
    ("SW_DST01",  "Gi0/1", "SW_ACC01",  "Gi0/1"),
    ("SW_DST01",  "Gi0/2", "SW_ACC02",  "Gi0/2"),
    ("SW_DST02",  "Gi0/1", "SW_ACC03",  "Gi0/1"),
    ("SW_DST02",  "Gi0/2", "SW_ACC04",  "Gi0/2"),
]

# Papel de cada switch na hierarquia (so para posicionamento visual / cores)
CAMADA_HIERARQUIA = {
    "SW_CORE01": "core", "SW_CORE02": "core",
    "SW_DST01": "dist",  "SW_DST02": "dist",
    "SW_ACC01": "acesso", "SW_ACC02": "acesso",
    "SW_ACC03": "acesso", "SW_ACC04": "acesso",
}

# ----------------------------------------------------------------------
# ESTADO 1: ANTES (Root Bridge = SW_DST01, situacao original do Lab 17)
# ----------------------------------------------------------------------
DADOS_STP_VLAN1_ANTES = {
    "SW_CORE01": {
        "is_root": False,
        "root_path_cost": 4,
        "root_port": "Gi0/0",
        "blocking_ports": ["Gi0/3"],
    },
    "SW_CORE02": {
        "is_root": False,
        "root_path_cost": 8,
        "root_port": "Gi0/0",
        "blocking_ports": ["Gi0/3", "Gi1/0", "Gi1/1"],
    },
    "SW_DST01": {
        "is_root": True,
        "root_path_cost": 0,
        "root_port": None,
        "blocking_ports": [],
    },
    "SW_DST02": {
        "is_root": False,
        "root_path_cost": 4,
        "root_port": "Gi1/2",
        "blocking_ports": ["Gi1/3"],
    },
    "SW_ACC01": {
        "is_root": False,
        "root_path_cost": 4,
        "root_port": "Gi0/1",
        "blocking_ports": [],
    },
    "SW_ACC02": {
        "is_root": False,
        "root_path_cost": 4,
        "root_port": "Gi0/2",
        "blocking_ports": [],
    },
    "SW_ACC03": {
        "is_root": False,
        "root_path_cost": 8,
        "root_port": "Gi0/1",
        "blocking_ports": [],
    },
    "SW_ACC04": {
        "is_root": False,
        "root_path_cost": 8,
        "root_port": "Gi0/2",
        "blocking_ports": [],
    },
}

# ----------------------------------------------------------------------
# ESTADO 2: DEPOIS (Root Bridge = SW_CORE01, apos "spanning-tree vlan 1
# root primary" aplicado no SW_CORE01)
# ----------------------------------------------------------------------
DADOS_STP_VLAN1_DEPOIS = {
    "SW_CORE01": {
        "is_root": True,
        "root_path_cost": 0,
        "root_port": None,
        "blocking_ports": [],
    },
    "SW_CORE02": {
        "is_root": False,
        "root_path_cost": 4,
        "root_port": "Gi1/0",
        "blocking_ports": ["Gi1/1"],
    },
    "SW_DST01": {
        "is_root": False,
        "root_path_cost": 4,
        "root_port": "Gi0/0",
        "blocking_ports": ["Gi0/3"],
    },
    "SW_DST02": {
        "is_root": False,
        "root_path_cost": 8,
        "root_port": "Gi1/2",
        "blocking_ports": ["Gi0/0", "Gi0/3", "Gi1/3"],
    },
    "SW_ACC01": {
        "is_root": False,
        "root_path_cost": 8,
        "root_port": "Gi0/1",
        "blocking_ports": [],
    },
    "SW_ACC02": {
        "is_root": False,
        "root_path_cost": 8,
        "root_port": "Gi0/2",
        "blocking_ports": [],
    },
    "SW_ACC03": {
        "is_root": False,
        "root_path_cost": 12,
        "root_port": "Gi0/1",
        "blocking_ports": [],
    },
    "SW_ACC04": {
        "is_root": False,
        "root_path_cost": 12,
        "root_port": "Gi0/2",
        "blocking_ports": [],
    },
}


# ======================================================================
# CAMADA DE RENDERIZACAO
# ======================================================================

CORES_HIERARQUIA = {
    "core": "#2c3e50",
    "dist": "#2980b9",
    "acesso": "#27ae60",
}

COR_ROOT = "#e74c3c"
COR_BLOQUEADO = "#e74c3c"
COR_ATIVO = "#2c3e50"


COR_ATIVO = "#2980b9"  # azul


def classificar_link(switch_a, porta_a, switch_b, porta_b, dados_stp):
    """
    Decide se um link esta ATIVO (forwarding nos dois lados) ou BLOQUEADO
    (uma das pontas esta em Blocking), a partir dos dados de STP coletados.
    """
    bloqueado_no_a = porta_a in dados_stp[switch_a]["blocking_ports"]
    bloqueado_no_b = porta_b in dados_stp[switch_b]["blocking_ports"]
    return "bloqueado" if (bloqueado_no_a or bloqueado_no_b) else "ativo"


def montar_grafo(topologia_fisica, dados_stp):
    """
    Usa MultiGraph (nao Graph simples) de proposito: varios pares de switches
    tem 2 links fisicos redundantes entre si (ex: CORE01-DST01). Um Graph
    simples so permite 1 aresta por par e a segunda sobrescreveria a primeira,
    escondendo visualmente um dos dois links.
    """
    G = nx.MultiGraph()

    for switch in dados_stp:
        G.add_node(switch)

    for switch_a, porta_a, switch_b, porta_b in topologia_fisica:
        estado = classificar_link(switch_a, porta_a, switch_b, porta_b, dados_stp)
        G.add_edge(
            switch_a, switch_b,
            estado=estado,
            label=f"{porta_a} - {porta_b}",
        )

    return G


def _calcular_pontos_das_arestas(G, posicoes):
    """
    Para cada aresta, calcula os pontos (x0,y0)-(x1,y1) ja deslocados quando
    houver mais de um link fisico entre o mesmo par de switches (evita que
    as duas linhas fiquem perfeitamente sobrepostas).
    Retorna uma lista de dicts: switch_a, switch_b, estado, label, pontos, meio.
    """
    # agrupa arestas por par de switches (ordem normalizada) para saber
    # quantos links paralelos existem e o indice de cada um
    pares = {}
    for switch_a, switch_b, chave, d in G.edges(keys=True, data=True):
        par = tuple(sorted((switch_a, switch_b)))
        pares.setdefault(par, []).append((switch_a, switch_b, chave, d))

    resultado = []
    for par, lista_arestas in pares.items():
        n = len(lista_arestas)
        for i, (switch_a, switch_b, chave, d) in enumerate(lista_arestas):
            x0, y0 = posicoes[switch_a]
            x1, y1 = posicoes[switch_b]

            # deslocamento perpendicular ao link, para separar arestas paralelas
            if n > 1:
                offset = (i - (n - 1) / 2) * 0.12
                dx, dy = x1 - x0, y1 - y0
                comprimento = (dx ** 2 + dy ** 2) ** 0.5 or 1
                perp_x, perp_y = -dy / comprimento, dx / comprimento
                x0d, y0d = x0 + perp_x * offset, y0 + perp_y * offset
                x1d, y1d = x1 + perp_x * offset, y1 + perp_y * offset
            else:
                x0d, y0d, x1d, y1d = x0, y0, x1, y1

            resultado.append({
                "switch_a": switch_a, "switch_b": switch_b,
                "estado": d["estado"], "label": d["label"],
                "x0": x0d, "y0": y0d, "x1": x1d, "y1": y1d,
                "xm": (x0d + x1d) / 2, "ym": (y0d + y1d) / 2,
            })

    return resultado


def desenhar_grafo(G, dados_stp, camada_hierarquia, titulo, arquivo_saida):
    # Posicionamento manual por camada (fica mais legivel que layout automatico)
    posicoes = {
        "SW_CORE01": (-1, 3), "SW_CORE02": (1, 3),
        "SW_DST01":  (-1, 2), "SW_DST02":  (1, 2),
        "SW_ACC01":  (-1.7, 1), "SW_ACC02": (-0.3, 1),
        "SW_ACC03":  (0.3, 1),  "SW_ACC04": (1.7, 1),
    }

    plt.figure(figsize=(11, 8))
    ax = plt.gca()

    arestas = _calcular_pontos_das_arestas(G, posicoes)

    for aresta in arestas:
        cor = COR_BLOQUEADO if aresta["estado"] == "bloqueado" else COR_ATIVO
        estilo = "dashed" if aresta["estado"] == "bloqueado" else "solid"
        ax.plot(
            [aresta["x0"], aresta["x1"]], [aresta["y0"], aresta["y1"]],
            color=cor, linewidth=2.2, linestyle=estilo, zorder=1,
        )
        # rotulo da porta, um pouco acima do meio do link
        ax.text(
            aresta["xm"], aresta["ym"] + 0.05, aresta["label"],
            fontsize=6, ha="center", color="#555555",
        )
        # marcador X vermelho exatamente no meio dos links bloqueados
        if aresta["estado"] == "bloqueado":
            ax.plot(
                aresta["xm"], aresta["ym"], marker="x", markersize=14,
                markeredgewidth=3, color=COR_BLOQUEADO, zorder=2,
            )

    # --- Nos (desenhados por cima das arestas) ---
    cores_dos_nos = []
    for switch in G.nodes():
        if dados_stp[switch]["is_root"]:
            cores_dos_nos.append(COR_ROOT)
        else:
            cores_dos_nos.append(CORES_HIERARQUIA[camada_hierarquia[switch]])

    nx.draw_networkx_nodes(
        G, posicoes, node_size=2600, node_color=cores_dos_nos,
        edgecolors="white", linewidths=2, ax=ax,
    )

    rotulos_nos = {}
    for switch in G.nodes():
        nome_curto = switch.replace("SW_", "")
        marca_root = " *ROOT*" if dados_stp[switch]["is_root"] else ""
        rotulos_nos[switch] = f"{nome_curto}{marca_root}\ncost={dados_stp[switch]['root_path_cost']}"

    nx.draw_networkx_labels(
        G, posicoes, labels=rotulos_nos, font_size=7, font_color="white",
        font_weight="bold", ax=ax,
    )

    plt.title(titulo, fontsize=13, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(arquivo_saida, dpi=150)
    print(f"Grafo salvo em: {arquivo_saida}")


def desenhar_grafo_plotly(G, dados_stp, camada_hierarquia, titulo, arquivo_saida):
    """
    Mesma camada de dados (G, dados_stp), renderizacao alternativa em Plotly.
    Gera um HTML interativo (hover mostra Role/Cost/portas), separado do PNG estatico.
    """
    import plotly.graph_objects as go

    posicoes = {
        "SW_CORE01": (-1, 3), "SW_CORE02": (1, 3),
        "SW_DST01":  (-1, 2), "SW_DST02":  (1, 2),
        "SW_ACC01":  (-1.7, 1), "SW_ACC02": (-0.3, 1),
        "SW_ACC03":  (0.3, 1),  "SW_ACC04": (1.7, 1),
    }

    fig = go.Figure()

    arestas = _calcular_pontos_das_arestas(G, posicoes)

    # --- Arestas: uma trace por link, ja com offset calculado p/ links paralelos ---
    for aresta in arestas:
        cor = COR_BLOQUEADO if aresta["estado"] == "bloqueado" else COR_ATIVO
        estilo = "dash" if aresta["estado"] == "bloqueado" else "solid"

        fig.add_trace(go.Scatter(
            x=[aresta["x0"], aresta["x1"]], y=[aresta["y0"], aresta["y1"]],
            mode="lines",
            line=dict(color=cor, width=3, dash=estilo),
            hoverinfo="text",
            hovertext=(
                f"{aresta['switch_a']} ({aresta['label'].split(' - ')[0]}) - "
                f"{aresta['switch_b']} ({aresta['label'].split(' - ')[1]})<br>"
                f"Estado: {aresta['estado'].upper()}"
            ),
            showlegend=False,
        ))

        # rotulo da porta, perto do meio do link
        fig.add_trace(go.Scatter(
            x=[aresta["xm"]], y=[aresta["ym"] + 0.05],
            mode="text", text=[aresta["label"]], textfont=dict(size=9, color="#555555"),
            hoverinfo="skip", showlegend=False,
        ))

        # marcador X vermelho exatamente no link bloqueado (visivel sem precisar de hover)
        if aresta["estado"] == "bloqueado":
            fig.add_trace(go.Scatter(
                x=[aresta["xm"]], y=[aresta["ym"]],
                mode="markers",
                marker=dict(symbol="x-thin", size=16, color=COR_BLOQUEADO,
                            line=dict(width=3, color=COR_BLOQUEADO)),
                hoverinfo="skip", showlegend=False,
            ))

    # --- Nos ---
    xs, ys, cores, textos, hovers = [], [], [], [], []
    for switch in G.nodes():
        x, y = posicoes[switch]
        xs.append(x)
        ys.append(y)
        info = dados_stp[switch]
        cores.append(COR_ROOT if info["is_root"] else CORES_HIERARQUIA[camada_hierarquia[switch]])
        nome_curto = switch.replace("SW_", "")
        marca_root = " *ROOT*" if info["is_root"] else ""
        textos.append(f"{nome_curto}{marca_root}")
        rp = info["root_port"] or "N/A (e o Root)"
        bloq = ", ".join(info["blocking_ports"]) or "nenhuma"
        hovers.append(
            f"<b>{switch}</b><br>"
            f"Root Path Cost: {info['root_path_cost']}<br>"
            f"Root Port: {rp}<br>"
            f"Blocking Ports: {bloq}"
        )

    fig.add_trace(go.Scatter(
        x=xs, y=ys, mode="markers+text",
        marker=dict(size=55, color=cores, line=dict(color="white", width=2)),
        text=textos, textposition="middle center",
        textfont=dict(color="white", size=10),
        hoverinfo="text", hovertext=hovers,
        showlegend=False,
    ))

    fig.update_layout(
        title=titulo,
        plot_bgcolor="white",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        width=1000, height=700,
    )

    fig.write_html(arquivo_saida)
    print(f"Grafo interativo salvo em: {arquivo_saida}")


if __name__ == "__main__":
    grafo_antes = montar_grafo(TOPOLOGIA_FISICA, DADOS_STP_VLAN1_ANTES)
    grafo_depois = montar_grafo(TOPOLOGIA_FISICA, DADOS_STP_VLAN1_DEPOIS)

    # --- ANTES: Root Bridge = SW_DST01 (situacao original, problema identificado) ---
    desenhar_grafo(
        grafo_antes, DADOS_STP_VLAN1_ANTES, CAMADA_HIERARQUIA,
        titulo="Arvore STP - VLAN 1 - ANTES (Root Bridge = SW_DST01)",
        arquivo_saida="stp_vlan1_antes.png",
    )
    desenhar_grafo_plotly(
        grafo_antes, DADOS_STP_VLAN1_ANTES, CAMADA_HIERARQUIA,
        titulo="Arvore STP - VLAN 1 - ANTES (Root Bridge = SW_DST01)",
        arquivo_saida="stp_vlan1_antes.html",
    )

    # --- DEPOIS: Root Bridge = SW_CORE01 (corrigido com root primary) ---
    desenhar_grafo(
        grafo_depois, DADOS_STP_VLAN1_DEPOIS, CAMADA_HIERARQUIA,
        titulo="Arvore STP - VLAN 1 - DEPOIS (Root Bridge = SW_CORE01)",
        arquivo_saida="stp_vlan1_depois.png",
    )
    desenhar_grafo_plotly(
        grafo_depois, DADOS_STP_VLAN1_DEPOIS, CAMADA_HIERARQUIA,
        titulo="Arvore STP - VLAN 1 - DEPOIS (Root Bridge = SW_CORE01)",
        arquivo_saida="stp_vlan1_depois.html",
    )
