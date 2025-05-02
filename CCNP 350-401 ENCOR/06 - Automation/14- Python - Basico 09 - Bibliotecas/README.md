# Python - Básico 09

## Bibliotecas

Agora vamos ver um conceito parecido com os módulos. As bibliotecas. E o que seria uma biblioteca ?  <br></br>
Basicamente uma biblioteca seria uma coleção de módulos organizados dentro de uma estrutura. Isso acontece pois conforme vamos crescendo os projetos, vamos criando cada vez mais módulos e vamos adicionando ao nosso projeto. Com isso, em projetos maiores e mais complexos acaba que ficamos com uma quantidade grande de módulos (ou funções dentro dos módulos). Então para organização e escalabilidade foram criadas as bibliotecas.  
**OBS:** quando temos uma biblioteca, os nossos módulos passam a ser chamados de pacotes. Estes por sua vez podem ser distribuidos para serem instalados via **pip**  

Quando Usar cada um?  <br></br>

**1. Módulos (Seus Arquivos .py)**

    Use quando:

        * Quiser organizar seu próprio código (ex: separar funções de SSH, ping, backup em arquivos diferentes).

        * Criar ferramentas específicas para sua rede (ex: scan_vlans.py, monitor_bgp.py).
    

**2. Bibliotecas (Pacotes da Comunidade)**

    Use quando:

        * Precisar de funcionalidades complexas já prontas (ex: SSH, APIs REST, parseamento de saídas de comandos Cisco).

        * Quiser evitar reinventar a roda (ex: usar netmiko em vez de implementar SSH manualmente).


# Transformando módulos em bibliotecas


Passo 1: Estrutura de Arquivos

Crie a seguinte estrutura de pastas e arquivos:

```Bash

    /automacoes
    │── main.py                     # Arquivo principal
    │── /ferramentas_rede           # Pasta da biblioteca
    │   │── __init__.py             # Arquivo vazio (transforma a pasta em pacote)
    │   │── ping.py                 # Módulo renomeado (opcional)
    │   │── ssh.py                  # Módulo renomeado (opcional)
```
**__init__.py:** Arquivo vazio que diz ao Python: "Esta pasta é um pacote".
    
Passo 2: Mova e Renomeie os Módulos

    Mova ping.py para ferramentas_rede/ping.py.

    Mova ssh.py para ferramentas_rede/ssh.py.

Passo 3: Atualize o main.py

Agora, importe os módulos como parte da biblioteca ferramentas_rede:

```Python
    # main.py
    from ferramentas_rede.ping import testar_ping
    from ferramentas_rede.ssh import conectar_dispositivo, executar_comando

    # Uso das funções (igual ao anterior, mas agora organizado como biblioteca)
    if testar_ping("8.8.8.8"):
        conexao = conectar_dispositivo("8.8.8.8", "admin", "senha123")
        print(executar_comando(conexao, "show ip interface brief"))
```

**Saída**

```Bash
    alcancil@linux:~/automacoes$ python3 main.py 
    Conectando a 8.8.8.8 como admin... (simulação)
    Executando: 'show ip interface brief' no dispositivo 8.8.8.8
    Saída do comando 'show ip interface brief'
    alcancil@linux:~/automacoes$ 
```

Passo 4: (Opcional) Torne a Biblioteca Instalável

Para usar ferramentas_rede em qualquer lugar do seu sistema (como o netmiko), crie um setup.py:
python

# setup.py
from setuptools import setup

setup(
    name="ferramentas_rede",
    version="0.1",
    packages=["ferramentas_rede"],  # Nome da pasta da biblioteca
    install_requires=[],            # Dependências (ex: "netmiko")
)

Instale a biblioteca em modo desenvolvimento:

```bash
    pip install -e .
```

### Exemplo

* Criando o ambiente virtual

```Bash
    alcancil@linux:~/automacoes$ python3 -m venv redes
    alcancil@linux:~/automacoes$ ls -la
    total 28
    drwxrwxr-x  5 alcancil alcancil 4096 mai  2 13:32 .
    drwxr-x--- 20 alcancil alcancil 4096 mai  2 13:14 ..
    drwxrwxr-x  3 alcancil alcancil 4096 mai  2 13:26 ferramentas_rede
    -rw-rw-r--  1 alcancil alcancil  727 mai  2 13:29 main.py
    drwxrwxr-x  2 alcancil alcancil 4096 mai  1 17:59 __pycache__
    drwxrwxr-x  5 alcancil alcancil 4096 mai  2 13:32 redes
    -rw-rw-r--  1 alcancil alcancil  232 mai  2 13:31 setup.py
```

* Ativando o ambiente  

```Bash
    alcancil@linux:~/automacoes$ source redes/bin/activate
    (redes) alcancil@linux:~/automacoes$
```

* Instalando a biblioteca  

```Bash
    (redes) alcancil@linux:~/automacoes$ pip list
    Package Version
    ------- -------
    pip     24.0
    (redes) alcancil@linux:~/automacoes$
    (redes) alcancil@linux:~/automacoes$ pip install -e .
    Obtaining file:///home/alcancil/automacoes
      Installing build dependencies ... done
      Checking if build backend supports build_editable ... done
      Getting requirements to build editable ... done
      Preparing editable metadata (pyproject.toml) ... done
    Building wheels for collected packages: ferramentas_rede
     Building editable for ferramentas_rede (pyproject.toml) ... done
      Created wheel for ferramentas_rede: filename=ferramentas_rede-0.1-0.editable-py3-none-any.whl size=2719 sha256=ca59d1651026f9db9752363c094f7c181a959009e81c71ac671c1a272aaa80e4
      Stored in directory: /tmp/pip-ephem-wheel-cache-12jvcg0l/wheels/e6/1c/68/53e78c2e777f48ad11d4e67928c2098ecbfe5de2470968c2c7
    Successfully built ferramentas_rede
    Installing collected packages: ferramentas_rede
    Successfully installed ferramentas_rede-0.1
```

* Verificando as bibliotecas instaladas  

```Bash
    (redes) alcancil@linux:~/automacoes$ pip list
    Package          Version Editable project location
    ---------------- ------- -------------------------
    ferramentas_rede 0.1     /home/alcancil/automacoes
    pip              24.0
    (redes) alcancil@linux:~/automacoes$ 
```

**OBS:** o python segue o conceito de código aberto. Com isso, a comunidade se organizou e sempre lança várias bibliotecas que podem ser instaladas através do **pip**. Essas bibliotecas ficam em : **https://pypi.org/** . Então sempre que precisarmos de algo é sempre interessante dar uma pesquisada e verificar se não existe algo pronto que nos ajude.

### Instalar bibliotecas externas:

```Python
    pip install netmiko requests
````
