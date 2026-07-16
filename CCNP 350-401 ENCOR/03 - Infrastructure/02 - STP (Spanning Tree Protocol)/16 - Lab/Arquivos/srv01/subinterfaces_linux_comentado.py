#!/usr/bin/env python3                             # Define o interpretador Python a ser usado (o primeiro encontrado no PATH)
import os                                          # Importa o módulo 'os' para interagir com o sistema operacional (arquivos, permissões, etc.)
import subprocess                                  # Importa o módulo 'subprocess' para executar comandos externos (apt, ip, modprobe, etc.)
import shutil                                      # Importa 'shutil' para operações de cópia e remoção de arquivos
import re                                          # Importa o módulo 're' para usar expressões regulares (busca e substituição de padrões)
from datetime import datetime                      # Importa a classe 'datetime' para trabalhar com data e hora (usada nos backups)
import glob                                        # Importa 'glob' para listar arquivos que correspondem a um padrão (usado na restauração de backups)

# ========= CONFIGURAÇÃO =========                 # Início da seção de configurações globais do script
INTERFACE_PROBLEMA = "ens3"                        # Define a interface usada no modo problema (todas as VLANs em uma única placa)
INTERFACE_IMPAR = "ens3"                           # Define a interface para as VLANs ímpares (posições pares na lista) no modo balanceamento
INTERFACE_PAR = "ens4"                             # Define a interface para as VLANs pares (posições ímpares na lista) no modo balanceamento
VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Lista das VLANs que serão configuradas (10 a 100, de 10 em 10)
CONFIG_FILE = "/etc/network/interfaces"            # Caminho do arquivo de configuração de redes do Debian
# =================================                # Fim da seção de configurações

# ========= FUNÇÕES DE BACKUP E RESTAURAÇÃO =========                      # Início das funções relacionadas a backup e restauração
def fazer_backup_arquivo():                                                # Define a função que cria backup do arquivo de interfaces
    """Faz backup do arquivo de interfaces"""                              # Docstring da função
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")                   # Gera um timestamp no formato YYYYMMDD_HHMMSS
    backup_file = f"{CONFIG_FILE}.backup_{timestamp}"                      # Cria o nome do arquivo de backup (ex: /etc/network/interfaces.backup_20250101_120000)
    print(f"🔐 Backup do arquivo de interfaces criado em: {backup_file}")  # Exibe mensagem informando o backup
    shutil.copy2(CONFIG_FILE, backup_file)                                 # Copia o arquivo original para o destino, preservando metadados
    return backup_file                                                     # Retorna o caminho do arquivo de backup

def fazer_backup_script():                                    # Define a função que cria backup do próprio script
    """Faz backup do próprio script"""                        # Docstring da função
    script_path = os.path.realpath(__file__)                  # Obtém o caminho completo do script atual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")      # Gera um timestamp no formato YYYYMMDD_HHMMSS
    backup_script = f"{script_path}.backup_{timestamp}"       # Cria o nome do arquivo de backup do script
    shutil.copy2(script_path, backup_script)                  # Copia o script para o destino
    print(f"📄 Backup do script criado em: {backup_script}")  # Exibe mensagem informando o backup do script
    return backup_script                                      # Retorna o caminho do arquivo de backup

def listar_backups():                                            # Define a função que lista os backups do arquivo de interfaces
    """Lista os backups do arquivo de interfaces disponíveis"""  # Docstring da função
    backups = glob.glob(f"{CONFIG_FILE}.backup_*")               # Busca todos os arquivos que correspondem ao padrão (interfaces.backup_*)
    if not backups:                                              # Se a lista estiver vazia (nenhum backup encontrado)
        print("Nenhum backup encontrado.")                       # Informa que não há backups
        return []                                                # Retorna uma lista vazia
    print("\n📂 Backups disponíveis:")                          # Exibe o cabeçalho da lista
    for i, b in enumerate(backups):                              # Percorre a lista de backups com índice
        print(f"  {i+1}. {b}")                                   # Exibe o número e o caminho do backup
    return backups                                               # Retorna a lista de backups

