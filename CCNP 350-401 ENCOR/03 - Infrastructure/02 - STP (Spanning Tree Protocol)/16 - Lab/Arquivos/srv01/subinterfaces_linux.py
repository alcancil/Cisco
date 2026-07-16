#!/usr/bin/env python3
import os
import subprocess
import shutil
import re
from datetime import datetime
import glob

# ========= CONFIGURAÇÃO =========
INTERFACE_PROBLEMA = "ens3"
INTERFACE_IMPAR = "ens3"
INTERFACE_PAR = "ens4"
VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
CONFIG_FILE = "/etc/network/interfaces"
# =================================

# ========= FUNÇÕES DE BACKUP E RESTAURAÇÃO =========
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

# ========= FUNÇÕES DE LIMPEZA TOTAL =========
def limpar_interface_do_arquivo(interface):
    """Remove TODAS as linhas relacionadas a uma interface (física, subinterfaces, dhcp, etc.) do arquivo de configuração"""
    try:
        with open(CONFIG_FILE, "r") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        linhas = []
    
    novas_linhas = []
    ignorar = False
    for linha in linhas:
        # Se a linha define a interface física, subinterface, ou qualquer configuração relacionada à interface
        if re.search(rf"\b{interface}\b", linha):
            ignorar = True
            continue
        # Se estamos ignorando e a linha começa com uma nova definição (de outra interface), para de ignorar
        if ignorar and linha.startswith(("allow-hotplug", "iface", "auto", "source")):
            ignorar = False
        if not ignorar:
            novas_linhas.append(linha)
    
    with open(CONFIG_FILE, "w") as f:
        f.writelines(novas_linhas)

def escrever_interface_fisica_manual(interface):
    """Adiciona a configuração manual da interface física no arquivo"""
    with open(CONFIG_FILE, "a") as f:
        f.write(f"\n# Interface física {interface} (manual, sem IP)\n")
        f.write(f"allow-hotplug {interface}\n")
        f.write(f"iface {interface} inet manual\n")
        f.write(f"    up ip link set {interface} up\n")
        f.write(f"    down ip link set {interface} down\n")

def escrever_subinterface_vlan(interface, vlan):
    """Adiciona a configuração de uma subinterface VLAN no arquivo"""
    with open(CONFIG_FILE, "a") as f:
        f.write(f"\n# VLAN {vlan} - Interface {interface}.{vlan}\n")
        f.write(f"allow-hotplug {interface}.{vlan}\n")
        f.write(f"iface {interface}.{vlan} inet static\n")
        f.write(f"    address 10.0.{vlan}.254/24\n")
        f.write(f"    vlan-raw-device {interface}\n")

def carregar_modulo_vlan():
    print("🔌 Carregando módulo 8021q...")
    subprocess.run(["sudo", "modprobe", "8021q"], check=True)

def garantir_interface_pai_up(interface):
    """Garante que a interface pai esteja UP"""
    print(f"⬆️  Garantindo que a interface {interface} esteja UP...")
    subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)

def ativar_interface_kernel(interface, vlan):
    """Ativa a VLAN imediatamente no kernel"""
    nome_iface = f"{interface}.{vlan}"
    ip_vlan = f"10.0.{vlan}.254/24"
    
    subprocess.run(
        ["sudo", "ip", "link", "add", "link", interface, "name", nome_iface, "type", "vlan", "id", str(vlan)],
        stderr=subprocess.DEVNULL,
        check=False
    )
    garantir_interface_pai_up(interface)
    subprocess.run(["sudo", "ip", "link", "set", "dev", nome_iface, "up"], check=True)
    subprocess.run(
        ["sudo", "ip", "addr", "add", ip_vlan, "dev", nome_iface],
        stderr=subprocess.DEVNULL,
        check=False
    )
    print(f"   ✔ {nome_iface} ativada (IP: {ip_vlan})")

