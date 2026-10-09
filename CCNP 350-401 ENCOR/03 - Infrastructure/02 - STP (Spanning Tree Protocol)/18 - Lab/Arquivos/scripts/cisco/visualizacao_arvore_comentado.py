"""
visualizacao_arvore.py

Renderiza um grafo de arvore STP (gerado por arvore_stp.construir_arvore)
como uma figura interativa do Plotly, seguindo o estilo visual do Lab 17:
- Cores fixas para cada camada (Core, Distribution, Access)
- Nós maiores com texto interno (nome curto, custo, marca *ROOT*)
- Links ativos em azul, bloqueados em vermelho tracejado com marcador X
- Deslocamento de links paralelos para evitar sobreposição
- Layout hierárquico manual (Core, Dist, Access) com coordenadas fixas
"""  # docstring do módulo, descreve propósito e padrões visuais

import networkx as nx                           # importa a biblioteca para manipulação de grafos
import plotly.graph_objects as go               # importa o Plotly para criação de figuras interativas
import math                                     # importa módulo matemático para cálculos de hipotenusa e deslocamento

# ========= CONFIGURAÇÕES VISUAIS (conforme Lab 17) =========
COR_CORE = "#2c3e50"          # define a cor cinza escuro para switches Core
COR_DST_ROOT = "#e74c3c"      # define a cor vermelha para Distribution quando é Root
COR_DST = "#2980b9"           # define a cor azul para Distribution (não Root)
COR_ACC = "#27ae60"           # define a cor verde para Access
COR_LINHA_ATIVO = "#2980b9"   # define a cor azul para links ativos (forwarding)
COR_LINHA_BLOQ = "#e74c3c"    # define a cor vermelha para links bloqueados

# Tamanho dos nós (Plotly size) – Lab 17 usa 55
TAMANHO_NO = 55                # define o tamanho dos círculos dos switches na figura
# Tamanho do marcador X nos bloqueados
TAMANHO_X = 16                 # define o tamanho do "X" vermelho nos links bloqueados

# ========= LAYOUT HIERÁRQUICO (coordenadas fixas do Lab 17) =========
# Posições baseadas no diagrama do Lab 17:
# Core: y=3, x=-1 e 1 (podem ser mais, mas serão distribuídos)
# Distribution: y=2, x=-1 e 1
# Access: y=1, x=-1.7, -0.3, 0.3, 1.7
POSICOES_BASE = {                               # dicionário com as configurações de posição para cada camada
    "core":   {"y": 3, "x_centro": 0, "x_espacamento": 2.0},   # camada core: y=3, centro x=0, espaçamento entre nós = 2.0
    "dist":   {"y": 2, "x_centro": 0, "x_espacamento": 2.0},   # camada distribution: y=2, centro x=0, espaçamento 2.0
    "access": {"y": 1, "x_centro": 0, "x_espacamento": 1.4},   # camada access: y=1, centro x=0, espaçamento 1.4
}

def _layout_hierarquico(grafo: nx.MultiGraph) -> dict:   # define função que calcula posições dos nós
    """
    Posiciona os nós manualmente conforme as camadas (core, dist, access).
    Se houver mais de um nó na mesma camada, distribui-os horizontalmente
    com espaçamento fixo.
    """  # docstring da função
    posicoes = {}                                      # dicionário para armazenar as posições (x, y) de cada nó
    # Agrupa nós por camada
    nos_por_camada = {"core": [], "dist": [], "access": []}   # dicionário com listas para cada camada
    for no in grafo.nodes():                           # percorre todos os nós do grafo
        if no.startswith("SW_CORE"):                   # se o nome começa com "SW_CORE"
            nos_por_camada["core"].append(no)          # adiciona à lista da camada core
        elif no.startswith("SW_DST"):                  # se começa com "SW_DST"
            nos_por_camada["dist"].append(no)          # adiciona à camada distribution
        elif no.startswith("SW_ACC"):                  # se começa com "SW_ACC"
            nos_por_camada["access"].append(no)        # adiciona à camada access
        else:                                          # para qualquer outro nome (fallback)
            nos_por_camada["access"].append(no)        # coloca na camada access (ou tratar como desconhecido)

    for camada, lista in nos_por_camada.items():       # percorre cada camada (core, dist, access)
        config = POSICOES_BASE[camada]                 # obtém as configurações de posição para essa camada
        y = config["y"]                                # coordenada y fixa para a camada
        x_centro = config["x_centro"]                  # centro horizontal da camada
        esp = config["x_espacamento"]                  # espaçamento entre nós na camada
        total = len(lista)                            # número de nós nessa camada
        if total == 0:                                # se não há nós nessa camada
            continue                                  # pula para a próxima camada
        # Distribui os nós simetricamente em torno de x_centro
        for i, no in enumerate(sorted(lista)):        # percorre os nós em ordem alfabética
            # Índice centralizado: i - (total-1)/2
            desloc = i - (total - 1) / 2               # calcula o deslocamento em relação ao centro
            x = x_centro + desloc * esp                # calcula a coordenada x do nó
            posicoes[no] = (x, y)                      # armazena a posição (x, y) no dicionário
    return posicoes                                   # retorna o dicionário com todas as posições


