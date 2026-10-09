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
"""

import pandas as pd

from output_writer import PARSED_OUTPUT_DIR
from consolidador import consolidar_topologia

CONSOLIDADO_DIR = PARSED_OUTPUT_DIR.parent / "consolidado"
CONSOLIDADO_PATH = CONSOLIDADO_DIR / "tabela_consolidada.csv"


def main():
    if not PARSED_OUTPUT_DIR.exists():
        print(f"Pasta {PARSED_OUTPUT_DIR} nao encontrada -- rode o Script 03 antes.")
        return

    hostnames = sorted(pasta.name for pasta in PARSED_OUTPUT_DIR.iterdir() if pasta.is_dir())
    print(f"Consolidando dados de {len(hostnames)} switch(es)...")

    linhas = consolidar_topologia(hostnames)
    df = pd.DataFrame(linhas)

    CONSOLIDADO_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CONSOLIDADO_PATH, index=False, encoding="utf-8")

    print(f"\nTabela consolidada: {len(df)} linha(s), {len(df.columns)} coluna(s)")
    print(f"Salva em: {CONSOLIDADO_PATH}")
    print("\nPrimeiras linhas:")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
