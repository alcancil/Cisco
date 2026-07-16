#!/usr/bin/env python3  # Define o interpretador Python a ser usado (o primeiro encontrado no PATH)
import os                              # Importa o módulo 'os' para interagir com o sistema operacional (arquivos, permissões, etc.)
import subprocess                      # Importa o módulo 'subprocess' para executar comandos externos (apt, ip, modprobe, etc.)
import re                              # Importa o módulo 're' para usar expressões regulares (busca e substituição de padrões)
import shutil                          # Importa 'shutil' para operações de cópia e remoção de arquivos
from datetime import datetime          # Importa a classe 'datetime' para trabalhar com data e hora (usada nos backups)
import glob                            # Importa 'glob' para listar arquivos que correspondem a um padrão (usado na restauração de backups)

# ========= CONFIGURAÇÕES =========                # Início da seção de configurações globais do script
VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Lista das VLANs que serão configuradas (10 a 100, de 10 em 10)
CONFIG_FILE = "/etc/network/interfaces"            # Caminho do arquivo de configuração de redes do Debian
# =================================                # Fim da seção de configurações

def detectar_interface_principal():                                                                  # Define a função que detecta a interface de rede ativa
    """Detecta automaticamente a interface ativa (ex: ens3)"""                                       # Docstring da função
    try:                                                                                             # Inicia um bloco de tratamento de exceções (para capturar erros)
        result = subprocess.run(["ip", "addr", "show"], capture_output=True, text=True, check=True)  # Executa 'ip addr show' e captura a saída
        for line in result.stdout.split("\n"):                                                       # Percorre cada linha da saída do comando
            if "inet " in line and "lo" not in line:                                                 # Se a linha contém um IP e não é a interface de loopback ('lo')
                match = re.search(r"\d+: (\w+):", line)                                              # Busca o nome da interface (ex: 'ens3') usando regex
                if match:                                                                            # Se encontrou um nome
                    return match.group(1)                                                            # Retorna o nome da interface
        return "ens3"                                                                                # Se não encontrou nenhuma, retorna 'ens3' como padrão
    except:                                                                                          # Se ocorrer qualquer erro no bloco try
        return "ens3"                                                                                # Retorna 'ens3' como fallback

def fazer_backup_arquivo():                                                             # Define a função que cria backup do arquivo de interfaces
    """Faz backup do arquivo de interfaces"""                                           # Docstring da função
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")                                # Gera um timestamp no formato YYYYMMDD_HHMMSS
    backup_file = f"{CONFIG_FILE}.backup_{timestamp}"                                   # Cria o nome do arquivo de backup (ex: /etc/network/interfaces.backup_20250101_120000)
    print(f"🔐 Backup do arquivo de interfaces criado em: {backup_file}")              # Exibe mensagem informando o backup
    shutil.copy2(CONFIG_FILE, backup_file)                                              # Copia o arquivo original para o destino, preservando metadados
    return backup_file                                                                  # Retorna o caminho do arquivo de backup

def fazer_backup_script():                                                              # Define a função que cria backup do próprio script
    """Faz backup do próprio script"""                                                  # Docstring da função
    script_path = os.path.realpath(__file__)                                            # Obtém o caminho completo do script atual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")                                # Gera um timestamp no formato YYYYMMDD_HHMMSS
    backup_script = f"{script_path}.backup_{timestamp}"                                 # Cria o nome do arquivo de backup do script
    shutil.copy2(script_path, backup_script)                                            # Copia o script para o destino
    print(f"📄 Backup do script criado em: {backup_script}")                            # Exibe mensagem informando o backup do script
    return backup_script                                                                # Retorna o caminho do arquivo de backup

