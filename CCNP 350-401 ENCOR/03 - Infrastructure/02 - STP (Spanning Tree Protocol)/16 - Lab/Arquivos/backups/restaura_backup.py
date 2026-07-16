from netmiko import ConnectHandler
import os
import glob
import getpass
import time

# ========= CONFIGURAÇÕES =========
BACKUP_DIR = "backups"
# =================================

def listar_backups():
    """Lista todos os arquivos .cfg na pasta backups e retorna uma lista com os nomes."""
    backups = glob.glob(f"{BACKUP_DIR}/*.cfg")
    if not backups:
        print("Nenhum backup encontrado na pasta 'backups'.")
        return []
    print("\n📂 Backups disponíveis:")
    for i, arquivo in enumerate(backups):
        print(f"  {i+1}. {arquivo}")
    return backups

def obter_hostname(connection):
    """Pega o nome do switch diretamente do prompt da conexão."""
    try:
        prompt = connection.base_prompt
        return prompt.replace('#', '').strip()
    except:
        return None

def restaurar_backup(ip, username, password, arquivo_backup):
    """Restaura a configuração de um equipamento a partir de um arquivo de backup."""
    # CORREÇÃO AQUI: Não use read_timeout no dicionário
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
        "conn_timeout": 10,
        "timeout": 180,          # 'timeout' controla o tempo máximo total
        "fast_cli": False
    }
    
    connection = None
    try:
        print(f"\n🔌 Conectando em {ip}...")
        connection = ConnectHandler(**device)
        
        if not os.path.isfile(arquivo_backup):
            print(f"❌ Arquivo de backup não encontrado: {arquivo_backup}")
            return False
        
        hostname = obter_hostname(connection)
        if hostname:
            print(f"✅ Conectado a {hostname}")
        else:
            print(f"✅ Conectado a {ip}")
            hostname = ip.replace('.', '_')
        
        print(f"🔄 Aplicando configuração a partir do arquivo {arquivo_backup}...")
        
        # CORREÇÃO AQUI: read_timeout é passado como argumento da função, não no dicionário
        output = connection.send_config_from_file(
            arquivo_backup,
            delay_factor=1,
            strip_command=False,
            read_timeout=180  # Passa o read_timeout aqui para controlar a leitura
        )
        
        print("🔁 Configuração aplicada.")
        connection.send_command("write memory")
        print("💾 Configuração salva na memória não volátil.")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao restaurar {ip}: {e}")
        print("⚠️ A configuração pode ter sido aplicada parcialmente. Verifique manualmente.")
        return False
    finally:
        if connection:
            try:
                connection.disconnect()
            except:
                pass

def restaurar_varios_backups(lista_ips, username, password):
    """Restaura a configuração de vários equipamentos usando a convenção de nome de arquivo."""
    sucessos = 0
    falhas = 0
    
    for ip in lista_ips:
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
            "conn_timeout": 10,
            "timeout": 30,
        }
        connection = None
        hostname = None
        try:
            connection = ConnectHandler(**device)
            hostname = obter_hostname(connection)
            connection.disconnect()
        except Exception as e:
            print(f"❌ Erro ao conectar em {ip} para obter hostname: {e}")
            falhas += 1
            continue
        finally:
            if connection:
                try:
                    connection.disconnect()
                except:
                    pass
        
        if not hostname:
            hostname = ip.replace('.', '_')
        
        hoje = datetime.now().strftime("%Y-%m-%d")
        arquivo = f"{BACKUP_DIR}/{hostname}_{hoje}.cfg"
        if not os.path.isfile(arquivo):
            backups_host = glob.glob(f"{BACKUP_DIR}/{hostname}_*.cfg")
            if not backups_host:
                print(f"❌ Nenhum backup encontrado para {hostname}.")
                falhas += 1
                continue
            arquivo = max(backups_host, key=os.path.getmtime)
            print(f"📄 Usando backup mais recente: {arquivo}")
        
        if restaurar_backup(ip, username, password, arquivo):
            sucessos += 1
        else:
            falhas += 1
        time.sleep(2)
    
    return sucessos, falhas

# === MENU PRINCIPAL ===
while True:
    print("\n" + "="*50)
    print("🔹 LABORATÓRIO DE RESTAURAÇÃO DE BACKUPS 🔹")
    print("1 - Restaurar backup de UM equipamento (escolher arquivo)")
    print("2 - Restaurar backup de VÁRIOS equipamentos (lista de IPs, usa nome automático)")
    print("3 - Sair")
    print("="*50)
    
    opcao = input("Escolha uma opção (1/2/3): ").strip()
    
    if opcao == "1":
        backups = listar_backups()
        if not backups:
            continue
        
        escolha = input("\nDigite o número do backup que deseja restaurar (ou Enter para cancelar): ").strip()
        if not escolha.isdigit() or int(escolha) > len(backups):
            print("Restauração cancelada.")
            continue
        arquivo_backup = backups[int(escolha)-1]
        
        ip = input("IP do dispositivo: ").strip()
        if not ip:
            print("⚠️ IP inválido.")
            continue
        username = input("Usuário: ").strip()
        password = getpass.getpass("Senha: ")
        
        sucesso = restaurar_backup(ip, username, password, arquivo_backup)
        
    elif opcao == "2":
        print("\n📋 Digite os IPs separados por VÍRGULA (Ex: 192.168.1.1, 10.0.0.5)")
        lista_ips_input = input("IPs: ").strip()
        lista_ips = [ip.strip() for ip in lista_ips_input.split(",") if ip.strip()]
        
        if not lista_ips:
            print("⚠️ Nenhum IP válido.")
            continue
        
        username = input("Usuário para todos: ").strip()
        password = getpass.getpass("Senha para todos: ")
        
        print(f"\n🔄 Iniciando restauração de {len(lista_ips)} equipamento(s)...")
        sucessos, falhas = restaurar_varios_backups(lista_ips, username, password)
        print(f"\n📊 Resumo: {sucessos} restaurações realizadas, {falhas} falhas.")
        
    elif opcao == "3":
        print("👋 Encerrando o script.")
        break
    else:
        print("❌ Opção inválida.")
    
    continuar = input("\n🔁 Deseja fazer mais restaurações? (s/n): ").lower()
    if continuar != "s":
        print("👋 Até mais!")
        break