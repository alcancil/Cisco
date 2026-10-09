"""
Script 04 - Consolidando os Dados

Objetivo: juntar os registros estruturados de todos os switches, gerados
pelo Script 03, em uma unica tabela -- uma linha por combinacao
switch + VLAN + interface participante do PVST+.

Fluxo:
    1. Descobre todos os hostnames ja processados (subpastas de outputs/parsed/).
    2. Para cada hostname, cruza show spanning-tree + show spanning-tree root
       + show processes cpu + show interfaces trunk (consolidador.py).
    3. Monta um DataFrame do Pandas com todas as linhas.
    4. Salva o resultado em outputs/consolidado/tabela_consolidada.csv.

Dependencia nova: pip install pandas
"""  # fecha a docstring do modulo, que documenta o objetivo, o fluxo e a dependencia nova

import pandas as pd  # importa o Pandas, usado para montar e salvar a tabela consolidada

from output_writer import PARSED_OUTPUT_DIR    # importa o caminho da pasta onde estao os JSON parseados pelo Script 03
from consolidador import consolidar_topologia  # importa a funcao que cruza os dados de todos os switches numa unica lista

CONSOLIDADO_DIR = PARSED_OUTPUT_DIR.parent / "consolidado"     # define a pasta de saida como irma de outputs/parsed/ e outputs/raw/
CONSOLIDADO_PATH = CONSOLIDADO_DIR / "tabela_consolidada.csv"  # define o caminho completo do arquivo CSV final


def main():                                                                            # define a funcao principal que orquestra toda a consolidacao
    if not PARSED_OUTPUT_DIR.exists():                                                 # verifica se a pasta outputs/parsed/ existe antes de tentar le-la
        print(f"Pasta {PARSED_OUTPUT_DIR} nao encontrada -- rode o Script 03 antes.")  # avisa no console que o parsing ainda nao foi executado
        return                                                                         # encerra a funcao imediatamente, pois nao ha nada para consolidar sem a pasta parsed

    hostnames = sorted(pasta.name for pasta in PARSED_OUTPUT_DIR.iterdir() if pasta.is_dir())  # lista, em ordem alfabetica, todos os hostnames ja processados pelo Script 03
    print(f"Consolidando dados de {len(hostnames)} switch(es)...")                             # informa no console quantos switches serao consolidados

    linhas = consolidar_topologia(hostnames)  # cruza os dados de todos os switches e retorna a lista de linhas consolidadas
    df = pd.DataFrame(linhas)                 # converte a lista de dicionarios num DataFrame do Pandas

    CONSOLIDADO_DIR.mkdir(parents=True, exist_ok=True)          # cria a pasta outputs/consolidado/ automaticamente, se ainda nao existir
    df.to_csv(CONSOLIDADO_PATH, index=False, encoding="utf-8")  # salva o DataFrame como CSV, sem a coluna de indice numerico do Pandas

    print(f"\nTabela consolidada: {len(df)} linha(s), {len(df.columns)} coluna(s)")  # informa no console o tamanho final da tabela gerada
    print(f"Salva em: {CONSOLIDADO_PATH}")                                           # informa no console o caminho completo onde o CSV foi salvo
    print("\nPrimeiras linhas:")                                                     # imprime um cabecalho antes de mostrar uma amostra da tabela
    print(df.head(10).to_string(index=False))                                        # imprime as 10 primeiras linhas do DataFrame no console, sem o indice numerico


if __name__ == "__main__":  # garante que main() so execute quando o arquivo for rodado diretamente, nao quando importado
    main()                  # chama a funcao principal, iniciando de fato a consolidacao
