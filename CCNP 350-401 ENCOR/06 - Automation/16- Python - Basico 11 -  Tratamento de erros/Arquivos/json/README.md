# Python - Básico 11

## Índice
- [Python - Básico 11](#python---básico-11)
  - [Índice](#índice)
  - [04 Tratamento de Erros com Arquivos JSON](#04-tratamento-de-erros-com-arquivos-json)
    - [Exemplo 01: Inventário de dispositivos (armazenar atributos complexos como VLANs, interfaces e políticas de QoS.)](#exemplo-01-inventário-de-dispositivos-armazenar-atributos-complexos-como-vlans-interfaces-e-políticas-de-qos)
    - [Exemplo 02: Backup de Configurações com Metadados](#exemplo-02-backup-de-configurações-com-metadados)
  - [Exemplo 03: Processamento de logs estruturados](#exemplo-03-processamento-de-logs-estruturados)
    - [Exemplo 04 : Comparação de configurações](#exemplo-04--comparação-de-configurações)
  - [Resumo do Aprendizado](#resumo-do-aprendizado)

## 04 Tratamento de Erros com Arquivos JSON

Em automação de redes, erros em arquivos JSON podem causar falhas em scripts críticos (backups, provisionamento, etc.). Veja como lidar com eles:

**Principais Erros e Soluções**

| Cenário de Erro            | Causa                               | Prevenção	                        | Tratamento                               |
|----------------------------|-------------------------------------|------------------------------------|------------------------------------------|
| Arquivo não encontrado     | Caminho incorreto ou permissões     | Verificar existência com os.path   | Criar arquivo padrão ou abortar          |
| JSON malformado            | Chaves sem aspas, vírgulas faltando | Validar com ferramentas online	    | Usar try-except com json.JSONDecodeError |
| Tipo de dado incorreto     | Número onde era string, etc.        | Esquema de validação (JSON Schema) | Converter tipos ou rejeitar entrada      |
| Chave ausente              | Campo obrigatório não presente      | Verificar chaves antes de acessar  | Usar .get() ou valores padrão            | 
| Acesso a arquivo bloqueado | Arquivo em uso por outro processo   | Implementar retry com timeout      | Esperar ou notificar usuário             |

### Exemplo 01: Inventário de dispositivos (armazenar atributos complexos como VLANs, interfaces e políticas de QoS.)

**Objetivo:** Extrair e mostrar dados de dispositivos de rede de um JSON, com tratamento seguro de erros. 

**inventario.json**    

```json
{
    "dispositivos": [
        {
             "hostname": "SW1",
             "ip": "192.168.1.1",
             "modelo": "Cisco Catalyst 2960",
             "ios": "16.12.4",
             "interfaces": ["Gig0/1", "Gig0/2"],
             "vlans": [10, 20, 30]
         },
         {
             "hostname": "R1",  
             "ip": "10.0.0.1",
             "modelo": "Cisco ISR 4331",
             "ios": "17.03.02",
             "interfaces": ["Gig0/0", "Gig0/1"],
             "vlans": [10, 40]
        }
     ]
}
```

Esse é um arquivo bem semelhante a um arquivo de respostas obtido de um equipamento Cisco.  

**Script ler_invetario.py**  

```Python
[01] import json
[02]
[03] try:
[04]     with open('inventario.json', 'r') as arquivo:
[05]         inventario = json.load(arquivo)
[07]    
[08]     print("=== INVENTÁRIO DE REDE ===")
[09]     for dispositivo in inventario['dispositivos']:
[10]         print(f"\nHostname: {dispositivo['hostname']}")
[11]         print(f"IP: {dispositivo['ip']}")
[12]         print(f"Modelo: {dispositivo['modelo']}")
[13]         print(f"IOS: {dispositivo['ios']}")
[14]         print(f"Interfaces: {', '.join(dispositivo['interfaces'])}")
[15]         print(f"VLANs: {dispositivo['vlans']}")
[16]
[17] except FileNotFoundError:
[18]     print("Erro: Arquivo 'inventario.json' não encontrado!")
[19] except json.JSONDecodeError:
[20]     print("Erro: JSON inválido!")
[21] except KeyError as e:
[22]     print(f"Erro: Campo faltando - {str(e)}")
[23] except Exception:
[24]     print("Erro desconhecido!")
```

**Explicação dos erros tratados**

  - FileNotFoundError: Se o arquivo não existir.

  - JSONDecodeError: Se o JSON estiver malformatado (vírgulas faltando, aspas erradas).

  - KeyError: Se uma chave obrigatória (como 'dispositivos' ou 'hostname') estiver faltando.

  - Exception: Erro genérico (último recurso).

**Saída**

```Bash
alcancil@linux:~/automacoes/erros/json/01$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/json/01$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/json/01$ python3 ler_inventario.py 
=== INVENTÁRIO DE REDE ===

Hostname: SW1
IP: 192.168.1.1
Modelo: Cisco Catalyst 2960
IOS: 16.12.4
Interfaces: Gig0/1, Gig0/2
VLANs: [10, 20, 30]

Hostname: R1
IP: 10.0.0.1
Modelo: Cisco ISR 4331
IOS: 17.03.02
Interfaces: Gig0/0, Gig0/1
VLANs: [10, 40]
(venv) alcancil@linux:~/automacoes/erros/json/01$ 
```

**Explicação**  

```Python
# Bloco 1: Importação de bibliotecas
[01] import json                                                           # Importa o módulo json para trabalhar com arquivos JSON

# Bloco 2: Tentativa de leitura e processamento do arquivo
[03] try:                                                                  # Inicia o bloco de tratamento de erros
[04]     with open('inventario.json', 'r') as arquivo:                     # Abre o arquivo no modo leitura
[05]         inventario = json.load(arquivo)                               # Carrega e converte o JSON para dicionário Python

# Bloco 3: Exibição do inventário
[08]     print("=== INVENTÁRIO DE REDE ===")                               # Cabeçalho
[09]     for dispositivo in inventario['dispositivos']:                    # Loop pelos dispositivos
[10]         print(f"\nHostname: {dispositivo['hostname']}")               # Nome do dispositivo
[11]         print(f"IP: {dispositivo['ip']}")                             # Endereço IP
[12]         print(f"Modelo: {dispositivo['modelo']}")                     # Modelo do equipamento
[13]         print(f"IOS: {dispositivo['ios']}")                           # Versão do sistema operacional
[14]         print(f"Interfaces: {', '.join(dispositivo['interfaces'])}")  # Lista de interfaces
[15]         print(f"VLANs: {dispositivo['vlans']}")                       # VLANs configuradas

# Bloco 4: Tratamento de erros específicos
[17] except FileNotFoundError:                                             # Se arquivo não existir
[18]     print("Erro: Arquivo 'inventario.json' não encontrado!")          # Mensagem informando o erro
[19] except json.JSONDecodeError:                                          # Se JSON estiver mal formatado
[20]     print("Erro: JSON inválido!")                                     # Mensagem informando o erro
[21] except KeyError as e:                                                 # Se faltar chave obrigatória
[22]     print(f"Erro: Campo faltando - {str(e)}")                         # Mensagem informando o erro - Informa o campo que falta no arquivo .json
[23] except Exception:                                                     # Para qualquer outro erro não previsto
[24]     print("Erro desconhecido!")                                       # Mensagem informando o erro 
```  

---
ARRUMAR

### Exemplo 02: Backup de Configurações com Metadados

**Script backup_config.py**

```Python
    [01] import json
    [02] from datetime import datetime
    [03] import getpass
    [04]
    [05] # 1. Dados do dispositivo e configuração
    [06] configuracao = """
    [07] hostname R1
    [08] interface GigabitEthernet0/1
    [09] ip address 192.168.1.1 255.255.255.0
    [10] !
    [11] vlan 10
    [12] name VLAN_GESTAO
    [13] """
    [14]
    [15] # 2. Metadados do backup
    [16] backup_data = {
    [17]    "dispositivo": {
    [18]        "hostname": "R1",
    [19]        "ip": "192.168.1.1",
    [20]        "tipo": "Cisco IOS"
    [21]    },
    [22]    "backup": {
    [23]        "config": configuracao.strip().split('\n'),  # Convertendo para lista
    [24]        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    [25]        "usuario": getpass.getuser(),  # Pega o usuário atual do Linux
    [26]        "versao_script": "1.0"
    [27]    }
    [28] }
    [29]
    [30] # 3. Salvar em arquivo JSON
    [31] nome_arquivo = f"backup_{backup_data['dispositivo']['hostname']}_{datetime.now().strftime('%Y%m%d')}.json"
    [32] with open(nome_arquivo, 'w') as f:
    [33]    json.dump(backup_data, f, indent=4)  # indent=4 para formatação legível
    [34]
    [35] print(f"Backup salvo em: {nome_arquivo}")
```

**Saída**  

```Bash
    alcancil@linux:~/automacoes/arquivos/json/02$ python3 baclup_config.py 
    Backup salvo em: backup_R1_20250507.json
    alcancil@linux:~/automacoes/arquivos/json/02$ cat backup_R1_20250507.json 
    {
        "dispositivo": {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "tipo": "Cisco IOS"
        },
        "backup": {
            "config": [
               "hostname R1",
                "interface GigabitEthernet0/1",
                " ip address 192.168.1.1 255.255.255.0",
                "!",
                "vlan 10",
                " name VLAN_GESTAO"
            ],
            "timestamp": "2025-05-07 18:12:42",
            "usuario": "alcancil",
            "versao_script": "1.0"
        }
    }alcancil@linux:~/automacoes/arquivos/json/02$
```

**Explicação**  

**Linhas 1-3:** Importação de Bibliotecas

```Bash
    Linha[01] : import json                     # Manipulação de arquivos JSON
    Linha[02] : from datetime import datetime   # Operações com data/hora (para timestamp)
    Linha[03] : import getpass                  # Captura o usuário do sistema
```  

**Linhas 6-13:** Configuração do Dispositivo  

```Bash
    Linha[06] : configuracao = """                    # String multilinha
    Linha[07] : hostname R1                           # Configuração Cisco típica
    Linha[08] : interface GigabitEthernet0/1          # Exemplo de interface
    Linha[09] : ip address 192.168.1.1 255.255.255.0  # Configuração de IP
    Linha[10] : !                                     # Delimitador Cisco
    Linha[11] : vlan 10                               # Configuração de VLAN
    Linha[12] : name VLAN_GESTAO                      # Nomeando VLAN
    Linha[13] : """                                   # Fecha String multilinha
```

- Simula a saída de um comando show running-config.  

**Linhas 16-28:** Estrutura de Metadados  

```Bash
    Linha[16] : backup_data = {                                                   # Dicionário principal
    Linha[17] :   "dispositivo": {                                                # Seção de identificação
    Linha[18] :        "hostname": "R1",                                          # Hostname do dispositivo
    Linha[19] :        "ip": "192.168.1.1",                                       # IP de gerenciamento
    Linha[20] :        "tipo": "Cisco IOS"                                        # Plataforma do dispositivo
    Linha[21] :   },                                                              # Fim do dicionário dispositivo 
    Linha[22] :   "backup": {                                                     # Seção de metadados
    Linha[23] :       "config": configuracao.strip().split('\n'),                 # Divide a configuração em linhas
    Linha[24] :       "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Data/hora formatada
    Linha[25] :       "usuario": getpass.getuser(),                               # Usuário que executou o backup
    Linha[26] :       "versao_script": "1.0"                                      # Controle de versão
    Linha[27] :   }                                                               # Fim do dicionário backup
    Linha[28] : }                                                                 # Fim do dicionário principal
```
**Pontos chave:**

        strip().split('\n') (Linha 23): Converte a configuração em lista removendo espaços extras
        datetime.now() (Linha 24):      Boa prática para registro de mudanças (exigido em ambientes enterprise)
        getpass.getuser() (Linha 25):   Auditoria de quem executou o backup  

**Linhas 31-35:** Persistência do Backup  

```Bash
    Linha[31] : nome_arquivo = f"backup_{backup_data['dispositivo']['hostname']}_{datetime.now().strftime('%Y%m%d')}.json"  # f-string Formato do nome: backup_<hostname>_<data>.json
    Linha[32] : with open(nome_arquivo, 'w') as f:                                                                          # Cria/sobrescreve arquivo
    Linha[33] :   json.dump(backup_data, f, indent=4)                                                                       # Escreve com formatação
    Linha[35] : print(f"Backup salvo em: {nome_arquivo}")                                                                   # Feedback para o usuário
```

**Pontos chave:**  

    Nome dinâmico do arquivo (Linha 31): Padrão backup_R1_20240515.json
    indent=4 (Linha 33): Formatação legível para humanos (útil para debugging)
    Gerenciamento seguro de arquivos com with (Linha 32)

## Exemplo 03: Processamento de logs estruturados

Crie o arquivo **logs_switch.json** com o conteúdo:  

```json
{
    "dispositivo": "SW1",
    "tipo": "Cisco Catalyst 2960",
    "logs": [
        {
            "timestamp": "2024-05-15 09:15:23",
            "severidade": "ALERTA",
            "evento": "interface_down",
            "detalhes": {
                "interface": "GigabitEthernet0/1",
                "acao": "Enviar ticket para equipe NOC"
            }
        },
        {
            "timestamp": "2024-05-15 09:20:12",
            "severidade": "INFO",
            "evento": "interface_up",
            "detalhes": {
                "interface": "GigabitEthernet0/1",
                "acao": "Registrar no sistema"
            }
        },
        {
            "timestamp": "2024-05-15 10:05:34",
            "severidade": "CRITICO",
            "evento": "cpu_overload",
            "detalhes": {
                "utilizacao": "95%",
                "limite": "80%"
            }
        }
    ]
}
```

**Script processar_logs.py**

```Python
    [01] import json
    [02] from datetime import datetime
    [03]
    [04] # 1. Carregar logs
    [05] with open('logs_switch.json', 'r') as f:
    [06]    dados = json.load(f)
    [07]
    [08] # 2. Filtrar eventos críticos
    [09] print(f"\n=== LOGS DO DISPOSITIVO {dados['dispositivo']} ({dados['tipo']}) ===")
    [10] for log in dados['logs']:
    [11]    if log['severidade'] in ['ALERTA', 'CRITICO']:  # Filtro CCNP-relevante
    [12]        print(f"\n[!] Evento: {log['evento'].upper()}")
    [13]        print(f"    - Hora: {log['timestamp']}")
    [14]        print(f"    - Severidade: {log['severidade']}")
    [15]        
    [16]        # 3. Detalhes específicos (dinâmico para qualquer evento)
    [17]        for chave, valor in log['detalhes'].items():
    [18]            print(f"    - {chave.replace('_', ' ').title()}: {valor}")
    [19]
    [20] # 4. Estatísticas (útil para troubleshooting)
    [21] total_eventos = len(dados['logs'])
    [22] criticos = sum(1 for log in dados['logs'] if log['severidade'] == 'CRITICO')
    [23] print(f"\n=== RESUMO ===")
    [24] print(f"Total de eventos: {total_eventos}")
    [25] print(f"Eventos críticos: {criticos}")
```

**Saída**

```Bash
alcancil@linux:~/automacoes/arquivos/json/03$ ls -la
total 12
drwxrwxr-x 2 alcancil alcancil 4096 mai  8 11:11 .
drwxrwxr-x 5 alcancil alcancil 4096 mai  8 11:10 ..
-rw-r--r-- 1 root     root      908 mai  8 11:11 logs_switch.json
alcancil@linux:~/automacoes/arquivos/json/03$ sudo nano processar_logs.py
alcancil@linux:~/automacoes/arquivos/json/03$ python3 processar_logs.py 

=== LOGS DO DISPOSITIVO SW1 (Cisco Catalyst 2960) ===

[!] Evento: INTERFACE_DOWN
    - Hora: 2024-05-15 09:15:23
    - Severidade: ALERTA
    - Interface: GigabitEthernet0/1
    - Acao: Enviar ticket para equipe NOC

[!] Evento: CPU_OVERLOAD
    - Hora: 2024-05-15 10:05:34
    - Severidade: CRITICO
    - Utilizacao: 95%
    - Limite: 80%

=== RESUMO ===
Total de eventos: 3
Eventos críticos: 1
alcancil@linux:~/automacoes/arquivos/json/03$ 
```

**Explicação**

**Linhas 1-2:** Importação de Bibliotecas

```Python
    [01] import json                      # Manipulação de arquivos JSON
    [02] from datetime import datetime    # Para cálculo de duração de eventos (não usado aqui, mas preparado para expansão)
```
   
**Linhas 5-6:** Carregamento do Arquivo JSON

```Python
    [05] with open('logs_switch.json', 'r') as f:  # Abre o arquivo no modo leitura
    [06]    dados = json.load(f)                   # Faz o parsing do JSON para dicionário Python
```

**Pontos Chave:**
    
    O with garante que o arquivo será fechado automaticamente.

**Linhas 9-14:** Cabeçalho e Filtragem de Eventos

```Python
    [09] print(f"\n=== LOGS DO DISPOSITIVO {dados['dispositivo']} ({dados['tipo']}) ===")   # Cabeçalho personalizado
    [10] for log in dados['logs']:                                                          # Itera sobre cada entrada de log
    [11]    if log['severidade'] in ['ALERTA', 'CRITICO']:                                  # Filtra por severidade (equivalente a "show logging | include CRITICAL")
    [12]        print(f"\n[!] Evento: {log['evento'].upper()}")                             # Formata o nome do evento
    [13]        print(f"    - Hora: {log['timestamp']}")                                    # Exibe timestamp 
    [14]        print(f"    - Severidade: {log['severidade']}")                             # Nível de severidade
```

**Pontos Chave:**

        Filtro por severidade simula comandos Cisco como show logging | include ALERTA

        Timestamp no formato ISO 8601 (padrão para ferramentas Cisco)

**Linhas 17-18:** Processamento Dinâmico de Detalhes

```Python
    [17]        for chave, valor in log['detalhes'].items():                    # Itera sobre todos os pares chave-valor
    [18]            print(f"    - {chave.replace('_', ' ').title()}: {valor}")  # Formatação automática (ex: "acao" → "Acao")
```
   
 **Pontos Chave :**

    Técnica avançada:

        Processa qualquer campo de detalhes sem hardcoding - essencial para logs complexos  
                 
        replace('_', ' '): Converte snake_case para texto legível

        title(): Capitaliza a primeira letra (ex: "interface" → "Interface")


    **OBS:** hardcoding: em desenvolvimento de software, "hard code" (ou "codificação rígida") refere-se à prática de inserir dados diretamente no código-fonte do programa, em vez de obtê-los de fontes externas ou gerá-los em tempo de execução. Isso significa que se precisar alterar esses dados, é necessário modificar o código e recompilar o programa

    **OBS2:** Snake case é uma convenção de nomenclatura em programação onde as palavras de um nome (variável, função, etc.) são separadas por um sublinhado ( _ ), e todas as letras são minúsculas. É usado em várias linguagens, principalmente em Python, para melhorar a legibilidade do código. 
        Exemplo:
            snake_case (um nome de variável em snake case)
            funcao_importante (uma função em snake case)
            tabela_de_usuarios (nome de uma tabela em snake case) 

**Linhas 21-25:** Estatísticas (Troubleshooting)

```Python
    [21] total_eventos = len(dados['logs'])                                            # Conta todos os logs
    [22] criticos = sum(1 for log in dados['logs'] if log['severidade'] == 'CRITICO')  # Conta eventos críticos
    [23] print(f"\n=== RESUMO ===")                                                    # Imprime cabeçalho === RESUMO ===
    [24] print(f"Total de eventos: {total_eventos}")                                   # Exemplo: 3
    [25] print(f"Eventos críticos: {criticos}")                                        # Exemplo: 1
```

**Pontos Chave**

        sum() com generator expression: Técnica python para contagem

        Estatísticas similares às geradas por show logging summary em IOS-XE  

### Exemplo 04 : Comparação de configurações  

- Criar Arquivos de Configuração  

Criar o arquivo **config_antes.json** com o conteúdo:  

```json
{
    "hostname": "SW1",
    "interfaces": {
        "GigabitEthernet0/1": {
            "status": "up",
            "vlan": 10,
            "ip": "192.168.1.1/24"
        },
        "GigabitEthernet0/2": {
            "status": "down",
            "vlan": 20,
            "ip": null
        }
    },
    "vlans": [10, 20],
    "last_change": "2024-05-10 09:00:00"
}
```

Criar o arquivo **config_depois.json** com o conteúdo: 

```json
{
    "hostname": "SW1",
    "interfaces": {
        "GigabitEthernet0/1": {
            "status": "up",
            "vlan": 100,
            "ip": "192.168.1.1/24"
        },
        "GigabitEthernet0/2": {
            "status": "up",
            "vlan": 20,
            "ip": "192.168.2.1/24"
        }
    },
    "vlans": [10, 20, 100],
    "last_change": "2024-05-15 14:30:00"
}
```

**Script comparar_configs.py**

```Python
    [01] import json
    [02] from difflib import unified_diff
    [03]
    [04] # 1. Carregar configurações
    [05] with open('config_antes.json') as f:
    [06]    antes = json.load(f)
    [07]
    [08] with open('config_depois.json') as f:
    [09]    depois = json.load(f)
    [10]
    [11] # 2. Comparação textual (simulando 'diff' do Cisco)
    [12] print("=== DIFF ENTRE CONFIGURAÇÕES ===")
    [13] config_antes_str = json.dumps(antes, indent=2).splitlines()
    [14] config_depois_str = json.dumps(depois, indent=2).splitlines()
    [15]
    [16] for line in unified_diff(config_antes_str, config_depois_str, fromfile='ANTES', tofile='DEPOIS', n=2):
    [17]    print(line)
    [18]
    [19] # 3. Comparação estruturada (CCNP-relevante)
    [20] print("\n=== MUDANÇAS DETECTADAS ===")
    [21]
    [22] # 3.1 Comparar VLANs
    [23] vlan_removidas = set(antes['vlans']) - set(depois['vlans'])
    [24] vlan_adicionadas = set(depois['vlans']) - set(antes['vlans'])
    [25]
    [26] if vlan_adicionadas:
    [27]    print(f"[+] VLANs adicionadas: {vlan_adicionadas}")
    [28] if vlan_removidas:
    [29]    print(f"[-] VLANs removidas: {vlan_removidas}")
    [30]
    [31] # 3.2 Comparar interfaces
    [31] for interface in antes['interfaces']:
    [32]    if interface in depois['interfaces']:
    [33]        for chave in antes['interfaces'][interface]:
    [34]            if antes['interfaces'][interface][chave] != depois['interfaces'][interface][chave]:
    [35]                print(f"[!] Interface {interface}: {chave} alterado de '{antes['interfaces'][interface][chave]}' para '{depois['interfaces'][interface][chave]}'")
```

**Saída:**  

```Bash
    alcancil@linux:~/automacoes/arquivos/json/04$ python3 comparar_configs.py 
    === DIFF ENTRE CONFIGURAÇÕES ===
    --- ANTES

    +++ DEPOIS

    @@ -4,17 +4,18 @@

         "GigabitEthernet0/1": {
           "status": "up",
    -      "vlan": 10,
    +      "vlan": 100,
           "ip": "192.168.1.1/24"
         },
         "GigabitEthernet0/2": {
    -      "status": "down",
    +      "status": "up",
           "vlan": 20,
    -      "ip": null
    +      "ip": "192.168.2.1/24"
         }
       },
       "vlans": [
         10,
    -    20
    +    20,
    +    100
       ],
    -  "last_change": "2024-05-10 09:00:00"
    +  "last_change": "2024-05-15 14:30:00"
     }

    === MUDANÇAS DETECTADAS ===
    [+] VLANs adicionadas: {100}
    [!] Interface GigabitEthernet0/1: vlan alterado de '10' para '100'
    [!] Interface GigabitEthernet0/2: status alterado de 'down' para 'up'
    [!] Interface GigabitEthernet0/2: ip alterado de 'None' para '192.168.2.1/24'
    alcancil@linux:~/automacoes/arquivos/json/04$ 
```  

**Explicação**  

Seção 1: Importação de Bibliotecas
```Python
    Linha [01] import json                      # Importa o módulo para trabalhar com JSON
    Linha [02] from difflib import unified_diff # Importa a função para comparação de diferenças
```

Seção 2: Carregamento dos Arquivos de Configuração

```Python
    Linha [04]                                       # 1. Carregar configurações
    Linha [05] with open('config_antes.json') as f:  # Abre o arquivo de configuração "antes"
    Linha [06]    antes = json.load(f)               # Carrega o conteúdo JSON para a variável 'antes'
    Linha [08] with open('config_depois.json') as f: # Abre o arquivo de configuração "depois"
    Linha [09]    depois = json.load(f)              # Carrega o conteúdo JSON para a variável 'depois'
```

Seção 3: Comparação Textual (Diff)

```Python
    Linha [11]                                                                                                        # 2. Comparação textual (simulando 'diff' do Cisco)
    Linha [12] print("=== DIFF ENTRE CONFIGURAÇÕES ===")
    Linha [13] config_antes_str = json.dumps(antes, indent=2).splitlines()                                            # Converte JSON para string formatada e divide em linhas
    Linha [14] config_depois_str = json.dumps(depois, indent=2).splitlines()                                          # Mesmo para a configuração "depois"
    Linha [16] for line in unified_diff(config_antes_str, config_depois_str, fromfile='ANTES', tofile='DEPOIS', n=2):
    Linha [17]    print(line)                                                                                         # Imprime cada linha das diferenças no formato unificado
```

Seção 4: Comparação Estruturada (Análise Específica)

```Python
    Linha [19] # 3. Comparação estruturada (CCNP-relevante)
    Linha [20] print("\n=== MUDANÇAS DETECTADAS ===")
    Linha [22] # 3.1 Comparar VLANs
    Linha [23] vlan_removidas = set(antes['vlans']) - set(depois['vlans'])                                                                      # VLANs que existiam antes mas não depois
    Linha [24] vlan_adicionadas = set(depois['vlans']) - set(antes['vlans'])                                                                    # VLANs que existem depois mas não antes
    Linha [26] if vlan_adicionadas:
    Linha [27]    print(f"[+] VLANs adicionadas: {vlan_adicionadas}")                                                                           # Mostra VLANs adicionadas
    Linha [28] if vlan_removidas:
    Linha [29]    print(f"[-] VLANs removidas: {vlan_removidas}")                                                                               # Mostra VLANs removidas
    Linha [31] # 3.2 Comparar interfaces
    Linha [31] for interface in antes['interfaces']:                                                                                            # Itera sobre cada interface da configuração "antes"
    Linha [32]    if interface in depois['interfaces']:                                                                                         # Verifica se a interface também existe na configuração "depois"
    Linha [33]        for chave in antes['interfaces'][interface]:                                                                              # Itera sobre cada propriedade da interface
    Linha [34]            if antes['interfaces'][interface][chave] != depois['interfaces'][interface][chave]:
    Linha [35]                print(f"[!] Interface {interface}: {chave} alterado de '{antes['interfaces'][interface][chave]}' para '{depois['interfaces'][interface][chave]}'")
```  

## Resumo do Aprendizado 

```Bash
1. JSON é o padrão para automação Cisco

    Substitui XML em APIs modernas (DNA Center, Meraki)

    Estrutura ideal para configurações de rede (VLANs, ACLs, interfaces)

2. Mapeamento direto entre JSON e Python

    Objetos JSON → Dicionários Python

    Arrays JSON → Listas Python

    Facilita manipulação de configurações

3. Casos de uso essenciais:

    Backup de configurações com metadados (timestamp, usuário)  

    Comparação de configs (diff textual e análise estruturada)  

    Processamento de logs com filtros por severidade

4. Técnicas CCNP-relevantes:

    Simular show running-config e diff via Python

    Identificar mudanças em VLANs/interfaces

    Extrair eventos críticos de logs (como show logging | include CRITICAL)
```