def verificar_e_carregar_modulo_vlan():                                                 # Define a função que verifica e carrega o módulo 8021q
    """Verifica se o módulo 8021q está carregado. Se não, carrega."""                   # Docstring da função
    result = subprocess.run(["lsmod"], capture_output=True, text=True)                  # Executa 'lsmod' para listar módulos carregados
    if "8021q" in result.stdout:                                                        # Verifica se o módulo '8021q' aparece na lista
        print("✅ Módulo 8021q já está carregado.")                                    # Se já estiver, exibe mensagem de sucesso
        return                                                                          # Retorna sem fazer nada
    print("🔌 Carregando módulo 8021q...")                                             # Se não estiver, informa que vai carregar
    subprocess.run(["sudo", "modprobe", "8021q"], check=True)                           # Executa 'sudo modprobe 8021q' para carregar o módulo
    print("✅ Módulo 8021q carregado com sucesso.")                                    # Confirma o carregamento

def configurar_interface_fisica(interface_base):                                          # Define a função que configura a interface física (com ou sem IP)
    """Pergunta os dados da interface física e retorna as linhas de configuração"""       # Docstring da função
    print("\n🖧  CONFIGURAÇÃO DA INTERFACE FÍSICA")                                       # Exibe título da seção
    resp = input("Deseja configurar a interface física com IP? (s/n): ").strip().lower()  # Pergunta se o usuário quer IP
    linhas = [                                                                            # Inicia a lista de linhas para a configuração (modo padrão: manual, sem IP)
        f"allow-hotplug {interface_base}",                                                # Permite que a interface seja ativada automaticamente ao ser plugada
        f"iface {interface_base} inet manual",                                            # Define a interface como 'manual' (sem IP automático)
        f"    up ip link set {interface_base} up",                                        # Comando executado quando a interface sobe: ativa a interface
        f"    down ip link set {interface_base} down"                                     # Comando executado quando a interface desce: desativa a interface
    ]
    if resp == "s":                                                                       # Se o usuário respondeu 's' (sim)
        ip = input("IP da interface (ex: 10.0.80.1): ").strip()                           # Solicita o IP da interface
        mascara = input("Máscara em CIDR (ex: 24): ").strip()                             # Solicita a máscara (em formato CIDR)
        gateway = input("Gateway (ex: 10.0.80.100): ").strip()                            # Solicita o gateway padrão
        dns1 = input("DNS Primário (ex: 1.1.1.1): ").strip()                              # Solicita o primeiro servidor DNS
        dns2 = input("DNS Secundário (ex: 8.8.8.8): ").strip()                            # Solicita o segundo servidor DNS
        linhas = [                                                                        # Substitui a lista de linhas pela configuração com IP estático
            f"allow-hotplug {interface_base}",                                            # Permite ativação automática
            f"iface {interface_base} inet static",                                        # Define a interface como estática (IP fixo)
            f"    address {ip}/{mascara}",                                                # Define o endereço IP e máscara
            f"    gateway {gateway}",                                                     # Define o gateway padrão
            f"    dns-nameservers {dns1} {dns2}"                                          # Define os servidores DNS
        ]
    else:                                                                                 # Se o usuário respondeu 'n' (não)
        print("   Interface física configurada sem IP (apenas UP).")                      # Informa que a interface ficará sem IP
    return linhas                                                                         # Retorna a lista de linhas de configuração

