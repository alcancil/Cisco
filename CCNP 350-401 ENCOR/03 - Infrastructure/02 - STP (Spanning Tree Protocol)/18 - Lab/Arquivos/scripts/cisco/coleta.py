"""
coleta.py

Orquestra a coleta automatizada: percorre todos os dispositivos do
inventario, conecta em cada um, executa a lista de comandos definida em
script_02 e salva cada saida em um arquivo individual via output_writer.py.

Uma falha em um dispositivo (timeout, autenticacao) nao interrompe a
coleta dos demais -- o erro e registrado no console e o script segue
para o proximo equipamento.
"""

import time

from connection import conectar, executar_comando, desconectar
from output_writer import salvar_saida

# Numero de tentativas de conexao e pausa entre elas, em segundos.
# Cobre falhas transitorias comuns em lab virtualizado (perda de pacote na
# negociacao SSH, porta ainda em listening/learning do STP, VTY ocupada).
TENTATIVAS_MAXIMAS = 3
PAUSA_ENTRE_TENTATIVAS = 5


def _conectar_com_retry(dispositivo: dict):
    """
    Tenta conectar no dispositivo ate TENTATIVAS_MAXIMAS vezes, com uma
    pausa curta entre cada tentativa. Retorna a conexao, ou None se todas
    as tentativas falharem.
    """
    hostname = dispositivo["hostname"]

    for tentativa in range(1, TENTATIVAS_MAXIMAS + 1):
        try:
            return conectar(dispositivo)
        except Exception:
            if tentativa < TENTATIVAS_MAXIMAS:
                print(f"[{hostname}] Tentativa {tentativa} falhou -- "
                      f"nova tentativa em {PAUSA_ENTRE_TENTATIVAS}s...")
                time.sleep(PAUSA_ENTRE_TENTATIVAS)
            else:
                print(f"[{hostname}] Falha na conexao apos {TENTATIVAS_MAXIMAS} "
                      "tentativas -- pulando este dispositivo.")
    return None


def coletar_dispositivo(dispositivo: dict, comandos: list[str]) -> None:
    """
    Conecta em um unico dispositivo, executa todos os comandos da lista
    e salva cada saida em um arquivo individual.
    """
    hostname = dispositivo["hostname"]
    print(f"\n[{hostname}] Conectando em {dispositivo['host']}...")

    conexao = _conectar_com_retry(dispositivo)
    if conexao is None:
        return

    for comando in comandos:
        print(f"[{hostname}] Executando: {comando}")
        saida = executar_comando(conexao, comando)
        caminho = salvar_saida(hostname, comando, saida)
        print(f"[{hostname}] Saida salva em: {caminho}")

    desconectar(conexao)
    print(f"[{hostname}] Conexao encerrada.")


def coletar_topologia(dispositivos: list[dict], comandos: list[str]) -> None:
    """
    Percorre todos os dispositivos do inventario e executa a coleta em cada um.
    """
    total = len(dispositivos)
    for indice, dispositivo in enumerate(dispositivos, start=1):
        print(f"\n=== Dispositivo {indice}/{total} ===")
        coletar_dispositivo(dispositivo, comandos)
