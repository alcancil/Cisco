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
"""                                                                               # fecha a docstring do modulo, que documenta o objetivo e o fluxo do script

from inventory_loader import obter_dispositivo                                    # importa a funcao que busca um dispositivo especifico no inventario.yaml
from connection import conectar, executar_comando, desconectar                    # importa as funcoes de conexao, execucao de comando e desconexao

HOSTNAME_ALVO = "SW_DST01"                                                        # troque aqui para testar outro equipamento do inventario
COMANDO_TESTE = "show version"                                                    # define o comando IOS usado apenas para validar a conexao


def main():                                                                       # define a funcao principal que orquestra todo o fluxo do script
    dispositivo = obter_dispositivo(HOSTNAME_ALVO)                                # busca no inventario o dicionario de conexao do hostname definido em HOSTNAME_ALVO

    print(f"Conectando em {dispositivo['hostname']} ({dispositivo['host']})...")  # informa no console qual dispositivo esta sendo alvo da conexao
    conexao = conectar(dispositivo)                                               # abre a sessao SSH usando a funcao conectar de connection.py

    print("Conexao estabelecida. Executando comando de teste...")                 # informa no console que a conexao foi aberta com sucesso
    saida = executar_comando(conexao, COMANDO_TESTE)                              # executa o comando de teste na sessao aberta e guarda a saida retornada

    print("\n--- Saida do comando ---\n")                                         # imprime um cabecalho visual antes de mostrar a saida do comando
    print(saida)                                                                  # imprime no console a saida bruta retornada pelo equipamento

    desconectar(conexao)                                                          # encerra a sessao SSH usando a funcao desconectar de connection.py
    print("\nConexao encerrada com sucesso.")                                     # confirma no console que a sessao foi encerrada corretamente


if __name__ == "__main__":                                                        # garante que main() so execute quando o arquivo for rodado diretamente, nao quando importado
    main()                                                                        # chama a funcao principal, iniciando de fato o fluxo do script
