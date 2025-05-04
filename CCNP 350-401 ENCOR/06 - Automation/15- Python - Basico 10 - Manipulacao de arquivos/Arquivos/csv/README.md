# Python - Básico 10

## 01 Manipulação de arquivos - .csv

Arquivos **.csv** são utilizados em diversos casos como:  

1. Inventário de dispositivos de rede  
2. Backup de configurações em massa  
3. Processamento de Logs estruturados  
4. Integração com ferramentas de automação  
5. Exportação de dados de APIs  
6. Comparação de dados (Antes/Depois)  

Quando Escolher CSV em vez de TXT?  

| Vantagens do CSV                                                  | Use TXT quando                                     |
|-------------------------------------------------------------------|----------------------------------------------------|
| Estrutura clara (colunas/linhas).                                 | Os dados são não estruturados (ex.: logs brutos).  |
| Facilidade de importação em Excel, bancos de dados e ferramentas. |  Não há necessidade de divisão por colunas.        |
| Suporte nativo em linguagens (Python, PowerShell).                |                                                    |
       
  




















Então vamos olhar alguns exemplos práticos para ver como eles funcionam na prática. <br></br>

**Exemplo 1:** Criar e Escrever em um Arquivo .txt (Básico)

Objetivo: Criar um arquivo chamado roteador.txt e salvar uma configuração simples.

```Python
    [01] # Abre o arquivo em modo de escrita ('w')
    [02] with open('roteador.txt', 'w') as arquivo:
    [03]    arquivo.write('hostname R1\n')
    [04]    arquivo.write('interface GigabitEthernet0/1\n')
    [05]    arquivo.write('  description Link para Core\n')
    [06]
    [07] print("Arquivo 'roteador.txt' criado com sucesso!")
```

**Execução do script**

```Bash
    alcancil@linux:~/automacoes/arquivos$ python3 arquivos01.py 
    Arquivo 'roteador.txt' criado com sucesso!
    alcancil@linux:~/automacoes/arquivos$ 
```

**Conteúdo no arquivo**

```Bash
    hostname R1
    interface GigabitEthernet0/1
      description Link para Core
```

Esse exemplo cria um arquivo **.txt** com textos dentro dele. Vamos analisar a linha: <br></br>
     
     [02] with open('roteador.txt', 'w') as arquivo: 

Então temos a estrutura : **with open()**. Aqui cabe dizer que para criarmos o nosso arquivo somente é preciso o método **open()**. Mas vamos imaginar a seguinte situação, para criar o arquivo, ou mesmo para ler o arquivo, precisamos abrir o arquivo temporariamente. Mas e se algo acontece e nosso script encerra abruptamente no meio do processo ?  
Ocorre que se executarmos o nosso script novamente podemos ter algum tipo de erro. Isso ocorre porque o arquivo pode ter permanecido em estado de aberto e ao tentarmos abri-lo novamente vamos receber um erro. Então o método **with open()** pode ser lido: "com o arquivo aberto faça()", ou seja, isso garante que o arquivo seja sempre seja fechado. <br></br>

**sintaxe: open(arquivo, modo)**  <br></br>

| PARÂMETRO   | DESCRIÇÃO                                                                                                          |
|-------------|:-------------------------------------------------------------------------------------------------------------------|
|**arquivo**  | Caminho e (ou) nome do arquivo                                                                                     | 
| **modo**    | **r - Read** . Modo padrão. Abre um arquivo para leitura, porém irá dar um erro se o arquivo não existir           |
|             | **a - Append** . Abre o arquivo no modo appending, ou seja, adiciona no arquivo. Cria o arquivo se ele não existir |
|             | **w - Write** . Abre o arquivo no modo escrita. Também cria o arquivo se ele não existir                           |
|             | **x - Create** . Cria o arquivo especificado. Retorna um erro se o arquivo existir                                 |
|             | **t - Text** . Especifica o modo do arquivo como texto. Já é o modo padrão                                         |
|             | **b - Binary** . Especifica o modo do arquivo como binário. Uso em imagens, por exemplo                            |

**OBS:** **\n** em Python significa Enter, ou manda pular uma linha. <br></br>

**Exemplo 2:** Ler o arquivo roteador.txt e extrair apenas as linhas que contêm "interface".

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

Saída no terminal:

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

**Linha [01]:** abre o arquivo roteador.txt, no modo leitura e coloca o conteúdo a variável **arquivo**  
**Linha [02]:** aqui utilizamos o método **arquivo.readlines()** . Isso é feito para ler todas as linhas do arquivo.  
**Linha [06]:** aqui vamos quebrar a explicação em partes:  
&nbsp; &nbsp; &nbsp; &nbsp; - **linha.strip():** Remove espaços em branco e quebras de linha (\n) do início/fim de cada linha.  
&nbsp; &nbsp; &nbsp; &nbsp; - **for linha in linhas**: aqui temos uma iteração, ou seja, vamos percorrer todas as linhas  
&nbsp; &nbsp; &nbsp; &nbsp; - **if 'interface' in linha.lower()**: isso torna a busca da palavra interface em Case-Sensitive, ou seja, **linha.lower()** transforma a palavra interfaces em minusculas.  
    

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

Saída no arquivo (atualizado):

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

**Linha [01]:** Aqui importamos a biblioteca **os** para podermos utilizar a função **path()** e outras funções de sistema.  
**Linha [02]:** Aqui importamos a biblioteca **plataform** para podermos utilizar suas funções e identificar os sistemas.  
**Linha [05]:** A variável **sistema** recebe a função **plataform.system()**. Aqui é que reconhecemos o sistema operacional.  
**Linha [08]:** Aqui começamos a lógica do if, se o sistema operacional for **Windows** então:  
**Linha [09]:** a variável **caminho** recebe o caminho. Isso mesmo, nessa abordagem temos que indicar o caminho aqui.  
**Linha [10]:** Se a variável **sistema** for **Linux**  
**Linha [11]:** a variável **caminho** recebe o caminho. Digite o caminho aqui.  
**Linha [12]:** senão  
**Linha [13]:** imprima : "Sistema não suportado!"  
**Linha [14]:** sai do script  
**Linha [16]:** Imprime o nome do sistema e o caminho do arquivo  
**Linha [19]:** Aqui iniciamos a lógica se o caminho do os existir  
**Linha [20]:** Imprima "Arquivo encontrado!"  
**Linha [21]:** senão  
**Linha [22]:** Imprima "Arquivo não existe!"  