from netmiko import ConnectHandler                     # Importa a classe ConnectHandler da biblioteca Netmiko, que gerencia conexões SSH com equipamentos de rede
from datetime import datetime                         # Importa a classe datetime para obter a data e hora atuais, usada no nome do arquivo de backup
import os                                             # Importa o módulo os para interagir com o sistema operacional (criar diretórios, verificar arquivos)
import getpass                                         # Importa o módulo getpass para ler senhas sem exibi-las no terminal
import time                                            # Importa o módulo time para usar pausas (sleep) entre conexões

os.makedirs("backups", exist_ok=True)                  # Cria o diretório 'backups' se ele não existir; 'exist_ok=True' evita erro se o diretório já existir

def obter_hostname(connection):                        # Define uma função que recebe uma conexão Netmiko e retorna o nome do host
    """Pega o nome do switch diretamente do prompt da conexão (confiável 100%)."""  # Docstring explicando que o nome é extraído do prompt do equipamento
    try:                                               # Inicia um bloco de tratamento de exceções (para capturar erros)
        prompt = connection.base_prompt                # Obtém o prompt completo da conexão (ex: "SW_CORE01#")
        return prompt.replace('#', '').strip()         # Remove o caractere '#' do final e remove espaços em branco, retornando apenas o nome (ex: "SW_CORE01")
    except:                                            # Se ocorrer qualquer erro no bloco try
        return None                                    # Retorna None para indicar que não foi possível obter o hostname

def fazer_backup(ip, username, password):              # Define a função principal que faz o backup de um único equipamento, recebendo IP, usuário e senha
    device = {                                         # Cria um dicionário com as credenciais e parâmetros de conexão
        "device_type": "cisco_ios",                    # Define o tipo de dispositivo como Cisco IOS
        "host": ip,                                    # Define o endereço IP do equipamento
        "username": username,                          # Define o nome de usuário para autenticação
        "password": password,                          # Define a senha para autenticação
        "conn_timeout": 10,                            # Tempo máximo (em segundos) para estabelecer a conexão
        "timeout": 30,                                 # Tempo máximo (em segundos) para a execução de comandos
    }
    
    connection = None                                  # Inicializa a variável connection como None (para controle no bloco finally)
    try:                                               # Inicia o bloco de tratamento de exceções
        print(f"\n🔌 Conectando em {ip}...")          # Exibe uma mensagem informando que está conectando ao IP fornecido
        connection = ConnectHandler(**device)          # Estabelece a conexão SSH usando os parâmetros do dicionário 'device'
        
        hostname = obter_hostname(connection)          # Chama a função obter_hostname para pegar o nome do switch a partir do prompt
        if not hostname:                               # Verifica se o hostname não foi obtido (retornou None)
            print(f"⚠️  Não foi possível obter o hostname para {ip}. Usando IP no nome.")  # Exibe um aviso
            hostname = ip.replace('.', '_')            # Substitui os pontos do IP por underscore para usá-lo como nome do arquivo
        
        print(f"📥 Baixando configuração de {hostname}...")  # Exibe mensagem informando que está baixando a configuração do host
        output = connection.send_command("show running-config")  # Executa o comando 'show running-config' e armazena a saída na variável 'output'
        
        hoje = datetime.now().strftime("%Y-%m-%d")     # Obtém a data atual no formato AAAA-MM-DD (ex: 2026-06-11)
        filename = f"backups/{hostname}_{hoje}.cfg"    # Constrói o nome do arquivo de backup: pasta backups, nome do host, data, extensão .cfg
        
        with open(filename, "w") as f:                 # Abre o arquivo no modo escrita
            f.write(output)                           # Escreve a saída do comando 'show running-config' no arquivo
        
        print(f"✅ Backup salvo: {filename}")          # Exibe uma mensagem de confirmação com o caminho do arquivo salvo
        return True                                   # Retorna True indicando que o backup foi bem-sucedido
        
    except Exception as e:                            # Captura qualquer exceção que ocorra no bloco try
        print(f"❌ Erro no dispositivo {ip}: {e}")   # Exibe a mensagem de erro com o IP do dispositivo e a descrição do erro
        return False                                  # Retorna False indicando que o backup falhou
    finally:                                          # Bloco que será executado sempre, independentemente de erros
        if connection:                                # Verifica se a conexão foi estabelecida (não é None)
            try:                                      # Tenta desconectar
                connection.disconnect()               # Desconecta do equipamento
            except:                                   # Se ocorrer erro na desconexão, ignora (não faz nada)
                pass                                  # Não faz nada

