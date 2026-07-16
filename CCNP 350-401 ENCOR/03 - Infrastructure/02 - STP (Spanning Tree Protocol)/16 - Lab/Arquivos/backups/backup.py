from netmiko import ConnectHandler
from datetime import datetime
import os
import getpass
import time

os.makedirs("backups", exist_ok=True)

def obter_hostname(connection):
    """Pega o nome do switch diretamente do prompt da conexão (confiável 100%)."""
    try:
        # O base_prompt retorna o prompt completo, ex: "SW_CORE01#"
        prompt = connection.base_prompt
        # Remove o caractere '#' do final para pegar apenas o nome
        return prompt.replace('#', '').strip()
    except:
        return None

def fazer_backup(ip, username, password):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": username,
        "password": password,
        "conn_timeout": 10,
        "timeout": 30,
    }
    
    connection = None
    try:
        print(f"\n🔌 Conectando em {ip}...")
        connection = ConnectHandler(**device)
        
        # Obtém o nome via prompt
        hostname = obter_hostname(connection)
        if not hostname:
            print(f"⚠️  Não foi possível obter o hostname para {ip}. Usando IP no nome.")
            hostname = ip.replace('.', '_')
        
        print(f"📥 Baixando configuração de {hostname}...")
        output = connection.send_command("show running-config")
        
        hoje = datetime.now().strftime("%Y-%m-%d")
        filename = f"backups/{hostname}_{hoje}.cfg"
        
        with open(filename, "w") as f:
            f.write(output)
        
        print(f"✅ Backup salvo: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no dispositivo {ip}: {e}")
        return False
    finally:
        if connection:
            try:
                connection.disconnect()
            except:
                pass

# === MENU PRINCIPAL ===
while True:
    print("\n" + "="*50)
    print("🔹 LABORATÓRIO DE BACKUP - VERSÃO ROBUSTA 🔹")
    print("1 - Fazer backup de UM equipamento")
    print("2 - Fazer backup de VÁRIOS equipamentos (lista de IPs)")
    print("3 - Sair")
    print("="*50)
    
    opcao = input("Escolha uma opção (1/2/3): ").strip()
    
    if opcao == "1":
        ip = input("\nDigite o IP do dispositivo: ").strip()
        if not ip:
            print("⚠️ IP inválido.")
            continue
        username = input("Usuário: ").strip()
        password = getpass.getpass("Senha: ")
        fazer_backup(ip, username, password)
        
    elif opcao == "2":
        print("\n📋 Digite os IPs separados por VÍRGULA (Ex: 192.168.1.1, 10.0.0.5)")
        lista_ips_input = input("IPs: ").strip()
        lista_ips = [ip.strip() for ip in lista_ips_input.split(",") if ip.strip()]
        
        if not lista_ips:
            print("⚠️ Nenhum IP válido.")
            continue
            
        username = input("Usuário para todos: ").strip()
        password = getpass.getpass("Senha para todos: ")
        
        print(f"\n🔄 Iniciando backup de {len(lista_ips)} equipamento(s)...")
        
        sucessos = 0
        falhas = 0
        for ip in lista_ips:
            if fazer_backup(ip, username, password):
                sucessos += 1
            else:
                falhas += 1
            # Pequena pausa para garantir que a rede "respire" entre as conexões
            time.sleep(1)
        
        print(f"\n📊 Resumo: {sucessos} backups realizados, {falhas} falhas.")
        
    elif opcao == "3":
        print("👋 Encerrando o script.")
        break
    else:
        print("❌ Opção inválida.")
    
    continuar = input("\n🔁 Deseja fazer mais backups? (s/n): ").lower()
    if continuar != "s":
        print("👋 Até mais!")
        break