# ========= OPÇÕES DE CONFIGURAÇÃO =========
def configurar_modo_problema():
    """Configura todas as VLANs em uma única interface (ens3)"""
    print(f"\n⚠️  Modo Problema: Todas as VLANs em {INTERFACE_PROBLEMA}")
    
    # Limpa completamente as duas interfaces para garantir que não haja resíduos
    limpar_interface_do_arquivo(INTERFACE_PROBLEMA)
    limpar_interface_do_arquivo(INTERFACE_PAR)
    
    # Escreve a interface física como manual (ens3)
    escrever_interface_fisica_manual(INTERFACE_PROBLEMA)
    # Escreve a interface física como manual (ens4) também, para evitar DHCP conflitante
    escrever_interface_fisica_manual(INTERFACE_PAR)
    
    # Adiciona todas as VLANs na ens3
    for vlan in VLANS:
        escrever_subinterface_vlan(INTERFACE_PROBLEMA, vlan)
        ativar_interface_kernel(INTERFACE_PROBLEMA, vlan)
    
    print("\n✅ Configuração concluída! As interfaces agora devem ficar UP.")
    print("💡 Dica: Se ainda houver algum problema, execute: sudo systemctl restart networking")

def configurar_modo_balanceamento():
    """Configura VLANs em ordem alternada: 1ª, 3ª, 5ª, 7ª, 9ª na ens3; 2ª, 4ª, 6ª, 8ª, 10ª na ens4"""
    print(f"\n⚖️  Modo Balanceamento: Ímpares na lista (10,30,50,70,90) em {INTERFACE_IMPAR}, Pares na lista (20,40,60,80,100) em {INTERFACE_PAR}")
    
    # Limpa completamente as duas interfaces
    limpar_interface_do_arquivo(INTERFACE_IMPAR)
    limpar_interface_do_arquivo(INTERFACE_PAR)
    
    # Escreve ambas as interfaces como manual
    escrever_interface_fisica_manual(INTERFACE_IMPAR)
    escrever_interface_fisica_manual(INTERFACE_PAR)
    
    # Itera sobre a lista de VLANs usando índice
    for idx, vlan in enumerate(VLANS):
        if idx % 2 == 0:  # Posições 0, 2, 4, 6, 8 → VLANs 10,30,50,70,90
            escrever_subinterface_vlan(INTERFACE_IMPAR, vlan)
            ativar_interface_kernel(INTERFACE_IMPAR, vlan)
        else:  # Posições 1, 3, 5, 7, 9 → VLANs 20,40,60,80,100
            escrever_subinterface_vlan(INTERFACE_PAR, vlan)
            ativar_interface_kernel(INTERFACE_PAR, vlan)
    
    print("\n✅ Configuração concluída! As interfaces agora devem ficar UP.")
    print("💡 Dica: Se ainda houver algum problema, execute: sudo systemctl restart networking")

# ========= MENU PRINCIPAL =========
def exibir_menu():
    print("\n" + "="*50)
    print("  Gerenciador de VLANs no Linux")
    print("="*50)
    print("  1. Realizar Backup das Interfaces")
    print("  2. Restaurar Backup das Interfaces")
    print("  3. Configurar Interfaces em uma placa (sem balanceamento)")
    print("  4. Configurar Interfaces em duas placas (com balanceamento)")
    print("  5. Sair")
    print("="*50)

def main():
    if os.geteuid() != 0:
        print("❌ Este script precisa ser executado com sudo.")
        return

    # Backup automático do próprio script sempre que executado
    fazer_backup_script()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            fazer_backup_arquivo()
            print("✅ Backup concluído.")
        
        elif opcao == "2":
            restaurar_backup()
        
        elif opcao == "3":
            backup_arquivo = fazer_backup_arquivo()
            configurar_modo_problema()
            print(f"📄 Backup do arquivo de interfaces: {backup_arquivo}")
        
        elif opcao == "4":
            backup_arquivo = fazer_backup_arquivo()
            configurar_modo_balanceamento()
            print(f"📄 Backup do arquivo de interfaces: {backup_arquivo}")
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("⚠️  Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()