# Python - Básico 10

## 03 Manipulação de arquivos - .json

Arquivos **.json** são amplamente utilizados em automação de redes para:

1. **Inventário de dispositivos**: armazenar atributos complexos como VLANs, interfaces e políticas de QoS.  
2. **Backup de configurações**: salvar configurações com metadados (timestamp, usuário que fez o backup).  
3. **Processamento de logs estruturados**: registrar eventos com múltiplos níveis de detalhe (ex.: interface, severidade, timestamp).  
4. **Comparação de configurações**: identificar diferenças entre versões de configs (antes/depois de mudanças).  
5. **Integração com APIs**: 99% das APIs modernas (Cisco DNA Center, Meraki, ACI) usam JSON.  
6. **Troca de dados entre sistemas**: comunicação entre Ansible/Nornir e dispositivos de rede.  

### Quando Usar JSON vs Outros Formatos

| **Escolha JSON quando...**                  |   **Evite JSON quando...**                 |
|---------------------------------------------|--------------------------------------------|
| Dados têm estrutura hierárquica/aninhada    | Dados são tabulares simples (ex.: CSV)     |
| Necessidade de interoperabilidade com APIs  | Arquivos muito grandes (>100MB)            |
| Legibilidade humana é importante            | Configurações ultra-simples (ex.: .env)    |
| Metadados complexos (ex.: timestamp, tags)  | Performance crítica (use binário/protobuf) |

### **Por que JSON é essencial para o CCNP?**
- **Estrutura hierárquica:** Ideal para configurações de rede (ex.: VLANs, ACLs).
- **Interoperabilidade:** Suporte nativo em Python, JavaScript, APIs Cisco/Meraki/etc.
- **Legibilidade:** Facilita debugging e colaboração em equipe.
- **Compatibilidade:** Suportado nativamente por Python e ferramentas Cisco.

**XML** (Extensible Markup Language):  
- Primeiro formato amplamente adotado para APIs.  
- Problema: Verbosidade excessiva e difícil leitura humana.  

   ```xml
   <device>
       <hostname>R1</hostname>
       <ip>10.0.0.1</ip>
   </device>
   ```

**JSON (JavaScript Object Notation):**

Desenvolvido como parte do JavaScript, mas tornou-se independente.

**Vantagens:**
- Estrutura leve e fácil de ler/escrever.  
- Mapeamento direto para estruturas de dados em linguagens modernas.  
    
```json
    {
        "device": {
            "hostname": "switch01",
            "vlans": [
                {"id": 10, "name": "VLAN_GESTAO"},
                {"id": 20, "name": "VLAN_VOIP"}
            ]
        }
    }
```

Certo, mas vamos analisar de perto a estrutura do arquivos json. Ele  não lembra algo que já vimos ?  
Sim. Se pararmos para verificar bem de perto, podemos notar que ele é praticamente um dicionário aninhado de python. Ele também aceita uma lista dentro dentro dele.  

**Exemplo .json**  

```json
    {
        "hostname": "R1",
        "ip": "10.0.0.1",
        "interfaces": ["Gig0/1", "Gig0/2"], # [ ] é uma lista
        "ativo": true # Note o 'T' minusculo em json
    }
```

- **Chaves ({}):** Delimitam objetos (equivalente a dicionários em Python).  
- **Colchetes ([]):** Delimitam arrays (listas).  
- **Tipos de dados suportados:** Strings (" "), números, booleanos (true/false), null, objetos e arrays.  

**Exemplo dicionário python**

```Python
    # Equivalente em Python:
    dispositivo = {
        "hostname": "R1",
        "ip": "10.0.0.1",
        "interfaces": ["Gig0/1", "Gig0/2"], # [ ] é uma lista
        "ativo": True  # Note o 'T' maiúsculo em Python
    }
```

- **Diferença:** JSON é um formato de texto padronizado, enquanto dicionários são estruturas de dados nativas do Python.  

Como podemos notar, os dois arquivos tem a estrutura de **chave: valor** . Isso em python é um dicionário.  


### Exemplo 01: Inventário de dispositivos (armazenar atributos complexos como VLANs, interfaces e políticas de QoS.)

