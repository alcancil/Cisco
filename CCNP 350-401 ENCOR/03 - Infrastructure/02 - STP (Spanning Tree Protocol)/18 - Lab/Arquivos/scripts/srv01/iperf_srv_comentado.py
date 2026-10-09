#!/usr/bin/env python3
# Define que este script deve ser executado usando o interpretador Python 3 encontrado no PATH do sistema (shebang, usado ao rodar o arquivo diretamente no Linux, ex: ./iperf_srv.py)

import subprocess
# Importa o módulo subprocess, usado para criar e controlar processos externos (neste caso, os processos do iperf3)

import signal
# Importa o módulo signal, usado para capturar sinais do sistema operacional, como o Ctrl+C (SIGINT)

import sys
# Importa o módulo sys, usado aqui para encerrar o script de forma controlada (sys.exit)

import time
# Importa o módulo time, usado para pausas (sleep) entre etapas do script

import os
# Importa o módulo os, usado aqui para limpar a tela do terminal (os.system('clear'))

# ========= CONFIGURAÇÕES =========
# Comentário de seção, separando visualmente o bloco de configurações do restante do código

VLANS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Lista com os números das 10 VLANs que terão um servidor iperf3 dedicado

PORTA_BASE = 5200
# Porta base usada para calcular a porta de cada VLAN (a porta final será PORTA_BASE + número da VLAN)

# =================================
# Fecha visualmente o bloco de configurações

processos = {}  # {porta: processo}
# Dicionário global que vai guardar, para cada porta, o objeto de processo (Popen) do servidor iperf3 correspondente

def limpar_processos():
    # Define a função que mata quaisquer processos iperf3 que já estejam rodando antes de iniciar novos
    """Mata todos os processos iperf3 que estão rodando"""
    # Docstring explicando o propósito da função
    print("🧹 Limpando processos iperf3 antigos...")
    # Exibe mensagem informando que a limpeza está em andamento
    subprocess.run(["sudo", "pkill", "-f", "iperf3"], stderr=subprocess.DEVNULL)
    # Executa o comando "sudo pkill -f iperf3", que mata todo processo cujo nome/linha de comando contenha "iperf3"; erros são descartados (não exibidos)
    time.sleep(1)
    # Aguarda 1 segundo para dar tempo do sistema operacional finalizar os processos mortos

def iniciar_servidores():
    # Define a função responsável por subir um servidor iperf3 para cada VLAN
    """Inicia um servidor iperf3 para cada VLAN em uma porta única"""
    # Docstring explicando o propósito da função
    print(f"🚀 Iniciando servidores iperf3 para {len(VLANS)} VLANs...\n")
    # Exibe quantos servidores serão iniciados, com base no tamanho da lista VLANS
    for vlan in VLANS:
        # Percorre cada número de VLAN da lista, um de cada vez
        ip = f"10.0.{vlan}.254"
        # Monta o endereço IP da SVI daquela VLAN, assumindo o padrão 10.0.<vlan>.254
        porta = PORTA_BASE + vlan
        # Calcula a porta única desse servidor somando a porta base ao número da VLAN
        cmd = ["sudo", "iperf3", "-s", "-B", ip, "-p", str(porta)]
        # Monta a lista de argumentos do comando: roda o iperf3 em modo servidor (-s), vinculado (bind) ao IP da VLAN (-B) e escutando na porta calculada (-p)
        try:
            # Inicia um bloco de tratamento de exceção, caso o comando falhe ao iniciar
            # Redireciona stdout/stderr para o terminal (mostra mensagens de conexão)
            # Comentário explicando a escolha de parâmetros do Popen logo abaixo
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            # Inicia o processo do servidor iperf3 em segundo plano, capturando sua saída como texto (stdout e stderr combinados no mesmo pipe)
            processos[porta] = p
            # Guarda o processo criado no dicionário global "processos", indexado pela porta, para controle posterior
        except Exception as e:
            # Captura qualquer erro que ocorra ao tentar iniciar o processo
            print(f"❌ Falha ao iniciar VLAN {vlan}: {e}")
            # Exibe mensagem de erro informando qual VLAN falhou e o motivo

