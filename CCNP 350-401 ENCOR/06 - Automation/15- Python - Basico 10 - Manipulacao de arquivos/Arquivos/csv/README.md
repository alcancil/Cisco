# Python - Básico 10

## 01 Manipulação de arquivos - .csv

Arquivos **.csv** são utilizados em diversos casos como:  

 
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

```Python
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