def restaurar_backup():                                                                  # Define a função que restaura um backup do arquivo de interfaces
    """Restaura um backup do arquivo de interfaces"""                                    # Docstring da função
    backups = listar_backups()                                                           # Obtém a lista de backups disponíveis
    if not backups:                                                                      # Se não houver backups
        return                                                                           # Sai da função
    escolha = input("Digite o número do backup a restaurar (ou Enter para cancelar): ")  # Pergunta qual backup restaurar
    if not escolha.isdigit() or int(escolha) > len(backups):                             # Se a entrada não for um número válido ou estiver fora do intervalo
        print("Restauração cancelada.")                                                  # Informa cancelamento
        return                                                                           # Sai da função
    backup = backups[int(escolha)-1]                                                     # Obtém o caminho do backup selecionado (índice 0-based)
    shutil.copy2(backup, CONFIG_FILE)                                                    # Copia o backup para o lugar do arquivo original
    print(f"✅ Backup {backup} restaurado com sucesso.")                                # Confirma a restauração
    print("🔄 Reinicie o serviço de rede com: sudo systemctl restart networking")       # Instrução para reiniciar a rede

# ========= FUNÇÕES DE LIMPEZA TOTAL =========                                                   # Início das funções que limpam configurações antigas
def limpar_interface_do_arquivo(interface):                                                      # Define a função que remove todas as configurações de uma interface do arquivo
    """Remove TODAS as linhas relacionadas a uma interface (física, subinterfaces, dhcp, etc.) do arquivo de configuração"""  # Docstring da função
    try:                                                                                         # Tenta ler o arquivo existente
        with open(CONFIG_FILE, "r") as f:                                                        # Abre o arquivo no modo leitura
            linhas = f.readlines()                                                               # Lê todas as linhas para uma lista
    except FileNotFoundError:                                                                    # Se o arquivo não existir
        linhas = []                                                                              # Usa uma lista vazia
    novas_linhas = []                                                                            # Cria uma lista para armazenar as novas linhas
    ignorar = False                                                                              # Flag para indicar se a linha atual deve ser ignorada
    for linha in linhas:                                                                         # Percorre cada linha do arquivo original
        if re.search(rf"\b{interface}\b", linha):                                                # Se a linha contém o nome da interface (incluindo sub interfaces)
            ignorar = True                                                                       # Ativa o modo 'ignorar'
            continue                                                                             # Pula para a próxima iteração (não adiciona esta linha)
        if ignorar and linha.startswith(("allow-hotplug", "iface", "auto", "source")):           # Se estamos ignorando e a linha começa com uma nova definição
            ignorar = False                                                                      # Desativa o modo 'ignorar' (parou o bloco)
        if not ignorar:                                                                          # Se não estiver no modo 'ignorar'
            novas_linhas.append(linha)                                                           # Adiciona a linha original à nova lista
    with open(CONFIG_FILE, "w") as f:                                                            # Abre o arquivo no modo escrita (sobrescreve)
        f.writelines(novas_linhas)                                                               # Escreve todas as novas linhas

def escrever_interface_fisica_manual(interface):                         # Define a função que adiciona a configuração manual da interface física no arquivo
    """Adiciona a configuração manual da interface física no arquivo"""  # Docstring da função
    with open(CONFIG_FILE, "a") as f:                                    # Abre o arquivo no modo 'append' (adicionar ao final)
        f.write(f"\n# Interface física {interface} (manual, sem IP)\n")  # Escreve um comentário com o nome da interface
        f.write(f"allow-hotplug {interface}\n")                          # Permite que a interface seja ativada automaticamente ao ser plugada
        f.write(f"iface {interface} inet manual\n")                      # Define a interface como 'manual' (sem IP automático)
        f.write(f"    up ip link set {interface} up\n")                  # Comando executado quando a interface sobe: ativa a interface
        f.write(f"    down ip link set {interface} down\n")              # Comando executado quando a interface desce: desativa a interface

def escrever_subinterface_vlan(interface, vlan):                       # Define a função que adiciona a configuração de uma subinterface VLAN no arquivo
    """Adiciona a configuração de uma subinterface VLAN no arquivo"""  # Docstring da função
    with open(CONFIG_FILE, "a") as f:                                  # Abre o arquivo no modo 'append' (adicionar ao final)
        f.write(f"\n# VLAN {vlan} - Interface {interface}.{vlan}\n")   # Escreve um comentário com a VLAN e a interface
        f.write(f"allow-hotplug {interface}.{vlan}\n")                 # Permite que a subinterface seja ativada automaticamente
        f.write(f"iface {interface}.{vlan} inet static\n")             # Define a subinterface como estática (IP fixo)
        f.write(f"    address 10.0.{vlan}.254/24\n")                   # Define o IP da subinterface (ex: 10.0.10.254/24)
        f.write(f"    vlan-raw-device {interface}\n")                  # Indica que a VLAN é criada sobre a interface física 'interface'

