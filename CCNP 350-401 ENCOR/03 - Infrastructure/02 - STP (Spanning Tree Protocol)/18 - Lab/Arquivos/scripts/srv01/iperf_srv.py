#!/usr/bin/env python3
import subprocess
import signal
import sys
import time
import os

# ========= CONFIGURAÇÕES =========
VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
PORTA_BASE = 5200
# =================================

processos = {}  # {porta: processo}

def limpar_processos():
    """Mata todos os processos iperf3 que estão rodando"""
    print("🧹 Limpando processos iperf3 antigos...")
    subprocess.run(["sudo", "pkill", "-f", "iperf3"], stderr=subprocess.DEVNULL)
    time.sleep(1)

def iniciar_servidores():
    """Inicia um servidor iperf3 para cada VLAN em uma porta única"""
    print(f"🚀 Iniciando servidores iperf3 para {len(VLANS)} VLANs...\n")
    for vlan in VLANS:
        ip = f"10.0.{vlan}.254"
        porta = PORTA_BASE + vlan
        cmd = ["sudo", "iperf3", "-s", "-B", ip, "-p", str(porta)]
        try:
            # Redireciona stdout/stderr para o terminal (mostra mensagens de conexão)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            processos[porta] = p
        except Exception as e:
            print(f"❌ Falha ao iniciar VLAN {vlan}: {e}")

def verificar_servidores():
    """Verifica quais portas estão ouvindo e exibe um diagnóstico imediato"""
    print("\n🔍 DIAGNÓSTICO IMEDIATO DOS SERVIDORES IPERF3")
    print("="*60)
    print(f"{'VLAN':<6} {'PORTA':<8} {'IP':<20} {'STATUS'}")
    print("-"*60)
    
    for vlan in VLANS:
        porta = PORTA_BASE + vlan
        ip = f"10.0.{vlan}.254"
        
        # Verifica se a porta está em estado LISTEN usando ss
        try:
            result = subprocess.run(["ss", "-tulpn"], capture_output=True, text=True)
            if f":{porta}" in result.stdout:
                # Tenta pegar o PID do iperf3
                pid = "?"
                for linha in result.stdout.split('\n'):
                    if f":{porta}" in linha and "iperf3" in linha:
                        partes = linha.split()
                        for parte in partes:
                            if "pid=" in parte:
                                pid = parte.split("=")[1].split(",")[0]
                                break
                        break
                print(f"VLAN {vlan:<4} {porta:<8} {ip:<20} 🟢 OK (PID: {pid})")
            else:
                print(f"VLAN {vlan:<4} {porta:<8} {ip:<20} 🔴 FALHA (NÃO ESTÁ OUVINDO)")
        except Exception as e:
            print(f"VLAN {vlan:<4} {porta:<8} {ip:<20} ❌ ERRO: {e}")
    
    print("-"*60)
    
    # Exibe conexões ativas nas portas das VLANs
    print("\n📡 Conexões ativas (ESTAB):")
    try:
        result = subprocess.run(["ss", "-tnp"], capture_output=True, text=True)
        linhas = result.stdout.split('\n')
        encontrou = False
        for linha in linhas:
            if "ESTAB" in linha:
                for vlan in VLANS:
                    porta = PORTA_BASE + vlan
                    if f":{porta}" in linha:
                        print(f"   ✅ {linha.strip()}")
                        encontrou = True
                        break
        if not encontrou:
            print("   (Nenhuma conexão ativa no momento)")
    except:
        pass
    print("="*60)

def exibir_status():
    """Exibe uma tabela atualizada dos processos iperf3 escutando e conexões ativas (loop)"""
    os.system('clear')
    print("=" * 60)
    print("🟢 SERVIDORES IPERF3 RODANDO (atualizado a cada 3s)")
    print("=" * 60)
    print(f"{'VLAN':<6} {'PORTA':<8} {'PID':<8} {'IP':<20} {'STATUS'}")
    print("-" * 60)
    
    for vlan in VLANS:
        porta = PORTA_BASE + vlan
        ip = f"10.0.{vlan}.254"
        p = processos.get(porta)
        if p is not None:
            if p.poll() is None:
                status = "🟢 OK"
                # Tenta pegar o PID real do iperf3 via pgrep
                try:
                    result = subprocess.run(["pgrep", "-f", f"iperf3 -s -B {ip} -p {porta}"],
                                           capture_output=True, text=True)
                    pid = result.stdout.strip()
                    if not pid:
                        pid = "?"
                    print(f"VLAN {vlan:<4} {porta:<8} {pid:<8} {ip}    {status}")
                except:
                    print(f"VLAN {vlan:<4} {porta:<8} {'?':<8} {ip}    {status}")
            else:
                status = "🔴 MORTO"
                print(f"VLAN {vlan:<4} {porta:<8} {'?':<8} {ip}    {status}")
        else:
            print(f"VLAN {vlan:<4} {porta:<8} {'?':<8} {ip}    ❌ NÃO INICIADO")
    
    print("\n📡 Conexões ativas (ESTAB):")
    try:
        result = subprocess.run(["ss", "-tnp"], capture_output=True, text=True)
        linhas = result.stdout.split('\n')
        encontrou = False
        for linha in linhas:
            if "ESTAB" in linha:
                for vlan in VLANS:
                    porta = PORTA_BASE + vlan
                    if f":{porta}" in linha:
                        print(f"   ✅ {linha.strip()}")
                        encontrou = True
                        break
        if not encontrou:
            print("   (Nenhuma conexão ativa no momento)")
    except:
        pass
    print("=" * 60)

def encerrar_processos():
    """Mata os processos iperf3 que este script iniciou e qualquer outro iperf3 restante"""
    print("\n🛑 Encerrando servidores iperf3...")
    for porta, p in processos.items():
        try:
            p.terminate()
            p.wait(timeout=2)
        except:
            pass
    subprocess.run(["sudo", "pkill", "-f", "iperf3"], stderr=subprocess.DEVNULL)
    print("✅ Servidores encerrados.")

def handler(signum, frame):
    print("\n\n⚠️  Interrupção detectada. Encerrando servidores...")
    encerrar_processos()
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handler)
    limpar_processos()
    iniciar_servidores()
    
    # Espera um pouco para os servidores inicializarem
    time.sleep(2)
    
    # Executa o diagnóstico imediato
    verificar_servidores()
    
    print("\n⏳ Servidores rodando. Pressione Ctrl+C para parar.")
    print("💡 Execute o teste de estresse no Host Linux agora.\n")
    print("🔄 Atualizando status a cada 3 segundos...")
    
    try:
        while True:
            exibir_status()
            time.sleep(3)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()