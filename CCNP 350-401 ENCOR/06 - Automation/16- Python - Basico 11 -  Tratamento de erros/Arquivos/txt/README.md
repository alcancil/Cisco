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

```Python

   [01] # Abre o arquivo em modo leitura ('r')
   [02] with open('roteador.txt', 'r') as arquivo:
   [03]     linhas = arquivo.readlines()  # Lê todas as linhas
   [04]
   [05] # Filtra linhas com "interface"
   [06] interfaces = [linha.strip() for linha in linhas if 'interface' in linha.lower()]
   [07]
   [08] print("Interfaces encontradas:")
   [09] for interface in interfaces:
   [10]     print(interface)
```

**Saída no terminal:**

```Bash
    alcancil@linux:~/automacoes/arquivos/02$ python3 arquivo.py 
    Traceback (most recent call last):
      File "/home/alcancil/automacoes/arquivos/02/arquivo.py", line 2, in <module>
        with open('roteador.txt', 'r') as arquivo:
             ^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'roteador.txt'
    alcancil@linux:~/automacoes/arquivos/02$ 
```
Podemos perceber que ao executar o arquivo recebemos um erro. Isso acontece pois não temos o arquivo **"roteador.txt"** . Então vamos criar o arquivo com conteúdo dentro e depois executar o script para ver a diferença. <br></br>

```Bash
    alcancil@linux:~/automacoes/arquivos/02$ python3 arquivo.py 
    Interfaces encontradas:
    interface GigabitEthernet0/1
    interface GigabitEthernet0/2
    interface GigabitEthernet0/3
    alcancil@linux:~/automacoes/arquivos/02$ 
```

**Explicação:**

```Bash
    Linha [01]: abre o arquivo roteador.txt, no modo leitura e coloca o conteúdo a variável **arquivo**  
    Linha [02]: aqui utilizamos o método **arquivo.readlines()** . Isso é feito para ler todas as linhas do arquivo.  
    Linha [06]: aqui vamos quebrar a explicação em partes:  
                - **linha.strip():** Remove espaços em branco e quebras de linha (\n) do início/fim de cada linha.  
                - **for linha in linhas**: aqui temos uma iteração, ou seja, vamos percorrer todas as linhas  
                - **if 'interface' in linha.lower()**: isso torna a busca da palavra interface em Case-Sensitive, ou seja, **linha.lower()** transforma a palavra interfaces em minusculas.  
```

**Exemplo 3:** Adicionar Configurações a um Arquivo Existente.

Objetivo: Adicionar uma nova VLAN ao arquivo roteador.txt sem apagar o conteúdo atual.

```Python
    # Nova configuração para adicionar
    nova_config = 'vlan 10\n  name VLAN_GESTAO\n'

    # Abre o arquivo em modo append ('a')
    with open('roteador.txt', 'a') as arquivo:
        arquivo.write('\n' + nova_config)

    print("Configuração de VLAN adicionada ao arquivo!")
```

**Saída no arquivo (atualizado):**

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