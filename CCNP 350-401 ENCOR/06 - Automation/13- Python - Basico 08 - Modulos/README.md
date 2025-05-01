# Python - Básico 09

Agora vamos ver um pouco sobre módulos.

## Módulos

Agora que vimos o que são funções, então sabemos que elas servem para organizar nossos códigos e que podem facilitar a nossa vida uma vez que permitem que parte do nosso código seja reutilizado. Diante disso, vamos imaginar que tenhamos uma coleção de funções. Não seria legal se a gente conseguisse criar essas funções em arquivos separados e que depois, quando formos criar um projeto novo termos como importar essas funções de alguma maneira ? Então aqui podemos chamar isso de módulos.  
Primeiro vamos criar nossas funções dentro de uma estrutura de diretórios que fica assim:  

    /automacoes
    │── main.py
    │── ping_utils.py
    │── ssh_utils.py

***Módulo 1: ping.py***

Aqui estamos criando um arquivo com uma função que vai testar se um host vai responder a um ping. No nosso caso estaremos utilizando o endereço do dns público do google como exemplo. Caso ele responda ao ping, nossa função responde com **True** na tela.  

```Python

    [01] # ping.py
    [02] import os
    [03]
    [04] def testar_ping(ip):
    [06]    """
    [07]    Testa conectividade com um IP via ping.
    [08]    Retorna True se o host responder.
    [09]    """
    [10]    resposta = os.system(f"ping -n 1 {ip} > nul" if os.name == 'nt' else f"ping -c 1 {ip} > /dev/null")
    [11]    return resposta == 0
    [12]
    [13] if __name__ == "__main__":
    [14]    # Teste local do módulo
    [15]    print(testar_ping("8.8.8.8"))  # Só executa se rodar este arquivo diretamente
```

Veja, agora eu posso executar diretamente nosso código chamando o próprio interpretador uma vez que salvamos o arquivo com a extensão **.py**

```Bash
    alcancil@linux:~/automacoes$ python3 ping.py
    True
    alcancil@linux:~/automacoes$ 
```
Nesse código podemos notar algumas coisas interessantes. Na linha [02] temos **import os**. Isso quer dizer que estamos importando a biblioteca **os** inteira e que a partir de agora podemos desfrutar de todas as suas funcionalidades.  
Na linha [04] começamos nossa função testar_ping que vai até a linha [11], ou seja, nossa função somente irá realizar os comandos das linhas [10] e [11]. Mas e o que essas linhas fazem ?  
Vou dividir a linha [10] em algumas partes para facilitar o entendimento. Primeiro a variável **resposta** vai guardar o resultado de os.system(). Bom como dito antes, .system é uma funcionalidade da biblioteca os que foi desenvolvida pela comunidade. É nessa parte que podemos executar o comando ping pois o os.system é que nos habilita o comando ping. Porém como não sabemos em que sistema iremos executar o comando **ping**, que é o mesmo em Windows / Linux / Mac mas com algumas diferenças, vamos ter uma estrutura de **if** e **else** para fazer esse teste. Então começamos comando: **f"ping -n 1 {ip} > nul"**, ou seja, vamos realizar um único ping para o host **{ip}**, e como iremos fornecer o valor e queremos guardar esse valor em uma string, então utilizamos o **f string**. Porém vamos redirecionar o resultado do ping para **> null**, ou seja o ping não irá mostrar resultado nenhum na tela.  
Mas, como dito, como vamos saber em que sistema operacional estamos ? Simples, utilizamos **os.name** que nos permite verificar o sistema. Então a lógica fica: execute o comando anterior **(f"ping -n 1 {ip} > nul")** se o nome do sistema for **nt** senão execute o comando **f"ping -c 1 {ip} > /dev/null"**.  
Logo após retornamos resposta == 0. Mas quando rodamos **os.system("comando")**, o Python executa o comando no terminal/shell do sistema operacional e retorna **0**, se conseguir executar o comando, ou **1** se não conseguir executar o ping. Então, como ele trabalha com o conceito de **True or False**,  resposta == 0 compara com o resultado do ping e se ambos forem 0, é porque o host está online e acessível. Se o resultado de ping for 1 e a variável resultado é sempre 0 então o resultado e **False**  

**Módulo 2: ssh.py**

Agora vamos criar as nossas funções para simular uma conexão SSH.  

