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

### Exemplo 02: Backup de Configurações com Metadados

**Objetivo:** Realizar backup de configurações de dispositivos de rede em formato JSON, incluindo metadados como data/hora, usuário que executou o backup e informações do dispositivo. O script gera um arquivo organizado e legível que pode ser usado para auditoria, restore ou versionamento de configurações.  


**Script backup_config.py**

```Python
[01] import json
[02] from datetime import datetime
[03] import getpass
[04] import sys
[05]
[06] def main():
[07]     try:
[08]         # 1. Dados do dispositivo e configuração
[09]         configuracao = """
[10]         hostname R1
[11]         interface GigabitEthernet0/1
[12]         ip address 192.168.1.1 255.255.255.0
[13]         !
[14]         vlan 10
[15]         name VLAN_GESTAO
[16]         """
[17] 
[18]         # 2. Metadados do backup
[19]         backup_data = {
[20]             "dispositivo": {
[21]                 "hostname": "R1",
[22]                 "ip": "192.168.1.1",
[23]                 "tipo": "Cisco IOS"
[24]             },
[25]             "backup": {
[26]                 "config": configuracao.strip().split('\n'),  # Convertendo para lista
[27]                 "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
[28]                 "usuario": getpass.getuser(),  # Pega o usuário atual do Linux
[29]                 "versao_script": "1.0"
[30]             }
[31]         }
[32] 
[33]         # 3. Salvar em arquivo JSON
[34]         nome_arquivo = f"backup_{backup_data['dispositivo']['hostname']}_{datetime.now().strftime('%Y%m%d')}.json"
[35]         
[36]         try:
[37]             with open(nome_arquivo, 'w') as f:
[38]                 json.dump(backup_data, f, indent=4)  # indent=4 para formatação legível
[39]         except IOError as e:
[40]             print(f"Erro ao escrever no arquivo: {e}", file=sys.stderr)
[41]             raise
[42]         except json.JSONEncodeError as e:
[43]             print(f"Erro ao serializar dados para JSON: {e}", file=sys.stderr)
[44]             raise
[46]         else:
[47]             print(f"Backup salvo com sucesso em: {nome_arquivo}")
[48]             
[49]     except Exception as e:
[50]         print(f"Erro inesperado durante o backup: {e}", file=sys.stderr)
[51]         sys.exit(1)
[52]     finally:
[53]         print("Operação de backup concluída.")
[54] 
[55] if __name__ == "__main__":
[56]     main()
```

**Saída**  

```Bash
alcancil@linux:~/automacoes/erros/json/02$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/json/02$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/json/02$ python3 backup_config.py 
Backup salvo com sucesso em: backup_R1_20250615.json
Operação de backup concluída.
(venv) alcancil@linux:~/automacoes/erros/json/02$ cat backup_R1_20250615.json 
{
    "dispositivo": {
        "hostname": "R1",
        "ip": "192.168.1.1",
        "tipo": "Cisco IOS"
    },
    "backup": {
        "config": [
            "hostname R1",
            "        interface GigabitEthernet0/1",
            "        ip address 192.168.1.1 255.255.255.0",
            "        !",
            "        vlan 10",
            "        name VLAN_GESTAO"
        ],
        "timestamp": "2025-06-15 21:21:29",
        "usuario": "alcancil",
        "versao_script": "1.0"
    }
}(venv) alcancil@linux:~/automacoes/erros/json/02$ 

```

**Explicação**  