Certo, primeiro vamos criar um arquivo chamado **inventario.json** com o conteúdo:  

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
    [03] # Lê o arquivo JSON
    [04] with open('inventario.json', 'r') as arquivo:
    [05]    inventario = json.load(arquivo)
    [06]
    [07] # Processa os dispositivos
    [08] print("=== INVENTÁRIO DE REDE ===")
    [09] for dispositivo in inventario['dispositivos']:
    [10]    print(f"\nDispositivo: {dispositivo['hostname']}")
    [11]    print(f"IP: {dispositivo['ip']}")
    [12]    print(f"Modelo: {dispositivo['modelo']}")
    [13]    print(f"IOS: {dispositivo['ios']}")
    [14]    print(f"Interfaces: {', '.join(dispositivo['interfaces'])}")
    [15]    print(f"VLANs: {dispositivo['vlans']}")
```

**Saída**

```Bash
    alcancil@linux:~/automacoes/arquivos/json/01$ ls -la
    total 16
    drwxrwxr-x 2 alcancil alcancil 4096 mai  7 16:53 .
    drwxrwxr-x 3 alcancil alcancil 4096 mai  7 16:48 ..
    -rw-r--r-- 1 root     root      503 mai  7 16:50 inventario.json
    -rw-r--r-- 1 root     root      516 mai  7 16:53 ler_inventario.py
    alcancil@linux:~/automacoes/arquivos/json/01$ python3 ler_inventario.py 
    === INVENTÁRIO DE REDE ===

    Dispositivo: SW1
    IP: 192.168.1.1
    Modelo: Cisco Catalyst 2960
    IOS: 16.12.4
    Interfaces: Gig0/1, Gig0/2
    VLANs: [10, 20, 30]

    Dispositivo: R1
    IP: 10.0.0.1
    Modelo: Cisco ISR 4331
    IOS: 17.03.02
    Interfaces: Gig0/0, Gig0/1
    VLANs: [10, 40]
    alcancil@linux:~/automacoes/arquivos/json/01$
```

**Explicação**  

```Bash
    Linha[01] : Importa o módulo json do Python, que contém todas as funções necessárias para trabalhar com arquivos JSON. 
    Linha[04] : Abre o arquivo inventario.json em modo leitura ('r').
                with: Garante que o arquivo será fechado automaticamente após o uso (gerenciamento de recursos).
                O conteúdo do arquivo é associado à variável arquivo. 
    Linha[05] : Faz o parsing do conteúdo do arquivo JSON.
                json.load(): Converte o texto JSON em uma estrutura de dados Python (normalmente dicionários e listas).
                O resultado é armazenado na variável inventario.  
    Linha[08] : Imprime um cabeçalho para organizar a saída no terminal.  
    Linha[09] : Inicia um loop que itera sobre cada item da lista dispositivos contida no dicionário inventario.
                inventario['dispositivos']: Acessa a lista de dispositivos armazenada no JSON.  
    Linha[10] : Imprime o hostname do dispositivo atual.
                \n: Insere uma linha vazia antes de cada dispositivo para melhorar a legibilidade.
                dispositivo['hostname']: Acessa o valor da chave hostname no dicionário do dispositivo atual. 
    Linha[11] : Imprime o endereço IP do dispositivo.   
    Linha[12] : Imprime o modelo do equipamento (ex: Cisco Catalyst 2960).   
    Linha[13] : Imprime a versão do IOS/XE do dispositivo.   
    Linha[14] : Converte a lista de interfaces em uma string formatada.
                ', '.join(): Une os elementos da lista com vírgula e espaço (ex: "Gig0/1, Gig0/2").
                dispositivo['interfaces']: Acessa a lista de interfaces do dispositivo.
    Linha[15] : Imprime a lista de VLANs do dispositivo.   
```  

**OBS:** aqui eu citei o conceito de **Parsing**. Mas por hora vou falar que **Parsing** é o processo de ler uma string JSON e convertê-la em uma estrutura de dados nativa da linguagem (no Python, um dicionário ou lista). Falaremos mais sobre o tema em um novo tópico.  

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