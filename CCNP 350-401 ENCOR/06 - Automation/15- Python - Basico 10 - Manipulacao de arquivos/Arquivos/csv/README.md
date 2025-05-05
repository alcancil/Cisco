# Python - Básico 10

## 01 Manipulação de arquivos - .csv

Arquivos **.csv** são utilizados em diversos casos como:  

1. Inventário de dispositivos de rede 
2. Backup de configurações em massa  
3. Processamento de Logs estruturados  
4. Comparação de dados (Antes/Depois)
5. Integração com ferramentas de automação  
6. Exportação de dados de APIs  
  

Quando Escolher CSV em vez de TXT?  

| Vantagens do CSV                                                  | Use TXT quando                                     |
|-------------------------------------------------------------------|----------------------------------------------------|
| Estrutura clara (colunas/linhas).                                 | Os dados são não estruturados (ex.: logs brutos).  |
| Facilidade de importação em Excel, bancos de dados e ferramentas. |  Não há necessidade de divisão por colunas.        |
| Suporte nativo em linguagens (Python, PowerShell).                |                                                    |
       
Antes de começarmos nossos exemplos, vamos criar uma pasta chamada **automacoes** onde vamos deixar nossos arquivos.  
Nas explicações, algumas linhas serão omitidas por questões de clareza e redundância.  

**Exemplo 01:** Inventário de dispositivos de rede  

Nesse exemplo, vamos criar um arquivo chamado **inventario.csv**.  Esse arquivo vai conter as informações de nosso inventário. Percebam como ele vem estruturado: são informações separadas por vírgulas. Olhando somente seu conteúdo fica difícil de entendermos. Então nosso objetivo vai ser criar um arquivo em python que leia o conteúdo desse arquivo e depois nos exiba na tela de forma legível nosso conteúdo. <br></br>

**Conteúdo do arquivo inventario.csv**

```Python
    hostname,ip,modelo,localizacao
    linux-server,192.168.1.100,Ubuntu 22.04,Sala de Servidores
    switch01,192.168.1.1,Cisco Catalyst 2960,Rack Principal
    router01,192.168.1.254,Cisco ISR 4331,Rack Principal
``` 

Explicação:

    hostname: Nome do dispositivo.

    ip: Endereço IP (simulado).

    modelo: Tipo do dispositivo.

    localizacao: Onde o dispositivo está "fisicamente".


**Script ler_inventario.py**

```Python
    [01] import csv
    [02]
    [04] # Lê o arquivo CSV
    [05] with open('inventario.csv', 'r') as arquivo_csv:
    [06]    leitor = csv.DictReader(arquivo_csv)
    [07]    for dispositivo in leitor:
    [08]        print(f"Dispositivo: {dispositivo['hostname']}")
    [09]        print(f"IP: {dispositivo['ip']}")
    [10]        print(f"Modelo: {dispositivo['modelo']}")
    [11]        print(f"Localização: {dispositivo['localizacao']}\n")
```

**Saída**

```Bash
    alcancil@linux:~/automacoes/arquivos/csv/01$ python3 ler_inventario.csv
    Dispositivo: linux-server
    IP: 192.168.1.100
    Modelo: Ubuntu 22.04
    Localização: Sala de Servidores

    Dispositivo: switch01
    IP: 192.168.1.1
    Modelo: Cisco Catalyst 2960
    Localização: Rack Principal

    Dispositivo: router01
    IP: 192.168.1.254
    Modelo: Cisco ISR 4331
    Localização: Rack Principal

    alcancil@linux:~/automacoes/arquivos/csv/01$
```

**Explicação**  

```Bash
    Linha [01] : importando o módulo csv para poder utilizar as funções de arquivos csv  
    Linha [05] : com o arquivo inventario.csv aberto em modo leitura, onde o conteúdo vai para avariável **arquivo_csv** faça:  
    Linha [06] : a variável leitor recebe o conteúdo de arquivo_csv em forma de dicionário. O método csv.DictReader mapeia cada linha para um dicionário ao invés de colocar como índice  
    Linha [07] : para cada dispositivo dentro do conteúdo da variável leitor faça :  
    Linha [08] : imprima **Dispositivo {nome do dispositivo}**  
    Linha [09] : imprima **IP: {número do ip}**  
    Linha [10] : imprima **Modelo: {tipo do modelo}**  
    Linha [11] : imprima **Localização: {localização}**  
```

**Exemplo 02:** Backup de configurações em massa  

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

```Bash
    Linha [01] : importando o módulo csv para poder utilizar as funções de arquivos csv  
    Linha [02] : importando o módulo os para poder utilizar as funções relativa a sistemas operacionais  
    Linha [05] : Função que cria diretórios recursivamente (ou seja, pode criar várias pastas de uma vez, como pasta/subpasta).  
                **exist_ok=True:**  
                    Se True, evita que o Python lance um erro (FileExistsError) se o diretório já existir.  
    Linha [07] : com o arquivo dispositivos.csv aberto em modo leitura (envie o conteúdo para a variável **arquivo_csv**) faça:  
    Linha [08] : a variável **leitor** recebe o conteúdo da variável arquivo.csv em forma de dicionário.  
    Linha [09] : para cada dispositivo dentro da variável leitor faça:  
    Linha [11] : se o tipo do dispositivo for **linux**  
    Linha [12] : cria uma string formatada (um texto) que simula uma "configuração" de um dispositivo Linux, usando os valores lidos do arquivo **("hostname servidor-linux\nIP: endereço ip\nSO: Ubuntu 22.04")**  
    Linha [13] : se o tipo do dispositivo for **cisco**  
    Linha [14] : cria uma string formatada (um texto) que simula uma "configuração" de um dispositivo Cisco, usando os valores lidos do arquivo **("hostname roteador-simulado\ninterface GigabitEthernet0/1\nIP: endereço ip 255.255.255.0")**  
    Linha [17] : Esta linha define o caminho (path) completo onde o arquivo de backup será salvo, usando f-strings para inserir dinamicamente o nome do dispositivo   
    Linha [18] : com a variável caminho_backup aberta em modo leitura (envie o conteúdo para a variável arquivo_backup) faça:   
    Linha [19] : escreve o conteúdo da variável config (que contém as configurações simuladas do dispositivo) no arquivo de backup que foi aberto anteriormente.  
    Linha [21] : Esta linha imprime uma mensagem no terminal para informar que o backup de um dispositivo foi salvo com sucesso, incluindo dinamicamente: **nome do dispositivo** e **caminho completo**  
```

**Exemplo 03:** Processamento de Logs estruturados  

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