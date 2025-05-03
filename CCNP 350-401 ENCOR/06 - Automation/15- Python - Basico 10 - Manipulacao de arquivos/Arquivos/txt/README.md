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
    # Abre o arquivo em modo de escrita ('w')
    with open('roteador.txt', 'w') as arquivo:
        arquivo.write('hostname R1\n')
        arquivo.write('interface GigabitEthernet0/1\n')
        arquivo.write('  description Link para Core\n')

    print("Arquivo 'roteador.txt' criado com sucesso!")
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

Explicação:

    open('roteador.txt', 'w'): Abre o arquivo em modo escrita (se existir, será sobrescrito).

    with: Garante que o arquivo seja fechado automaticamente.

📌 Exemplo 2: Ler um Arquivo .txt e Filtrar Linhas (Intermediário)

Objetivo: Ler o arquivo roteador.txt e extrair apenas as linhas que contêm "interface".
python

# Abre o arquivo em modo leitura ('r')
with open('roteador.txt', 'r') as arquivo:
    linhas = arquivo.readlines()  # Lê todas as linhas

# Filtra linhas com "interface"
interfaces = [linha.strip() for linha in linhas if 'interface' in linha.lower()]

print("Interfaces encontradas:")
for interface in interfaces:
    print(interface)

Saída no terminal:

Interfaces encontradas:
interface GigabitEthernet0/1

Explicação:

    readlines(): Retorna uma lista com todas as linhas do arquivo.

    List comprehension: Filtra linhas que contêm a palavra "interface".

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