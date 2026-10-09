#!/usr/bin/env python3
# Define que este script deve ser executado usando o interpretador Python 3 encontrado no PATH do sistema (shebang, usado ao rodar o arquivo diretamente no Linux, ex: ./iperf_stress_.py)

import subprocess
# Importa o módulo subprocess, usado para executar o comando externo "iperf3" como cliente

import threading
# Importa o módulo threading, usado para disparar os testes de várias VLANs ao mesmo tempo (em paralelo)

VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]   
# Lista com os números das VLANs que serão testadas simultaneamente; comentário original do autor sugerindo começar com um subconjunto (3 VLANs) antes de escalar para as 10

DURATION = 10
# Duração, em segundos, de cada teste de tráfego do iperf3

PORTA_BASE = 5200
# Porta base usada para calcular a porta de cada VLAN (mesma lógica do script do servidor: PORTA_BASE + número da VLAN)

def atacar(vlan):
    # Define a função que gera tráfego de estresse para uma única VLAN; recebe o número da VLAN como parâmetro
    ip_origem = f"10.0.{vlan}.1"      # Ajuste se seu host usa outro IP
    # Monta o IP de origem do teste (o IP do host cliente nesta VLAN), com nota do autor lembrando de ajustar se necessário
    ip_destino = f"10.0.{vlan}.254"
    # Monta o IP de destino do teste, que é a SVI da VLAN no servidor (mesmo padrão usado no script do servidor)
    porta = PORTA_BASE + vlan
    # Calcula a porta do servidor iperf3 correspondente a esta VLAN, usando a mesma fórmula do script do servidor
    cmd = ["iperf3", "-c", ip_destino, "-B", ip_origem, "-p", str(porta), "-t", str(DURATION), "-P", "2"]
    # Monta a lista de argumentos do comando: roda o iperf3 em modo cliente (-c) contra o IP de destino, vinculado (bind) ao IP de origem (-B), na porta calculada (-p), pela duração definida (-t), abrindo 2 fluxos paralelos por VLAN (-P)
    print(f"🔴 [VLAN {vlan}] Iniciando...")
    # Exibe no terminal que o teste desta VLAN está começando
    subprocess.run(cmd)
    # Executa o comando iperf3 de forma síncrona (bloqueante) dentro desta thread, aguardando o teste terminar antes de seguir

threads = []
# Cria uma lista vazia para guardar as referências de todas as threads que serão criadas, uma por VLAN

for vlan in VLANS:
    # Percorre cada VLAN da lista para disparar seu teste em uma thread separada
    t = threading.Thread(target=atacar, args=(vlan,))
    # Cria uma nova thread configurada para executar a função "atacar", passando o número da VLAN como argumento
    t.start()
    # Inicia a execução da thread imediatamente (o teste desta VLAN começa a rodar em paralelo com as demais)
    threads.append(t)
    # Adiciona a referência desta thread à lista, para poder aguardá-la terminar mais adiante

for t in threads:
    # Percorre todas as threads criadas, uma a uma, na ordem em que foram iniciadas
    t.join()
    # Bloqueia a execução do script principal até que esta thread específica termine, garantindo que o script só continue depois que todas as VLANs tiverem concluído seus testes

print("✅ Todos os testes finalizados.")
# Exibe mensagem final confirmando que todos os testes de estresse (nas 3 VLANs, rodando em paralelo) foram concluídos