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
"""

from inventory_loader import carregar_inventario
from coleta import coletar_topologia

# Mesma sequencia de comandos executada em todos os switches do inventario.
# Ajuste esta lista conforme os comandos que voce quer coletar para a
# analise de PVST+ (Parte IV em diante -- parsing com TextFSM/NTC-Templates).
COMANDOS = [
    "show spanning-tree summary",
    "show spanning-tree",
    "show spanning-tree root",
    "show vlan brief",
    "show interfaces trunk",
    "show interfaces",
    "show processes cpu",
    "show cdp neighbors detail",

]


def main():
    dispositivos = carregar_inventario()
    print(f"Inventario carregado: {len(dispositivos)} dispositivo(s) encontrado(s).")

    coletar_topologia(dispositivos, COMANDOS)

    print("\nColeta finalizada em todos os dispositivos do inventario.")


if __name__ == "__main__":
    main()