def _calcular_pontos_arestas(grafo, posicoes):        # define função que calcula os pontos das arestas com offset
    """
    Calcula os pontos (x0, y0) e (x1, y1) para cada aresta,
    aplicando um deslocamento perpendicular para arestas paralelas.
    Retorna uma lista de dicionários com os dados de cada aresta.
    """  # docstring da função
    # Agrupa arestas por par de nós (ordem normalizada)
    pares = {}                                        # dicionário para agrupar arestas pelo par de nós
    for u, v, chave, dados in grafo.edges(keys=True, data=True):   # percorre todas as arestas com chave e dados
        par = tuple(sorted((u, v)))                   # cria uma tupla ordenada para identificar o par (indiferente à direção)
        pares.setdefault(par, []).append((u, v, chave, dados))   # adiciona a aresta à lista do par

    resultado = []                                   # lista para armazenar os dados de cada aresta com pontos calculados
    for par, lista_arestas in pares.items():          # percorre cada par de nós
        n = len(lista_arestas)                        # número de arestas paralelas entre esse par
        for i, (u, v, chave, dados) in enumerate(lista_arestas):   # percorre cada aresta do par
            x0, y0 = posicoes[u]                      # posição do nó de origem
            x1, y1 = posicoes[v]                      # posição do nó de destino
            # Se houver mais de uma aresta, aplica offset perpendicular
            if n > 1:                                 # se há mais de uma aresta paralela
                offset = (i - (n - 1) / 2) * 0.12      # calcula o deslocamento perpendicular (simétrico)
                dx, dy = x1 - x0, y1 - y0             # vetor da aresta
                comprimento = math.hypot(dx, dy) or 1 # comprimento do vetor (evita divisão por zero)
                perp_x, perp_y = -dy / comprimento, dx / comprimento   # vetor unitário perpendicular
                x0d = x0 + perp_x * offset            # novo x do ponto inicial com deslocamento
                y0d = y0 + perp_y * offset            # novo y do ponto inicial
                x1d = x1 + perp_x * offset            # novo x do ponto final
                y1d = y1 + perp_y * offset            # novo y do ponto final
            else:                                     # se é a única aresta
                x0d, y0d, x1d, y1d = x0, y0, x1, y1  # mantém as coordenadas originais

            resultado.append({                       # adiciona um dicionário com os dados da aresta
                "origem": u,                         # nó origem
                "destino": v,                       # nó destino
                "dados": dados,                     # dados da aresta (inclui bloqueado e detalhes)
                "x0": x0d, "y0": y0d,               # coordenadas do início com offset
                "x1": x1d, "y1": y1d,               # coordenadas do fim com offset
                "xm": (x0d + x1d) / 2,              # coordenada x do ponto médio
                "ym": (y0d + y1d) / 2,              # coordenada y do ponto médio
            })
    return resultado                               # retorna a lista com todas as arestas calculadas


