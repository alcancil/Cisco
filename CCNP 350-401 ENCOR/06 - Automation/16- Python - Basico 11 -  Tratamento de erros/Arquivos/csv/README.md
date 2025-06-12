
# Python - Básico 11

## Índice

- [Python - Básico 11](#python---básico-11)
  - [Índice](#índice)
  - [Tratamento de Erros com Arquivos `.csv`](#tratamento-de-erros-com-arquivos-csv)
  - [Erros comuns com arquivos .csv](#erros-comuns-com-arquivos-csv)
  - [Contexto de uso em redes](#contexto-de-uso-em-redes)
    - [Exemplo 01 – Leitura segura de inventario.csv](#exemplo-01--leitura-segura-de-inventariocsv)
    - [Exemplo 02 – Backup de configurações em massa com tratamento de erros](#exemplo-02--backup-de-configurações-em-massa-com-tratamento-de-erros)
    - [Exemplo 03: Processamento de Logs Estruturados com Tratamento de Erros](#exemplo-03-processamento-de-logs-estruturados-com-tratamento-de-erros)
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

**Saída**

```Bash
(venv) alcancil@linux:~/automacoes/erros/csv/02$ python3 backup_config.py 
✅ Backup de servidor-linux salvo em: backups/servidor-linux_backup.txt
✅ Backup de roteador-simulado salvo em: backups/roteador-simulado_backup.txt
✅ Backup de switch-simulado salvo em: backups/switch-simulado_backup.txt

✅ Todos os backups foram gerados com sucesso.
🔁 Fim do processamento.
(venv) alcancil@linux:~/automacoes/erros/csv/02$ ls -r backups
switch-simulado_backup.txt  servidor-linux_backup.txt  roteador-simulado_backup.txt
(venv) alcancil@linux:~/automacoes/erros/csv/02$ 
```

**Saída com erro**

```Bash
(venv) alcancil@linux:~/automacoes/erros/csv/02$ mv dispositivos.csv dispositivos1.csv 
(venv) alcancil@linux:~/automacoes/erros/csv/02$ python3 backup_config.py 
❌ Erro: Arquivo dispositivos.csv não encontrado.
🔁 Fim do processamento.
```

**Explicação**

```Python
Importações e variáveis iniciais

import csv                                                                                                 # Importa o módulo para manipulação de arquivos CSV
import os                                                                                                  # Importa o módulo para interagir com o sistema de arquivos

caminho_csv = "dispositivos.csv"                                                                           # Define o caminho do arquivo de entrada CSV
pasta_backup = "backups"                                                                                   # Define o nome da pasta onde os backups serão salvos

Início do tratamento de erros

try:                                                                                                       # Inicia o bloco de tratamento de exceções
    if not os.path.exists(caminho_csv):                                                                    # Verifica se o arquivo CSV existe no sistema
        raise FileNotFoundError("Arquivo dispositivos.csv não encontrado.")                                # Lança exceção personalizada se não existir

Criação do diretório de saída

    os.makedirs(pasta_backup, exist_ok=True)                                                               # Cria a pasta "backups" se ela ainda não existir

Leitura do CSV e processamento linha a linha

    with open(caminho_csv, 'r') as arquivo_csv:                                                            # Abre o arquivo CSV em modo leitura
        leitor = csv.DictReader(arquivo_csv)                                                               # Lê o conteúdo como dicionário (coluna → valor)

        for dispositivo in leitor:                                                                         # Itera sobre cada linha do CSV
            tipo = dispositivo.get("tipo", "").lower()                                                     # Obtém o tipo do dispositivo e converte para minúsculas

Geração do conteúdo de backup por tipo

            if tipo == "linux":                                                                            # Se o dispositivo for do tipo "linux"
                config = f"hostname {dispositivo['hostname']}\nIP: {dispositivo['ip']}\nSO: Ubuntu 22.04"  # Gera uma "configuração" simulada

            elif "cisco" in tipo:                                                                          # Se o tipo contiver "cisco" (ex: cisco_ios)
                config = f"hostname {dispositivo['hostname']}\ninterface GigabitEthernet0/1\n  ip address {dispositivo['ip']} 255.255.255.0"  # Gera config Cisco simulada

            else:
                raise ValueError(f"Tipo de dispositivo não reconhecido: {tipo}")                           # Lança erro se o tipo for desconhecido

Escrita do backup em arquivo

            caminho_saida = os.path.join(pasta_backup, f"{dispositivo['hostname']}_backup.txt")            # Define o caminho de saída do arquivo de backup
            with open(caminho_saida, 'w') as saida:                                                        # Abre o arquivo em modo escrita
                saida.write(config)                                                                        # Escreve a configuração no arquivo

            print(f"✅ Backup de {dispositivo['hostname']} salvo em: {caminho_saida}")                    # Mensagem de sucesso

🔹 Bloco 7 – Tratamento de exceções específicas

except FileNotFoundError as e:                                                                            # Captura erro se o arquivo CSV não existir
    print(f"❌ Erro: {e}")

except PermissionError:                                                                                   # Captura erro se não houver permissão para ler ou gravar
    print("❌ Permissão negada para criar arquivos ou ler o CSV.")

except KeyError as e:                                                                                     # Captura erro se alguma coluna obrigatória estiver ausente
    print(f"❌ Coluna ausente no CSV: {e}")

except ValueError as e:                                                                                   # Captura erro se o tipo do dispositivo for inválido
    print(f"❌ Erro de valor: {e}")

except Exception as e:                                                                                    # Captura qualquer outro erro não tratado acima
    print(f"❌ Erro inesperado: {e}")

🔹 Bloco 8 – Finalização

else:                                                                                                    # Executa somente se nenhum erro ocorreu no try
    print("\n✅ Todos os backups foram gerados com sucesso.")

finally:                                                                                                 # Sempre executado, com ou sem erro
    print("🔁 Fim do processamento.")
```

### Exemplo 03: Processamento de Logs Estruturados com Tratamento de Erros

**Objetivo:**  

Ler um arquivo CSV de logs, filtrar entradas críticas e exibir um resumo, com tratamento robusto para erros (arquivo não encontrado, formato inválido, etc.).

**logs.csv**  

```csv
timestamp,dispositivo,nivel,mensagem
2024-05-10 09:15:23,switch01,ALERTA,Interface GigabitEthernet0/1 down
2024-05-10 09:16:45,router01,CRITICO,CPU usage 95%
2024-05-10 09:20:12,switch01,INFO,Interface GigabitEthernet0/1 up
2024-05-10 09:25:34,firewall01,ALERTA,Blocked 10 SSH attempts
```

**Script processar_log.py**

```python
[01] import csv
[02]
[03] try:
[04]     # Tenta abrir e processar o arquivo
[05]     with open('logs.csv', 'r') as arquivo_csv:
[06]         leitor = csv.DictReader(arquivo_csv)
[07]         
[08]         # Filtra logs com nível "CRITICO" ou "ALERTA"
[09]         logs_filtrados = [
[10]             log for log in leitor 
[11]             if log['nivel'] in ['CRITICO', 'ALERTA']
[12]         ]
[13]
[14] except FileNotFoundError:
[15]     print("❌ Erro: Arquivo 'logs.csv' não encontrado!")
[16]     exit(1)
[17]
[18] except KeyError as e:
[19]     print(f"❌ Erro: Campo inválido no CSV - {e} (verifique o cabeçalho)")
[20]     exit(1)
[21]
[22] except Exception as e:
[23]     print(f"❌ Erro inesperado: {e}")
[24]     exit(1)
[25]
[26] else:
[27]     # Executa apenas se não houver erros
[28]     print("===== LOGS CRÍTICOS/ALERTAS =====")
[29]     for log in logs_filtrados:
[30]         print(f"{log['timestamp']} | {log['dispositivo']} | {log['nivel']}: {log['mensagem']}")
[31]
[32]     # Contagem por dispositivo
[33]     contagem = {}
[34]     for log in logs_filtrados:
[35]         dispositivo = log['dispositivo']
[36]         contagem[dispositivo] = contagem.get(dispositivo, 0) + 1
[37]
[38]     print("\n===== RESUMO =====")
[39]     for dispositivo, total in contagem.items():
[40]         print(f"{dispositivo}: {total} alerta(s)")
[41]
[42] finally:
[43]     print("\n✅ Processamento concluído (com ou sem erros).")
```

**Saída**

```Bash
alcancil@linux:~/automacoes/erros/csv/03$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/csv/03$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/csv/03$ python processar_log.py 
===== LOGS CRÍTICOS/ALERTAS =====
2024-05-10 09:15:23 | switch01 | ALERTA: Interface GigabitEthernet0/1 down
2024-05-10 09:16:45 | router01 | CRITICO: CPU usage 95%
2024-05-10 09:25:34 | firewall01 | ALERTA: Blocked 10 SSH attempts

===== RESUMO =====
switch01: 1 alerta(s)
router01: 1 alerta(s)
firewall01: 1 alerta(s)

✅ Processamento concluído (com ou sem erros).
(venv) alcancil@linux:~/automacoes/erros/csv/03$
```

**Saída com de Erro (Arquivo Não Encontrado)**

```bash
(venv) alcancil@linux:~/automacoes/erros/csv/03$ ls -la
total 20
drwxrwxr-x 3 alcancil alcancil 4096 jun 12 15:07 .
drwxrwxr-x 5 alcancil alcancil 4096 jun 12 14:46 ..
-rw-r--r-- 1 root     root      286 jun 12 14:48 logs.csv
-rw-r--r-- 1 root     root     1243 jun 12 14:59 processar_log.py
drwxrwxr-x 5 alcancil alcancil 4096 jun 12 15:07 venv
(venv) alcancil@linux:~/automacoes/erros/csv/03$ mv logs.csv logs1.csv 
(venv) alcancil@linux:~/automacoes/erros/csv/03$ python processar_log.py 
❌ Erro: Arquivo 'logs.csv' não encontrado!

✅ Processamento concluído (com ou sem erros).
(venv) alcancil@linux:~/automacoes/erros/csv/03$ 
```

**Explicação**

**OBS:** antes de seguir a explicação vale citar o uso do comando `exit()`  

**Comando exit( )**

O que faz exit(1)?

  - exit(): É uma função do Python que encerra imediatamente a execução do script.

  - 1: É um código de status (também chamado de "código de saída" ou "exit code"). Indica que o script terminou com um erro.

Significado dos Códigos de Saída

Os códigos de saída são convenções universais em sistemas Unix/Linux e Windows:  

| Código | Significado              | Uso Comum                                                           |
|--------|--------------------------|---------------------------------------------------------------------|
| 0      | Sucesso	                | Script concluído sem erros. Ex.: exit(0) (implícito se omitido).    |
| 1	     | Erro genéric             | Falha não especificada. Ex.: exit(1) em tratamentos de erro simples.|
| 2	     | Uso incorreto do comando	| Argumentos inválidos (ex.: falta de arquivo obrigatório).           |
| 3+	 | Erros personalizados     | Podem ser definidos pelo desenvolvedor para casos específicos.      |

```Python
Bloco 1: Importação de Bibliotecas

[01] import csv                                                                # Importa o módulo 'csv' para manipulação de arquivos CSV.

Bloco 2: Tratamento de Erros Principal (try)

[03] try:                                                                      # Inicia um bloco de código protegido para capturar erros.
[04]                                                                           # Tenta abrir e processar o arquivo
[05]     with open('logs.csv', 'r') as arquivo_csv:                            # Abre o arquivo 'logs.csv' em modo leitura.
[06]         leitor = csv.DictReader(arquivo_csv)                              # Cria um leitor de CSV que mapeia linhas para dicionários.
[07]         
[08]                                                                           # Filtra logs com nível "CRITICO" ou "ALERTA"
[09]         logs_filtrados = [                                                # List comprehension para filtrar logs.
[10]             log for log in leitor                                         # Itera sobre cada linha (log) do CSV.
[11]             if log['nivel'] in ['CRITICO', 'ALERTA']                      # Filtra logs com nível CRITICO ou ALERTA.
[12]         ]

Explicação:

    - O bloco try tenta executar operações críticas (abrir arquivo, ler CSV, filtrar dados).

    - DictReader converte cada linha do CSV em um dicionário (ex.: log['nivel']).

    - As linhas 9-12 filtram apenas logs relevantes.

Bloco 3: Tratamento de Erros Específicos (except)

[14] except FileNotFoundError:                                                  # Captura erro se o arquivo não existir.
[15]     print("❌ Erro: Arquivo 'logs.csv' não encontrado!")                   # Mensagem amigável.
[16]     exit(1)                                                                 # Encerra o script com código de erro (1).
[17]
[18] except KeyError as e:                                                       # Captura erro se uma chave (ex.: 'nivel') não existir no CSV.
[19]     print(f"❌ Erro: Campo inválido no CSV - {e} (verifique o cabeçalho)")  # Indica o campo problemático.
[20]     exit(1)
[21]
[22] except Exception as e:                                                       # Captura qualquer outro erro não previsto.
[23]     print(f"❌ Erro inesperado: {e}")                                       # Exibe detalhes do erro.
[24]     exit(1)

Explicação:

    - FileNotFoundError: Falha se o arquivo não existir.

    - KeyError: Falha se o CSV não tiver a coluna esperada (ex.: nivel).

    - Exception: "Pega" qualquer outro erro genérico (ex.: permissão negada).

    - exit(1) encerra o script imediatamente após o erro.

Bloco 4: Execução em Caso de Sucesso (else)

[26] else:                                                                        # Executa apenas se NENHUM erro ocorrer no bloco 'try'.
[27]                                                                              # Executa apenas se não houver erros
[28]     print("===== LOGS CRÍTICOS/ALERTAS =====")                               # Cabeçalho para a saída.
[29]     for log in logs_filtrados:                                               # Itera sobre os logs filtrados.
[30]         print(f"{log['timestamp']} | {log['dispositivo']} | {log['nivel']}: {log['mensagem']}")  # Formata e exibe cada log.
[31]
[32]                                                                              # Contagem por dispositivo
[33]     contagem = {}                                                            # Inicializa um dicionário para contagem.
[34]     for log in logs_filtrados:                                               # Itera novamente para contar ocorrências.
[35]         dispositivo = log['dispositivo']                                     # Obtém o nome do dispositivo.
[36]         contagem[dispositivo] = contagem.get(dispositivo, 0) + 1             # Incrementa a contagem.
[37]
[38]     print("\n===== RESUMO =====")                                            # Cabeçalho do resumo.
[39]     for dispositivo, total in contagem.items():                              # Itera sobre o dicionário de contagem.
[40]         print(f"{dispositivo}: {total} alerta(s)")                           # Exibe o total por dispositivo.

Explicação:

    - O bloco else só roda se o try for bem-sucedido.

    - Exibe os logs filtrados (linhas 28-30) e um resumo por dispositivo (linhas 33-40).

    - contagem.get(dispositivo, 0) retorna 0 se a chave não existir (evita KeyError).

Bloco 5: Finalização (finally)

[42] finally:                                                                     # Sempre executa, independentemente de erros.
[43]     print("\n✅ Processamento concluído (com ou sem erros).")               # Mensagem final.

Explicação:

    - O bloco finally é sempre executado, mesmo que ocorra um erro.

    - Útil para ações de limpeza (ex.: fechar conexões) ou mensagens finais.

```

**Fluxo do Script**

- Tenta (try):

    Abrir arquivo → Ler CSV → Filtrar logs.

- Se falhar (except):

    Trata erros específicos e exibe mensagens claras.

- Se der certo (else):

    Exibe logs filtrados e resumo.

- Sempre (finally):

    Mostra mensagem de conclusão.

---
ARRUMAR

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