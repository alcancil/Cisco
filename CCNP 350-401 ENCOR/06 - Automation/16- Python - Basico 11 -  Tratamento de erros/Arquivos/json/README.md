# Python - Básico 11

## Índice
- [Python - Básico 11](#python---básico-11)
  - [Índice](#índice)
  - [04 Tratamento de Erros com Arquivos JSON](#04-tratamento-de-erros-com-arquivos-json)
    - [Exemplo 01: Inventário de dispositivos (armazenar atributos complexos como VLANs, interfaces e políticas de QoS.)](#exemplo-01-inventário-de-dispositivos-armazenar-atributos-complexos-como-vlans-interfaces-e-políticas-de-qos)
    - [Exemplo 02: Backup de Configurações com Metadados](#exemplo-02-backup-de-configurações-com-metadados)
    - [Exemplo 03: Processamento de logs estruturados](#exemplo-03-processamento-de-logs-estruturados)
    - [Exemplo 04 : Comparação de configurações](#exemplo-04--comparação-de-configurações)
    - [Resumo de Boas Práticas para Tratamento de JSON em Automação de Redes](#resumo-de-boas-práticas-para-tratamento-de-json-em-automação-de-redes)
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
[01] import json
[02] from datetime import datetime
[03] import sys
[04]
[05] def main():
[06]     try:
[07]         # 1. Carregar logs com tratamento de erros de arquivo/JSON
[08]         try:
[09]             with open('logs_switch.json', 'r') as f:
[10]                 dados = json.load(f)
[11]         except FileNotFoundError:
[12]             print("[ERRO] Arquivo 'logs_switch.json' não encontrado", file=sys.stderr)
[13]             sys.exit(1)
[14]         except json.JSONDecodeError as e:
[15]             print(f"[ERRO] Arquivo JSON inválido: {e}", file=sys.stderr)
[16]             sys.exit(1)
[17]         except PermissionError:
[18]             print("[ERRO] Sem permissão para ler o arquivo", file=sys.stderr)
[19]             sys.exit(1)
[20] 
[21]         # 2. Validar estrutura básica do JSON
[22]         try:
[23]             required_keys = ['dispositivo', 'tipo', 'logs']
[24]             if not all(key in dados for key in required_keys):
[25]                 raise ValueError("Estrutura do JSON inválida - chaves obrigatórias ausentes")
[26]                 
[27]             if not isinstance(dados['logs'], list):
[28]                 raise ValueError("Campo 'logs' deve ser uma lista")
[29]         except ValueError as e:
[30]             print(f"[ERRO] {e}", file=sys.stderr)
[31]             sys.exit(1)
[32] 
[33]         # 3. Processar logs com tratamento de erros de estrutura
[34]         try:
[35]             print(f"\n=== LOGS DO DISPOSITIVO {dados['dispositivo']} ({dados['tipo']}) ===")
[36]             
[37]             for log in dados['logs']:
[38]                 if log.get('severidade') in ['ALERTA', 'CRITICO']:
[39]                     print(f"\n[!] Evento: {log.get('evento', 'DESCONHECIDO').upper()}")
[40]                     print(f"    - Hora: {log.get('timestamp', 'N/A')}")
[41]                     print(f"    - Severidade: {log.get('severidade', 'N/A')}")
[42]                     
[43]                     # Detalhes dinâmicos com tratamento seguro
[44]                     detalhes = log.get('detalhes', {})
[45]                     for chave, valor in detalhes.items():
[46]                         print(f"    - {chave.replace('_', ' ').title()}: {valor}")
[47]
[48]         except AttributeError as e:
[49]             print(f"[ERRO] Estrutura de log inválida: {e}", file=sys.stderr)
[50]             sys.exit(1)
[51]
[52]         # 4. Gerar estatísticas (com tratamento de possíveis erros)
[53]         try:
[54]            total_eventos = len(dados['logs'])
[55]            criticos = sum(1 for log in dados['logs'] 
[56]                         if isinstance(log, dict) and 
[57]                         log.get('severidade') == 'CRITICO')
[58]             
[59]             print(f"\n=== RESUMO ===")
[60]             print(f"Total de eventos: {total_eventos}")
[61]             print(f"Eventos críticos: {criticos}")
[62] 
[63]         except Exception as e:
[64]             print(f"[ERRO] Ao gerar estatísticas: {e}", file=sys.stderr)
[65] 
[66]     except KeyboardInterrupt:
[67]         print("\n[INFO] Processamento interrompido pelo usuário", file=sys.stderr)
[68]         sys.exit(0)
[69]     except Exception as e:
[70]         print(f"[ERRO CRÍTICO] {e}", file=sys.stderr)
[71]         sys.exit(1)
[72]     finally:
[73]         print("\nProcessamento concluído.")
[74]
[75] if __name__ == "__main__":
[76]     main()
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

**Explicação**

```Python

Bloco 1: Importações

[01] import json                                                                                  # Manipulação de arquivos JSON
[02] from datetime import datetime                                                                # Trabalhar com datas/horas (não usado diretamente, mas útil para extensões)
[03] import sys                                                                                   # Acesso ao stderr e sys.exit()

Bloco 2: Definição da Função Principal

[05] def main():                                                                                  # Função principal encapsulando toda a lógica
[06]     try:                                                                                     # Bloco principal de tratamento de erros

Bloco 3: Carregamento do Arquivo JSON

[07]                                                                                              # 1. Carregar logs com tratamento de erros de arquivo/JSON
[08]         try:                                                                                 # Bloco específico para operações de arquivo
[09]             with open('logs_switch.json', 'r') as f:                                         # Abre o arquivo no modo leitura
[10]                 dados = json.load(f)                                                         # Carrega e parseia o JSON
[11]         except FileNotFoundError:                                                            # Erro se arquivo não existe
[12]             print("[ERRO] Arquivo 'logs_switch.json' não encontrado", file=sys.stderr)       # Função de impressão de mensagens
                                                                                                    # "[ERRO] Arquivo 'logs_switch.json' não encontrado",  Mensagem de erro descritiva:
                                                                                                       # - Prefixo [ERRO] para identificação visual
                                                                                                       # - Nome exato do arquivo procurado
                                                                                                       # file=sys.stderr - Redirecionamento para o fluxo de erro padrão:
                                                                                                       # 1. Segregação de saídas (erros vs dados normais)
                                                                                                       # 2. Permite redirecionamento seletivo (ex: 2> erros.log)
                                                                                                       # 3. Melhor prática para ferramentas CLI
              )
[13]             sys.exit(1)                                                                      # Sai com código de erro
[14]         except json.JSONDecodeError as e:                                                    # Erro se JSON inválido
[15]             print(f"[ERRO] Arquivo JSON inválido: {e}", file=sys.stderr)                     # Mensagem de erro - Mesmo estilo da anterior
[16]             sys.exit(1)
[17]         except PermissionError:                                                              # Erro de permissão
[18]             print("[ERRO] Sem permissão para ler o arquivo", file=sys.stderr)                # Mensagem de erro - Mesmo estilo das anteriores
[19]             sys.exit(1)

Bloco 4: Validação da Estrutura do JSON

[21]                                                                                               # 2. Validar estrutura básica do JSON
[22]         try:                                                                                  # Bloco de tratamento de erro
[23]             required_keys = ['dispositivo', 'tipo', 'logs']                                   # Chaves obrigatórias
[24]             if not all(key in dados for key in required_keys):                                # Verifica presença
[25]                 raise ValueError("Estrutura do JSON inválida - chaves obrigatórias ausentes") # Instrução para lançar uma exceção manualmente
                    ValueError(                                                                       # Tipo de exceção específica para valores inválidos:
                                                                                                      # - Mais específico que Exception genérico
                                                                                                      # - Adequado para problemas de validação
                                                                                                      # "Estrutura do JSON inválida - chaves obrigatórias ausentes"  # Mensagem detalhada:
                                                                                                                     # 1. Contexto do erro (estrutura JSON)
                                                                                                                     # 2. Natureza do problema (chaves ausentes)
                                                                                                                     # 3. Autoexplicativo para logs/troubleshooting
                    )
              )
[26]                 
[27]             if not isinstance(dados['logs'], list):                                           # Verifica tipo da lista de logs
[28]                 raise ValueError("Campo 'logs' deve ser uma lista")                           # Instrução para lançar uma exceção manualmente no mesmo estilo da anterior
[29]         except ValueError as e:                                                               # Captura erros de validação
[30]             print(f"[ERRO] {e}", file=sys.stderr)
[31]             sys.exit(1)

Bloco 5: Processamento dos Logs

[33]                                                                                                # 3. Processar logs com tratamento de erros de estrutura
[34]         try:                                                                                   # Bloco de tratamento de erro
[35]             print(f"\n=== LOGS DO DISPOSITIVO {dados['dispositivo']} ({dados['tipo']}) ===")   # Cabeçalho
[36]             
[37]             for log in dados['logs']:                                                          # Itera sobre cada log
[38]                 if log.get('severidade') in ['ALERTA', 'CRITICO']:                             # Filtra severidade
[39]                     print(f"\n[!] Evento: {log.get('evento', 'DESCONHECIDO').upper()}")        # Nome do evento
[40]                     print(f"    - Hora: {log.get('timestamp', 'N/A')}")                        # Timestamp
[41]                     print(f"    - Severidade: {log.get('severidade', 'N/A')}")                 # Nível severidade
[42]                     
[43]                     # Detalhes dinâmicos com tratamento seguro
[44]                     detalhes = log.get('detalhes', {})                                         # Dicionário vazio se não existir
[45]                     for chave, valor in detalhes.items():                                      # Itera sobre detalhes
[46]                         print(f"    - {chave.replace('_', ' ').title()}: {valor}")             # Formata chaves
[47]
[48]         except AttributeError as e:                                                            # Erro se estrutura inválida
[49]             print(f"[ERRO] Estrutura de log inválida: {e}", file=sys.stderr)                   # Mensagem de erro no estilo das anteriores
[50]             sys.exit(1)                                                                        # Função para encerramento imediato do programa
                                                                                                         # Código de status de saída:
                                                                                                         # - Convenção Unix: 0 = sucesso, ≠0 = erro
                                                                                                         # - 1 indica falha genérica (valores comuns:)
                                                                                                         #   1: Erro geral
                                                                                                         #   2: Uso incorreto do comando
                                                                                                         #   126: Permissão negada
                                                                                                         #   127: Comando não encontrado

Bloco 6: Geração de Estatísticas

[52]                                                                                                # 4. Gerar estatísticas (com tratamento de possíveis erros)
[53]         try:                                                                                   # Bloco de tratamento de erro
[54]            total_eventos = len(dados['logs'])                                                  # Conta total de logs
[55]            criticos = sum(1 for log in dados['logs']                                           # Conta eventos críticos
[56]                         if isinstance(log, dict) and                                           # Verifica se é dicionário
[57]                         log.get('severidade') == 'CRITICO')
[58]             
[59]             print(f"\n=== RESUMO ===")                                                         # Seção de resumo
[60]             print(f"Total de eventos: {total_eventos}")                                        # Função built-in de saída padrão
                                                                                                    # f"Total de eventos: {total_eventos}" # String formatada (f-string) contendo:
                                                                                                                                           # - Texto descritivo fixo "Total de eventos: "
                                                                                                                                           # - Variável {total_eventos} com:
                                                                                                                                           #   * Valor calculado na linha 54 (len(dados['logs']))
                                                                                                                                           #   * Representação automática como string
              )
[61]             print(f"Eventos críticos: {criticos}")
[62] 
[63]         except Exception as e:                                                                 # Erro genérico em estatísticas
[64]             print(f"[ERRO] Ao gerar estatísticas: {e}", file=sys.stderr)                       # Função de saída de mensagens
                                                                                                    # f"[ERRO] Ao gerar estatísticas: {e}", # Mensagem de erro formatada:
                                                                                                                                            # - Prefixo [ERRO] para identificação visual
                                                                                                                                            # - Contexto claro ("Ao gerar estatísticas")
                                                                                                                                            # - Detalhe do erro via {e} (exception capturada)
                                                                                                     # file=sys.stderr                       # Redirecionamento para saída de erros:
                                                                                                                                             # 1. Separação lógica de fluxos (erros vs dados)
                                                                                                                                             # 2. Permite tratamento diferenciado em:
                                                                                                                                             #    - Logs de sistema
                                                                                                                                             #    - Pipelines Unix (2> erros.log)
                                                                                                                                             # 3. Melho

Bloco 7: Tratamento Global de Exceções

[66]     except KeyboardInterrupt:                                                                  # Captura CTRL+C
[67]         print("\n[INFO] Processamento interrompido pelo usuário", file=sys.stderr)
[68]         sys.exit(0)                                                                            # Sai com código de sucesso
[69]     except Exception as e:                                                                     # Captura qualquer erro não tratado
[70]         print(f"[ERRO CRÍTICO] {e}", file=sys.stderr)
[71]         sys.exit(1)                                                                            # Sai com código de erro
[72]     finally:                                                                                   # Sempre executa
[73]         print("\nProcessamento concluído.")                                                    # Mensagem final

Bloco 8: Execução do Script

[75] if __name__ == "__main__":                                                                     # Verifica se é o módulo principal
[76]     main()                                                                                     # Chama a função principal
```

### Exemplo 04 : Comparação de configurações  

**Objetivo:**
  - Comparar versões anteriores e posteriores de configurações de dispositivos
  - Identificar mudanças textuais e estruturais
  - Gerar relatório detalhado de alterações
  - Tratar erros de forma robusta para uso em produção

**config_antes.json**    

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

**config_depois.json**   

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
[03] import sys
[04] 
[05] def carregar_configuracao(arquivo):
[06]     """Carrega um arquivo JSON de configuração com tratamento de erros"""
[07]     try:
[08]         with open(arquivo, 'r') as f:
[09]             return json.load(f)
[10]     except FileNotFoundError:
[11]         print(f"[ERRO] Arquivo {arquivo} não encontrado", file=sys.stderr)
[12]         sys.exit(1)
[13]     except json.JSONDecodeError as e:
[14]         print(f"[ERRO] Arquivo {arquivo} com formato JSON inválido: {e}", file=sys.stderr)
[15]         sys.exit(1)
[16]     except PermissionError:
[17]         print(f"[ERRO] Sem permissão para ler o arquivo {arquivo}", file=sys.stderr)
[18]         sys.exit(1)
[19] 
[20] def comparar_textualmente(antes, depois):
[21]     """Gera um diff textual entre as configurações"""
[22]     try:
[23]         print("\n=== DIFF ENTRE CONFIGURAÇÕES ===")
[24]         config_antes = json.dumps(antes, indent=2).splitlines()
[25]         config_depois = json.dumps(depois, indent=2).splitlines()
[26]         
[27]         for line in unified_diff(config_antes, config_depois, 
[28]                                fromfile='ANTES', tofile='DEPOIS', n=2):
[29]             print(line)
[30]     except Exception as e:
[31]         print(f"[ERRO] Falha na comparação textual: {e}", file=sys.stderr)
[32] 
[33] def comparar_estruturalmente(antes, depois):
[34]     """Realiza comparação estrutural das configurações"""
[35]     try:
[36]         print("\n=== MUDANÇAS DETECTADAS ===")
[37]         
[38]         # Comparação de VLANs
[39]         try:
[40]             vlans_antes = set(antes.get('vlans', []))
[41]             vlans_depois = set(depois.get('vlans', []))
[42]             
[43]             if added := vlans_depois - vlans_antes:
[43]                print(f"[+] VLANs adicionadas: {added}")
[44]             if removed := vlans_antes - vlans_depois:
[45]                 print(f"[-] VLANs removidas: {removed}")
[46]         except AttributeError:
[47]             print("[AVISO] Campo 'vlans' ausente ou inválido", file=sys.stderr)
[48] 
[49]        # Comparação de interfaces
[50]        try:
[51]             interfaces_antes = antes.get('interfaces', {})
[52]             interfaces_depois = depois.get('interfaces', {})
[53]             
[54]             for interface in interfaces_antes:
[55]                 if interface in interfaces_depois:
[56]                     for chave in interfaces_antes[interface]:
[57]                         if interfaces_antes[interface].get(chave) != interfaces_depois[interface].get(chave):
[58]                             print(f"[!] Interface {interface}: {chave} alterado de "
[59]                                   f"'{interfaces_antes[interface].get(chave)}' para "
[60]                                   f"'{interfaces_depois[interface].get(chave)}'")
[70]         except AttributeError:
[71]             print("[AVISO] Campo 'interfaces' ausente ou inválido", file=sys.stderr)
[72]            
[73]     except Exception as e:
[74]         print(f"[ERRO] Falha na comparação estrutural: {e}", file=sys.stderr)
[75] 
[76] def main():
[77]     try:
[78]         # Carregar configurações
[79]         antes = carregar_configuracao('config_antes.json')
[80]         depois = carregar_configuracao('config_depois.json')
[81]        
[82]         # Realizar comparações
[83]         comparar_textualmente(antes, depois)
[84]         comparar_estruturalmente(antes, depois)
[85]        
[86]     except KeyboardInterrupt:
[87]         print("\n[INFO] Execução interrompida pelo usuário", file=sys.stderr)
[88]         sys.exit(0)
[89]     except Exception as e:
[90]         print(f"[ERRO CRÍTICO] {e}", file=sys.stderr)
[91]         sys.exit(1)
[92]     finally:
[93]         print("\nAnálise concluída.")
[94] 
[95] if __name__ == "__main__":
[96]     main()
```

**Saída:**  

```Bash
alcancil@linux:~/automacoes/erros/json/04$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/json/04$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/json/04$ python3 comparar_configs.py 

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

Análise concluída.
(venv) alcancil@linux:~/automacoes/erros/json/04$ 
```

**Explicação**  

```Python

Bloco 1: Importações

import json                                                                                 # Manipulação de arquivos JSON
from difflib import unified_diff                                                            # Geração de diff entre textos
import sys                                                                                  # Acesso a stderr e sys.exit()

Bloco 2: Função carregar_configuracao()

def carregar_configuracao(arquivo):                                                         # Cria a função carregar_configuracao e usa como parâmetro a variável arquivo 
    """Carrega um arquivo JSON de configuração com tratamento de erros"""
    try:
        with open(arquivo, 'r') as f:                                                       # Abre arquivo no modo leitura
            return json.load(f)                                                             # Carrega e parseia o JSON
    except FileNotFoundError:                                                               # Erro se arquivo não existe
        print(f"[ERRO] Arquivo {arquivo} não encontrado", file=sys.stderr)                  # Função para imprimir mensagem no console
                                                                                            # f"[ERRO] Arquivo {arquivo} não encontrado", - Mensagem de erro formatada:
                                                                                                     # - [ERRO] como prefixo identificador
                                                                                                     # - Nome do arquivo dinâmico via {arquivo}
                                                                                            # file=sys.stderr - Redireciona para saída padrão de erros:
                                                                                                              # 1. Permite separar logs de erro de saídas normais
                                                                                                              # 2. Facilita redirecionamento (ex: 2> erros.log)
                                                                                                              # 3. Segue convenções Unix para ferramentas CLI
        sys.exit(1)                                                                         # Encerra o programa imediatamente com código de erro 1 (falha genérica)
                                                                                            # Convenções comuns de códigos de saída:
                                                                                                              # - 0: Sucesso
                                                                                                              # - 1: Erro geral (usado aqui)
                                                                                                              # - 2: Uso incorreto de comando
                                                                                                              # - 3-127: Outros erros específicos (padrão Unix)
                                                                                                              # Útil para scripts em pipelines (ex: if [ $? -ne 0 ]; then...)
    except json.JSONDecodeError as e:                                                       # Erro se JSON inválido
        print(f"[ERRO] Arquivo {arquivo} com formato JSON inválido: {e}", file=sys.stderr)  # Imprime mensagem de erro no mesmo estilo da anterior
        sys.exit(1)                                                                         # Sai com código de erro no estilo do anterior
    except PermissionError:                                                                 # Erro de permissão
        print(f"[ERRO] Sem permissão para ler o arquivo {arquivo}", file=sys.stderr)        # Imprime mensagem de erro no mesmo estilo da anterior
        sys.exit(1)                                                                         # Sai com código de erro no estilo do anterior

Bloco 3: Função comparar_textualmente()

def comparar_textualmente(antes, depois):                                                   # Cria a funcao comparar_textualmente usando como parâmetros antes, depois
    """Gera um diff textual entre as configurações"""
    try:                                                                                    # Inicia o bloco de tratamento de erros com try
        print("\n=== DIFF ENTRE CONFIGURAÇÕES ===")                                         # Cabeçalho
        config_antes = json.dumps(antes, indent=2).splitlines()                             # Converte o dicionário 'antes' para:
                                                                                                       # 1. String JSON formatada (indent=2 para identação de 2 espaços)
                                                                                                       # 2. Divide em linhas (splitlines()) para comparação linha-a-linha
                                                                                                       # Resultado: Lista de strings pronta para diff textual
        config_depois = json.dumps(depois, indent=2).splitlines()                           # Converte para string formatada no padrão da linha anteriror
        
        for line in unified_diff(config_antes, config_depois,                               # # Itera sobre as diferenças entre:
                                                                                            # - config_antes: Lista de linhas da versão anterior
                                                                                            # - config_depois: Lista de linhas da versão nova
                              fromfile='ANTES', tofile='DEPOIS', n=2):                      # fromfile='ANTES', - Rótulo para o arquivo origem (exibido no diff)
                                                                                            # tofile='DEPOIS', - Rótulo para o arquivo destino (exibido no diff)
                                                                                            # n=2): - Número de linhas de contexto (mostra 2 linhas antes/depois das mudanças)
            print(line)                                                                     # Imprime cada linha do diff
    except Exception as e:                                                                  # Captura qualquer exceção não tratada anteriormente
                                                                                                    # - 'Exception': Classe base para todas as exceções built-in
                                                                                                    # - 'as e': Armazena o objeto da exceção na variável 'e'
                                                                                                    # Uso típico em blocos try-except como último recurso
        print(f"[ERRO] Falha na comparação textual: {e}", file=sys.stderr)                  # Imprime mensagem de erro no mesmo estilo da anterior

Bloco 4: Função comparar_estruturalmente()

def comparar_estruturalmente(antes, depois):                                                # Inicio da funcao comparar_estruturalmente tendo como parâmetros as variáveis antes e depois
    """Realiza comparação estrutural das configurações"""
    try:                                                                                    # Inicio do bloco de tratamento de erros com Try
        print("\n=== MUDANÇAS DETECTADAS ===")                                              # Cabeçalho
        
        # Comparação de VLANs
        try:                                                                                # Segundo bloco de tratamento de erros com try aninhado dentrdo do anterior
            vlans_antes = set(antes.get('vlans', []))                                       # Converte a lista de VLANs para um conjunto (set):
                                                                                                       # 1. antes.get('vlans', []): Acessa a chave 'vlans' no dicionário 'antes'
                                                                                                       #    - Se não existir, retorna lista vazia ([]) como valor padrão
                                                                                                       # 2. set(): Converte a lista para conjunto, permitindo operações matemáticas:
                                                                                                       #    - Diferença de conjuntos (vlan_removidas = vlans_antes - vlans_depois)
                                                                                                       #    - União, interseção, etc
                                                                                                       # Objetivo: Facilitar comparação de VLANs entre configurações
            vlans_depois = set(depois.get('vlans', []))                                     # Usa get() para evitar KeyError como na linha anterior
            
            if added := vlans_depois - vlans_antes:                                         # Se houver VLANs em vlans_depois que não estão em vlans_antes
                print(f"[+] VLANs adicionadas: {added}")                                    # Imprime VLANs novas com prefixo [+]
            if removed := vlans_antes - vlans_depois:                                       # Se houver VLANs em vlans_antes que não estão em vlans_depois
                print(f"[-] VLANs removidas: {removed}")                                    # Imprime VLANs removidas com prefixo [-]
        except AttributeError:                                                              # Captura erro se 'vlans' não for lista/dicionário (tratamento de erros com except)
            print("[AVISO] Campo 'vlans' ausente ou inválido", file=sys.stderr)             # Mensagem de aviso no estilo das anteriores

        # Comparação de interfaces      
        try:                                                                                # Inicio do bloco de tratamento de erros com Try 
            interfaces_antes = antes.get('interfaces', {})                                  # Obtém interfaces da config anterior (ou dicionário vazio)
            interfaces_depois = depois.get('interfaces', {})                                # Obtém interfaces da config nova (ou dicionário vazio)
            
            for interface in interfaces_antes:                                              # Itera sobre cada interface da config anterior
                if interface in interfaces_depois:                                          # Verifica se interface existe na config nova
                    for chave in interfaces_antes[interface]:                               # Itera sobre cada propriedade da interface
                        if interfaces_antes[interface].get(chave) != interfaces_depois[interface].get(chave):  # Compara valores entre configurações
                            print(f"[!] Interface {interface}: {chave} alterado de "        # Imprime mudanças
                                  f"'{interfaces_antes[interface].get(chave)}' para "       # Imprime mudanças
                                  f"'{interfaces_depois[interface].get(chave)}'")           # Imprime mudanças
        except AttributeError:                                                              # Captura erro se 'interfaces' não for dicionário
            print("[AVISO] Campo 'interfaces' ausente ou inválido", file=sys.stderr)        # Mensagem de aviso
            
    except Exception as e:                                                                  # Captura qualquer outro erro não previsto
        print(f"[ERRO] Falha na comparação estrutural: {e}", file=sys.stderr)               # Imprime erro detalhado

Bloco 5: Função main()

def main():
    try:
        # Carregar configurações
        antes = carregar_configuracao('config_antes.json')                                  # Chama função de carregamento
        depois = carregar_configuracao('config_depois.json')                               # Carrega e retorna o conteúdo do arquivo JSON de configuração "depois                       
        
        # Realizar comparações
        comparar_textualmente(antes, depois)                                                 # Diferenças textuais
        comparar_estruturalmente(antes, depois)                                              # Análise estrutural
        
    except KeyboardInterrupt:  # Captura Ctrl+C
        print("\n[INFO] Execução interrompida pelo usuário", file=sys.stderr)                # Mensagem de erro em estilo amigável         
        sys.exit(0)                                                                          # Sai com código de sucesso
    except Exception as e:                                                                   # Erro genérico
        print(f"[ERRO CRÍTICO] {e}", file=sys.stderr)                                        # Mensagem de erro em estilo amigável 
        sys.exit(1)                                                                          # Sai com código de erro
    finally:                                                                                 # Sempre executa
        print("\nAnálise concluída.")                                                        # Mensagem final

Bloco 6: Execução principal

if __name__ == "__main__":                                                                   # Verifica se é o módulo principal
    main()                                                                                   # Chama a função principal
```

### Resumo de Boas Práticas para Tratamento de JSON em Automação de Redes

| Categoria           | Boa Prática                                               | Exemplo no Código                            | Benefício                                  |
|---------------------|-----------------------------------------------------------|----------------------------------------------|--------------------------------------------|
| Tratamento de Erros | Usar blocos try-except específicos para cada tipo de erro | except json.JSONDecodeError, except KeyError | Detecta problemas precisos e evita falhas catastróficas |
| Capturar Exception como último recurso	except Exception as e:	Garante que nenhum erro passe despercebido
| Manipulação de Dados	Usar .get() com valor padrão para acessar chaves	dados.get('vlans', [])	Evita KeyError e define fallbacks seguros
| Converter listas para set() quando necessário	set(antes.get('vlans', []))	Permite operações de comparação eficientes (diferença, união)
Saída e Logs	Redirecionar erros para sys.stderr	print("[ERRO]", file=sys.stderr)	Separa mensagens de erro de saídas normais para pipelines
	Padronizar prefixos em mensagens ([ERRO], [AVISO])	print("[!] Interface alterada...")	Facilita filtragem e troubleshooting
Estrutura de Código	Modularizar funções por responsabilidade	carregar_configuracao(), comparar_textualmente()	Código mais legível e testável
	Usar if __name__ == "__main__": para execução controlada	Bloco final do script	Permite reutilização como módulo
Controle de Fluxo	Usar sys.exit() com códigos padronizados (0=sucesso, 1=erro)	sys.exit(1)	Integração com scripts shell e sistemas de monitoramento
	Implementar finally para ações obrigatórias	print("Processamento concluído")	Garante execução mesmo com falhas
Validação	Verificar estrutura do JSON antes de processar	if not all(key in dados for key in required_keys):	Evita erros em dados incompletos ou malformados
	Validar tipos de dados (isinstance(dados['logs'], list))	Linha 27 do Exemplo 03	Previne erros de tipo em operações subsequentes

**Tabela de Códigos de Saída Recomendados**
Código	Significado	Uso Típico
0	Sucesso	Execução normal
1	Erro geral	Falha genérica (arquivo não encontrado, JSON inválido)
2	Erro de sintaxe/argumentos	Uso incorreto do script
3	Erro de permissão	Falha ao acessar arquivos
4	Erro de dados	Validação de schema falhou

Essas práticas são diretamente aplicáveis aos exemplos do arquivo, especialmente:

    Exemplo 01: Demonstra tratamento hierárquico de erros

    Exemplo 02: Ilustra padrões de metadados e saída estruturada

    Exemplo 03: Mostra validação de estrutura e filtragem segura

    Exemplo 04: Exemplifica comparação robusta entre configurações

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