```Python
Bloco 1: Importação de bibliotecas
python

[01] import json                                                                     # Biblioteca para manipulação de arquivos JSON
[02] from datetime import datetime                                                   # Para obter data/hora atual
[03] import getpass                                                                  # Para obter o nome do usuário do sistema
[04] import sys                                                                      # Para manipulação de sistema (saída de erros)

Bloco 2: Definição da função principal

[06] def main():                                                                     # Define a função principal do script
[07]     try:                                                                        # Início do bloco try para tratamento de erros global

Bloco 3: Dados de configuração do dispositivo

[08]                                                                                 # 1. Dados do dispositivo e configuração
[09]         configuracao = """                                                      # Início da string multilinha com a configuração
[10]         hostname R1                                                             # Configuração do hostname do dispositivo
[11]         interface GigabitEthernet0/1                                            # Configuração de interface
[12]         ip address 192.168.1.1 255.255.255.0                                    # Configuração de IP
[13]         !                                                                       # Delimitador comum em configurações Cisco
[14]         vlan 10                                                                 # Configuração de VLAN
[15]         name VLAN_GESTAO                                                        # Nome da VLAN
[16]         """                                                                     # Fim da string de configuração

Bloco 4: Construção dos metadados

[18]                                                                                 # 2. Metadados do backup
[19]         backup_data = {                                                         # Dicionário principal para armazenar todos os dados
[20]             "dispositivo": {                                                    # Metadados sobre o dispositivo
[21]                 "hostname": "R1",                                               # Nome do dispositivo
[22]                 "ip": "192.168.1.1",                                            # Endereço IP
[23]                 "tipo": "Cisco IOS"                                             # Tipo de dispositivo
[24]             },
[25]             "backup": {                                                         # Metadados sobre o backup
[26]                 "config": configuracao.strip().split('\n'),                     # Config convertida para lista
[27]                 "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),      # Data/hora
[28]                 "usuario": getpass.getuser(),                                   # Usuário que executou o backup
[29]                 "versao_script": "1.0"                                          # Versão do script
[30]             }
[31]         }

Bloco 5: Operação de salvamento do arquivo

[33]                                                                                 # 3. Salvar em arquivo JSON
[34]         nome_arquivo = f"backup_{backup_data['dispositivo']['hostname']}_{datetime.now().strftime('%Y%m%d')}.json"  # Gera nome do arquivo
[35]         
[36]         try:                                                                    # Bloco try para operações de arquivo/JSON
[37]             with open(nome_arquivo, 'w') as f:                                  # Abre arquivo para escrita
[38]                 json.dump(backup_data, f, indent=4)                             # Escreve dados formatados

Bloco 6: Tratamento de erros específicos
python

[39]         except IOError as e:                                                    # Erros de entrada/saída (arquivo)
[40]             print(f"Erro ao escrever no arquivo: {e}", file=sys.stderr)         # Mensagem de erro
[41]             raise                                                               # Re-lança a exceção para tratamento externo
[42]         except json.JSONEncodeError as e:                                       # Erros de serialização JSON
[43]             print(f"Erro ao serializar dados para JSON: {e}", file=sys.stderr)  # Mensagem formatada (f-string) que inclui:
                                                                                            # - Texto fixo de erro
                                                                                            # - Variável {e} que contém a exceção capturada
                                                                                            # file=sys.stderr - Redireciona a saída para o fluxo de erro padrão (stderr)
                                                                                            # em vez da saída padrão (stdout), seguindo boas práticas para:
                                                                                            # 1. Separar mensagens de erro de saídas normais
                                                                                            # 2. Permitir redirecionamento adequado em pipelines
                                                                                            # 3. Facilitar filtragem de logs
[44]             raise                                                               # Re-lança a exceção

Bloco 7: Fluxo alternativo e finalização
python

[46]         else:                                                                   # Executa se não ocorrerem erros
[47]             print(f"Backup salvo com sucesso em: {nome_arquivo}")               # Mensagem de sucesso
[48]             
[49]     except Exception as e:                                                      # Captura qualquer exceção não tratada
[50]         print(f"Erro inesperado durante o backup: {e}", file=sys.stderr)        # Mensagem de erro no estilo da anterior
[51]         sys.exit(1)                                                             # Termina o programa com código de erro
[52]     finally:                                                                    # Sempre executa, com ou sem erros
[53]         print("Operação de backup concluída.")                                  # Mensagem final

Bloco 8: Execução do script
python

[55] if __name__ == "__main__":                                                      # Verifica se o script está sendo executado diretamente
[56]     main()                                                                      # Chama a função principal
```