```Python
    [01] # ssh.py
    [02] def conectar_dispositivo(ip, usuario, senha):
    [03]    """
    [04]    Simula conexão SSH a um dispositivo de rede.
    [05]    Em um cenário real, usaria netmiko/paramiko.
    [06]    """
    [07]    print(f"Conectando a {ip} como {usuario}... (simulação)")
    [08]    return {"ip": ip, "status": "conectado"}  # Retorna um dicionário simulando uma conexão
    [09]
    [10] def executar_comando(conexao, comando):
    [11]    """Simula a execução de um comando remoto"""
    [12]    print(f"Executando: '{comando}' no dispositivo {conexao['ip']}")
    [13]    return f"Saída do comando '{comando}'"
    [14]
    [15] if __name__ == "__main__":
    [16]    # Teste local
    [17]    conexao = conectar_dispositivo("192.168.1.1", "admin", "senha123")
    [18]    print(executar_comando(conexao, "show ip interface brief"))
```
Como na função anterior, podemos executar diretamente nosso arquivo que salvamos como **ssh.py**

```Bash
    alcancil@linux:~/automacoes$ python3 ssh.py 
    Conectando a 192.168.1.1 como admin... (simulação)
    Executando: 'show ip interface brief' no dispositivo 192.168.1.1
    Saída do comando 'show ip interface brief'
    alcancil@linux:~/automacoes$ 
```

Agora vamos nos atentar na linha [15] if __name__ == "__main__":  
if __name__ == "__main__": é uma condição que verifica se o módulo (arquivo Python) está sendo executado diretamente ou se está sendo importado por outro módulo.  

**Como funciona?**

    __name__ é uma variável especial que Python define automaticamente para cada módulo:

        Quando um arquivo Python é executado diretamente, __name__ é definido como "__main__"
        Quando um arquivo é importado como módulo, __name__ recebe o nome do arquivo (sem a extensão .py)

Ou seja, o código dentro deste bloco só será executado quando o arquivo for rodado diretamente, não quando for importado.  

**Criar o Arquivo Principal (main.py)**

Agora que criamos nossos módulos, podemos importá-los dentro de um arquivo. Por convenção, temos o arquivo chamado de **main.py**. Esse é o arquivo principal. Então a ideia é que estamos desenvolvendo um programa / script e queremos utilizar algumas funções que já criamos antes. Porém essas funções estão nesses outros arquivos que criamos nos passos anteriores.  
Percebam as vantagens, isso irá organizar nosso código e nos permite reutilizar essas funções em forma de módulos em outros programas.  

```Python
    [01] # main.py
    [02] from ping import testar_ping
    [03] from ssh import conectar_dispositivo, executar_comando
    [04] 
    [05] # Usando as funções dos módulos
    [06] ips = ["192.168.1.1", "8.8.8.8", "10.0.0.1"]
    [07]
    [08] for ip in ips:
    [08]    if testar_ping(ip):
    [09]        print(f"\n{ip} está respondendo ao ping")
    [10]        conexao = conectar_dispositivo(ip, "admin", "senha123")
    [11]        saida = executar_comando(conexao, "show running-config")
    [12]        print(f"Saída do dispositivo:\n{saida}")
    [13]    else:
    [15]        print(f"\n{ip} inacessível")
```

Agora para executarmos nossa aplicação, iremos executar somente o arquivo **main.py** . Esse arquivo que irá disparar as funções contidas em nossos módulos.  

```Bash
    alcancil@linux:~/automacoes$ python3 main.py 

    192.168.1.1 inacessível

    8.8.8.8 está respondendo ao ping
    Conectando a 8.8.8.8 como admin... (simulação)
    Executando: 'show running-config' no dispositivo 8.8.8.8
    Saída do dispositivo:
    Saída do comando 'show running-config'

    10.0.0.1 inacessível
    alcancil@linux:~/automacoes$
```

Lembram que na primeira parte fomos importar a biblioteca os ? Então utilizamos **import os**. Nesse caso importamos todas as funções da biblioteca os. Mas e nessas linhas:

```Python
    [02] from ping import testar_ping
    [03] from ssh import conectar_dispositivo, executar_comando
```
Certo, aqui estamos dizendo assim: **do módulo x importe a função z**, ou sejam como no nosso caso do módulo ssh, temos mais de uma função. Aqui nós importamos todas as funções presentes nesse módulo. Mas e se formos utilizar uma função ? Dessa maneira podemos importar somente a(s) função(ões) que precisamos reduzindo o consumo de cpu.<br></br>

Como podemos observar, essa abordagem traz várias vantagens:

* realizar testes individuais nos módulos
* manutenção melhorada. Se mais de uma pessoa precisar trabalhar com essa estrutura, cada um pode ficar responsável por partes dos códigos.  
* reaproveitamento dos módulos em outros projetos
* clareza e organização do código principal 

Próximo Passo (Opcional)

Transforme esses módulos em uma biblioteca local:

    Crie uma pasta chamada ferramentas_rede.

    Adicione um arquivo vazio __init__.py dentro dela.

    Mova ping_utils.py e ssh_utils.py para essa pasta.

    No main.py, importe assim:
    python

from ferramentas_rede.ping_utils import testar_ping
from ferramentas_rede.ssh_utils import conectar_dispositivo