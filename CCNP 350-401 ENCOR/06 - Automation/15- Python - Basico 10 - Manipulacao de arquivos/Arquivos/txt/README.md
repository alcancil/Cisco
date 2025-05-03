# Python - Básico 10

## 01 Manipulação de arquivos - .txt

Bom vamos começar pelo básico. Arquivos .txt, em automação de redes, são utilizados para casos mais básicos como:  

1. Para Configurações Simples de Dispositivos
2. Logs de Sistemas ou Dispositivos
3. Armazenar Saídas de Comandos para Análise

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
**Linha [06]:** aqui vamos quebrar a explicação em partes:  <br></br>
           &NBSP **linha.strip():** Remove espaços em branco e quebras de linha (\n) do início/fim de cada linha.  
            **for linha in linhas** aqui temos uma iteração, ou seja, vamos percorrer todas as linhas  
            **if 'interface' in linha.lower()** isso torna a busca da palavra interface em Case-Sensitive, ou seja, **linha.lower()** transforma a palavra interfaces em minusculas.  
    




📌 Exemplo 3: Adicionar Configurações a um Arquivo Existente (Intermediário)

Objetivo: Adicionar uma nova VLAN ao arquivo roteador.txt sem apagar o conteúdo atual.
python

# Nova configuração para adicionar
nova_config = 'vlan 10\n  name VLAN_GESTAO\n'

# Abre o arquivo em modo append ('a')
with open('roteador.txt', 'a') as arquivo:
    arquivo.write('\n' + nova_config)

print("Configuração de VLAN adicionada ao arquivo!")

Saída no arquivo (atualizado):

hostname R1
interface GigabitEthernet0/1
  description Link para Core

vlan 10
  name VLAN_GESTAO

Explicação:

    open(..., 'a'): Modo append adiciona conteúdo ao final do arquivo sem sobrescrever.

🎯 Como Isso se Aplica à Automação de Redes?

    Backup de Configurações: Salvar o output de show running-config em .txt.

    Processamento de Logs: Filtrar linhas de arquivos de log (ex.: %LINK-3-UPDOWN).

    Atualização Incremental: Adicionar novas configurações a arquivos existentes.

Próximo Passo (Desafio Opcional)

Que tal modificar o Exemplo 2 para ler um log de switch e extrair todas as mensagens de erro? Exemplo:
python

with open('switch_log.txt', 'r') as arquivo:
    erros = [linha.strip() for linha in arquivo if '%ERROR' in linha]