def verificar_servidores():
    # Define a função que faz um diagnóstico único (não repetido em loop) logo após os servidores subirem
    """Verifica quais portas estão ouvindo e exibe um diagnóstico imediato"""
    # Docstring explicando o propósito da função
    print("\n🔍 DIAGNÓSTICO IMEDIATO DOS SERVIDORES IPERF3")
    # Exibe o título do relatório de diagnóstico
    print("="*60)
    # Imprime uma linha separadora de 60 sinais de igual, para formatação visual
    print(f"{'VLAN':<6} {'PORTA':<8} {'IP':<20} {'STATUS'}")
    # Imprime o cabeçalho da tabela, com colunas alinhadas à esquerda em larguras fixas
    print("-"*60)
    # Imprime uma linha separadora de 60 traços, abaixo do cabeçalho

    for vlan in VLANS:
        # Percorre cada VLAN da lista para verificar seu respectivo servidor
        porta = PORTA_BASE + vlan
        # Recalcula a porta correspondente a essa VLAN
        ip = f"10.0.{vlan}.254"
        # Recalcula o IP correspondente a essa VLAN

        # Verifica se a porta está em estado LISTEN usando ss
        # Comentário explicando a estratégia de verificação usada a seguir
        try:
            # Inicia bloco de tratamento de exceção para a checagem desta VLAN
            result = subprocess.run(["ss", "-tulpn"], capture_output=True, text=True)
            # Executa o comando "ss -tulpn", que lista sockets TCP/UDP em escuta com processo e PID, capturando a saída como texto
            if f":{porta}" in result.stdout:
                # Verifica se a porta desta VLAN aparece na saída do comando (ou seja, se está em escuta)
                # Tenta pegar o PID do iperf3
                # Comentário explicando o bloco seguinte
                pid = "?"
                # Inicializa o PID como desconhecido, caso não seja encontrado
                for linha in result.stdout.split('\n'):
                    # Percorre cada linha da saída do comando "ss", separando por quebras de linha
                    if f":{porta}" in linha and "iperf3" in linha:
                        # Verifica se esta linha específica contém a porta procurada E a palavra "iperf3"
                        partes = linha.split()
                        # Quebra a linha em pedaços separados por espaço, para poder localizar o campo do PID
                        for parte in partes:
                            # Percorre cada pedaço da linha em busca do campo que contém o PID
                            if "pid=" in parte:
                                # Verifica se este pedaço contém o texto "pid=", indicando o campo do identificador do processo
                                pid = parte.split("=")[1].split(",")[0]
                                # Extrai o valor do PID: pega o que vem depois do "=" e, antes de uma eventual vírgula
                                break
                                # Interrompe o loop interno assim que o PID for encontrado
                        break
                        # Interrompe o loop externo (percorrer linhas), já que a linha certa foi localizada
                print(f"VLAN {vlan:<4} {porta:<8} {ip:<20} 🟢 OK (PID: {pid})")
                # Imprime a linha da tabela indicando que a VLAN está OK, junto com o PID encontrado
            else:
                # Caso a porta não apareça na saída do "ss" (não está escutando)
                print(f"VLAN {vlan:<4} {porta:<8} {ip:<20} 🔴 FALHA (NÃO ESTÁ OUVINDO)")
                # Imprime a linha da tabela indicando falha, pois nenhum processo está escutando nessa porta
        except Exception as e:
            # Captura qualquer erro inesperado durante a checagem desta VLAN
            print(f"VLAN {vlan:<4} {porta:<8} {ip:<20} ❌ ERRO: {e}")
            # Imprime a linha da tabela indicando erro técnico, junto com a mensagem da exceção

    print("-"*60)
    # Imprime uma linha separadora, fechando a tabela de status

    # Exibe conexões ativas nas portas das VLANs
    # Comentário introduzindo a próxima seção do diagnóstico
    print("\n📡 Conexões ativas (ESTAB):")
    # Imprime o título da seção de conexões estabelecidas
    try:
        # Inicia bloco de tratamento de exceção para a checagem de conexões ativas
        result = subprocess.run(["ss", "-tnp"], capture_output=True, text=True)
        # Executa o comando "ss -tnp", que lista conexões TCP com informações de processo, capturando a saída como texto
        linhas = result.stdout.split('\n')
        # Separa a saída do comando em uma lista de linhas individuais
        encontrou = False
        # Inicializa uma flag indicando que, até agora, nenhuma conexão ativa foi encontrada
        for linha in linhas:
            # Percorre cada linha da saída do comando "ss"
            if "ESTAB" in linha:
                # Verifica se esta linha representa uma conexão no estado "ESTABLISHED" (estabelecida)
                for vlan in VLANS:
                    # Para cada conexão estabelecida, percorre todas as VLANs para identificar a qual ela pertence
                    porta = PORTA_BASE + vlan
                    # Recalcula a porta correspondente a esta VLAN
                    if f":{porta}" in linha:
                        # Verifica se a porta desta VLAN aparece nesta linha de conexão
                        print(f"   ✅ {linha.strip()}")
                        # Imprime a linha da conexão (sem espaços extras nas bordas), confirmando que pertence a uma VLAN monitorada
                        encontrou = True
                        # Marca que pelo menos uma conexão ativa foi encontrada
                        break
                        # Interrompe o loop de VLANs, já que a porta desta linha já foi identificada
        if not encontrou:
            # Verifica se, após percorrer todas as linhas, nenhuma conexão ativa foi encontrada
            print("   (Nenhuma conexão ativa no momento)")
            # Informa que não há conexões ativas nas portas monitoradas
    except:
        # Captura silenciosamente qualquer erro nesta checagem (sem exibir mensagem)
        pass
        # Não faz nada em caso de erro, apenas ignora e segue o fluxo
    print("="*60)
    # Imprime uma linha separadora final, fechando o relatório de diagnóstico

