from netmiko import ConnectHandler                     # Importa a classe ConnectHandler da biblioteca Netmiko, que gerencia conexões SSH com equipamentos de rede
import os                                              # Importa o módulo 'os' para interagir com o sistema operacional (verificar arquivos, caminhos)
import glob                                            # Importa o módulo 'glob' para listar arquivos que correspondem a um padrão (ex: todos os .cfg da pasta backups)
import getpass                                         # Importa o módulo 'getpass' para ler senhas sem exibi-las no terminal
import time                                            # Importa o módulo 'time' para usar pausas (sleep) entre operações

# ========= CONFIGURAÇÕES =========                        # Início da seção de configurações
BACKUP_DIR = "backups"                                  # Define o diretório onde os backups estão armazenados
# =================================                        # Fim da seção de configurações

def listar_backups():                                   # Define a função que lista todos os backups disponíveis
    """Lista todos os arquivos .cfg na pasta backups e retorna uma lista com os nomes."""  # Docstring da função
    backups = glob.glob(f"{BACKUP_DIR}/*.cfg")          # Usa glob para encontrar todos os arquivos .cfg dentro do diretório backups
    if not backups:                                     # Verifica se a lista de backups está vazia
        print("Nenhum backup encontrado na pasta 'backups'.")  # Exibe mensagem informando que não há backups
        return []                                        # Retorna uma lista vazia
    print("\n📂 Backups disponíveis:")                  # Exibe o cabeçalho da lista de backups
    for i, arquivo in enumerate(backups):               # Percorre a lista de backups com índice (i = 0,1,2...)
        print(f"  {i+1}. {arquivo}")                    # Exibe o número (i+1) e o caminho do arquivo
    return backups                                      # Retorna a lista completa de backups

def obter_hostname(connection):                         # Define a função que extrai o hostname do prompt do dispositivo
    """Pega o nome do switch diretamente do prompt da conexão."""  # Docstring da função
    try:                                                # Inicia um bloco de tratamento de exceções
        prompt = connection.base_prompt                 # Obtém o prompt completo da conexão (ex: "SW_CORE01#")
        return prompt.replace('#', '').strip()          # Remove o caractere '#' do final e espaços, retornando apenas o nome
    except:                                             # Se ocorrer qualquer erro no bloco try
        return None                                     # Retorna None para indicar que não foi possível obter o hostname

def restaurar_backup(ip, username, password, arquivo_backup):  # Define a função principal de restauração de um único equipamento
    """Restaura a configuração de um equipamento a partir de um arquivo de backup."""  # Docstring da função
    # CORREÇÃO AQUI: Não use read_timeout no dicionário
    device = {                                          # Cria o dicionário com os parâmetros de conexão
        "device_type": "cisco_ios",                     # Define o tipo de dispositivo como Cisco IOS
        "host": ip,                                     # Define o endereço IP do equipamento
        "username": username,                           # Define o nome de usuário para autenticação
        "password": password,                           # Define a senha para autenticação
        "conn_timeout": 10,                             # Tempo máximo (em segundos) para estabelecer a conexão
        "timeout": 180,                                 # Tempo máximo total (em segundos) para a execução de comandos (3 minutos)
        "fast_cli": False                               # Desabilita o modo rápido (mais seguro para configurações grandes)
    }
    
    connection = None                                   # Inicializa a variável connection como None (para controle no bloco finally)
    try:                                                # Inicia o bloco de tratamento de exceções
        print(f"\n🔌 Conectando em {ip}...")           # Exibe mensagem informando que está conectando ao IP fornecido
        connection = ConnectHandler(**device)           # Estabelece a conexão SSH usando os parâmetros do dicionário 'device'
        
        if not os.path.isfile(arquivo_backup):          # Verifica se o arquivo de backup existe no sistema
            print(f"❌ Arquivo de backup não encontrado: {arquivo_backup}")  # Exibe mensagem de erro
            return False                                # Retorna False indicando falha
        
        hostname = obter_hostname(connection)           # Chama a função obter_hostname para pegar o nome do switch
        if hostname:                                    # Verifica se o hostname foi obtido com sucesso
            print(f"✅ Conectado a {hostname}")        # Exibe mensagem de confirmação com o nome do host
        else:                                           # Se não foi possível obter o hostname
            print(f"✅ Conectado a {ip}")              # Exibe mensagem com o IP do dispositivo
            hostname = ip.replace('.', '_')             # Usa o IP (com underscores) como nome para o arquivo
        
        print(f"🔄 Aplicando configuração a partir do arquivo {arquivo_backup}...")  # Exibe mensagem informando a aplicação da configuração
        
        # CORREÇÃO AQUI: read_timeout é passado como argumento da função, não no dicionário
        output = connection.send_config_from_file(      # Executa a aplicação da configuração diretamente do arquivo
            arquivo_backup,                             # Caminho do arquivo de backup a ser aplicado
            delay_factor=1,                             # Fator de atraso padrão (1 = sem atraso adicional)
            strip_command=False,                        # Não remove os comandos da saída (útil para debug)
            read_timeout=180                            # Tempo máximo (em segundos) para leitura da saída (3 minutos)
        )
        
        print("🔁 Configuração aplicada.")             # Exibe mensagem confirmando que a configuração foi aplicada
        connection.send_command("write memory")         # Envia o comando 'write memory' para salvar a configuração na NVRAM
        print("💾 Configuração salva na memória não volátil.")  # Exibe mensagem confirmando o salvamento
        return True                                     # Retorna True indicando sucesso
        
    except Exception as e:                              # Captura qualquer exceção que ocorra no bloco try
        print(f"❌ Erro ao restaurar {ip}: {e}")       # Exibe a mensagem de erro com o IP e a descrição do erro
        print("⚠️ A configuração pode ter sido aplicada parcialmente. Verifique manualmente.")  # Aviso sobre possível aplicação parcial
        return False                                    # Retorna False indicando falha
    finally:                                            # Bloco que será executado sempre, independentemente de erros
        if connection:                                  # Verifica se a conexão foi estabelecida (não é None)
            try:                                        # Tenta desconectar
                connection.disconnect()                 # Desconecta do equipamento
            except:                                     # Se ocorrer erro na desconexão
                pass                                    # Ignora e não faz nada

