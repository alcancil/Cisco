"""
coleta.py

Orquestra a coleta automatizada: percorre todos os dispositivos do
inventario, conecta em cada um, executa a lista de comandos definida em
script_02 e salva cada saida em um arquivo individual via output_writer.py.

Uma falha em um dispositivo (timeout, autenticacao) nao interrompe a
coleta dos demais -- o erro e registrado no console e o script segue
para o proximo equipamento.
"""                                                                                # fecha a docstring do modulo, que documenta o proposito e a tolerancia a falha

import time                                                                        # importa o modulo usado para pausar a execucao entre tentativas de conexao

from connection import conectar, executar_comando, desconectar                     # importa as funcoes de conexao, execucao de comando e desconexao
from output_writer import salvar_saida                                             # importa a funcao que salva cada saida coletada em arquivo individual

# Numero de tentativas de conexao e pausa entre elas, em segundos.
# Cobre falhas transitorias comuns em lab virtualizado (perda de pacote na
# negociacao SSH, porta ainda em listening/learning do STP, VTY ocupada).
TENTATIVAS_MAXIMAS = 3                                                             # define o numero maximo de tentativas de conexao por dispositivo
PAUSA_ENTRE_TENTATIVAS = 5                                                         # define a pausa em segundos entre uma tentativa e a proxima


def _conectar_com_retry(dispositivo: dict):                                        # define a funcao interna que tenta conectar com repeticao automatica
    """
    Tenta conectar no dispositivo ate TENTATIVAS_MAXIMAS vezes, com uma
    pausa curta entre cada tentativa. Retorna a conexao, ou None se todas
    as tentativas falharem.
    """                                                                            # fecha a docstring da funcao, explicando o comportamento de retry
    hostname = dispositivo["hostname"]                                             # extrai o hostname apenas para identificar o dispositivo nas mensagens de log

    for tentativa in range(1, TENTATIVAS_MAXIMAS + 1):                             # percorre as tentativas de 1 ate TENTATIVAS_MAXIMAS, incluindo o limite
        try:                                                                       # inicia o bloco protegido, pois cada tentativa de conexao pode falhar
            return conectar(dispositivo)                                           # se a conexao funcionar, retorna imediatamente e encerra a funcao
        except Exception:                                                          # captura qualquer falha de conexao (timeout, autenticacao, etc.) para decidir se tenta de novo
            if tentativa < TENTATIVAS_MAXIMAS:                                     # verifica se ainda ha tentativas restantes antes de desistir
                print(f"[{hostname}] Tentativa {tentativa} falhou -- "             # informa no console qual tentativa falhou (inicio da mensagem, continua na proxima linha)
                      f"nova tentativa em {PAUSA_ENTRE_TENTATIVAS}s...")           # completa a mensagem informando em quantos segundos a proxima tentativa ocorrera
                time.sleep(PAUSA_ENTRE_TENTATIVAS)                                 # pausa a execucao pelo tempo definido antes de tentar conectar novamente
            else:                                                                  # executa quando a ultima tentativa tambem falhou
                print(f"[{hostname}] Falha na conexao apos {TENTATIVAS_MAXIMAS} "  # informa no console que todas as tentativas se esgotaram (inicio da mensagem)
                      "tentativas -- pulando este dispositivo.")                   # completa a mensagem avisando que este dispositivo sera pulado
    return None                                                                    # retorna None quando todas as tentativas falharam, sinalizando ao chamador que nao ha conexao


def coletar_dispositivo(dispositivo: dict, comandos: list[str]) -> None:           # define a funcao que coleta todos os comandos de um unico dispositivo
    """
    Conecta em um unico dispositivo, executa todos os comandos da lista
    e salva cada saida em um arquivo individual.
    """                                                                            # fecha a docstring da funcao, explicando seu proposito
    hostname = dispositivo["hostname"]                                             # extrai o hostname do dicionario para usar nas mensagens de log
    print(f"\n[{hostname}] Conectando em {dispositivo['host']}...")                # informa no console qual dispositivo esta sendo alvo da conexao

    conexao = _conectar_com_retry(dispositivo)                                     # tenta estabelecer a conexao usando a logica de retry definida acima
    if conexao is None:                                                            # verifica se todas as tentativas de conexao falharam
        return                                                                     # encerra a funcao imediatamente, pulando este dispositivo, se a conexao nao foi obtida

    for comando in comandos:                                                       # percorre cada comando da lista recebida como parametro
        print(f"[{hostname}] Executando: {comando}")                               # informa no console qual comando esta sendo executado no momento
        saida = executar_comando(conexao, comando)                                 # executa o comando na sessao aberta e guarda a saida retornada
        caminho = salvar_saida(hostname, comando, saida)                           # salva a saida em arquivo individual e recebe de volta o caminho gerado
        print(f"[{hostname}] Saida salva em: {caminho}")                           # informa no console o caminho completo do arquivo que acabou de ser salvo

    desconectar(conexao)                                                           # encerra a sessao SSH apos executar todos os comandos da lista
    print(f"[{hostname}] Conexao encerrada.")                                      # confirma no console que a sessao deste dispositivo foi encerrada


def coletar_topologia(dispositivos: list[dict], comandos: list[str]) -> None:      # define a funcao que percorre todo o inventario e aciona a coleta em cada dispositivo
    """
    Percorre todos os dispositivos do inventario e executa a coleta em cada um.
    """                                                                            # fecha a docstring da funcao, explicando seu proposito
    total = len(dispositivos)                                                      # calcula o total de dispositivos, usado apenas para exibir o progresso no console
    for indice, dispositivo in enumerate(dispositivos, start=1):                   # percorre a lista de dispositivos, numerando a partir de 1 para exibicao
        print(f"\n=== Dispositivo {indice}/{total} ===")                           # exibe um cabecalho indicando o progresso da coleta (ex: Dispositivo 3/8)
        coletar_dispositivo(dispositivo, comandos)                                 # chama a coleta completa (conexao + comandos + salvamento) para este dispositivo
