# Python - Básico 10

## Índice
- [Python - Básico 10](#python---básico-10)
  - [Índice](#índice)
- [05 Manipulação de arquivos – .env](#05-manipulação-de-arquivos--env)
  - [Vantagens de usar arquivos `.env`](#vantagens-de-usar-arquivos-env)
  - [Como usar](#como-usar)
    - [Casos de uso de arquivos .env na automação de redes:](#casos-de-uso-de-arquivos-env-na-automação-de-redes)
    - [Quando usar .env vs outras abordagens](#quando-usar-env-vs-outras-abordagens)
    - [Por que .env é essencial para o CCNP e para automação de redes?](#por-que-env-é-essencial-para-o-ccnp-e-para-automação-de-redes)
    - [Fluxo do uso de .env com Python puro e com Ansible](#fluxo-do-uso-de-env-com-python-puro-e-com-ansible)
    - [Exemplo 01 – Leitura básica do .env com python-dotenv](#exemplo-01--leitura-básica-do-env-com-python-dotenv)
    - [Exemplo 02 – Integração com template Jinja2 usando variáveis do .env](#exemplo-02--integração-com-template-jinja2-usando-variáveis-do-env)
- [Exemplo 02 – Integração com Jinja2 usando variáveis do `.env`](#exemplo-02--integração-com-jinja2-usando-variáveis-do-env)
    - [Exemplo 03 – Simulação de login via .env (sem aplicar)](#exemplo-03--simulação-de-login-via-env-sem-aplicar)
    - [Exemplo 04 – Validação de variáveis faltantes no .env (com os.getenv(..., default))](#exemplo-04--validação-de-variáveis-faltantes-no-env-com-osgetenv-default)

# 05 Manipulação de arquivos – .env

Arquivos `.env` são amplamente utilizados para armazenar **variáveis de ambiente sensíveis**, como:

- Credenciais de acesso (usuário e senha)
- Endereço IP de dispositivos
- Tokens de APIs

O objetivo é **separar os dados sensíveis do código-fonte**, permitindo que os scripts sejam mais seguros, reutilizáveis e organizados.  

Site oficial: https://pypi.org/project/python-dotenv/  

---

## Vantagens de usar arquivos `.env`

| Benefício                  | Explicação prática                       |
|----------------------------|------------------------------------------|
| Segurança básica           | Evita deixar senhas no código-fonte      |
| Reutilização de scripts    | Basta trocar o `.env` para novo ambiente |
| Compatível com frameworks  | Suporte em Python, Ansible, Docker etc.  |
| Git-safe                   | Pode ser ignorado com `.gitignore`       |

---

## Como usar

1. **Crie um arquivo `.env` com suas variáveis**
2. Instale a biblioteca:

```bash
pip install python-dotenv
```

### Casos de uso de arquivos .env na automação de redes:

- Armazenamento seguro de credenciais: usuário, senha, token de API, chaves privadas.  
- Separação entre lógica e dados sensíveis: o script não precisa conter IPs ou senhas diretamente.  
- Criação de ambientes reutilizáveis: troca-se o .env e o mesmo script pode ser usado em sites diferentes.  
- Facilidade para testes e simulações: carregar configurações diferentes sem editar o código.  
- Integração com bibliotecas Python: como Netmiko, Paramiko, Napalm, requests, pyATS, etc.  
- Organização e padronização de projetos: cada projeto possui seu próprio .env, facilitando o versionamento.  

### Quando usar .env vs outras abordagens

| Use .env quando...                                  | Evite .env quando...                                 |  
|-----------------------------------------------------|------------------------------------------------------|
| Você precisa manter dados sensíveis fora do código	| Os dados são públicos ou não sensíveis               |
| O script será usado em ambientes diferentes	        | O projeto é totalmente fixo, para uso único          |
| Trabalha em equipe ou múltiplos ambientes           | Não há variações de configuração entre ambientes     |
| Vai usar Git/GitHub e quer manter segurança	        | O projeto será executado localmente, sem versionar   |
| Deseja facilitar integração com CI/CD, Ansible      | Precisa de criptografia real (use cofres nesse caso) |

### Por que .env é essencial para o CCNP e para automação de redes?

- Separação entre dados sensíveis e lógica: permite que senhas, IPs e tokens fiquem fora do código-fonte, facilitando manutenção e segurança.
- Reutilização de scripts em múltiplos ambientes: você usa o mesmo código em diferentes sites, mudando apenas o conteúdo do .env.
- Integração natural com Python e ferramentas de rede: bibliotecas como Netmiko, Paramiko, requests e Nornir podem consumir dados externos via .env.
- Escalabilidade com segurança básica: ideal para ambientes pequenos a médios, com controle de acesso por permissões (chmod) e exclusão de versionamento (.gitignore).
- Ponto de transição para práticas avançadas: usar .env é a base para depois adotar cofres de segredos como Ansible Vault, AWS Secrets Manager, ou HashiCorp Vault.
 
**OBS:** Antes de ver exemplos práticos com .env, é fundamental entender o fluxo de como variáveis de ambiente (armazenadas em .env) se integram aos scripts de automação.
O fluxograma a seguir mostra dois cenários comuns: uso com Python puro e uso com ferramentas como Ansible, que podem consumir variáveis externas ou cofres de forma segura.

### Fluxo do uso de .env com Python puro e com Ansible

```mermaid
flowchart TB

    A[Início] --> B[Arquivo .env]

    B --> C[Variáveis de ambiente]
    C --> C1[IP do dispositivo]
    C --> C2[Usuário/Senha]
    C --> C3[Token/API Key]

    %% Caminho com Python puro
    C --> D[Script Python]
    D --> E[Usa python-dotenv]
    E --> F[Carrega as variáveis]
    F --> G[Utiliza com Netmiko / Paramiko / API]
    G --> H[Aplica ou consulta dispositivo]

    %% Caminho com Ansible ou outros
    C --> J[Integração com Cofres - Vault, AWS Secrets]
    J --> K[Playbook ou pipeline]
    K --> L[Substitui variáveis no momento da execução]
    L --> M[Aplica a configuração]
```

**OBS:** estaremos utilizando somente scripts python puro por enquanto. Todas as saídas serão locais e não serão enviadas para nenhum equipamento por questões de boas práticas. Depois irei adicionar tópicos para acesso dos equipamentos.

### Exemplo 01 – Leitura básica do .env com python-dotenv

Este exemplo demonstra como **carregar variáveis de ambiente** armazenadas em um arquivo `.env` usando a biblioteca `python-dotenv`. Isso é útil para separar **dados sensíveis (como IPs e senhas)** do código-fonte.  

**Estrutura de arquivos usada no exemplo**  

```Bash
01/
├── .env # Arquivo com as variáveis reais
├── .env.exemplo # Modelo para distribuição segura
├── script.py # Script Python que lê as variáveis
└── requirements.txt
```

**.env**

```dotenv
DISPOSITIVO_IP=192.168.100.10
USERNAME=admin
PASSWORD=cisco123
```

**.env.exemplo**  

```dotenv
DISPOSITIVO_IP=
USERNAME=
PASSWORD=
```

**script.py**

```Python
[01] from dotenv import load_dotenv
[02] import os
[03]
[04] # 1. Carrega variáveis do arquivo .env
[05] load_dotenv()
[06]
[07] # 2. Lê as variáveis de ambiente
[08] ip = os.getenv("DISPOSITIVO_IP")
[09] usuario = os.getenv("USERNAME")
[10] senha = os.getenv("PASSWORD")
[11]
[12] # 3. Imprime as informações (simulando uso)
[13] print("📡 Conectando ao dispositivo:")
[14] print(f"IP: {ip}")
[15] print(f"Usuário: {usuario}")
[16] print("Senha: ********")  # Nunca exiba senhas reais
```

**requirements.txt**

```txt
python-dotenv
```

**saída**

```bash
alcancil@linux:~/automacoes/arquivos/env/01$ python3 -m venv venv
alcancil@linux:~/automacoes/arquivos/env/01$ source venv/bin/activate
(venv) alcancil@linux:~/automacoes/arquivos/env/01$ pip install -r requirements.txt
Collecting python-dotenv (from -r requirements.txt (line 1))
  Downloading python_dotenv-1.1.0-py3-none-any.whl.metadata (24 kB)
Downloading python_dotenv-1.1.0-py3-none-any.whl (20 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.1.0
(venv) alcancil@linux:~/automacoes/arquivos/env/01$ python3 script.py 
📡 Conectando ao dispositivo:
IP: 192.168.100.10
Usuário: admin
Senha: ********
(venv) alcancil@linux:~/automacoes/arquivos/env/01$ 
```

**Observações**

- O arquivo .env.example é um modelo seguro para ser compartilhado com a equipe.
- O .env não deve ser versionado (adicione ao .gitignore).
- Este é um passo essencial para tornar seus scripts modulares, seguros e reutilizáveis.

**Explicação**  

**script.py**  

```Python
Seção 1: Importações  

[01] from dotenv import load_dotenv           # Importa a função 'load_dotenv' para carregar as variáveis do arquivo .env
[02] import os                                # Importa o módulo 'os' para acessar variáveis de ambiente com os.getenv()

Seção 2: Carregamento do arquivo .env  

[04]                                           # 1. Carrega variáveis do arquivo .env    
[05] load_dotenv()                             # Lê o arquivo .env e carrega suas variáveis para o ambiente do Python

Seção 3: Leitura das variáveis de ambiente

[07]                                           # 2. Lê as variáveis de ambiente          
[08] ip = os.getenv("DISPOSITIVO_IP")          # Lê a variável 'DISPOSITIVO_IP' do ambiente e armazena na variável 'ip'
[09] usuario = os.getenv("USERNAME")           # Lê a variável 'USERNAME' e armazena na variável 'usuario'
[10] senha = os.getenv("PASSWORD")             # Lê a variável 'PASSWORD' e armazena na variável 'senha'

Seção 4: Exibição dos dados simulando uma conexão

[12]                                               # 3. Imprime as informações (simulando uso)  
[13] print("📡 Conectando ao dispositivo:")        # Mensagem indicando o início da conexão (simulada)
[14] print(f"IP: {ip}")                            # Exibe o IP capturado do .env
[15] print(f"Usuário: {usuario}")                  # Exibe o nome de usuário capturado do .env
[16] print("Senha: ********")                      # Máscara a senha na saída (boa prática de segurança)

```

### Exemplo 02 – Integração com template Jinja2 usando variáveis do .env

# Exemplo 02 – Integração com Jinja2 usando variáveis do `.env`

Este exemplo demonstra como **integrar variáveis carregadas de um arquivo `.env`** com um **template Jinja2**, para gerar um banner de login Cisco de forma dinâmica e segura.  

**Estrutura de arquivos usada no exemplo**

```Bash
02-env-com-jinja2/
├── .env
├── .env.example
├── template_banner.j2
├── gerar_banner.py
├── requirements.txt
└── README.md
```

**.env**

```dotenv
HOSTNAME=SW01
BANNER=Mantenha-se autorizado. Este equipamento está sendo monitorado.
```

**.env.example**

```dotenv
HOSTNAME=
BANNER=
```

**template_banner.j2**

```jinja2
hostname {{ hostname }}

banner login ^C
{{ banner }}
^C
```

**gerar_banner.py**

```Python
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import os

# 1. Carrega variáveis do arquivo .env
load_dotenv()

# 2. Lê as variáveis de ambiente
hostname = os.getenv("HOSTNAME")
banner = os.getenv("BANNER")

# 3. Prepara o ambiente do Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template_banner.j2")

# 4. Renderiza o template com os dados do .env
saida = template.render(hostname=hostname, banner=banner)

# 5. Salva o resultado em um arquivo .txt
with open(f"{hostname}_banner.txt", "w") as f:
    f.write(saida)

print(f"✅ Configuração gerada: {hostname}_banner.txt")
```

**requirements.txt**

```text
python-dotenv
jinja2
```

### Exemplo 03 – Simulação de login via .env (sem aplicar)

### Exemplo 04 – Validação de variáveis faltantes no .env (com os.getenv(..., default))