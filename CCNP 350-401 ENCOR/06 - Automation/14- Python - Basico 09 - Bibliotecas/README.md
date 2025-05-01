# Python - Básico 08

Agora vamos ver um pouco sobre módulos.

## Módulos

Agora que vimos o que são funções, então sabemos que elas servem para organizar nossos códigos e que podem facilitar a nossa vida uma vez que permitem que parte do nosso código seja reutilizado. Diante disso, vamos imaginar que tenhamos uma coleção de funções. Não seria legal se a gente conseguisse criar essas funções em arquivos separados e que depois, quando formos criar um projeto novo termos como importar essas funções de alguma maneira ? Então aqui podemos chamar isso de módulos.  
Primeiro vamos criar nossas funções dentro de uma estrutura de diretórios que fica assim:  

    /automatizacao_rede
    │── main.py
    │── ping_utils.py
    │── ssh_utils.py

Passo 1: Criar os Módulos
Módulo 1: ping_utils.py

(Funções para teste de conectividade)
python

# ping_utils.py
import os

def testar_ping(ip):
    """
    Testa conectividade com um IP via ping.
    Retorna True se o host responder.
    """
    resposta = os.system(f"ping -n 1 {ip} > nul" if os.name == 'nt' else f"ping -c 1 {ip} > /dev/null")
    return resposta == 0

if __name__ == "__main__":
    # Teste local do módulo
    print(testar_ping("8.8.8.8"))  # Só executa se rodar este arquivo diretamente

Módulo 2: ssh_utils.py

(Funções para conexão SSH - simulado sem bibliotecas externas)
python

# ssh_utils.py
def conectar_dispositivo(ip, usuario, senha):
    """
    Simula conexão SSH a um dispositivo de rede.
    Em um cenário real, usaria netmiko/paramiko.
    """
    print(f"Conectando a {ip} como {usuario}... (simulação)")
    return {"ip": ip, "status": "conectado"}  # Retorna um dicionário simulando uma conexão

def executar_comando(conexao, comando):
    """Simula a execução de um comando remoto"""
    print(f"Executando: '{comando}' no dispositivo {conexao['ip']}")
    return f"Saída do comando '{comando}'"

if __name__ == "__main__":
    # Teste local
    conexao = conectar_dispositivo("192.168.1.1", "admin", "senha123")
    print(executar_comando(conexao, "show ip interface brief"))

Passo 2: Criar o Arquivo Principal (main.py)
python

# main.py
from ping_utils import testar_ping
from ssh_utils import conectar_dispositivo, executar_comando

# Usando as funções dos módulos
ips = ["192.168.1.1", "8.8.8.8", "10.0.0.1"]

for ip in ips:
    if testar_ping(ip):
        print(f"\n✅ {ip} está respondendo ao ping")
        conexao = conectar_dispositivo(ip, "admin", "senha123")
        saida = executar_comando(conexao, "show running-config")
        print(f"Saída do dispositivo:\n{saida}")
    else:
        print(f"\n❌ {ip} inacessível")

Passo 3: Estrutura de Arquivos

Certifique-se de que os arquivos estejam no mesmo diretório:

/automatizacao_rede
│── main.py
│── ping_utils.py
│── ssh_utils.py

Como Executar?

    Salve os 3 arquivos na mesma pasta.

    Execute o arquivo principal:
    bash

    python main.py

Saída Esperada (Exemplo):

❌ 192.168.1.1 inacessível

✅ 8.8.8.8 está respondendo ao ping
Conectando a 8.8.8.8 como admin... (simulação)
Executando: 'show running-config' no dispositivo 8.8.8.8
Saída do dispositivo:
Saída do comando 'show running-config'

❌ 10.0.0.1 inacessível

Explicação Chave

    Módulos:

        São arquivos .py independentes com funções específicas.

        Podem ser testados individualmente (veja os blocos if __name__ == "__main__").

    Importação no main.py:

        Use from modulo import função para trazer apenas o necessário.

        Funções de diferentes módulos trabalham juntas no arquivo principal.

    Vantagens para Automação de Redes:

        Organização: Separa lógicas distintas (ping vs. SSH).

        Reuso: Os mesmos módulos podem ser usados em outros scripts.

        Manutenção: Corrija/atualize um módulo sem afetar os outros.

Próximo Passo (Opcional)

Transforme esses módulos em uma biblioteca local:

    Crie uma pasta chamada ferramentas_rede.

    Adicione um arquivo vazio __init__.py dentro dela.

    Mova ping_utils.py e ssh_utils.py para essa pasta.

    No main.py, importe assim:
    python

from ferramentas_rede.ping_utils import testar_ping
from ferramentas_rede.ssh_utils import conectar_dispositivo