def desenhar_arvore(grafo: nx.MultiGraph, vlan) -> go.Figure:   # função principal que desenha o grafo
    """
    Desenha o grafo com linhas retas, nós coloridos por camada e custo dentro do círculo.
    """  # docstring da função
    posicoes = _layout_hierarquico(grafo)           # obtém as posições dos nós usando o layout hierárquico

    figura = go.Figure()                           # cria uma figura Plotly vazia

    # ===== Arestas =====
    arestas = _calcular_pontos_arestas(grafo, posicoes)   # calcula os pontos das arestas com offsets

    # Listas para armazenar traços de linha e textos de rótulo
    for aresta in arestas:                          # percorre cada aresta calculada
        dados = aresta["dados"]                     # obtém os dados da aresta (bloqueado, detalhes)
        bloqueado = dados.get("bloqueado", False)   # verifica se o link está bloqueado
        cor = COR_LINHA_BLOQ if bloqueado else COR_LINHA_ATIVO   # escolhe a cor conforme o estado
        estilo = "dash" if bloqueado else "solid"   # define o estilo da linha: tracejado ou sólido

        # Linha da aresta
        figura.add_trace(go.Scatter(               # adiciona um traço para a linha
            x=[aresta["x0"], aresta["x1"]],        # coordenadas x do início e fim
            y=[aresta["y0"], aresta["y1"]],        # coordenadas y do início e fim
            mode="lines",                          # modo de exibição: apenas linhas
            line=dict(color=cor, width=3, dash=estilo),   # configurações da linha (cor, largura, estilo)
            hoverinfo="text",                      # define que o hover mostrará o texto personalizado
            hovertext=f"{aresta['origem']} - {aresta['destino']} ({'Bloqueado' if bloqueado else 'Forwarding'})",
            showlegend=False,                      # não mostra legenda para as arestas
        ))

        # Rótulo da(s) interface(s) – exibe as portas de ambos os lados
        rotulo_interface = " - ".join([lado["interface"] for lado in dados.get("detalhes", [])])   # junta as interfaces com " - "
        if rotulo_interface:                      # se existir rótulo
            figura.add_trace(go.Scatter(           # adiciona um traço para o texto
                x=[aresta["xm"]],                  # posição x do ponto médio
                y=[aresta["ym"] + 0.05],          # posição y ligeiramente acima do centro
                mode="text",                      # modo texto
                text=[rotulo_interface],          # texto a ser exibido
                textfont=dict(size=12, color="#7F8C8D"),   # fonte do rótulo
                hoverinfo="skip",                 # desabilita hover para o rótulo
                showlegend=False,                 # sem legenda
            ))

        # Marcador X vermelho nos links bloqueados
        if bloqueado:                              # se o link está bloqueado
            figura.add_trace(go.Scatter(           # adiciona um marcador X
                x=[aresta["xm"]],                  # coordenada x do centro
                y=[aresta["ym"]],                  # coordenada y do centro
                mode="markers",                   # modo marcadores
                marker=dict(                      # configurações do marcador
                    symbol="x",                   # símbolo "X"
                    size=TAMANHO_X,               # tamanho do X
                    color=COR_LINHA_BLOQ,         # cor vermelha
                    line=dict(width=3)            # espessura da linha do X
                ),
                hoverinfo="skip",                  # desabilita hover
                showlegend=False,                  # sem legenda
            ))

    # ===== Nós =====
    nos = list(grafo.nodes())                      # lista de todos os nós
    xs = [posicoes[no][0] for no in nos]           # coordenadas x de cada nó
    ys = [posicoes[no][1] for no in nos]           # coordenadas y de cada nó

    cores = []                                     # lista para armazenar as cores de cada nó
    textos = []                                    # lista para armazenar os textos internos de cada nó
    for no in nos:                                 # percorre cada nó
        dados_no = grafo.nodes[no]                 # obtém os dados do nó (root, cost)
        is_root = dados_no.get("root", False)      # verifica se é o root bridge
        custo = dados_no.get("cost", "")           # obtém o custo (string)

        # Cor do nó conforme camada e se é root
        if no.startswith("SW_CORE"):               # se é Core
            cor = COR_CORE                         # cor cinza escuro
        elif no.startswith("SW_DST"):              # se é Distribution
            cor = COR_DST_ROOT if is_root else COR_DST   # vermelho se root, senão azul
        elif no.startswith("SW_ACC"):              # se é Access
            cor = COR_ACC                          # cor verde
        else:                                      # fallback para qualquer outro
            cor = COR_DST                          # usa azul como padrão
        cores.append(cor)                          # adiciona a cor à lista

        # Nome curto (sem "SW_")
        nome_curto = no.replace("SW_", "")         # remove o prefixo "SW_" do nome
        # Texto interno: nome, custo e marca *ROOT* se for root
        if is_root:                                # se for root
            texto = f"{nome_curto}<br>*ROOT*<br>cost={custo}" if custo else f"{nome_curto}<br>*ROOT*"
        else:                                      # se não for root
            texto = f"{nome_curto}<br>cost={custo}" if custo else nome_curto
        textos.append(texto)                       # adiciona o texto à lista

    # Desenha os nós
    figura.add_trace(go.Scatter(                   # adiciona um traço para os nós
        x=xs, y=ys,                                # coordenadas x e y dos nós
        mode="markers+text",                      # modo: marcadores + texto
        marker=dict(                              # configurações dos marcadores
            size=TAMANHO_NO,                      # tamanho do círculo
            color=cores,                          # cores definidas
            line=dict(width=3, color="white")     # borda branca
        ),
        text=textos,                              # textos a serem exibidos dentro dos círculos
        textposition="middle center",             # posição do texto: centralizado
        textfont=dict(size=13, color="white", family="Arial"),   # fonte do texto
        hoverinfo="text",                         # hover exibirá o texto personalizado
        hovertext=[f"{no}<br>Custo: {custos}" for no, custos in zip(nos, [grafo.nodes[n].get("cost", "") for n in nos])],
        showlegend=False,                         # sem legenda
    ))

    # Ajuste do layout da figura
    figura.update_layout(                         # ajusta o layout da figura
        title=f"Arvore STP - VLAN {vlan}",       # título com o número da VLAN
        xaxis=dict(visible=False, range=[-3, 3]),  # oculta o eixo X e define o range para caber todos os nós
        yaxis=dict(visible=False, range=[0, 4]),   # oculta o eixo Y e define o range (y varia de 1 a 3)
        plot_bgcolor="white",                      # fundo branco
        margin=dict(l=20, r=20, t=50, b=20),      # margens da figura
    )

    return figura                                  # retorna a figura Plotly pronta