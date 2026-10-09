"""
Script 02 - Automatizando Toda a Topologia

Objetivo: percorrer automaticamente todo o inventario da rede, conectar em
cada switch, executar a mesma sequencia de comandos e armazenar as saidas
em arquivos individuais e organizados por dispositivo.

Fluxo:
    1. Carrega todos os dispositivos definidos em inventario.yaml.
    2. Para cada dispositivo, abre a conexao SSH (connection.py).
    3. Executa a lista de comandos definida em COMANDOS.
    4. Salva cada saida em arquivos/outputs/raw/<hostname>/<comando>.txt (output_writer.py).
    5. Encerra a sessao e segue para o proximo dispositivo (coleta.py).
"""                                                                                    # fecha a docstring do modulo, que documenta o objetivo e o fluxo do script

from inventory_loader import carregar_inventario                                       # importa a funcao que le o inventario.yaml e devolve todos os dispositivos
from coleta import coletar_topologia                                                   # importa a funcao que orquestra a coleta em todos os dispositivos

# Mesma sequencia de comandos executada em todos os switches do inventario.
# Ajuste esta lista conforme os comandos que voce quer coletar para a
# analise de PVST+ (Parte IV em diante -- parsing com TextFSM/NTC-Templates).
COMANDOS = [                                                                           # inicia a lista de comandos que serao executados em cada dispositivo do inventario
    "show spanning-tree summary",                                                      # comando que traz um resumo do estado do STP em todas as VLANs
    "show spanning-tree",                                                              # comando que traz o detalhamento completo do STP por instancia de VLAN
    "show vlan brief",                                                                 # comando que lista as VLANs configuradas e suas portas associadas
    "show interfaces trunk",                                                           # comando que lista as interfaces em modo trunk e as VLANs permitidas
]                                                                                      # fecha a lista de comandos COMANDOS


def main():                                                                            # define a funcao principal que orquestra todo o fluxo do script
    dispositivos = carregar_inventario()                                               # carrega todos os dispositivos definidos no inventario.yaml
    print(f"Inventario carregado: {len(dispositivos)} dispositivo(s) encontrado(s).")  # informa no console quantos dispositivos foram encontrados no inventario

    coletar_topologia(dispositivos, COMANDOS)                                          # dispara a coleta completa (conexao + comandos + salvamento) em todos os dispositivos

    print("\nColeta finalizada em todos os dispositivos do inventario.")               # informa no console que a coleta de toda a topologia foi concluida


if __name__ == "__main__":                                                             # garante que main() so execute quando o arquivo for rodado diretamente, nao quando importado
    main()                                                                             # chama a funcao principal, iniciando de fato o fluxo do script