def carregar_modulo_vlan():                                            # Define a função que carrega o módulo 8021q
    print("🔌 Carregando módulo 8021q...")                             # Exibe mensagem informando que vai carregar o módulo
    subprocess.run(["sudo", "modprobe", "8021q"], check=True)          # Executa 'sudo modprobe 8021q' para carregar o módulo

def garantir_interface_pai_up(interface):                                       # Define a função que garante que a interface pai esteja UP
    """Garante que a interface pai esteja UP"""                                 # Docstring da função
    print(f"⬆️  Garantindo que a interface {interface} esteja UP...")          # Exibe mensagem informando que vai ativar a interface
    subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)  # Executa 'sudo ip link set interface up' para ativar a interface

def ativar_interface_kernel(interface, vlan):                                                                  # Define a função que ativa a VLAN imediatamente no kernel
    """Ativa a VLAN imediatamente no kernel"""                                                                 # Docstring da função
    nome_iface = f"{interface}.{vlan}"                                                                         # Nome da subinterface (ex: ens3.10)
    ip_vlan = f"10.0.{vlan}.254/24"                                                                            # IP da subinterface com máscara
    subprocess.run(                                                                                            # Executa o comando para criar a subinterface
        ["sudo", "ip", "link", "add", "link", interface, "name", nome_iface, "type", "vlan", "id", str(vlan)], # Comando para adicionar a VLAN
        stderr=subprocess.DEVNULL,                                                                             # Redireciona erros para /dev/null (ignora)
        check=False                                                                                            # Não interrompe o script se houver erro (já pode existir)
    )
    garantir_interface_pai_up(interface)                                                 # Garante que a interface pai esteja UP
    subprocess.run(["sudo", "ip", "link", "set", "dev", nome_iface, "up"], check=True)   # Ativa a subinterface (coloca UP)
    subprocess.run(                                                                      # Adiciona o endereço IP à subinterface
        ["sudo", "ip", "addr", "add", ip_vlan, "dev", nome_iface],                       # Comando para adicionar o IP
        stderr=subprocess.DEVNULL,                                                       # Ignora erros (se o IP já existir, não quebra)
        check=False
    )
    print(f"   ✔ {nome_iface} ativada (IP: {ip_vlan})")                                  # Confirma a ativação

# ========= OPÇÕES DE CONFIGURAÇÃO =========                                                      # Início das funções que configuram os modos problema e balanceamento
def configurar_modo_problema():                                                                   # Define a função que configura todas as VLANs em uma única interface (ens3)
    """Configura todas as VLANs em uma única interface (ens3)"""                                  # Docstring da função
    print(f"\n⚠️  Modo Problema: Todas as VLANs em {INTERFACE_PROBLEMA}")                        # Exibe mensagem informando o modo problema
    limpar_interface_do_arquivo(INTERFACE_PROBLEMA)                                               # Limpa configurações antigas da ens3
    limpar_interface_do_arquivo(INTERFACE_PAR)                                                    # Limpa configurações antigas da ens4 (para evitar conflitos)
    escrever_interface_fisica_manual(INTERFACE_PROBLEMA)                                          # Escreve a configuração manual da ens3
    escrever_interface_fisica_manual(INTERFACE_PAR)                                               # Escreve a configuração manual da ens4 (para evitar DHCP)
    for vlan in VLANS:                                                                            # Percorre a lista de VLANs
        escrever_subinterface_vlan(INTERFACE_PROBLEMA, vlan)                                      # Adiciona a VLAN no arquivo, na ens3
        ativar_interface_kernel(INTERFACE_PROBLEMA, vlan)                                         # Ativa a VLAN imediatamente no kernel
    print("\n✅ Configuração concluída! As interfaces agora devem ficar UP.")                     # Exibe mensagem de conclusão
    print("💡 Dica: Se ainda houver algum problema, execute: sudo systemctl restart networking")  # Dica de solução de problemas

