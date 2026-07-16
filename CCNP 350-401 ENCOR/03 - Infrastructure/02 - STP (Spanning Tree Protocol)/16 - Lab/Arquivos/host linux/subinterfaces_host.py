#!/usr/bin/env python3
import os
import subprocess
import re
import shutil
from datetime import datetime
import glob

# ========= CONFIGURAÇÕES =========
VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
CONFIG_FILE = "/etc/network/interfaces"
# =================================

def detectar_interface_principal():
    """Detecta automaticamente a interface ativa (ex: ens3)"""
    try:
        result = subprocess.run(["ip", "addr", "show"], capture_output=True, text=True, check=True)
        for line in result.stdout.split("\n"):
            if "inet " in line and "lo" not in line:
                match = re.search(r"\d+: (\w+):", line)
                if match:
                    return match.group(1)
        return "ens3"
    except:
        return "ens3"

def fazer_backup_arquivo():
    """Faz backup do arquivo de interfaces"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{CONFIG_FILE}.backup_{timestamp}"
    print(f"🔐 Backup do arquivo de interfaces criado em: {backup_file}")
    shutil.copy2(CONFIG_FILE, backup_file)
    return backup_file

def fazer_backup_script():
    """Faz backup do próprio script"""
    script_path = os.path.realpath(__file__)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_script = f"{script_path}.backup_{timestamp}"
    shutil.copy2(script_path, backup_script)
    print(f"📄 Backup do script criado em: {backup_script}")
    return backup_script

def verificar_e_carregar_modulo_vlan():
    """Verifica se o módulo 8021q está carregado. Se não, carrega."""
    result = subprocess.run(["lsmod"], capture_output=True, text=True)
    if "8021q" in result.stdout:
        print("✅ Módulo 8021q já está carregado.")
        return
    print("🔌 Carregando módulo 8021q...")
    subprocess.run(["sudo", "modprobe", "8021q"], check=True)
    print("✅ Módulo 8021q carregado com sucesso.")

def configurar_interface_fisica(interface_base):
    """Pergunta os dados da interface física e retorna as linhas de configuração"""
    print("\n🖧  CONFIGURAÇÃO DA INTERFACE FÍSICA")
    resp = input("Deseja configurar a interface física com IP? (s/n): ").strip().lower()
    
    linhas = [
        f"allow-hotplug {interface_base}",
        f"iface {interface_base} inet manual",
        f"    up ip link set {interface_base} up",
        f"    down ip link set {interface_base} down"
    ]
    
    if resp == "s":
        ip = input("IP da interface (ex: 10.0.80.1): ").strip()
        mascara = input("Máscara em CIDR (ex: 24): ").strip()
        gateway = input("Gateway (ex: 10.0.80.100): ").strip()
        dns1 = input("DNS Primário (ex: 1.1.1.1): ").strip()
        dns2 = input("DNS Secundário (ex: 8.8.8.8): ").strip()
        
        linhas = [
            f"allow-hotplug {interface_base}",
            f"iface {interface_base} inet static",
            f"    address {ip}/{mascara}",
            f"    gateway {gateway}",
            f"    dns-nameservers {dns1} {dns2}"
        ]
    else:
        print("   Interface física configurada sem IP (apenas UP).")
    
    return linhas

def adicionar_vlan_no_arquivo(interface_base, vlan, ultimo_octeto_gateway):
    """Adiciona a configuração da VLAN no arquivo de interfaces de forma persistente"""
    try:
        with open(CONFIG_FILE, "r") as f:
            if f"allow-hotplug {interface_base}.{vlan}" in f.read():
                print(f"   ⚠️  VLAN {vlan} já configurada no arquivo. Pulando.")
                return
    except FileNotFoundError:
        pass

    gateway_ip = f"10.0.{vlan}.{ultimo_octeto_gateway}"
    with open(CONFIG_FILE, "a") as f:
        f.write(f"\n# VLAN {vlan} - Interface {interface_base} (criada em {datetime.now()})\n")
        f.write(f"allow-hotplug {interface_base}.{vlan}\n")
        f.write(f"iface {interface_base}.{vlan} inet static\n")
        f.write(f"    address 10.0.{vlan}.1/24\n")
        f.write(f"    gateway {gateway_ip}\n")
        f.write(f"    vlan-raw-device {interface_base}\n")
    print(f"   ✔ VLAN {vlan} adicionada (gateway: {gateway_ip})")

def ativar_interface_agora(interface_base, vlan):
    """Ativa a VLAN imediatamente via comandos ip"""
    nome_iface = f"{interface_base}.{vlan}"
    ip_vlan = f"10.0.{vlan}.1/24"
    
    subprocess.run(
        ["sudo", "ip", "link", "add", "link", interface_base, "name", nome_iface, "type", "vlan", "id", str(vlan)],
        stderr=subprocess.DEVNULL,
        check=False
    )
    subprocess.run(["sudo", "ip", "link", "set", "dev", nome_iface, "up"], check=True)
    subprocess.run(
        ["sudo", "ip", "addr", "add", ip_vlan, "dev", nome_iface],
        stderr=subprocess.DEVNULL,
        check=False
    )
    print(f"   ✔ {nome_iface} ativada (IP: {ip_vlan})")

def escrever_nova_configuracao(interface_base, linhas_fisica):
    """Gera um novo arquivo de configuração completo, removendo qualquer referência antiga à interface base."""
    try:
        with open(CONFIG_FILE, "r") as f:
            linhas_originais = f.readlines()
    except FileNotFoundError:
        linhas_originais = []
    
    novas_linhas = []
    ignorar = False
    for linha in linhas_originais:
        if re.match(rf"^(allow-hotplug|iface) {interface_base}(\.|$)", linha):
            ignorar = True
            continue
        if ignorar and linha.startswith(("allow-hotplug", "iface", "auto", "source")):
            ignorar = False
        if not ignorar:
            novas_linhas.append(linha)
    
    # Adiciona as novas linhas da interface física
    novas_linhas.append("\n")
    for linha in linhas_fisica:
        novas_linhas.append(linha + "\n")
    novas_linhas.append("\n")
    
    # Escreve o arquivo
    with open(CONFIG_FILE, "w") as f:
        f.writelines(novas_linhas)

def listar_backups():
    """Lista os backups do arquivo de interfaces disponíveis"""
    backups = glob.glob(f"{CONFIG_FILE}.backup_*")
    if not backups:
        print("Nenhum backup encontrado.")
        return []
    print("\n📂 Backups disponíveis:")
    for i, b in enumerate(backups):
        print(f"  {i+1}. {b}")
    return backups

def restaurar_backup():
    """Restaura um backup do arquivo de interfaces"""
    backups = listar_backups()
    if not backups:
        return
    escolha = input("Digite o número do backup a restaurar (ou Enter para cancelar): ")
    if not escolha.isdigit() or int(escolha) > len(backups):
        print("Restauração cancelada.")
        return
    backup = backups[int(escolha)-1]
    shutil.copy2(backup, CONFIG_FILE)
    print(f"✅ Backup {backup} restaurado com sucesso.")
    print("🔄 Reinicie o serviço de rede com: sudo systemctl restart networking")

def configurar_vlans():
    """Executa toda a configuração das VLANs com backups automáticos"""
    print("\n🚀 Iniciando configuração das VLANs...\n")

    # 1. Backup automático do arquivo de interfaces
    backup_arquivo = fazer_backup_arquivo()
    
    # 2. Backup automático do próprio script
    backup_script = fazer_backup_script()

    # 3. Detecta a interface principal
    interface_base = detectar_interface_principal()
    print(f"🖧  Interface base detectada: {interface_base}")

    # 4. Carrega o módulo de VLAN (verificando se já está carregado)
    verificar_e_carregar_modulo_vlan()

    # 5. Pergunta o gateway das VLANs (último octeto)
    print("\n🏠 CONFIGURAÇÃO DO GATEWAY PARA AS VLANS")
    ultimo_octeto = input("Qual o último octeto do gateway das VLANs? (ex: 2 para 10.0.10.2): ").strip()
    if not ultimo_octeto.isdigit():
        print("⚠️  Valor inválido. Usando padrão '2'.")
        ultimo_octeto = "2"

    # 6. Configura a interface física (escreve no arquivo)
    print("\n📝 Escrevendo configuração da interface física...")
    linhas_fisica = configurar_interface_fisica(interface_base)
    escrever_nova_configuracao(interface_base, linhas_fisica)

    # 7. Adiciona as VLANs no arquivo de configuração (com gateway)
    print("\n➕ Adicionando configurações das VLANs ao arquivo de interfaces...")
    for vlan in VLANS:
        adicionar_vlan_no_arquivo(interface_base, vlan, ultimo_octeto)

    # 8. Ativa as interfaces agora
    print("\n🧷 Ativando as interfaces imediatamente...")
    subprocess.run(["sudo", "ip", "link", "set", interface_base, "up"], check=True)
    for vlan in VLANS:
        ativar_interface_agora(interface_base, vlan)

    # 9. Reinicia o serviço de rede (para garantir que as mudanças sejam aplicadas)
    print("\n🔄 Reiniciando serviço de rede...")
    subprocess.run(["sudo", "systemctl", "restart", "networking"], check=True)
    print("✅ Serviço de rede reiniciado.")

    print("\n✅ Configuração concluída com segurança!")
    print(f"📄 Backup do arquivo de interfaces: {backup_arquivo}")
    print(f"📄 Backup do script: {backup_script}")

def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("  Gerenciador de VLANs no Linux")
    print("="*50)
    print("  1. Criar Backup da Interface (apenas backup)")
    print("  2. Restaurar Backup")
    print("  3. Configurar Interface (com backup automático)")
    print("  4. Sair")
    print("="*50)

def main():
    if os.geteuid() != 0:
        print("❌ Este script precisa ser executado com sudo.")
        return

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            # Apenas backup do arquivo de interfaces
            fazer_backup_arquivo()
            print("✅ Backup concluído.")
        
        elif opcao == "2":
            # Restaurar backup
            restaurar_backup()
        
        elif opcao == "3":
            # Configurar interface com backup automático
            configurar_vlans()
        
        elif opcao == "4":
            print("Saindo...")
            break
        
        else:
            print("⚠️  Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()