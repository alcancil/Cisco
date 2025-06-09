# Python - Básico 10

## Índice

- [Python - Básico 10](#python---básico-10)
  - [Índice](#índice)
  - [01 Tratamento de erros (try/excepet/else/finnaly) - arquivos .txt](#01-tratamento-de-erros-tryexcepetelsefinnaly---arquivos-txt)
    - [Exemplo 01: Criar/Escrever em Arquivo (Modo 'w')](#exemplo-01-criarescrever-em-arquivo-modo-w)
    - [Exemplo 02: Ler o arquivo roteador.txt e extrair apenas as linhas que contêm "interface".](#exemplo-02-ler-o-arquivo-roteadortxt-e-extrair-apenas-as-linhas-que-contêm-interface)
    - [Exemplo 03: Adicionar Configurações a um Arquivo Existente.](#exemplo-03-adicionar-configurações-a-um-arquivo-existente)
    - [Exemplo 4: Caminhos locais, identificando o SO (Sistema Operacional)](#exemplo-4-caminhos-locais-identificando-o-so-sistema-operacional)
    - [Boas Práticas](#boas-práticas)
  

## 01 Tratamento de erros (try/excepet/else/finnaly) - arquivos .txt  

A manipulação de arquivos em automação de redes é crítica, e erros podem ocorrer por diversos motivos (arquivo não encontrado, permissões negadas, disco cheio, etc.). Vamos adaptar os exemplos anteriores com try/except/finally/else para torná-los robustos.

1. Tratamento de Erros Comuns em Arquivos

| Erro (Exception)  | Causa Típica                      | Boa Prática de Tratamento            |
|-------------------|-----------------------------------|--------------------------------------|
| FileNotFoundError | Arquivo não existe.               | Verificar caminho ou criar arquivo.  |
| PermissionError   | Sem permissão para ler/escrever.  | Solicitar permissões ou mudar local. |
| IsADirectoryError | Tentativa de abrir uma pasta.     | Validar se o caminho é um arquivo.   |
| IOError           | Disco cheio ou problema genérico. | Logar o erro e abortar operação.     |

Agora vamos olhar alguns exemplos. <br></br>

### Exemplo 01: Criar/Escrever em Arquivo (Modo 'w')

**gerar_arquivo.py**

```python
[01] try:
[02]     with open('roteador.txt', 'w') as arquivo:
[03]         arquivo.write('hostname R1\n')
[04]         arquivo.write('interface GigabitEthernet0/1\n')
[05]         arquivo.write('  description Link para Core\n')
[06] except PermissionError:
[08]     print("Erro: Sem permissão para escrever no arquivo!")
[09] except IOError as e:
[10]     print(f"Erro de E/S: {e}")
[11] else:
[12]     print("Arquivo criado com sucesso!")
[13] finally:
[14 ]    print("Operação finalizada (com ou sem erros).")
```

**Saída**

```Bash
alcancil@linux:~/automacoes/erros/txt/01$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/txt/01$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/txt/01$ python3 gerar_arquivo.py 
Arquivo criado com sucesso!
Operação finalizada (com ou sem erros).
(venv) alcancil@linux:~/automacoes/erros/txt/01$ ls -la
total 20
drwxrwxr-x 3 alcancil alcancil 4096 jun  9 09:13 .
drwxrwxr-x 3 alcancil alcancil 4096 jun  9 09:11 ..
-rw-r--r-- 1 root     root      450 jun  9 09:13 gerar_arquivo.py
-rw-rw-r-- 1 alcancil alcancil   70 jun  9 09:13 roteador.txt
drwxrwxr-x 5 alcancil alcancil 4096 jun  9 09:13 venv
(venv) alcancil@linux:~/automacoes/erros/txt/01$ cat roteador.txt 
hostname R1
interface GigabitEthernet0/1
  description Link para Core
(venv) alcancil@linux:~/automacoes/erros/txt/01$ 
```

**OBS:** agora vou remover as permissões de escrita no arquivo e vamos rodar novamente o scipt para analisar o comportamento.

```bash
(venv) alcancil@linux:~/automacoes/erros/txt/01$ chmod -ww roteador.txt 
(venv) alcancil@linux:~/automacoes/erros/txt/01$ ls -la
total 20
drwxrwxr-x 3 alcancil alcancil 4096 jun  9 09:13 .
drwxrwxr-x 3 alcancil alcancil 4096 jun  9 09:11 ..
-rw-r--r-- 1 root     root      450 jun  9 09:13 gerar_arquivo.py
-r--r--r-- 1 alcancil alcancil   70 jun  9 09:13 roteador.txt
drwxrwxr-x 5 alcancil alcancil 4096 jun  9 09:13 venv
(venv) alcancil@linux:~/automacoes/erros/txt/01$ python3 gerar_arquivo.py 
Erro: Sem permissão para escrever no arquivo!
Operação finalizada (com ou sem erros).
(venv) alcancil@linux:~/automacoes/erros/txt/01$ 
```

Perceba agora a mensagem de erro gerado.

**Explicação**

```Python
Bloco 1: Tentativa de Execução (try)

[01] try:                                                        # Inicia o bloco de tentativa (onde erros podem ocorrer)
[02]     with open('roteador.txt', 'w') as arquivo:              # Abre o arquivo em modo escrita ('w')
[03]         arquivo.write('hostname R1\n')                      # Escreve a linha 1 no arquivo
[04]         arquivo.write('interface GigabitEthernet0/1\n')     # Escreve a linha 2
[05]         arquivo.write('  description Link para Core\n')     # Escreve a linha 3

Bloco 2: Tratamento de Erros (except)


[06] except PermissionError:                                     # Captura erros de permissão (ex.: arquivo só-leitura)
[07]     print("Erro: Sem permissão para escrever no arquivo!")  # Mensagem amigável
[08] except IOError as e:                                        # Captura outros erros de E/S (ex.: disco cheio)
[09]     print(f"Erro de E/S: {e}")                              # Exibe detalhes do erro (armazenado em 'e')

Bloco 3: Execução em Caso de Sucesso (else)

[10] else:                                                       # Executa apenas se NÃO houver erros no 'try'
[11]     print("Arquivo criado com sucesso!")                    # Confirmação de sucesso

Bloco 4: Finalização Obrigatória (finally)

[12] finally:                                                    # Sempre executa, com ou sem erros
[13]     print("Operação finalizada (com ou sem erros).")        # Mensagem final
```

### Exemplo 02: Ler o arquivo roteador.txt e extrair apenas as linhas que contêm "interface".

**ler_arquivo.py**

```python

[01] try:
[02]     with open('roteador.txt', 'r') as arquivo:
[03]         linhas = arquivo.readlines()
[04] except FileNotFoundError:
[05]     print("Erro: Arquivo 'roteador.txt' não encontrado!")
[06] except UnicodeDecodeError:
[07]     print("Erro: Arquivo não está em formato texto válido.")
[08] else:
[09]     interfaces = [linha.strip() for linha in linhas if 'interface' in linha.lower()]
[10]     print("Interfaces encontradas:")
[11]     for interface in interfaces:
[12]         print(interface)
[13] finally:
[14]     print("Leitura concluída.")
```

**Saída**

```Bash
alcancil@linux:~/automacoes/erros/txt/02$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/txt/02$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/txt/02$ python3 ler_arquivo.py 
Interfaces encontradas:
interface GigabitEthernet0/1
Leitura concluída.
(venv) alcancil@linux:~/automacoes/erros/txt/02$ 
```

**Saída com erro**

```Bash
(venv) alcancil@linux:~/automacoes/erros/txt/02$ mv roteador.txt roteador01.txt 
(venv) alcancil@linux:~/automacoes/erros/txt/02$ python3 ler_arquivo.py 
Erro: Arquivo 'roteador.txt' não encontrado!
Leitura concluída.
(venv) alcancil@linux:~/automacoes/erros/txt/02$
```

**Explicação**

```Python
Bloco 1: Tentativa de Leitura (try)

[01] try:                                                                                 # Inicia o bloco de tentativa (onde erros podem ocorrer)
[02]     with open('roteador.txt', 'r') as arquivo:                                       # Abre o arquivo em modo leitura ('r')
[03]         linhas = arquivo.readlines()                                                 # Lê TODAS as linhas do arquivo

Bloco 2: Tratamento de Erros (except)

[04] except FileNotFoundError:                                                            # Captura erro se o arquivo não existir
[05]     print("Erro: Arquivo 'roteador.txt' não encontrado!")                            # Mensagem amigável
[06] except UnicodeDecodeError:                                                           # Captura erro se o arquivo não for texto válido
[07]     print("Erro: Arquivo não está em formato texto válido.")                         # Ex: arquivo binário

Bloco 3: Execução em Caso de Sucesso (else)

[08] else:                                                                                 # Executa apenas se NÃO houver erros no 'try'
[09]     interfaces = [linha.strip() for linha in linhas if 'interface' in linha.lower()]  # Cria uma lista chamada 'interfaces'
                                                                                           # linha.strip() - Remove espaços/quebras de linha (\n) de cada linha
                                                                                           # for linha in linhas - Itera sobre cada linha do arquivo (armazenada em 'linhas')
[10]     print("Interfaces encontradas:")                                                  # Imprime cabeçalho para organizar a saída
[11]     for interface in interfaces:                                                      # Loop para processar cada item da lista 'interfaces':
[12]         print(interface)                                                              # print(interface) - Imprime cada configuração de interface encontrada

Bloco 4: Finalização Obrigatória (finally)


[13] finally:                                                                               # Sempre executa, com ou sem erros
[14]     print("Leitura concluída.")                                                        # Mensagem final (útil para logs)
```

Por Que Usar else e finally Juntos?

   - else: Separa a lógica de sucesso do tratamento de erros (código mais limpo).

   - finally: Garante ações finais (ex.: logs, fechar conexões externas).

### Exemplo 03: Adicionar Configurações a um Arquivo Existente.

Objetivo: Adicionar uma nova VLAN ao arquivo roteador.txt sem apagar o conteúdo atual.

**adicionar_vlan.py**  

```Python
[01] nova_config = 'vlan 10\n  name VLAN_GESTAO\n'
[02] try:
[03]    with open('roteador.txt', 'a') as arquivo:
[04]        arquivo.write('\n' + nova_config)
[05] except PermissionError:
[06]     print("Erro: Sem permissão para modificar o arquivo!")
[07] except IOError as e:
[08]     print(f"Erro ao escrever no arquivo: {e}")
[09] else:
[10]     print("Configuração adicionada com sucesso!")
[11] finally:
[12]     print("Processo finalizado.")
```

**Saída no arquivo (atualizado):**

```Bash
alcancil@linux:~/automacoes/erros/txt/03$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/txt/03$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/erros/txt/03$ python3 
adicionar_vlan.py  venv/              
(venv) alcancil@linux:~/automacoes/erros/txt/03$ python3 adicionar_vlan.py 
Configuração adicionada com sucesso!
Processo finalizado.
```

**Saída com erro**

```Bash
(venv) alcancil@linux:~/automacoes/erros/txt/03$ sudo chmod -wrwr roteador.txt 
chmod: roteador.txt: as novas permissões são ----w----, e não ---------
(venv) alcancil@linux:~/automacoes/erros/txt/03$ python3 adicionar_vlan.py 
Erro: Sem permissão para modificar o arquivo!
Processo finalizado.
(venv) alcancil@linux:~/automacoes/erros/txt/03$ 
```

**Explicação:**  
```Python
Bloco 1: Preparação da Configuração

[01] nova_config = 'vlan 10\n  name VLAN_GESTAO\n'              # Define a configuração da VLAN (10) em formato texto. \n = quebra de linha (formatação Cisco)
                                                    
Bloco 2: Tentativa de Escrita no Arquivo (try)

[02] try:                                                       # Inicia o bloco de tratamento de erros
[03]    with open('roteador.txt', 'a') as arquivo:              # Abre o arquivo em modo APPEND ('a')
[04]        arquivo.write('\n' + nova_config)                   # Adiciona a nova_config após uma quebra de linha

Bloco 3: Tratamento de Erros (except)

[05] except PermissionError:                                     # Captura erro de permissão (ex.: arquivo só-leitura)
[06]     print("Erro: Sem permissão para modificar o arquivo!")  # Mensagem amigável
[07] except IOError as e:                                        # Captura outros erros de E/S (ex.: disco cheio)
[08]     print(f"Erro ao escrever no arquivo: {e}")              # Exibe detalhes do erro (armazenado em 'e')

Bloco 4: Execução em Caso de Sucesso (else)

[09] else:                                                       # Executa apenas se NÃO houver erros no 'try'
[10]     print("Configuração adicionada com sucesso!")           # Confirmação de sucesso

Bloco 5: Finalização Obrigatória (finally)

[11] finally:                                                    # Sempre executa, com ou sem erros
[12]     print("Processo finalizado.")                           # Mensagem final (útil para logs)
```
 
### Exemplo 4: Caminhos locais, identificando o SO (Sistema Operacional)

**caminho.py**

```Python
[01] import os
[02] import platform
[03]
[04] try:
[05]     sistema = platform.system()
[06]     if sistema == "Windows":
[07]         caminho = r"C:\Users\alcancil\Documents\roteador.txt"
[08]     elif sistema == "Linux":
[09]         caminho = "/home/alcancil/automacao/roteador.txt"
[10]     else:
[11]         raise OSError("Sistema operacional não suportado.")
[12] 
[13]     if not os.path.exists(caminho):
[14]         raise FileNotFoundError(f"Arquivo {caminho} não existe.")
[15]
[16]     print(f"Caminho válido no {sistema}: {caminho}")
[18]
[19] except (FileNotFoundError, PermissionError) as e:
[20]     print(f"Erro de acesso: {e}")
[21] except OSError as e:
[22]     print(f"Erro de sistema: {e}")
[23] else:
[24]     print("Pronto para manipular o arquivo!")
```

**Saída**  

```Bash
alcancil@linux:~/automacoes/erros/txt/04$ python3 -m venv venv
alcancil@linux:~/automacoes/erros/txt/04$ python3 caminho.py 
Caminho válido no Linux: /home/alcancil/automacoes/erros/txt/04/roteador.txt
Pronto para manipular o arquivo!
alcancil@linux:~/automacoes/erros/txt/04$ 
```

**Saída com erro**

```Bash
alcancil@linux:~/automacoes/erros/txt/04$ python3 caminho.py 
Erro de acesso: Arquivo /home/alcancil/automacao/roteador.txt não existe.
```

---
Arrumar

**Explicação:**

```Python
Bloco 1 – Importações

[01] import os                                                                  # Importa o módulo 'os' para interagir com o sistema de arquivos
[02] import platform                                                            # Importa 'platform' para detectar o sistema operacional

Bloco 2 – Bloco try: identificação do sistema e definição do caminho

[04] try:                                                                       # Inicia o bloco de tratamento de erros
[05]     sistema = platform.system()                                            # Detecta o sistema operacional atual (ex: "Windows", "Linux", "Darwin")
[06]     if sistema == "Windows":                                               # Se o sistema for Windows...
[07]         caminho = r"C:\Users\alcancil\Documents\roteador.txt"              # Define o caminho com sintaxe Windows (raw string)
[08]     elif sistema == "Linux":                                               # Se for Linux...
[09]         caminho = "/home/alcancil/automacoes/erros/txt/04/roteador.txt"    # Define caminho no padrão de arquivos do Linux
[10]     else:                                                                  # Qualquer outro sistema (ex: macOS, Unix, etc.)
[11]         raise OSError("Sistema operacional não suportado.")                # Lança exceção se o sistema não for suportado

Bloco 3 – Verifica se o arquivo existe

[13]     if not os.path.exists(caminho):                                        # Verifica se o caminho existe no sistema de arquivos
[14]         raise FileNotFoundError(f"Arquivo {caminho} não existe.")          # Lança erro se o arquivo não for encontrado

Bloco 4 – Confirmação de sucesso

[16]     print(f"Caminho válido no {sistema}: {caminho}")                       # Mostra que o caminho foi localizado com sucesso

Bloco 5 – Tratamento de exceções

[19] except (FileNotFoundError, PermissionError) as e:                          # Captura erros de arquivo não encontrado ou sem permissão
[20]     print(f"Erro de acesso: {e}")                                          # Exibe o erro encontrado
[21] except OSError as e:                                                       # Captura erro de sistema operacional
[22]     print(f"Erro de sistema: {e}")                                         # Exibe mensagem de erro relacionada ao SO

Bloco 6 – Bloco else (sem erros)

[23] else:                                                                      # Executa se nenhum erro tiver ocorrido no bloco try
[24]     print("Pronto para manipular o arquivo!")                              # Confirma que o script pode prosseguir
```

### Boas Práticas

Seja Específico nos **except**:

   - **Evite except**: genérico. Capture FileNotFoundError, PermissionError, etc.

Use **else** para Código de Sucesso:

   - Separe a lógica principal (que depende do try) no bloco else.

   - **finally** para Limpeza:

   - Mesmo que não haja erros, garanta que recursos sejam liberados (ex.: fechar conexões).

Log de Erros:

   - Em scripts reais, use logging em vez de print para registrar falhas.

