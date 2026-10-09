#!/usr/bin/env python3
import subprocess
import threading

VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
DURATION = 10
PORTA_BASE = 5200

def atacar(vlan):
    ip_origem = f"10.0.{vlan}.1"      # Ajuste se seu host usa outro IP
    ip_destino = f"10.0.{vlan}.254"
    porta = PORTA_BASE + vlan
    cmd = ["iperf3", "-c", ip_destino, "-B", ip_origem, "-p", str(porta), "-t", str(DURATION), "-P", "2"]
    print(f"🔴 [VLAN {vlan}] Iniciando...")
    subprocess.run(cmd)

threads = []
for vlan in VLANS:
    t = threading.Thread(target=atacar, args=(vlan,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("✅ Todos os testes finalizados.")