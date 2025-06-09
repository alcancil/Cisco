# Python - Básico 10

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

---
ARRUMAR

### Exemplo 2: Ler o arquivo roteador.txt e extrair apenas as linhas que contêm "interface".

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

**Exemplo 3:** Adicionar Configurações a um Arquivo Existente.

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

---
Arrumar


```Bash
    alcancil@linux:~/automacoes/arquivos/03$ python3 arquivo.py 
    Configuração de VLAN adicionada ao arquivo!
    alcancil@linux:~/automacoes/arquivos/03$ ls -la
    total 16
    drwxrwxr-x 2 alcancil alcancil 4096 mai  3 16:59 .
    drwxrwxr-x 5 alcancil alcancil 4096 mai  3 16:58 ..
    -rw-r--r-- 1 root     root      257 mai  3 16:59 arquivo.py
    -rw-rw-r-- 1 alcancil alcancil   28 mai  3 16:59 roteador.txt
    alcancil@linux:~/automacoes/arquivos/03$ cat roteador.txt 

    vlan 10
      name VLAN_GESTAO
    alcancil@linux:~/automacoes/arquivos/03$
```

**Explicação:**

    open(..., 'a'): Modo append adiciona conteúdo ao final do arquivo sem sobrescrever.  

**Exemplo 3:** Caminhos locais, identificando o SO (Sistema Operacional)

```Python

    [01] import os
    [02] import platform
    [03]
    [04] # Identifica o SO
    [05] sistema = platform.system()
    [06]
    [07] # Exemplo de caminhos locais
    [08] if sistema == "Windows":
    [09]    caminho = r"C:\Users\alcancil\Documents\roteador.txt"  # Raw string (evita conflitos com \)
    [10] elif sistema == "Linux":
    [11]    caminho = "/home/seuusuario/automacao/roteador.txt"
    [12] else:
    [13]    print("Sistema não suportado!")
    [14]    exit()
    [15]
    [16] print(f"Caminho no {sistema}: {caminho}")
    [17]
    [18] # Verifica se o arquivo existe
    [19] if os.path.exists(caminho):
    [20]    print("Arquivo encontrado!")
    [21] else:
    [22]    print("Arquivo não existe.")

Saída no Linux: 

```Bash
    alcancil@linux:~/automacoes/arquivos/04$ python3 arquivo.py 
    Caminho no Linux: /home/alcancil/automacoes/arquivos/04
    Arquivo encontrado!
    alcancil@linux:~/automacoes/arquivos/04$ 
```

Saída no Windows:

```Bash
    Caminho no Windows: C:\Users\alcancil\Documents\roteador.txt
    Arquivo encontrado!
```

**Explicação:**

```Bash

    Linha [01]: Aqui importamos a biblioteca os para podermos utilizar a função path() e outras funções de sistema.  
    Linha [02]: Aqui importamos a biblioteca plataform para podermos utilizar suas funções e identificar os sistemas.  
    Linha [05]: A variável sistema recebe a função plataform.system(). Aqui é que reconhecemos o sistema operacional.  
    Linha [08]: Aqui começamos a lógica do if, se o sistema operacional for Windows então:  
    Linha [09]: a variável caminho recebe o caminho. Isso mesmo, nessa abordagem temos que indicar o caminho aqui.  
    Linha [10]: Se a variável sistema for Linux  
    Linha [11]: a variável caminho recebe o caminho. Digite o caminho aqui.  
    Linha [12]: senão  
    Linha [13]: imprima : "Sistema não suportado!"  
    Linha [14]: sai do script  
    Linha [16]: Imprime o nome do sistema e o caminho do arquivo  
    Linha [19]: Aqui iniciamos a lógica se o caminho do os existir  
    Linha [20]: Imprima "Arquivo encontrado!"  
    Linha [21]: senão  
    Linha [22]: Imprima "Arquivo não existe!"  
```






















---
ARRUMAR

Exemplo 3: Adicionar Configurações (Modo 'a')
python

nova_config = 'vlan 10\n  name VLAN_GESTAO\n'
try:
    with open('roteador.txt', 'a') as arquivo:
        arquivo.write('\n' + nova_config)
except PermissionError:
    print("Erro: Sem permissão para modificar o arquivo!")
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")
else:
    print("Configuração adicionada com sucesso!")
finally:
    print("Processo finalizado.")

Exemplo 4: Verificar Caminhos Multiplataforma
python

import os
import platform

try:
    sistema = platform.system()
    if sistema == "Windows":
        caminho = r"C:\Users\alcancil\Documents\roteador.txt"
    elif sistema == "Linux":
        caminho = "/home/alcancil/automacao/roteador.txt"
    else:
        raise OSError("Sistema operacional não suportado.")

    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo {caminho} não existe.")

    print(f"Caminho válido no {sistema}: {caminho}")

except (FileNotFoundError, PermissionError) as e:
    print(f"Erro de acesso: {e}")
except OSError as e:
    print(f"Erro de sistema: {e}")
else:
    print("Pronto para manipular o arquivo!")

1. Boas Práticas

    Seja Específico nos except:

        Evite except: genérico. Capture FileNotFoundError, PermissionError, etc.

    Use else para Código de Sucesso:

        Separe a lógica principal (que depende do try) no bloco else.

    finally para Limpeza:

        Mesmo que não haja erros, garanta que recursos sejam liberados (ex.: fechar conexões).

    Log de Erros:

        Em scripts reais, use logging em vez de print para registrar falhas.

