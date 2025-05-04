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
