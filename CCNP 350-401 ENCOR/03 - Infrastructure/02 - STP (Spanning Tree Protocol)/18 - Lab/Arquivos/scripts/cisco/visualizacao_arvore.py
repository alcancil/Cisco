"""
visualizacao_arvore.py

Renderiza um grafo de arvore STP (gerado por arvore_stp.construir_arvore)
como uma figura interativa do Plotly, seguindo o estilo visual do Lab 17:
- Cores fixas para cada camada (Core, Distribution, Access)
- Nós maiores com texto interno (nome curto, custo, marca *ROOT*)
- Links ativos em azul, bloqueados em vermelho tracejado com marcador X
- Deslocamento de links paralelos para evitar sobreposição
- Layout hierárquico manual (Core, Dist, Access) com coordenadas fixas
"""

import networkx as nx
import plotly.graph_objects as go
import math

# ========= CONFIGURAÇÕES VISUAIS (conforme Lab 17) =========
COR_CORE = "#2c3e50"          # Cinza escuro para CORE
COR_DST_ROOT = "#e74c3c"      # Vermelho para DST quando Root
COR_DST = "#2980b9"           # Azul para DST (não Root)
COR_ACC = "#27ae60"           # Verde para Access
COR_LINHA_ATIVO = "#2980b9"   # Azul para links ativos
COR_LINHA_BLOQ = "#e74c3c"    # Vermelho para links bloqueados

# Tamanho dos nós (Plotly size) – Lab 17 usa 55
TAMANHO_NO = 55
# Tamanho do marcador X nos bloqueados
TAMANHO_X = 16

# ========= LAYOUT HIERÁRQUICO (coordenadas fixas do Lab 17) =========
# Posições baseadas no diagrama do Lab 17:
# Core: y=3, x=-1 e 1 (podem ser mais, mas serão distribuídos)
# Distribution: y=2, x=-1 e 1
# Access: y=1, x=-1.7, -0.3, 0.3, 1.7
POSICOES_BASE = {
    "core":   {"y": 3, "x_centro": 0, "x_espacamento": 2.0},
    "dist":   {"y": 2, "x_centro": 0, "x_espacamento": 2.0},
    "access": {"y": 1, "x_centro": 0, "x_espacamento": 1.4},
}

def _layout_hierarquico(grafo: nx.MultiGraph) -> dict:
    """
    Posiciona os nós manualmente conforme as camadas (core, dist, access).
    Se houver mais de um nó na mesma camada, distribui-os horizontalmente
    com espaçamento fixo.
    """
    posicoes = {}
    # Agrupa nós por camada
    nos_por_camada = {"core": [], "dist": [], "access": []}
    for no in grafo.nodes():
        if no.startswith("SW_CORE"):
            nos_por_camada["core"].append(no)
        elif no.startswith("SW_DST"):
            nos_por_camada["dist"].append(no)
        elif no.startswith("SW_ACC"):
            nos_por_camada["access"].append(no)
        else:
            # Fallback: coloca em 'access' (ou trata como desconhecido)
            nos_por_camada["access"].append(no)

    for camada, lista in nos_por_camada.items():
        config = POSICOES_BASE[camada]
        y = config["y"]
        x_centro = config["x_centro"]
        esp = config["x_espacamento"]
        total = len(lista)
        if total == 0:
            continue
        # Distribui os nós simetricamente em torno de x_centro
        for i, no in enumerate(sorted(lista)):
            # Índice centralizado: i - (total-1)/2
            desloc = i - (total - 1) / 2
            x = x_centro + desloc * esp
            posicoes[no] = (x, y)
    return posicoes


def _calcular_pontos_arestas(grafo, posicoes):
    """
    Calcula os pontos (x0, y0) e (x1, y1) para cada aresta,
    aplicando um deslocamento perpendicular para arestas paralelas.
    Retorna uma lista de dicionários com os dados de cada aresta.
    """
    # Agrupa arestas por par de nós (ordem normalizada)
    pares = {}
    for u, v, chave, dados in grafo.edges(keys=True, data=True):
        par = tuple(sorted((u, v)))
        pares.setdefault(par, []).append((u, v, chave, dados))

    resultado = []
    for par, lista_arestas in pares.items():
        n = len(lista_arestas)
        for i, (u, v, chave, dados) in enumerate(lista_arestas):
            x0, y0 = posicoes[u]
            x1, y1 = posicoes[v]
            # Se houver mais de uma aresta, aplica offset perpendicular
            if n > 1:
                offset = (i - (n - 1) / 2) * 0.12
                dx, dy = x1 - x0, y1 - y0
                comprimento = math.hypot(dx, dy) or 1
                perp_x, perp_y = -dy / comprimento, dx / comprimento
                x0d = x0 + perp_x * offset
                y0d = y0 + perp_y * offset
                x1d = x1 + perp_x * offset
                y1d = y1 + perp_y * offset
            else:
                x0d, y0d, x1d, y1d = x0, y0, x1, y1

            resultado.append({
                "origem": u,
                "destino": v,
                "dados": dados,
                "x0": x0d, "y0": y0d,
                "x1": x1d, "y1": y1d,
                "xm": (x0d + x1d) / 2,
                "ym": (y0d + y1d) / 2,
            })
    return resultado