def restaurar_varios_backups(lista_ips, username, password):  # Define a função que restaura múltiplos equipamentos
    """Restaura a configuração de vários equipamentos usando a convenção de nome de arquivo."""  # Docstring da função
    sucessos = 0                                        # Inicializa o contador de restaurações bem-sucedidas
    falhas = 0                                          # Inicializa o contador de restaurações com falha
    
    for ip in lista_ips:                                # Loop através de cada IP na lista fornecida
        device = {                                      # Cria o dicionário com os parâmetros de conexão (apenas para obter o hostname)
            "device_type": "cisco_ios",                 # Define o tipo de dispositivo como Cisco IOS
            "host": ip,                                 # Define o endereço IP do equipamento
            "username": username,                       # Define o nome de usuário
            "password": password,                       # Define a senha
            "conn_timeout": 10,                         # Tempo máximo para estabelecer a conexão
            "timeout": 30,                              # Tempo máximo para execução de comandos (obter hostname é rápido)
        }
        connection = None                               # Inicializa a variável connection como None
        hostname = None                                 # Inicializa a variável hostname como None
        try:                                            # Tenta conectar para obter o hostname
            connection = ConnectHandler(**device)       # Estabelece a conexão SSH
            hostname = obter_hostname(connection)       # Obtém o hostname do dispositivo
            connection.disconnect()                     # Desconecta após obter o hostname
        except Exception as e:                          # Captura qualquer exceção
            print(f"❌ Erro ao conectar em {ip} para obter hostname: {e}")  # Exibe mensagem de erro
            falhas += 1                                 # Incrementa o contador de falhas
            continue                                    # Pula para o próximo IP (não tenta restaurar este)
        finally:                                        # Bloco que será executado sempre
            if connection:                              # Verifica se a conexão foi estabelecida
                try:                                    # Tenta desconectar
                    connection.disconnect()             # Desconecta do equipamento
                except:                                 # Se ocorrer erro na desconexão
                    pass                                # Ignora
        
        if not hostname:                                # Se não foi possível obter o hostname
            hostname = ip.replace('.', '_')             # Usa o IP (com underscores) como nome para o arquivo
        
        from datetime import datetime                   # Importa a classe datetime (para obter a data atual)
        hoje = datetime.now().strftime("%Y-%m-%d")      # Obtém a data atual no formato AAAA-MM-DD
        arquivo = f"{BACKUP_DIR}/{hostname}_{hoje}.cfg" # Constrói o nome do arquivo esperado: backups/hostname_data.cfg
        if not os.path.isfile(arquivo):                 # Verifica se o arquivo com a data atual existe
            backups_host = glob.glob(f"{BACKUP_DIR}/{hostname}_*.cfg")  # Procura qualquer backup desse hostname (qualquer data)
            if not backups_host:                        # Se nenhum backup for encontrado
                print(f"❌ Nenhum backup encontrado para {hostname}.")  # Exibe mensagem de erro
                falhas += 1                             # Incrementa o contador de falhas
                continue                                # Pula para o próximo IP
            arquivo = max(backups_host, key=os.path.getmtime)  # Escolhe o backup mais recente (maior data de modificação)
            print(f"📄 Usando backup mais recente: {arquivo}")  # Exibe qual backup será usado
        
        if restaurar_backup(ip, username, password, arquivo):  # Chama a função restaurar_backup com os dados obtidos
            sucessos += 1                                 # Se retornou True, incrementa o contador de sucessos
        else:                                             # Se retornou False
            falhas += 1                                   # Incrementa o contador de falhas
        time.sleep(2)                                     # Pausa de 2 segundos entre restaurações para evitar sobrecarga
    
    return sucessos, falhas                               # Retorna a quantidade de sucessos e falhas