def adicionar_vlan_no_arquivo(interface_base, vlan, ultimo_octeto_gateway):  # Adiciona uma VLAN no arquivo de interfaces
    """Adiciona a configuração da VLAN no arquivo de interfaces de forma persistente"""  # Docstring da função
    try:  # Tenta abrir o arquivo para leitura
        with open(CONFIG_FILE, "r") as f:  # Abre o arquivo no modo leitura
            if f"allow-hotplug {interface_base}.{vlan}" in f.read():  # Verifica se a VLAN já está configurada (pela linha 'allow-hotplug')
                print(f"   ⚠️  VLAN {vlan} já configurada no arquivo. Pulando.")  # Se já existe, exibe aviso e pula
                return  # Sai da função sem adicionar
    except FileNotFoundError:  # Se o arquivo não existir
        pass  # Ignora (vai criar um novo automaticamente)
    gateway_ip = f"10.0.{vlan}.{ultimo_octeto_gateway}"  # Constrói o IP do gateway para esta VLAN (ex: 10.0.10.2)
    with open(CONFIG_FILE, "a") as f:  # Abre o arquivo no modo 'append' (adicionar ao final)
        f.write(f"\n# VLAN {vlan} - Interface {interface_base} (criada em {datetime.now()})\n")  # Escreve um comentário com a data
        f.write(f"allow-hotplug {interface_base}.{vlan}\n")  # Permite que a subinterface seja ativada automaticamente
        f.write(f"iface {interface_base}.{vlan} inet static\n")  # Define a subinterface como estática
        f.write(f"    address 10.0.{vlan}.1/24\n")  # Define o IP da subinterface (ex: 10.0.10.1/24)
        f.write(f"    gateway {gateway_ip}\n")  # Define o gateway para esta VLAN
        f.write(f"    vlan-raw-device {interface_base}\n")  # Indica que a VLAN é criada sobre a interface física 'interface_base'
    print(f"   ✔ VLAN {vlan} adicionada (gateway: {gateway_ip})")  # Confirma a adição da VLAN

def ativar_interface_agora(interface_base, vlan):  # Ativa a VLAN imediatamente (sem esperar reinicialização)
    """Ativa a VLAN imediatamente via comandos ip"""  # Docstring da função
    nome_iface = f"{interface_base}.{vlan}"  # Nome da subinterface (ex: ens3.10)
    ip_vlan = f"10.0.{vlan}.1/24"  # IP da subinterface com máscara
    subprocess.run(  # Executa o comando para criar a subinterface
        ["sudo", "ip", "link", "add", "link", interface_base, "name", nome_iface, "type", "vlan", "id", str(vlan)],
        stderr=subprocess.DEVNULL,  # Redireciona erros para /dev/null (ignora)
        check=False  # Não interrompe o script se houver erro (já pode existir)
    )
    subprocess.run(["sudo", "ip", "link", "set", "dev", nome_iface, "up"], check=True)  # Ativa a subinterface (coloca UP)
    subprocess.run(  # Adiciona o endereço IP à subinterface
        ["sudo", "ip", "addr", "add", ip_vlan, "dev", nome_iface],
        stderr=subprocess.DEVNULL,  # Ignora erros (se o IP já existir, não quebra)
        check=False
    )
    print(f"   ✔ {nome_iface} ativada (IP: {ip_vlan})")  # Confirma a ativação

def escrever_nova_configuracao(interface_base, linhas_fisica):  # Remove a configuração antiga e escreve a nova
    """Gera um novo arquivo de configuração completo, removendo qualquer referência antiga à interface base."""  # Docstring da função
    try:  # Tenta ler o arquivo existente
        with open(CONFIG_FILE, "r") as f:  # Abre o arquivo no modo leitura
            linhas_originais = f.readlines()  # Lê todas as linhas para uma lista
    except FileNotFoundError:  # Se o arquivo não existir
        linhas_originais = []  # Usa uma lista vazia
    novas_linhas = []  # Cria uma lista para armazenar as novas linhas
    ignorar = False  # Flag para indicar se a linha atual deve ser ignorada
    for linha in linhas_originais:  # Percorre cada linha do arquivo original
        if re.match(rf"^(allow-hotplug|iface) {interface_base}(\.|$)", linha):  # Se a linha define a interface base (ou uma subinterface)
            ignorar = True  # Ativa o modo 'ignorar'
            continue  # Pula para a próxima iteração (não adiciona esta linha)
        if ignorar and linha.startswith(("allow-hotplug", "iface", "auto", "source")):  # Se estamos ignorando e a linha começa com uma nova definição
            ignorar = False  # Desativa o modo 'ignorar' (parou o bloco)
        if not ignorar:  # Se não estiver no modo 'ignorar'
            novas_linhas.append(linha)  # Adiciona a linha original à nova lista
    # Adiciona as novas linhas da interface física
    novas_linhas.append("\n")  # Adiciona uma linha em branco
    for linha in linhas_fisica:  # Para cada linha da nova configuração da interface física
        novas_linhas.append(linha + "\n")  # Adiciona a linha (com quebra de linha)
    novas_linhas.append("\n")  # Adiciona uma linha em branco
    # Escreve o arquivo
    with open(CONFIG_FILE, "w") as f:  # Abre o arquivo no modo escrita (sobrescreve)
        f.writelines(novas_linhas)  # Escreve todas as novas linhas