def desenhar_arvore(grafo: nx.MultiGraph, vlan) -> go.Figure:
    """
    Desenha o grafo com linhas retas, nós coloridos por camada e custo dentro do círculo.
    """
    posicoes = _layout_hierarquico(grafo)

    figura = go.Figure()

    # ===== Arestas =====
    arestas = _calcular_pontos_arestas(grafo, posicoes)

    # Listas para armazenar traços de linha e textos de rótulo
    for aresta in arestas:
        dados = aresta["dados"]
        bloqueado = dados.get("bloqueado", False)
        cor = COR_LINHA_BLOQ if bloqueado else COR_LINHA_ATIVO
        estilo = "dash" if bloqueado else "solid"

        # Linha da aresta
        figura.add_trace(go.Scatter(
            x=[aresta["x0"], aresta["x1"]],
            y=[aresta["y0"], aresta["y1"]],
            mode="lines",
            line=dict(color=cor, width=3, dash=estilo),
            hoverinfo="text",
            hovertext=f"{aresta['origem']} - {aresta['destino']} ({'Bloqueado' if bloqueado else 'Forwarding'})",
            showlegend=False,
        ))

        # Rótulo da(s) interface(s) – exibe as portas de ambos os lados
        rotulo_interface = " - ".join([lado["interface"] for lado in dados.get("detalhes", [])])
        if rotulo_interface:
            figura.add_trace(go.Scatter(
                x=[aresta["xm"]],
                y=[aresta["ym"] + 0.05],  # ligeiramente acima do centro
                mode="text",
                text=[rotulo_interface],
                textfont=dict(size=12, color="#7F8C8D"),
                hoverinfo="skip",
                showlegend=False,
            ))

        # Marcador X vermelho nos links bloqueados
        if bloqueado:
            figura.add_trace(go.Scatter(
                x=[aresta["xm"]],
                y=[aresta["ym"]],
                mode="markers",
                marker=dict(
                    symbol="x",
                    size=TAMANHO_X,
                    color=COR_LINHA_BLOQ,
                    line=dict(width=3)
                ),
                hoverinfo="skip",
                showlegend=False,
            ))

    # ===== Nós =====
    nos = list(grafo.nodes())
    xs = [posicoes[no][0] for no in nos]
    ys = [posicoes[no][1] for no in nos]

    cores = []
    textos = []
    for no in nos:
        dados_no = grafo.nodes[no]
        is_root = dados_no.get("root", False)
        custo = dados_no.get("cost", "")

        # Cor do nó conforme camada e se é root
        if no.startswith("SW_CORE"):
            cor = COR_CORE
        elif no.startswith("SW_DST"):
            cor = COR_DST_ROOT if is_root else COR_DST
        elif no.startswith("SW_ACC"):
            cor = COR_ACC
        else:
            # Fallback
            cor = COR_DST
        cores.append(cor)

        # Nome curto (sem "SW_")
        nome_curto = no.replace("SW_", "")
        # Texto interno: nome, custo e marca *ROOT* se for root
        if is_root:
            texto = f"{nome_curto}<br>*ROOT*<br>cost={custo}" if custo else f"{nome_curto}<br>*ROOT*"
        else:
            texto = f"{nome_curto}<br>cost={custo}" if custo else nome_curto
        textos.append(texto)

    # Desenha os nós
    figura.add_trace(go.Scatter(
        x=xs, y=ys,
        mode="markers+text",
        marker=dict(
            size=TAMANHO_NO,
            color=cores,
            line=dict(width=3, color="white")
        ),
        text=textos,
        textposition="middle center",
        textfont=dict(size=13, color="white", family="Arial"),
        hoverinfo="text",
        hovertext=[f"{no}<br>Custo: {custos}" for no, custos in zip(nos, [grafo.nodes[n].get("cost", "") for n in nos])],
        showlegend=False,
    ))

    # Ajuste do layout da figura
    figura.update_layout(
        title=f"Arvore STP - VLAN {vlan}",
        xaxis=dict(visible=False, range=[-3, 3]),  # range ajustado para caber todos
        yaxis=dict(visible=False, range=[0, 4]),   # y varia de 1 a 3, com margem
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=50, b=20),
    )

    return figura