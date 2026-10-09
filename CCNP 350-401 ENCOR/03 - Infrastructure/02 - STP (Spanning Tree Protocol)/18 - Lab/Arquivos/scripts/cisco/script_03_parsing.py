"""
Script 03 - Parsing das Saidas da CLI

Objetivo: percorrer todos os arquivos gerados pelo Script 02 em
outputs/raw/, aplicar o template TextFSM correspondente a cada comando
(via NTC-Templates) e salvar o resultado estruturado em outputs/parsed/.

Fluxo:
    1. Percorre cada subpasta de outputs/raw/ (uma por hostname).
    2. Para cada arquivo .txt, identifica o comando original que o gerou.
    3. Aplica o parsing com TextFSM/NTC-Templates (parser.py).
    4. Salva os registros estruturados em outputs/parsed/<hostname>/<comando>.json (output_writer.py).
"""

from output_writer import RAW_OUTPUT_DIR, mapear_comandos, salvar_parsed
from parser import parsear_saida
from script_02_automatizar_topologia import COMANDOS

# Mapeia o nome sanitizado do arquivo de volta ao comando original,
# reaproveitando a mesma lista de comandos usada na coleta (Script 02).
# Assim garantimos que Script 02 e Script 03 nunca fiquem dessincronizados.
COMANDO_POR_ARQUIVO = mapear_comandos(COMANDOS)


def parsear_topologia():
    """
    Percorre todos os arquivos brutos coletados em outputs/raw/ e gera a
    versao parseada (estruturada) de cada um em outputs/parsed/.
    """
    if not RAW_OUTPUT_DIR.exists():
        print(f"Pasta {RAW_OUTPUT_DIR} nao encontrada -- rode o Script 02 antes.")
        return

    pastas_dispositivos = sorted(pasta for pasta in RAW_OUTPUT_DIR.iterdir() if pasta.is_dir())

    for pasta_dispositivo in pastas_dispositivos:
        hostname = pasta_dispositivo.name
        print(f"\n[{hostname}] Iniciando parsing...")

        for arquivo_raw in sorted(pasta_dispositivo.glob("*.txt")):
            comando = COMANDO_POR_ARQUIVO.get(arquivo_raw.stem)

            if comando is None:
                print(f"[{hostname}] Comando desconhecido para {arquivo_raw.name} -- pulando.")
                continue

            conteudo = arquivo_raw.read_text(encoding="utf-8")
            registros = parsear_saida(comando, conteudo)

            caminho = salvar_parsed(hostname, comando, registros)
            print(f"[{hostname}] {comando}: {len(registros)} registro(s) -> {caminho}")


if __name__ == "__main__":
    parsear_topologia()
