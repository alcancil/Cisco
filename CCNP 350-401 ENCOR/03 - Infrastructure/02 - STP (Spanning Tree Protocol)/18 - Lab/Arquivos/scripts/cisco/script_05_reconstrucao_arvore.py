"""
Script 05 - Reconstruindo Automaticamente as Arvores STP

Objetivo: usando a tabela consolidada (PVST+ + CDP) gerada pelo Script 04,
reconstruir e salvar a arvore STP de cada uma das VLANs 10 a 100.
A VLAN 1 fica de fora de proposito -- ja foi analisada manualmente no
Laboratorio 17, e nao participa do balanceamento entre os Cores.

Fluxo:
    1. Le a tabela consolidada (outputs/consolidado/tabela_consolidada.csv).
    2. Para cada VLAN de 10 a 100 (passo 10):
        - constroi o grafo da arvore (arvore_stp.py)
        - desenha a figura (visualizacao_arvore.py)
        - salva como PNG em outputs/arvores/vlan_<numero>.png
    3. Imprime um resumo (switches, enlaces, bloqueados) por VLAN.

As mesmas duas funcoes (construir_arvore e desenhar_arvore) serao
reaproveitadas depois no dashboard Streamlit, sem duplicar codigo -- so
muda o que e feito com a figura (salvar arquivo aqui, renderizar ao vivo
la).

Dependencias novas: pip install networkx plotly "kaleido==0.2.1"
(a versao 1.x do kaleido exige Chrome instalado; a 0.2.1 nao precisa)
"""

import pandas as pd

from output_writer import PARSED_OUTPUT_DIR
from arvore_stp import construir_arvore
from visualizacao_arvore import desenhar_arvore

CONSOLIDADO_PATH = PARSED_OUTPUT_DIR.parent / "consolidado" / "tabela_consolidada.csv"
ARVORES_DIR = PARSED_OUTPUT_DIR.parent / "arvores"

# VLAN 10, 20, 30 ... 100 -- VLAN 1 fica de fora de proposito (ver docstring).
VLANS_DE_DADOS = range(10, 101, 10)


def main():
    if not CONSOLIDADO_PATH.exists():
        print(f"Arquivo {CONSOLIDADO_PATH} nao encontrado -- rode o Script 04 antes.")
        return

    tabela = pd.read_csv(CONSOLIDADO_PATH)
    ARVORES_DIR.mkdir(parents=True, exist_ok=True)

    for vlan in VLANS_DE_DADOS:
        grafo = construir_arvore(tabela, vlan)

        if grafo.number_of_nodes() == 0:
            print(f"VLAN {vlan}: nenhum dado encontrado -- pulando.")
            continue

        figura = desenhar_arvore(grafo, vlan)
        caminho_png = ARVORES_DIR / f"vlan_{vlan}.png"
        caminho_html = ARVORES_DIR / f"vlan_{vlan}.html"
        figura.write_image(caminho_png, width=1000, height=750, scale=2)
        figura.write_html(caminho_html)

        bloqueados = sum(1 for _, _, dados in grafo.edges(data=True) if dados.get("bloqueado"))
        print(
            f"VLAN {vlan}: {grafo.number_of_nodes()} switch(es), "
            f"{grafo.number_of_edges()} enlace(s), {bloqueados} bloqueado(s) "
            f"-> {caminho_png.name} + {caminho_html.name}"
        )


if __name__ == "__main__":
    main()