def configurar_modo_balanceamento():                                                                # Define a função que configura VLANs em ordem alternada nas duas interfaces
    """Configura VLANs em ordem alternada: 1ª, 3ª, 5ª, 7ª, 9ª na ens3; 2ª, 4ª, 6ª, 8ª, 10ª na ens4"""  # Docstring da função
    print(f"\n⚖️  Modo Balanceamento: Ímpares na lista (10,30,50,70,90) em {INTERFACE_IMPAR}, Pares na lista (20,40,60,80,100) em {INTERFACE_PAR}")  # Exibe mensagem do modo balanceamento
    limpar_interface_do_arquivo(INTERFACE_IMPAR)                                                  # Limpa configurações antigas da ens3
    limpar_interface_do_arquivo(INTERFACE_PAR)                                                    # Limpa configurações antigas da ens4
    escrever_interface_fisica_manual(INTERFACE_IMPAR)                                             # Escreve a configuração manual da ens3
    escrever_interface_fisica_manual(INTERFACE_PAR)                                               # Escreve a configuração manual da ens4
    for idx, vlan in enumerate(VLANS):                                                            # Percorre a lista de VLANs com índice
        if idx % 2 == 0:                                                                          # Se o índice é par (0, 2, 4, 6, 8) → VLANs 10, 30, 50, 70, 90
            escrever_subinterface_vlan(INTERFACE_IMPAR, vlan)                                     # Adiciona a VLAN no arquivo, na ens3
            ativar_interface_kernel(INTERFACE_IMPAR, vlan)                                        # Ativa a VLAN imediatamente no kernel
        else:                                                                                     # Se o índice é ímpar (1, 3, 5, 7, 9) → VLANs 20, 40, 60, 80, 100
            escrever_subinterface_vlan(INTERFACE_PAR, vlan)                                       # Adiciona a VLAN no arquivo, na ens4
            ativar_interface_kernel(INTERFACE_PAR, vlan)                                          # Ativa a VLAN imediatamente no kernel
    print("\n✅ Configuração concluída! As interfaces agora devem ficar UP.")                     # Exibe mensagem de conclusão
    print("💡 Dica: Se ainda houver algum problema, execute: sudo systemctl restart networking")  # Dica de solução de problemas

# ========= MENU PRINCIPAL =========                                        # Início do menu interativo
def exibir_menu():                                                          # Define a função que exibe o menu principal
    """Exibe o menu principal"""                                            # Docstring da função
    print("\n" + "="*50)                                                    # Imprime uma linha de separação
    print("  Gerenciador de VLANs no Linux")                                # Título do menu
    print("="*50)                                                           # Imprime outra linha de separação
    print("  1. Realizar Backup das Interfaces")                            # Opção 1
    print("  2. Restaurar Backup das Interfaces")                           # Opção 2
    print("  3. Configurar Interfaces em uma placa (sem balanceamento)")    # Opção 3
    print("  4. Configurar Interfaces em duas placas (com balanceamento)")  # Opção 4
    print("  5. Sair")                                                      # Opção 5
    print("="*50)                                                           # Imprime linha de separação no final

def main():                                                                  # Define a função principal do script
    if os.geteuid() != 0:                                                    # Verifica se o script está sendo executado como root (UID 0)
        print("❌ Este script precisa ser executado com sudo.")             # Se não for root, exibe erro
        return                                                               # Encerra o script
    fazer_backup_script()                                                    # Faz backup do próprio script sempre que executado
    while True:                                                              # Inicia um loop infinito (até o usuário escolher sair)
        exibir_menu()                                                        # Chama a função que exibe o menu
        opcao = input("Escolha uma opção (1-5): ").strip()                   # Solicita a opção do usuário
        if opcao == "1":                                                     # Se a opção for 1
            fazer_backup_arquivo()                                           # Chama a função que faz backup do arquivo de interfaces
            print("✅ Backup concluído.")                                   # Confirma a conclusão do backup
        elif opcao == "2":                                                   # Se a opção for 2
            restaurar_backup()                                               # Chama a função que restaura um backup
        elif opcao == "3":                                                   # Se a opção for 3
            backup_arquivo = fazer_backup_arquivo()                          # Faz backup do arquivo antes de configurar
            configurar_modo_problema()                                       # Chama a função que configura o modo problema
            print(f"📄 Backup do arquivo de interfaces: {backup_arquivo}")   # Mostra o caminho do backup
        elif opcao == "4":                                                   # Se a opção for 4
            backup_arquivo = fazer_backup_arquivo()                          # Faz backup do arquivo antes de configurar
            configurar_modo_balanceamento()                                  # Chama a função que configura o modo balanceamento
            print(f"📄 Backup do arquivo de interfaces: {backup_arquivo}")   # Mostra o caminho do backup
        elif opcao == "5":                                                   # Se a opção for 5
            print("Saindo...")                                               # Exibe mensagem de saída
            break                                                            # Sai do loop while (encerra o script)
        else:                                                                # Se a opção não for nenhuma das anteriores
            print("⚠️  Opção inválida. Tente novamente.")                   # Exibe mensagem de erro e volta ao menu

if __name__ == "__main__":                                                   # Verifica se o script foi executado diretamente (não importado como módulo)
    main()                                                                   # Chama a função principal