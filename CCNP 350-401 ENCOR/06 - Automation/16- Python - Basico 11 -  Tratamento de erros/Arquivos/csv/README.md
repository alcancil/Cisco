
# Python - Básico 11

## Índice

- [Python - Básico 11](#python---básico-11)
  - [Índice](#índice)
  - [Tratamento de Erros com Arquivos `.csv`](#tratamento-de-erros-com-arquivos-csv)
  - [Erros comuns com arquivos .csv](#erros-comuns-com-arquivos-csv)
  - [Contexto de uso em redes](#contexto-de-uso-em-redes)
    - [Exemplo 01 – Leitura segura de inventario.csv](#exemplo-01--leitura-segura-de-inventariocsv)
    - [Exemplo 02 – Backup de configurações em massa com tratamento de erros](#exemplo-02--backup-de-configurações-em-massa-com-tratamento-de-erros)
    - [Exemplo 02: Backup de configurações em massa](#exemplo-02-backup-de-configurações-em-massa)
    - [Exemplo 03: Processamento de Logs estruturados](#exemplo-03-processamento-de-logs-estruturados)
    - [Exemplo 04: Comparação de dados (Antes/Depois)](#exemplo-04-comparação-de-dados-antesdepois)

## Tratamento de Erros com Arquivos `.csv`

Arquivos .csv (Comma-Separated Values) são amplamente utilizados em automação de redes para representar dados tabulares, como inventário de dispositivos, interfaces, VLANs e localização física de equipamentos.

Mas ao automatizar a leitura desses arquivos, podem ocorrer diversos problemas, como:

- Arquivo inexistente

- Falta de permissões

- Colunas obrigatórias ausentes

- Codificação inválida

A seguir, aprenderemos como usar **try, except, else e finally** para tornar scripts com **.csv** mais robustos e confiáveis.

## Erros comuns com arquivos .csv

| Tipo de erro	              | Exceção Python     | Situação típica                       |
|-----------------------------|--------------------|---------------------------------------| 
| Arquivo não encontrado	  | FileNotFoundError  | Caminho incorreto ou arquivo movido   |
| Permissão negada            | PermissionError    | Tentativa de leitura sem permissão    |
| Coluna ausente no cabeçalho | KeyError           | Cabeçalho incompleto ou mal formatado |
| Delimitador incorreto       | csv.Error	       | Arquivo com separadores errados       |
| Problemas gerais de leitura |	UnicodeDecodeError | Arquivo com codificação inválida      |

## Contexto de uso em redes

Arquivos .csv são úteis para:

- Inventário de switches, roteadores e servidores

- Geração de configurações em massa com base em planilhas

- Alimentar scripts Jinja2 ou Ansible com dados externos

### Exemplo 01 – Leitura segura de inventario.csv

**Objetivo**

Ler um inventário e exibir os dados formatados, garantindo que:

  - O arquivo existe

  - As colunas obrigatórias estão presentes

  - O processo não quebre caso algo esteja errado

**inventario.csv**  

```csv
hostname,ip,modelo,localizacao
switch01,192.168.1.1,Catalyst 9200,Rack 1
router01,192.168.1.254,ISR 4331,Rack Central
linux-server,192.168.1.100,Ubuntu 22.04,Sala de Servidores
```

**script ler_inventario_seguro.py**  

```Python
[01] import csv
[02] import os
[03]
[04] caminho = "inventario.csv"
[05]
[06] try:
[07]     if not os.path.exists(caminho):
[08]         raise FileNotFoundError(f"O arquivo {caminho} não foi encontrado.")
[09] 
[10]     with open(caminho, 'r') as arquivo_csv:
[11]         leitor = csv.DictReader(arquivo_csv)
[12] 
[13]         print("\n📦 Inventário de Dispositivos:")
[14]         for linha in leitor:
[15]             print(f"- {linha['hostname']} | IP: {linha['ip']} | Modelo: {linha['modelo']} | Local: {linha['localizacao']}")
[16] 
[17] except FileNotFoundError as e:
[18]     print(f"❌ Erro: {e}")
[19] except KeyError as e:
[20]     print(f"❌ Erro: Coluna esperada não encontrada no CSV ({e})")
[21] except PermissionError:
[22]     print("❌ Permissão negada para abrir o arquivo.")
[23] except Exception as e:
[24]     print(f"❌ Erro inesperado: {e}")
[25] else:
[26]     print("\n✅ Leitura finalizada com sucesso.")
[27] finally:
[28]     print("🔁 Fim do processamento.\n")
```

**Saída**

```bash
alcancil@linux:~/automacoes/erros/csv/01$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/csv/01$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/csv/01$ python3 ler_inventario_seguro.py 

📦 Inventário de Dispositivos:
- switch01 | IP: 192.168.1.1 | Modelo: Catalyst 9200 | Local: Rack 1
- router01 | IP: 192.168.1.254 | Modelo: ISR 4331 | Local: Rack Central
- linux-server | IP: 192.168.1.100 | Modelo: Ubuntu 22.04 | Local: Sala de Servidores

✅ Leitura finalizada com sucesso.
🔁 Fim do processamento.

(venv) alcancil@linux:~/automacoes/erros/csv/01$ 
```

**Saída com erro**

```Bash
(venv) alcancil@linux:~/automacoes/erros/csv/01$ ls -la
total 20
drwxrwxr-x 3 alcancil alcancil 4096 jun 11 16:10 .
drwxrwxr-x 3 alcancil alcancil 4096 jun 11 16:08 ..
-rw-r--r-- 1 root     root      177 jun 11 16:09 inventario.csv
-rw-r--r-- 1 root     root      867 jun 11 16:10 ler_inventario_seguro.py
drwxrwxr-x 5 alcancil alcancil 4096 jun 11 16:10 venv
(venv) alcancil@linux:~/automacoes/erros/csv/01$ mv inventario.csv inventario1.csv 
(venv) alcancil@linux:~/automacoes/erros/csv/01$ python3 ler_inventario_seguro.py 
❌ Erro: O arquivo inventario.csv não foi encontrado.
🔁 Fim do processamento.

(venv) alcancil@linux:~/automacoes/erros/csv/01$ 
```

**saída com erro 02**

```bash
(venv) alcancil@linux:~/automacoes/erros/csv/01$ sudo chmod -rwrr inventario.csv 
(venv) alcancil@linux:~/automacoes/erros/csv/01$ python3 ler_inventario_seguro.py 
❌ Permissão negada para abrir o arquivo.
🔁 Fim do processamento.

(venv) alcancil@linux:~/automacoes/erros/csv/01$
```

**Explicação**  

```python

Bloco 1: Importação de Bibliotecas

[01] import csv                                                                                                                  # Biblioteca para manipulação de arquivos CSV
[02] import os                                                                                                                   # Biblioteca para interação com sistema operacional
[03]                                                                                                                             # Espaço para melhorar legibilidade

Bloco 2: Definição do Caminho do Arquivo

[04] caminho = "inventario.csv"                                                                                                  # Define o caminho relativo do arquivo CSV
[05]                                                                                                                             # Espaço entre declarações e lógica principal

Bloco 3: Verificação e Leitura do Arquivo

[06] try:                                                                                                                         # Início do bloco para tratamento de erros
[07]     if not os.path.exists(caminho):                                                                                          # Verifica se o arquivo existe no sistema
[08]         raise FileNotFoundError(f"O arquivo {caminho} não foi encontrado.")                                                  # Força um erro específico
[09] 
[10]     with open(caminho, 'r') as arquivo_csv:                                                                                  # Abre o arquivo no modo leitura (seguro)
[11]         leitor = csv.DictReader(arquivo_csv)                                                                                 # Cria um leitor de CSV como dicionário

Bloco 4: Processamento dos Dados

[13]         print("\n📦 Inventário de Dispositivos:")                                                                            # Cabeçalho para organização da saída
[14]         for linha in leitor:                                                                                                 # Itera sobre cada linha do CSV
[15]             print(f"- {linha['hostname']} | IP: {linha['ip']} | Modelo: {linha['modelo']} | Local: {linha['localizacao']}")  # Formata os dados

Bloco 5: Tratamento de Exceções Específicas

[17] except FileNotFoundError as e:                                                                                                # Captura erro de arquivo não encontrado
[18]     print(f"❌ Erro: {e}")                                                                                                   # Mensagem amigável com detalhes do erro
[19] except KeyError as e:                                                                                                         # Captura erro de coluna faltante no CSV
[20]     print(f"❌ Erro: Coluna esperada não encontrada no CSV ({e})")                                                           # Indica qual coluna está faltando
[21] except PermissionError:                                                                                                       # Captura erro de permissão
[22]     print("❌ Permissão negada para abrir o arquivo.")                                                                        # Comum em sistemas Linux/Windows

Bloco 6: Tratamento Genérico e Finalização

[23] except Exception as e:                                                                                                         # Captura qualquer outro erro não previsto
[24]     print(f"❌ Erro inesperado: {e}")                                                                                         # Mensagem genérica para debug
[25] else:                                                                                                                          # Executa apenas se não ocorrerem erros
[26]     print("\n✅ Leitura finalizada com sucesso.")                                                                             # Confirmação de sucesso
[27] finally:                                                                                                                       # Sempre executa, independente de erros
[28]     print("🔁 Fim do processamento.\n")                                                                                       # Mensagem final de status
```

### Exemplo 02 – Backup de configurações em massa com tratamento de erros

**Objetivo**

Ler um arquivo dispositivos.csv, identificar o tipo de dispositivo e simular a criação de um backup de configuração, salvando o conteúdo em arquivos .txt dentro da pasta backups. O script deve:

  - Criar a pasta backups se não existir

  - Tratar erros como:

        * Arquivo ausente

        * Permissão negada

        * Colunas ausentes no CSV

        * Falhas ao criar ou escrever arquivos

**dispositivos.csv**  

```csv
hostname,ip,usuario,senha,tipo
servidor-linux,192.168.1.100,admin,senha123,linux
roteador-simulado,10.0.0.1,cisco,cisco123,cisco_ios
switch-simulado,192.168.1.2,admin,admin123,cisco_ios
```

**Script: backup_config.py**  

```Python
[01] import csv
[02] import os
[03]
[04] caminho_csv = "dispositivos.csv"
[05] pasta_backup = "backups"
[06]
[07] try:
[08]     if not os.path.exists(caminho_csv):
[09]         raise FileNotFoundError("Arquivo dispositivos.csv não encontrado.")
[10]
[11]     os.makedirs(pasta_backup, exist_ok=True)
[12]
[13]     with open(caminho_csv, 'r') as arquivo_csv:
[14]         leitor = csv.DictReader(arquivo_csv)
[15]
[16]         for dispositivo in leitor:
[17]             tipo = dispositivo.get("tipo", "").lower()
[18]
[19]             if tipo == "linux":
[20]                 config = f"hostname {dispositivo['hostname']}\nIP: {dispositivo['ip']}\nSO: Ubuntu 22.04"
[21]             elif "cisco" in tipo:
[22]                 config = f"hostname {dispositivo['hostname']}\ninterface GigabitEthernet0/1\n  ip address {dispositivo['ip']} 255.255.255.0"
[23]             else:
[24]                 raise ValueError(f"Tipo de dispositivo não reconhecido: {tipo}")
[25]
[26]             caminho_saida = os.path.join(pasta_backup, f"{dispositivo['hostname']}_backup.txt")
[27]             with open(caminho_saida, 'w') as saida:
[28]                 saida.write(config)
[29]
[30]             print(f"✅ Backup de {dispositivo['hostname']} salvo em: {caminho_saida}")
[31]
[32] except FileNotFoundError as e:
[33]     print(f"❌ Erro: {e}")
[34] except PermissionError:
[35]     print("❌ Permissão negada para criar arquivos ou ler o CSV.")
[36] except KeyError as e:
[37]     print(f"❌ Coluna ausente no CSV: {e}")
[38] except ValueError as e:
[39]     print(f"❌ Erro de valor: {e}")
[40] except Exception as e:
[41]     print(f"❌ Erro inesperado: {e}")
[42] else:
[43]     print("\n✅ Todos os backups foram gerados com sucesso.")
[44] finally:
[45]     print("🔁 Fim do processamento.")
```

---
Arrumar

🖥️ Saída esperada (com sucesso)

✅ Backup de servidor-linux salvo em: backups/servidor-linux_backup.txt
✅ Backup de roteador-simulado salvo em: backups/roteador-simulado_backup.txt
✅ Backup de switch-simulado salvo em: backups/switch-simulado_backup.txt

✅ Todos os backups foram gerados com sucesso.
🔁 Fim do processamento.

🖥️ Saída esperada (com erro: CSV ausente)

❌ Erro: Arquivo dispositivos.csv não encontrado.
🔁 Fim do processamento.





### Exemplo 02: Backup de configurações em massa  

Nesse exemplo vamos ler o conteúdo do arquivo dispositivos.csv Depois precisamos identificar o tipo de dispositivo. Feito isso, iremos criar um diretório chamado backups, se não existir, e dentro desse diretório vamos gravar o backup das configurações de cada dispositivo.  Os arquivos de backup será armazenado em arquivos separados por tipo de dispositivo.  

**Conteúdo do arquivo dispositivos.csv**

```Python
    hostname,ip,usuario,senha,tipo
    servidor-linux,192.168.1.100,admin,senha123,linux
    roteador-simulado,10.0.0.1,cisco,cisco123,cisco_ios
    switch-simulado,192.168.1.2,admin,admin123,cisco_ios
```

**Script backups.config**

```Python
    [01] import csv
    [02] import os
    [03]
    [04] # Diretório para salvar os backups
    [05] os.makedirs("backups", exist_ok=True)
    [06]
    [07] with open('dispositivos.csv', 'r') as arquivo_csv:
    [08]    leitor = csv.DictReader(arquivo_csv)
    [09]    for dispositivo in leitor:
    [10]        # Simula a "configuração" baseada no tipo do dispositivo
    [11]        if dispositivo['tipo'] == "linux":
    [12]            config = f"hostname {dispositivo['hostname']}\nIP: {dispositivo['ip']}\nSO: Ubuntu 22.04"
    [13]        elif "cisco" in dispositivo['tipo']:
    [14]            config = f"hostname {dispositivo['hostname']}\ninterface GigabitEthernet0/1\n  ip address {dispositivo['ip']} 255.255.255.0"
    [15]        
    [16]        # Salva o "backup" em um arquivo .txt
    [17]        caminho_backup = f"backups/{dispositivo['hostname']}_backup.txt"
    [18]        with open(caminho_backup, 'w') as arquivo_backup:
    [19]            arquivo_backup.write(config)
    [20]        
    [21]        print(f"Backup do {dispositivo['hostname']} salvo em: {caminho_backup}")
```

**Saída**

```Bash
    alcancil@linux:~/automacoes/arquivos/csv/02$ ls -la
    total 16
    drwxrwxr-x 2 alcancil alcancil 4096 mai  4 20:56 .
    drwxrwxr-x 4 alcancil alcancil 4096 mai  4 20:42 ..
    -rw-r--r-- 1 root     root      931 mai  4 20:45 backup.py
    -rw-r--r-- 1 root     root      186 mai  4 20:43 dispositivos.csv
```

Podemos notar que só temos o arquivo .csv e nosso script. Então vamos executar nosso script e ver o resultado.  

```Bash
    alcancil@linux:~/automacoes/arquivos/csv/02$ python3 backup.py
    Backup do servidor-linux salvo em: backups/servidor-linux_backup.txt
    Backup do roteador-simulado salvo em: backups/roteador-simulado_backup.txt
    Backup do switch-simulado salvo em: backups/switch-simulado_backup.txt
    alcancil@linux:~/automacoes/arquivos/csv/02$ ls -lah
    total 20K
    drwxrwxr-x 3 alcancil alcancil 4,0K mai  4 20:56 .
    drwxrwxr-x 4 alcancil alcancil 4,0K mai  4 20:42 ..
    -rw-r--r-- 1 root     root      931 mai  4 20:45 backup.py
    drwxrwxr-x 2 alcancil alcancil 4,0K mai  4 20:56 backups
    -rw-r--r-- 1 root     root      186 mai  4 20:43 dispositivos.csv
    alcancil@linux:~/automacoes/arquivos/csv/02$
```

Podemos notar que o diretório **backups** foi criado. Vamos analisa o conteúdo desse diretório.  

```Bash
    alcancil@linux:~/automacoes/arquivos/csv/02$ cd backups/
    alcancil@linux:~/automacoes/arquivos/csv/02/backups$ ls -la
    total 20
    drwxrwxr-x 2 alcancil alcancil 4096 mai  4 20:56 .
    drwxrwxr-x 3 alcancil alcancil 4096 mai  4 20:56 ..
    -rw-rw-r-- 1 alcancil alcancil   91 mai  4 20:56 roteador-simulado_backup.txt
    -rw-rw-r-- 1 alcancil alcancil   58 mai  4 20:56 servidor-linux_backup.txt
    -rw-rw-r-- 1 alcancil alcancil   92 mai  4 20:56 switch-simulado_backup.txt
    alcancil@linux:~/automacoes/arquivos/csv/02/backups$
```

**Explicação**

- Cria diretório para salvar os backups

```Bash
    Linha [01] : importando o módulo csv para poder utilizar as funções de arquivos csv  
    Linha [02] : importando o módulo os para poder utilizar as funções relativa a sistemas operacionais  
    Linha [05] : Função que cria diretórios recursivamente (ou seja, pode criar várias pastas de uma vez, como pasta/subpasta).  
                **exist_ok=True:**  
                    Se True, evita que o Python lance um erro (FileExistsError) se o diretório já existir.  
    Linha [07] : com o arquivo dispositivos.csv aberto em modo leitura (envie o conteúdo para a variável **arquivo_csv**) faça:  
    Linha [08] : a variável **leitor** recebe o conteúdo da variável arquivo.csv em forma de dicionário.  
 ``` 

 - Simula a "configuração" baseada no tipo do dispositivo  

```Bash
    Linha [09] : para cada dispositivo dentro da variável leitor faça:  
    Linha [11] : se o tipo do dispositivo for **linux**  
    Linha [12] : cria uma string formatada (um texto) que simula uma "configuração" de um dispositivo Linux, usando os valores lidos do arquivo **("hostname servidor-linux\nIP: endereço ip\nSO: Ubuntu 22.04")**  
    Linha [13] : se o tipo do dispositivo for **cisco**  
    Linha [14] : cria uma string formatada (um texto) que simula uma "configuração" de um dispositivo Cisco, usando os valores lidos do arquivo **("hostname roteador-simulado\ninterface GigabitEthernet0/1\nIP: endereço ip 255.255.255.0")**  
```

- Salva o "backup" em um arquivo .txt

```Bash
    Linha [17] : Esta linha define o caminho (path) completo onde o arquivo de backup será salvo, usando f-strings para inserir dinamicamente o nome do dispositivo   
    Linha [18] : com a variável caminho_backup aberta em modo leitura (envie o conteúdo para a variável arquivo_backup) faça:   
    Linha [19] : escreve o conteúdo da variável config (que contém as configurações simuladas do dispositivo) no arquivo de backup que foi aberto anteriormente.  
    Linha [21] : Esta linha imprime uma mensagem no terminal para informar que o backup de um dispositivo foi salvo com sucesso, incluindo dinamicamente: **nome do dispositivo** e **caminho completo**  
```

### Exemplo 03: Processamento de Logs estruturados  

Esse é um caso onde temos arquivos de log de equipamentos que já são um pouco mais estruturados. Então vamos criar um script que leia esse log armazenado em um arquivo csv e consigo separar o tipo de equipamento e o grau de severidade do log.  

**Conteúdo do arquivo log.csv**  

```Bash
    timestamp,dispositivo,nivel,mensagem
    2024-05-10 09:15:23,switch01,ALERTA,Interface GigabitEthernet0/1 down
    2024-05-10 09:16:45,router01,CRITICO,CPU usage 95%
    2024-05-10 09:20:12,switch01,INFO,Interface GigabitEthernet0/1 up
    2024-05-10 09:25:34,firewall01,ALERTA,Blocked 10 SSH attempts
```

**Script processar_log.py**

```Python
    [01] import csv
    [02]
    [03] # Lê o arquivo CSV
    [04] with open('logs.csv', 'r') as arquivo_csv:
    [05]    leitor = csv.DictReader(arquivo_csv)
    [06]   
    [07]    # Filtra logs com nível "CRITICO" ou "ALERTA"
    [08]    logs_filtrados = [
    [09]        log for log in leitor 
    [10]        if log['nivel'] in ['CRITICO', 'ALERTA']
    [11]    ]
    [12]
    [13] # Exibe os logs filtrados
    [14] print("===== LOGS CRÍTICOS/ALERTAS =====")
    [15] for log in logs_filtrados:
    [16]    print(f"{log['timestamp']} | {log['dispositivo']} | {log['nivel']}: {log['mensagem']}")
    [17]
    [18] # Contagem por dispositivo (opcional)
    [19] contagem = {}
    [20] for log in logs_filtrados:
    [21]    dispositivo = log['dispositivo']
    [22]    contagem[dispositivo] = contagem.get(dispositivo, 0) + 1
    [23]
    [24] print("\n===== RESUMO =====")
    [25] for dispositivo, total in contagem.items():
    [26]    print(f"{dispositivo}: {total} alerta(s)")
```  

**Saída**  

```Bash
    alcancil@linux:~/automacoes/arquivos/csv/03$ python3 processar_logo.py 
    ===== LOGS CRÍTICOS/ALERTAS =====
    2024-05-10 09:15:23 | switch01 | ALERTA: Interface GigabitEthernet0/1 down
    2024-05-10 09:16:45 | router01 | CRITICO: CPU usage 95%
    2024-05-10 09:25:34 | firewall01 | ALERTA: Blocked 10 SSH attempts

    ===== RESUMO =====
    switch01: 1 alerta(s)
    router01: 1 alerta(s)
    firewall01: 1 alerta(s)
    alcancil@linux:~/automacoes/arquivos/csv/03$ 
```  

**Explicação**

- Filtro dos logs com nível **CRÍTICO ou ALERTA**

```Bash
    Linha [08] : a variável logs_filtrados recebe o valor da lista ( começa com [ )  
    Linha [09] : percorra cada item (log) dentro do arquivo logs.csv  
    Linha [10] : armazene o valor na variável log se no campo nível conter os valores CRÍTICO ou ALERTA  
    Linha [11] : finaliza a lista ( ])  
``` 

- Contagem por dispositivo (opcional)  

```Bash
    Linha [19] : cria um dicionário chamado contagem  
    Linha [20] : inicia um loop for que percorre cada item da lista logs_filtrados ( Logs filtrados no passo anterior )
    Linha [21] : acessa o valor da chave 'dispositivo' no dicionário log atual e o armazena na variável dispositivo.  
    Linha [22] : inicia o dicionário contagem como contador. O método get() busca o número atual de logs de um dispositivo e, se não houver ainda, começa com 0. A cada log, ele soma 1.
```

### Exemplo 04: Comparação de dados (Antes/Depois)  

Nesse exemplo, vamos supor que temos o estados das portas de um Switch armazenados em um arquivo csv. Então vamos realizar a comparação do estados das portas armazenados nesse arquivo csv com um outro. Esse tipo de situação é útil quando fazemos algum tipo de interação automática com o equipamento e queremos realizar o antes / depois para comparar se a automação está funcionando corretamente.  

**Conteúdo do arquivo portas_antes**

```Bash
    interface,estado
    GigabitEthernet0/0,up
    GigabitEthernet0/1,down
    GigabitEthernet0/2,up
```

**Conteúdo do arquivo portas_depois**

```Bash
    interface,estado
    GigabitEthernet0/0,up
    GigabitEthernet0/1,up
    GigabitEthernet0/2,up
```

**Script comparar.py**

```Python
    [01] import csv
    [02]
    [03] def ler_csv(caminho):
    [04]    dados = {}
    [05]    with open(caminho, newline='') as arquivo:
    [06]        leitor = csv.DictReader(arquivo)
    [07]        for linha in leitor:
    [08]            interface = linha['interface']
    [09]            estado = linha['estado']
    [10]            dados[interface] = estado
    [11]    return dados
    [12]
    [13] # Leitura dos arquivos
    [14] antes = ler_csv("portas_antes.csv")
    [15] depois = ler_csv("portas_depois.csv")
    [16]
    [17] # Comparação
    [18] print("Mudanças detectadas:")
    [19] for interface in antes:
    [20]    if antes[interface] != depois.get(interface):
    [21]        print(f"- {interface}: {antes[interface]} >>> {depois.get(interface)}")
```

**Saída**

```Bash
    alcancil@linux:~/automacoes/arquivos/csv/04$ python3 comparar.py 
    Mudanças detectadas:
    - GigabitEthernet0/1: down >>> up
    alcancil@linux:~/automacoes/arquivos/csv/04$
```

**Explicação**  

- Criação de um dicionário que irá receber os dados das interfaces contidas nos arquivos csv

```Bash
    Linha [03] : criando a função ler_csv() que recebe o parâmetro caminho  
    Linha [04] : cria um dicionário vazio chamado dados para armazenar os pares interface: estado  
    Linha [05] : com o arquivo caminho adicione newline=''. Obs: newline é utilizado para se evitar problemas no Windows
    Linha [06] : Usa csv.DictReader para ler o conteúdo do arquivo CSV. Essa função converte automaticamente cada linha do CSV em um dicionário, onde os nomes das colunas viram  chaves (como 'interface' e 'estado').
    Linha [07] : inicia o loop for que percorre cada linha do arquivo
    Linha [08] : extrai da linha o valor da coluna interface, que é usado como chave no dicionário dados  
    Linha [09] : extrai da linha o valor da coluna estado, que será o valor associado à interface no dicionário.
    Linha [10] : adiciona uma nova entrada no dicionário dados, com a interface como chave e o estado como valor.
    Linha [11] : retorna o dicionário completo com todas as interfaces e seus respectivos estados.
```

- Leitura dos arquivos  

```Bash
    Linha [14] : variável antes recebe o valor do arquivo portas_antes.csv em forma de dicionário
    Linha [15] : variável antes recebe o valor do arquivo portas_depois.csv em forma de dicionário
```

- Comparação  

```Bash
    Linha [18] : imprime a mensagem fixa: "Mudanças detectadas:"  
    Linha [19] : verifica o estado das interfaces antes das mudanças uma, a uma
    Linha [20] : verifica se o valor da interface no dicionário antes é diferente do valor correspondente no dicionário depois.
                OBS: O método .get(interface) é usado para evitar erro se a interface não existir no depois. Retorna None se não encontrar.
                OBS2: Ou seja, compara o estado da interface antes e depois.
    Linha [21]: Se houver diferença, imprime a interface e o valor de antes e depois, no formato:  
                - GigabitEthernet0/1: down >>> up
```