def exibir_status():
    # Define a função que exibe o status em tempo real, atualizado repetidamente em loop
    """Exibe uma tabela atualizada dos processos iperf3 escutando e conexões ativas (loop)"""
    # Docstring explicando o propósito da função
    os.system('clear')
    # Limpa a tela do terminal antes de reimprimir o status atualizado
    print("=" * 60)
    # Imprime uma linha separadora de abertura
    print("🟢 SERVIDORES IPERF3 RODANDO (atualizado a cada 3s)")
    # Imprime o título do painel de status, indicando a frequência de atualização
    print("=" * 60)
    # Imprime outra linha separadora, fechando o cabeçalho do painel
    print(f"{'VLAN':<6} {'PORTA':<8} {'PID':<8} {'IP':<20} {'STATUS'}")
    # Imprime o cabeçalho da tabela de status, com colunas alinhadas
    print("-" * 60)
    # Imprime uma linha separadora abaixo do cabeçalho

    for vlan in VLANS:
        # Percorre cada VLAN para montar sua linha na tabela de status
        porta = PORTA_BASE + vlan
        # Recalcula a porta desta VLAN
        ip = f"10.0.{vlan}.254"
        # Recalcula o IP desta VLAN
        p = processos.get(porta)
        # Busca no dicionário global o processo associado a esta porta (ou None, se não existir)
        if p is not None:
            # Verifica se existe um processo registrado para esta porta
            if p.poll() is None:
                # Verifica se o processo ainda está em execução (poll() retorna None enquanto o processo estiver vivo)
                status = "🟢 OK"
                # Define o status como "OK", já que o processo está rodando
                # Tenta pegar o PID real do iperf3 via pgrep
                # Comentário explicando a checagem seguinte
                try:
                    # Inicia bloco de tratamento de exceção para a busca do PID real
                    result = subprocess.run(["pgrep", "-f", f"iperf3 -s -B {ip} -p {porta}"],
                                           capture_output=True, text=True)
                    # Executa "pgrep -f" buscando um processo cuja linha de comando bata exatamente com o comando iperf3 desta VLAN
                    pid = result.stdout.strip()
                    # Remove espaços/quebras de linha extras do PID retornado
                    if not pid:
                        # Verifica se nenhum PID foi retornado (string vazia)
                        pid = "?"
                        # Define o PID como desconhecido, caso não tenha sido encontrado
                    print(f"VLAN {vlan:<4} {porta:<8} {pid:<8} {ip}    {status}")
                    # Imprime a linha da tabela com VLAN, porta, PID encontrado, IP e status "OK"
                except:
                    # Captura qualquer erro ocorrido ao tentar buscar o PID
                    print(f"VLAN {vlan:<4} {porta:<8} {'?':<8} {ip}    {status}")
                    # Imprime a linha da tabela mesmo assim, com PID desconhecido, já que o processo está rodando
            else:
                # Caso o processo já tenha terminado (poll() retornou um código de saída)
                status = "🔴 MORTO"
                # Define o status como "MORTO", indicando que o processo não está mais rodando
                print(f"VLAN {vlan:<4} {porta:<8} {'?':<8} {ip}    {status}")
                # Imprime a linha da tabela indicando que o processo desta VLAN morreu
        else:
            # Caso não exista nenhum processo registrado para esta porta
            print(f"VLAN {vlan:<4} {porta:<8} {'?':<8} {ip}    ❌ NÃO INICIADO")
            # Imprime a linha da tabela indicando que o servidor desta VLAN nunca foi iniciado

    print("\n📡 Conexões ativas (ESTAB):")
    # Imprime o título da seção de conexões ativas, igual ao da função de diagnóstico
    try:
        # Inicia bloco de tratamento de exceção para checagem de conexões ativas
        result = subprocess.run(["ss", "-tnp"], capture_output=True, text=True)
        # Executa "ss -tnp" novamente, agora dentro do loop de atualização contínua
        linhas = result.stdout.split('\n')
        # Separa a saída em linhas individuais
        encontrou = False
        # Reinicializa a flag de "conexão encontrada" para esta atualização
        for linha in linhas:
            # Percorre cada linha da saída do comando
            if "ESTAB" in linha:
                # Verifica se a linha representa uma conexão estabelecida
                for vlan in VLANS:
                    # Percorre as VLANs para identificar a qual esta conexão pertence
                    porta = PORTA_BASE + vlan
                    # Recalcula a porta desta VLAN
                    if f":{porta}" in linha:
                        # Verifica se a porta aparece nesta linha de conexão
                        print(f"   ✅ {linha.strip()}")
                        # Imprime a linha da conexão ativa encontrada
                        encontrou = True
                        # Marca que uma conexão foi encontrada nesta atualização
                        break
                        # Interrompe o loop de VLANs, já que a porta desta conexão já foi identificada
        if not encontrou:
            # Verifica se nenhuma conexão ativa foi encontrada nesta atualização
            print("   (Nenhuma conexão ativa no momento)")
            # Informa a ausência de conexões ativas no momento
    except:
        # Captura silenciosamente qualquer erro nesta checagem
        pass
        # Ignora o erro e segue o fluxo do programa
    print("=" * 60)
    # Imprime uma linha separadora final, fechando esta atualização do painel

