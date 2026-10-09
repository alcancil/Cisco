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

from output_writer import RAW_OUTPUT_DIR, mapear_comandos, salvar_parsed  # importa a pasta raw, o mapeador de comandos e a funcao que salva o resultado parseado
from parser import parsear_saida                                          # importa a funcao que aplica o TextFSM/NTC-Templates sobre o conteudo bruto
from script_02_automatizar_topologia import COMANDOS                      # importa a mesma lista de comandos usada na coleta, evitando duplicidade

# Mapeia o nome sanitizado do arquivo de volta ao comando original,
# reaproveitando a mesma lista de comandos usada na coleta (Script 02).
# Assim garantimos que Script 02 e Script 03 nunca fiquem dessincronizados.
COMANDO_POR_ARQUIVO = mapear_comandos(COMANDOS)  # constroi o dicionario {nome_de_arquivo: comando_original} usado para identificar cada .txt


def parsear_topologia():                                                            # define a funcao que percorre todos os arquivos brutos e gera as versoes parseadas
    """
    Percorre todos os arquivos brutos coletados em outputs/raw/ e gera a
    versao parseada (estruturada) de cada um em outputs/parsed/.
    """                                                                             # fecha a docstring da funcao, explicando seu proposito
    if not RAW_OUTPUT_DIR.exists():                                                 # verifica se a pasta outputs/raw/ existe antes de tentar percorre-la
        print(f"Pasta {RAW_OUTPUT_DIR} nao encontrada -- rode o Script 02 antes.")  # avisa no console que a coleta ainda nao foi executada
        return                                                                      # encerra a funcao imediatamente, pois nao ha nada para parsear sem a pasta raw

    pastas_dispositivos = sorted(pasta for pasta in RAW_OUTPUT_DIR.iterdir() if pasta.is_dir())  # lista, em ordem alfabetica, todas as subpastas de outputs/raw/ (uma por hostname)

    for pasta_dispositivo in pastas_dispositivos:      # percorre cada pasta de dispositivo encontrada
        hostname = pasta_dispositivo.name              # extrai o nome do hostname a partir do nome da propria pasta
        print(f"\n[{hostname}] Iniciando parsing...")  # informa no console que o parsing deste dispositivo esta comecando

        for arquivo_raw in sorted(pasta_dispositivo.glob("*.txt")):  # percorre, em ordem alfabetica, todos os arquivos .txt salvos para este dispositivo
            comando = COMANDO_POR_ARQUIVO.get(arquivo_raw.stem)      # busca o comando original correspondente ao nome do arquivo (sem a extensao)

            if comando is None:                                                                  # verifica se o nome do arquivo nao bateu com nenhum comando conhecido
                print(f"[{hostname}] Comando desconhecido para {arquivo_raw.name} -- pulando.")  # informa no console que este arquivo sera ignorado por falta de mapeamento
                continue                                                                         # pula para o proximo arquivo da lista, sem tentar parsear este

            conteudo = arquivo_raw.read_text(encoding="utf-8")  # le o conteudo bruto do arquivo .txt como texto
            registros = parsear_saida(comando, conteudo)        # aplica o template TextFSM correspondente e obtem a lista de registros estruturados

            caminho = salvar_parsed(hostname, comando, registros)                        # salva os registros estruturados em outputs/parsed/ e recebe de volta o caminho gerado
            print(f"[{hostname}] {comando}: {len(registros)} registro(s) -> {caminho}")  # informa no console quantos registros foram extraidos e onde o arquivo foi salvo


if __name__ == "__main__":  # garante que parsear_topologia() so execute quando o arquivo for rodado diretamente, nao quando importado
    parsear_topologia()     # chama a funcao principal, iniciando de fato o parsing de toda a topologia