def listar_backups():  # Lista os backups do arquivo de interfaces
    """Lista os backups do arquivo de interfaces disponíveis"""  # Docstring da função
    backups = glob.glob(f"{CONFIG_FILE}.backup_*")  # Busca todos os arquivos que correspondem ao padrão (interfaces.backup_*)
    if not backups:  # Se a lista estiver vazia (nenhum backup encontrado)
        print("Nenhum backup encontrado.")  # Informa que não há backups
        return []  # Retorna uma lista vazia
    print("\n📂 Backups disponíveis:")  # Exibe o cabeçalho da lista
    for i, b in enumerate(backups):  # Percorre a lista de backups com índice
        print(f"  {i+1}. {b}")  # Exibe o número e o caminho do backup
    return backups  # Retorna a lista de backups

def restaurar_backup():  # Restaura um backup selecionado pelo usuário
    """Restaura um backup do arquivo de interfaces"""  # Docstring da função
    backups = listar_backups()  # Obtém a lista de backups disponíveis
    if not backups:  # Se não houver backups
        return  # Sai da função
    escolha = input("Digite o número do backup a restaurar (ou Enter para cancelar): ")  # Pergunta qual backup restaurar
    if not escolha.isdigit() or int(escolha) > len(backups):  # Se a entrada não for um número válido ou estiver fora do intervalo
        print("Restauração cancelada.")  # Informa cancelamento
        return  # Sai da função
    backup = backups[int(escolha)-1]  # Obtém o caminho do backup selecionado (índice 0-based)
    shutil.copy2(backup, CONFIG_FILE)  # Copia o backup para o lugar do arquivo original
    print(f"✅ Backup {backup} restaurado com sucesso.")  # Confirma a restauração
    print("🔄 Reinicie o serviço de rede com: sudo systemctl restart networking")  # Instrução para reiniciar a rede