def encerrar_processos():
    # Define a função responsável por encerrar todos os servidores iperf3 ao finalizar o script
    """Mata os processos iperf3 que este script iniciou e qualquer outro iperf3 restante"""
    # Docstring explicando o propósito da função
    print("\n🛑 Encerrando servidores iperf3...")
    # Informa que o processo de encerramento está começando
    for porta, p in processos.items():
        # Percorre todos os pares (porta, processo) armazenados no dicionário global
        try:
            # Inicia bloco de tratamento de exceção para encerrar este processo específico
            p.terminate()
            # Envia um sinal de término (SIGTERM) ao processo do servidor iperf3
            p.wait(timeout=2)
            # Aguarda até 2 segundos para o processo finalizar de fato
        except:
            # Captura qualquer erro ocorrido ao tentar terminar este processo específico
            pass
            # Ignora o erro e continua para o próximo processo
    subprocess.run(["sudo", "pkill", "-f", "iperf3"], stderr=subprocess.DEVNULL)
    # Executa um "pkill" final para garantir que nenhum processo iperf3 remanescente continue rodando
    print("✅ Servidores encerrados.")
    # Confirma que o encerramento foi concluído

def handler(signum, frame):
    # Define a função que trata o sinal de interrupção (Ctrl+C), recebendo o número do sinal e o frame de execução
    print("\n\n⚠️  Interrupção detectada. Encerrando servidores...")
    # Informa ao usuário que a interrupção foi detectada e que o encerramento está em andamento
    encerrar_processos()
    # Chama a função que mata todos os processos iperf3 em execução
    sys.exit(0)
    # Encerra o script com código de saída 0 (sucesso), após a limpeza

def main():
    # Define a função principal, que orquestra toda a execução do script
    signal.signal(signal.SIGINT, handler)
    # Registra a função "handler" para ser chamada sempre que o sinal SIGINT (Ctrl+C) for recebido
    limpar_processos()
    # Chama a função que mata quaisquer processos iperf3 antigos antes de começar
    iniciar_servidores()
    # Chama a função que sobe um servidor iperf3 para cada VLAN

    # Espera um pouco para os servidores inicializarem
    # Comentário explicando o motivo da pausa a seguir
    time.sleep(2)
    # Aguarda 2 segundos para dar tempo dos servidores iperf3 subirem completamente

    # Executa o diagnóstico imediato
    # Comentário introduzindo a chamada seguinte
    verificar_servidores()
    # Chama a função que exibe o diagnóstico único logo após a inicialização

    print("\n⏳ Servidores rodando. Pressione Ctrl+C para parar.")
    # Informa ao usuário que os servidores estão ativos e como pará-los
    print("💡 Execute o teste de estresse no Host Linux agora.\n")
    # Sugere ao usuário que inicie o teste de carga (iperf3 client) a partir de outro host
    print("🔄 Atualizando status a cada 3 segundos...")
    # Informa que o painel de status abaixo será atualizado periodicamente

    try:
        # Inicia bloco de tratamento de exceção para o loop principal de monitoramento
        while True:
            # Cria um laço infinito, que só é interrompido por Ctrl+C ou erro
            exibir_status()
            # Chama a função que limpa a tela e reimprime o status atualizado dos servidores
            time.sleep(3)
            # Aguarda 3 segundos antes da próxima atualização do painel
    except KeyboardInterrupt:
        # Captura o Ctrl+C caso ele escape do handler registrado (proteção extra)
        pass
        # Não faz nada, apenas permite que o script termine normalmente

if __name__ == "__main__":
    # Verifica se este arquivo está sendo executado diretamente (não importado como módulo)
    main()
    # Chama a função principal, iniciando toda a execução do script