# === MENU PRINCIPAL ===
while True:                                               # Inicia um loop infinito para exibir o menu até que o usuário escolha sair
    print("\n" + "="*50)                                  # Imprime uma linha de separação com 50 caracteres '='
    print("🔹 LABORATÓRIO DE RESTAURAÇÃO DE BACKUPS 🔹")  # Título do menu
    print("1 - Restaurar backup de UM equipamento (escolher arquivo)")  # Opção 1 do menu
    print("2 - Restaurar backup de VÁRIOS equipamentos (lista de IPs, usa nome automático)")  # Opção 2 do menu
    print("3 - Sair")                                     # Opção 3 do menu
    print("="*50)                                         # Imprime outra linha de separação
    
    opcao = input("Escolha uma opção (1/2/3): ").strip()  # Solicita ao usuário a opção desejada e remove espaços extras
    
    if opcao == "1":                                      # Se a opção for 1 (restaurar backup de um único equipamento)
        backups = listar_backups()                        # Chama a função listar_backups para obter a lista de backups disponíveis
        if not backups:                                   # Se não houver backups
            continue                                      # Volta para o início do loop (re-exibe o menu)
        
        escolha = input("\nDigite o número do backup que deseja restaurar (ou Enter para cancelar): ").strip()  # Solicita o número do backup
        if not escolha.isdigit() or int(escolha) > len(backups):  # Verifica se a entrada é válida (número dentro da faixa)
            print("Restauração cancelada.")                # Exibe mensagem de cancelamento
            continue                                      # Volta para o início do loop
        arquivo_backup = backups[int(escolha)-1]          # Obtém o caminho do backup selecionado (índice 0-based)
        
        ip = input("IP do dispositivo: ").strip()         # Solicita o IP do dispositivo
        if not ip:                                        # Verifica se o IP foi fornecido
            print("⚠️ IP inválido.")                      # Exibe mensagem de erro
            continue                                      # Volta para o início do loop
        username = input("Usuário: ").strip()             # Solicita o nome de usuário
        password = getpass.getpass("Senha: ")             # Solicita a senha (não exibe o que é digitado)
        
        sucesso = restaurar_backup(ip, username, password, arquivo_backup)  # Chama a função de restauração
        
    elif opcao == "2":                                    # Se a opção for 2 (restaurar múltiplos equipamentos)
        print("\n📋 Digite os IPs separados por VÍRGULA (Ex: 192.168.1.1, 10.0.0.5)")  # Instruções para digitar os IPs
        lista_ips_input = input("IPs: ").strip()          # Solicita a lista de IPs
        lista_ips = [ip.strip() for ip in lista_ips_input.split(",") if ip.strip()]  # Divide por vírgula, remove espaços e descarta vazios
        
        if not lista_ips:                                 # Se a lista estiver vazia
            print("⚠️ Nenhum IP válido.")                 # Exibe mensagem de erro
            continue                                      # Volta para o início do loop
        
        username = input("Usuário para todos: ").strip()  # Solicita o nome de usuário que será usado em todos os equipamentos
        password = getpass.getpass("Senha para todos: ")  # Solicita a senha que será usada em todos
        
        print(f"\n🔄 Iniciando restauração de {len(lista_ips)} equipamento(s)...")  # Informa quantos equipamentos serão processados
        sucessos, falhas = restaurar_varios_backups(lista_ips, username, password)  # Chama a função de restauração múltipla
        print(f"\n📊 Resumo: {sucessos} restaurações realizadas, {falhas} falhas.")  # Exibe o resumo das restaurações
        
    elif opcao == "3":                                    # Se a opção for 3 (sair)
        print("👋 Encerrando o script.")                  # Exibe mensagem de encerramento
        break                                             # Sai do loop while (encerra o script)
    else:                                                 # Se a opção não for 1, 2 ou 3
        print("❌ Opção inválida.")                       # Exibe mensagem de erro
    
    continuar = input("\n🔁 Deseja fazer mais restaurações? (s/n): ").lower()  # Pergunta se o usuário quer continuar
    if continuar != "s":                                  # Se a resposta for diferente de 's' (sim)
        print("👋 Até mais!")                             # Exibe mensagem de despedida
        break                                             # Sai do loop while (encerra o script)

# Fim do script