def configurar_vlans():  # Função principal que orquestra a configuração das VLANs
    """Executa toda a configuração das VLANs com backups automáticos"""  # Docstring da função
    print("\n🚀 Iniciando configuração das VLANs...\n")  # Exibe mensagem de início
    # 1. Backup automático do arquivo de interfaces
    backup_arquivo = fazer_backup_arquivo()  # Chama a função que faz backup do arquivo de interfaces
    # 2. Backup automático do próprio script
    backup_script = fazer_backup_script()  # Chama a função que faz backup do próprio script
    # 3. Detecta a interface principal
    interface_base = detectar_interface_principal()  # Chama a função que detecta a interface ativa
    print(f"🖧  Interface base detectada: {interface_base}")  # Exibe a interface detectada
    # 4. Carrega o módulo de VLAN (verificando se já está carregado)
    verificar_e_carregar_modulo_vlan()  # Chama a função que verifica e carrega o módulo 8021q
    # 5. Pergunta o gateway das VLANs (último octeto)
    print("\n🏠 CONFIGURAÇÃO DO GATEWAY PARA AS VLANS")  # Exibe título da seção
    ultimo_octeto = input("Qual o último octeto do gateway das VLANs? (ex: 2 para 10.0.10.2): ").strip()  # Pergunta o último octeto do gateway
    if not ultimo_octeto.isdigit():  # Se o valor não for numérico
        print("⚠️  Valor inválido. Usando padrão '2'.")  # Avisa e usa padrão '2'
        ultimo_octeto = "2"  # Define o padrão
    # 6. Configura a interface física (escreve no arquivo)
    print("\n📝 Escrevendo configuração da interface física...")  # Exibe mensagem
    linhas_fisica = configurar_interface_fisica(interface_base)  # Obtém as linhas de configuração da interface física
    escrever_nova_configuracao(interface_base, linhas_fisica)  # Escreve a nova configuração no arquivo
    # 7. Adiciona as VLANs no arquivo de configuração (com gateway)
    print("\n➕ Adicionando configurações das VLANs ao arquivo de interfaces...")  # Exibe mensagem
    for vlan in VLANS:  # Percorre a lista de VLANs
        adicionar_vlan_no_arquivo(interface_base, vlan, ultimo_octeto)  # Adiciona cada VLAN no arquivo de interfaces
    # 8. Ativa as interfaces agora
    print("\n🧷 Ativando as interfaces imediatamente...")  # Exibe mensagem
    subprocess.run(["sudo", "ip", "link", "set", interface_base, "up"], check=True)  # Ativa a interface física (coloca UP)
    for vlan in VLANS:  # Percorre a lista de VLANs
        ativar_interface_agora(interface_base, vlan)  # Ativa a subinterface imediatamente
    # 9. Reinicia o serviço de rede (para garantir que as mudanças sejam aplicadas)
    print("\n🔄 Reiniciando serviço de rede...")  # Exibe mensagem
    subprocess.run(["sudo", "systemctl", "restart", "networking"], check=True)  # Reinicia o serviço de rede
    print("✅ Serviço de rede reiniciado.")  # Confirma o reinício
    print("\n✅ Configuração concluída com segurança!")  # Exibe mensagem de conclusão
    print(f"📄 Backup do arquivo de interfaces: {backup_arquivo}")  # Mostra o caminho do backup do arquivo
    print(f"📄 Backup do script: {backup_script}")  # Mostra o caminho do backup do script

def exibir_menu():  # Define a função que exibe o menu principal
    """Exibe o menu principal"""  # Docstring da função
    print("\n" + "="*50)  # Imprime uma linha de separação
    print("  Gerenciador de VLANs no Linux")  # Título do menu
    print("="*50)  # Imprime outra linha de separação
    print("  1. Criar Backup da Interface (apenas backup)")  # Opção 1
    print("  2. Restaurar Backup")  # Opção 2
    print("  3. Configurar Interface (com backup automático)")  # Opção 3
    print("  4. Sair")  # Opção 4
    print("="*50)  # Imprime linha de separação no final

def main():  # Define a função principal do script
    if os.geteuid() != 0:  # Verifica se o script está sendo executado como root (UID 0)
        print("❌ Este script precisa ser executado com sudo.")  # Se não for root, exibe erro
        return  # Encerra o script
    while True:  # Inicia um loop infinito (até o usuário escolher sair)
        exibir_menu()  # Chama a função que exibe o menu
        opcao = input("Escolha uma opção (1-4): ").strip()  # Solicita a opção do usuário
        if opcao == "1":  # Se a opção for 1
            # Apenas backup do arquivo de interfaces
            fazer_backup_arquivo()  # Chama a função que faz backup do arquivo de interfaces
            print("✅ Backup concluído.")  # Confirma a conclusão do backup
        elif opcao == "2":  # Se a opção for 2
            # Restaurar backup
            restaurar_backup()  # Chama a função que restaura um backup
        elif opcao == "3":  # Se a opção for 3
            # Configurar interface com backup automático
            configurar_vlans()  # Chama a função que configura as VLANs
        elif opcao == "4":  # Se a opção for 4
            print("Saindo...")  # Exibe mensagem de saída
            break  # Sai do loop while (encerra o script)
        else:  # Se a opção não for nenhuma das anteriores
            print("⚠️  Opção inválida. Tente novamente.")  # Exibe mensagem de erro e volta ao menu

if __name__ == "__main__":  # Verifica se o script foi executado diretamente (não importado como módulo)
    main()  # Chama a função principal