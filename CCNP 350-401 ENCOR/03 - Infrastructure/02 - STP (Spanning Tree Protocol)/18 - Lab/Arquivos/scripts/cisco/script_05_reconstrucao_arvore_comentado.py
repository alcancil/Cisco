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
"""  # fecha a docstring do modulo, que documenta objetivo, fluxo e dependencias

import pandas as pd  # importa o Pandas, usado para ler a tabela consolidada em CSV

from output_writer import PARSED_OUTPUT_DIR      # importa o caminho base de outputs/parsed/, usado para localizar as pastas irmas
from arvore_stp import construir_arvore          # importa a funcao que monta o grafo NetworkX da arvore STP de uma VLAN
from visualizacao_arvore import desenhar_arvore  # importa a funcao que renderiza o grafo como figura Plotly

CONSOLIDADO_PATH = PARSED_OUTPUT_DIR.parent / "consolidado" / "tabela_consolidada.csv"  # define o caminho do CSV gerado pelo Script 04, a fonte de dados desta etapa
ARVORES_DIR = PARSED_OUTPUT_DIR.parent / "arvores"                                      # define a pasta de saida onde os PNG e HTML de cada VLAN serao salvos

# VLAN 10, 20, 30 ... 100 -- VLAN 1 fica de fora de proposito (ver docstring).
VLANS_DE_DADOS = range(10, 101, 10)  # gera a sequencia de VLANs a processar: 10, 20, 30 ... ate 100


def main():                                                                             # define a funcao principal que orquestra toda a reconstrucao das arvores
    if not CONSOLIDADO_PATH.exists():                                                   # verifica se a tabela consolidada existe antes de tentar le-la
        print(f"Arquivo {CONSOLIDADO_PATH} nao encontrado -- rode o Script 04 antes.")  # avisa no console que a consolidacao ainda nao foi executada
        return                                                                          # encerra a funcao imediatamente, pois nao ha dados para reconstruir sem o CSV

    tabela = pd.read_csv(CONSOLIDADO_PATH)          # le a tabela consolidada inteira para um DataFrame do Pandas
    ARVORES_DIR.mkdir(parents=True, exist_ok=True)  # cria a pasta outputs/arvores/ automaticamente, se ainda nao existir

    for vlan in VLANS_DE_DADOS:                 # percorre cada uma das dez VLANs de dados, uma por vez
        grafo = construir_arvore(tabela, vlan)  # constroi o grafo da arvore STP desta VLAN a partir da tabela consolidada

        if grafo.number_of_nodes() == 0:                               # verifica se a VLAN teve algum switch encontrado na tabela
            print(f"VLAN {vlan}: nenhum dado encontrado -- pulando.")  # informa no console que esta VLAN nao teve dado algum e sera ignorada
            continue                                                   # pula para a proxima VLAN, sem tentar desenhar um grafo vazio

        figura = desenhar_arvore(grafo, vlan)                             # renderiza o grafo desta VLAN como uma figura Plotly
        caminho_png = ARVORES_DIR / f"vlan_{vlan}.png"                    # monta o caminho do arquivo PNG estatico desta VLAN
        caminho_html = ARVORES_DIR / f"vlan_{vlan}.html"                  # monta o caminho do arquivo HTML interativo desta VLAN
        figura.write_image(caminho_png, width=1000, height=750, scale=2)  # salva a figura como imagem PNG estatica, em alta resolucao
        figura.write_html(caminho_html)                                   # salva a figura como pagina HTML interativa (zoom, hover, pan)

        bloqueados = sum(1 for _, _, dados in grafo.edges(data=True) if dados.get("bloqueado"))  # conta quantos enlaces desta VLAN estao marcados como bloqueados
        print(                                                                                   # inicia a chamada de print que resume o resultado desta VLAN
            f"VLAN {vlan}: {grafo.number_of_nodes()} switch(es), "                               # monta a primeira parte da mensagem, com o total de switches
            f"{grafo.number_of_edges()} enlace(s), {bloqueados} bloqueado(s) "                   # monta a segunda parte da mensagem, com o total de enlaces e bloqueados
            f"-> {caminho_png.name} + {caminho_html.name}"                                       # completa a mensagem informando os nomes dos dois arquivos gerados
        )                                                                                        # fecha a chamada de print, exibindo o resumo completo desta VLAN no console


if __name__ == "__main__":  # garante que main() so execute quando o arquivo for rodado diretamente, nao quando importado
    main()                  # chama a funcao principal, iniciando de fato a reconstrucao de todas as arvores
