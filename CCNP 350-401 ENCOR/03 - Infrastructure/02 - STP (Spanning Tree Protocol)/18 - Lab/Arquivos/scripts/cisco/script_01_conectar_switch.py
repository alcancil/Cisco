"""
Script 01 - Conectando a um Switch

Objetivo: validar a comunicacao com um unico equipamento antes de expandir
a automacao para toda a topologia (Script 02).

Fluxo:
    1. Busca o dispositivo alvo em inventario.yaml (via inventory_loader.py).
    2. Combina os dados de conexao com as credenciais do .env.
    3. Abre a conexao SSH via Netmiko (connection.py).
    4. Executa um comando simples.
    5. Exibe a saida.
    6. Encerra a sessao corretamente.
"""

from inventory_loader import obter_dispositivo
from connection import conectar, executar_comando, desconectar

HOSTNAME_ALVO = "SW_DST01"   # troque aqui para testar outro equipamento do inventario
COMANDO_TESTE = "show version"


def main():
    dispositivo = obter_dispositivo(HOSTNAME_ALVO)

    print(f"Conectando em {dispositivo['hostname']} ({dispositivo['host']})...")
    conexao = conectar(dispositivo)

    print("Conexao estabelecida. Executando comando de teste...")
    saida = executar_comando(conexao, COMANDO_TESTE)

    print("\n--- Saida do comando ---\n")
    print(saida)

    desconectar(conexao)
    print("\nConexao encerrada com sucesso.")


if __name__ == "__main__":
    main()