# === MENU PRINCIPAL ===
while True:                                           # Inicia um loop infinito para exibir o menu até que o usuário escolha sair
    print("\n" + "="*50)                              # Imprime uma linha de separação com 50 caracteres '='
    print("🔹 LABORATÓRIO DE BACKUP - VERSÃO ROBUSTA 🔹")  # Título do menu
    print("1 - Fazer backup de UM equipamento")       # Opção 1 do menu
    print("2 - Fazer backup de VÁRIOS equipamentos (lista de IPs)")  # Opção 2 do menu
    print("3 - Sair")                                 # Opção 3 do menu
    print("="*50)                                     # Imprime outra linha de separação
    
    opcao = input("Escolha uma opção (1/2/3): ").strip()  # Solicita ao usuário a opção desejada e remove espaços extras
    
    if opcao == "1":                                   # Se a opção for 1 (backup de um único equipamento)
        ip = input("\nDigite o IP do dispositivo: ").strip()  # Solicita o IP do dispositivo
        if not ip:                                     # Verifica se o IP não foi fornecido
            print("⚠️ IP inválido.")                  # Exibe mensagem de erro
            continue                                   # Volta para o início do loop (re-exibe o menu)
        username = input("Usuário: ").strip()          # Solicita o nome de usuário
        password = getpass.getpass("Senha: ")          # Solicita a senha (não exibe o que é digitado)
        fazer_backup(ip, username, password)           # Chama a função fazer_backup com os dados fornecidos
        
    elif opcao == "2":                                 # Se a opção for 2 (backup de múltiplos equipamentos)
        print("\n📋 Digite os IPs separados por VÍRGULA (Ex: 192.168.1.1, 10.0.0.5)")  # Instruções para digitar os IPs
        lista_ips_input = input("IPs: ").strip()       # Solicita a lista de IPs
        lista_ips = [ip.strip() for ip in lista_ips_input.split(",") if ip.strip()]  # Divide a string por vírgula, remove espaços e descarta entradas vazias
        
        if not lista_ips:                              # Se a lista estiver vazia
            print("⚠️ Nenhum IP válido.")              # Exibe mensagem de erro
            continue                                   # Volta para o início do loop
        
        username = input("Usuário para todos: ").strip()  # Solicita o nome de usuário que será usado em todos os equipamentos
        password = getpass.getpass("Senha para todos: ")  # Solicita a senha que será usada em todos
        
        print(f"\n🔄 Iniciando backup de {len(lista_ips)} equipamento(s)...")  # Informa quantos equipamentos serão processados
        
        sucessos = 0                                   # Inicializa o contador de backups bem-sucedidos
        falhas = 0                                     # Inicializa o contador de backups com falha
        for ip in lista_ips:                           # Loop através de cada IP na lista
            if fazer_backup(ip, username, password):   # Chama a função fazer_backup e verifica se retornou True
                sucessos += 1                          # Se sim, incrementa o contador de sucessos
            else:                                      # Se retornou False
                falhas += 1                            # Incrementa o contador de falhas
            time.sleep(1)                              # Pausa de 1 segundo para evitar sobrecarga na rede e permitir que as conexões sejam encerradas adequadamente
        
        print(f"\n📊 Resumo: {sucessos} backups realizados, {falhas} falhas.")  # Exibe o resumo dos backups
        
    elif opcao == "3":                                 # Se a opção for 3 (sair)
        print("👋 Encerrando o script.")               # Exibe mensagem de encerramento
        break                                          # Sai do loop while (encerra o script)
    else:                                              # Se a opção não for 1, 2 ou 3
        print("❌ Opção inválida.")                    # Exibe mensagem de erro
    
    continuar = input("\n🔁 Deseja fazer mais backups? (s/n): ").lower()  # Pergunta se o usuário quer continuar fazendo backups
    if continuar != "s":                               # Se a resposta for diferente de 's' (sim)
        print("👋 Até mais!")                         # Exibe mensagem de despedida
        break                                          # Sai do loop while (encerra o script)

# Fim do script