### Exemplo 03: Processamento de logs estruturados

**Objetivo:**  
  - Ler e processar logs de dispositivos de rede em formato JSON
  - Filtrar eventos relevantes (ALERTA e CRITICO)
  - Exibir detalhes técnicos para troubleshooting
  - Gerar estatísticas de eventos
  - Tratar possíveis erros durante a execução

**logs_switch.json**   

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
import json
from datetime import datetime
import sys

def main():
    try:
        # 1. Carregar logs com tratamento de erros de arquivo/JSON
        try:
            with open('logs_switch.json', 'r') as f:
                dados = json.load(f)
        except FileNotFoundError:
            print("[ERRO] Arquivo 'logs_switch.json' não encontrado", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"[ERRO] Arquivo JSON inválido: {e}", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print("[ERRO] Sem permissão para ler o arquivo", file=sys.stderr)
            sys.exit(1)

        # 2. Validar estrutura básica do JSON
        try:
            required_keys = ['dispositivo', 'tipo', 'logs']
            if not all(key in dados for key in required_keys):
                raise ValueError("Estrutura do JSON inválida - chaves obrigatórias ausentes")
                
            if not isinstance(dados['logs'], list):
                raise ValueError("Campo 'logs' deve ser uma lista")
        except ValueError as e:
            print(f"[ERRO] {e}", file=sys.stderr)
            sys.exit(1)

        # 3. Processar logs com tratamento de erros de estrutura
        try:
            print(f"\n=== LOGS DO DISPOSITIVO {dados['dispositivo']} ({dados['tipo']}) ===")
            
            for log in dados['logs']:
                if log.get('severidade') in ['ALERTA', 'CRITICO']:
                    print(f"\n[!] Evento: {log.get('evento', 'DESCONHECIDO').upper()}")
                    print(f"    - Hora: {log.get('timestamp', 'N/A')}")
                    print(f"    - Severidade: {log.get('severidade', 'N/A')}")
                    
                    # Detalhes dinâmicos com tratamento seguro
                    detalhes = log.get('detalhes', {})
                    for chave, valor in detalhes.items():
                        print(f"    - {chave.replace('_', ' ').title()}: {valor}")

        except AttributeError as e:
            print(f"[ERRO] Estrutura de log inválida: {e}", file=sys.stderr)
            sys.exit(1)

        # 4. Gerar estatísticas (com tratamento de possíveis erros)
        try:
            total_eventos = len(dados['logs'])
            criticos = sum(1 for log in dados['logs'] 
                        if isinstance(log, dict) and 
                        log.get('severidade') == 'CRITICO')
            
            print(f"\n=== RESUMO ===")
            print(f"Total de eventos: {total_eventos}")
            print(f"Eventos críticos: {criticos}")

        except Exception as e:
            print(f"[ERRO] Ao gerar estatísticas: {e}", file=sys.stderr)

    except KeyboardInterrupt:
        print("\n[INFO] Processamento interrompido pelo usuário", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"[ERRO CRÍTICO] {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        print("\nProcessamento concluído.")

if __name__ == "__main__":
    main()
```

**Saída**

```Bash
alcancil@linux:~/automacoes/erros/json/03$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/json/03$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/json/03$ ls
logs_switch.json  processar_log.json  venv
(venv) alcancil@linux:~/automacoes/erros/json/03$ mv processar_log.json processar_log.py
(venv) alcancil@linux:~/automacoes/erros/json/03$ python3 processar_log.py 

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

Processamento concluído.
(venv) alcancil@linux:~/automacoes/erros/json/03$
```

---
ARRUMAR

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