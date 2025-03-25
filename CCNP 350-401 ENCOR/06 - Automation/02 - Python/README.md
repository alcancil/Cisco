# Python

Python é uma linguagem de programação de alto nível, ou seja, mais próxima da linguagem humana, interpretada, e de código aberto, conhecida por sua simplicidade e legibilidade. Foi criada por Guido van Rossum e lançada em 1991.

🔹 Principais características do Python:  
✔ Fácil de aprender: Sintaxe limpa e intuitiva, parecida com linguagem humana.  
✔ Multiparadigma: Suporta programação orientada a objetos, estruturada e funcional.  
✔ Interpretada: O código é executado linha por linha, sem necessidade de compilação prévia.  
✔ Dinamicamente tipada: Não é necessário declarar o tipo das variáveis.  
✔ Extensível: Possui uma vasta biblioteca padrão e muitos frameworks (Django, Flask, Pandas, NumPy etc.).  
✔ Multiplataforma: Funciona em Windows, Linux, macOS e outros sistemas.  
✔ Comunidade ativa: Muitos recursos, tutoriais e suporte online.  

🔹 Para que o Python é usado?  
✔ Desenvolvimento Web (Django, Flask)  
✔ Ciência de Dados & Machine Learning (Pandas, TensorFlow, Scikit-learn)  
✔ **Automação/Scripts**  
✔ Análise de dados  
✔ Inteligência Artificial  
✔ Jogos (com Pygame)  
✔ IoT (Internet das Coisas)  

## Instalação

O Python pode ser encontrado em : **https://www.python.org/** . Toda a documentação e todos os recursos da linguagem podem ser encontrados nesse site oficial do desenvolvedor.  

Instalando o Python no Windows - **https://python.org.br/instalacao-windows/**  
Instalando o Python no Linux  - **https://python.org.br/instalacao-linux/**  

## Editando Códigos.

Agora que temos o Python instalado já podemos criar nossos códigos. Para isso basta abrir o terminal do sistema, entrar no python e digitar o código .  

| ![PYTHON](Imagens/versao_w.png) | ![PYTHON](Imagens/versao_l.png) |
|---------------------------------|---------------------------------|
| Verificando versão em Windows   | Verificando versão em Linux     |

Então, vamos escrever o nosso primeiro código em Python, o tradicional Olá mundo ! .  

![PYTHON](Imagens/codigo01.png)  

Então podemos ver que o Python é um interpretador simples e intuitivo.  O Python interpreta arquivos na extensão **.py**. Então para rodar o código desse arquivo basta digitar **python nome_do_arquivo.py**.  

![PYTHON](Imagens/arquivo01.png)  

De inicio era assim que os programadores faziam. Eles utilizam editores de texto como o notapd.exe (Windows) ou mesmo o nano (linux). Mas com o passar do tempo, foram criadas as **IDEs** que nada mais são programas em interface gráfica que permitem integrar vários recursos para facilitar a digitação dos códigos.  
Algumas das IDES mais populares são:  
* [Pycharm](https://www.jetbrains.com/pycharm/)  
* [Vscode](https://code.visualstudio.com/)  
* [Jupyter](https://jupyter.org/)  

Existem outras IDES mas cada uma tem suas propriedades e vantagens. Então o usuário tem que escolher a que mais se adequa as suas necessidades.  

## Gerenciador de pacotes - PIP

O Python funciona com bibliotecas e pacotes e para gerenciar (instalar, remover ou atualizar) os pacotes e le utiliza um gerenciador de pacotes chamado **pip**. O pip por sua vez utiliza um repositório de pacotes o pypy (https://pypi.org/).  
Então vamos supor que você precise de alguma biblioteca para manipular o **iptables** do linux. Como faríamos ?  
Para isso, precisamos saber se existe algum pacote com essa finalidade. Para isso, basta navegar no site do repositório **pypi** e no campo de busca vamos digitar iptables. Como resultado, podemos notar que a pesquisa irá retornar vários resultados. Dentre eles, você ira encontrar o pacote **iptables-tools**.  Se navegarmos por esse resultado, vamos ter toda a documentação oficial que ensina desde como se instala o pacote até mesmo como se utiliza o mesmo.  

Mas como o pip funciona então ?  

Como usar o PIP?  

1. Verificar se o PIP está instalado

No Windows, normalmente o Pip já vem instalado. Já no linux é necessário se instalar o mesmo.  

**Windows**

![PIP](Imagens/pip/pip_w.png)  

**Linux**

![PIP](Imagens/pip/pip_l.png)

bash
Copy
pip --version
# ou (para Python 3)
pip3 --version
Saída exemplo:

Copy
pip 23.3.1 from /usr/local/lib/python3.10/site-packages/pip (python 3.10)
⚠️ Se não estiver instalado, siga este guia oficial.

2. Instalar um pacote
bash
Copy
pip install nome_do_pacote
Exemplo:

bash
Copy
pip install requests  # Instala a biblioteca 'requests'
3. Listar pacotes instalados
bash
Copy
pip list
Saída:

Copy
Package    Version
---------- -------
requests   2.31.0
numpy      1.24.0
4. Atualizar um pacote
bash
Copy
pip install --upgrade nome_do_pacote
Exemplo:

bash
Copy
pip install --upgrade numpy
5. Desinstalar um pacote
bash
Copy
pip uninstall nome_do_pacote
Exemplo:

bash
Copy
pip uninstall pandas
6. Congelar dependências (salvar em um arquivo)
Útil para compartilhar projetos:

bash
Copy
pip freeze > requirements.txt
Conteúdo de requirements.txt:

Copy
requests==2.31.0
numpy==1.24.0
Para instalar dependências de um arquivo:

bash
Copy
pip install -r requirements.txt
🔹 PIP vs. Conda
PIP	Conda (Anaconda/Miniconda)
Gerenciador oficial do Python	Gerenciador de pacotes multi-linguagem
Instala apenas pacotes Python	Instala Python + bibliotecas científicas (R, C++, etc.)
Usa o PyPI como repositório	Usa o repo. Conda (mais focado em Data Science)
📌 Dica: Para ciência de dados, muitos usam conda, mas pip é universal.

🔹 Problemas comuns e soluções
❌ "pip não encontrado" → Instale-o com:

bash
Copy
python -m ensurepip --upgrade
❌ Erros de permissão → Use --user ou ambientes virtuais:

bash
Copy
pip install --user nome_do_pacote
❌ Conflito de versões → Use venv:

bash
Copy
python -m venv meu_ambiente
source meu_ambiente/bin/activate  # Linux/macOS
meu_ambiente\Scripts\activate     # Windows
📌 Resumo
PIP é essencial para trabalhar com Python.

PyPI é o "mercado" de bibliotecas Python.

requirements.txt padroniza dependências em equipe.

Quer um exemplo prático de como criar um ambiente virtual? 😊

O que é um pacote em python ?
O que é um Pacote em Python?
Em Python, um pacote (package) é uma maneira de organizar e estruturar módulos relacionados em um único diretório, tornando o código mais modular, reutilizável e fácil de compartilhar.

🔹 Diferença Básica: Módulo vs. Pacote
Módulo: Um arquivo .py com funções, classes ou variáveis.

Exemplo: meu_modulo.py

Pacote: Uma pasta contendo múltiplos módulos + um arquivo especial __init__.py.

Exemplo:

Copy
meu_pacote/
├── __init__.py
├── modulo1.py
└── modulo2.py
🔹 Estrutura de um Pacote
Um pacote Python tem:

Diretório com um nome único (ex: meu_pacote).

Arquivo __init__.py (pode estar vazio, mas é obrigatório para Python 3.3+).

Módulos (arquivos .py) ou subpacotes.

Exemplo:

Copy
meu_projeto/
├── main.py
└── meu_pacote/
    ├── __init__.py
    ├── modulo1.py
    └── subpacote/
        ├── __init__.py
        └── modulo2.py
🔹 Para que servem os pacotes?
✔ Organização: Dividir projetos grandes em partes lógicas.
✔ Reutilização: Compartilhar funcionalidades entre projetos.
✔ Distribuição: Publicar no PyPI (para instalação via pip).

🔹 Como usar um pacote?
1. Importar um módulo de um pacote
python
Copy
from meu_pacote import modulo1
modulo1.funcao()
2. Importar uma função específica
python
Copy
from meu_pacote.modulo1 import funcao
funcao()
3. Importar de um subpacote
python
Copy
from meu_pacote.subpacote.modulo2 import Classe
obj = Classe()
🔹 Pacotes vs. Bibliotecas
Pacote: Estrutura de diretórios com módulos.

Biblioteca: Coleção de pacotes distribuídos (ex: requests, numpy).

📌 Exemplo:

O pacote numpy é parte da biblioteca NumPy.

Você instala bibliotecas via pip install numpy.

🔹 Tipos de Pacotes
Pacotes Locais: Criados por você para organizar seu projeto.

Pacotes de Terceiros: Instalados via pip (ex: pandas, flask).

Pacotes Nativos: Já incluídos no Python (ex: os, math).

🔹 Como criar seu próprio pacote?
Crie uma pasta com o nome do pacote.

Adicione __init__.py (pode ser vazio).

Adicione módulos (arquivos .py).

Use-o em outros scripts com import.

Exemplo (meu_pacote/__init__.py):

python
Copy
# Opcional: defina o que é exportado
__all__ = ['modulo1', 'subpacote']
🔹 Como distribuir um pacote?
Para compartilhar seu pacote no PyPI (e permitir instalação via pip):

Crie um setup.py (ou pyproject.toml).

Gere um arquivo distribuível:

bash
Copy
python setup.py sdist bdist_wheel
Publique no PyPI:

bash
Copy
twine upload dist/*
📌 Exemplo de setup.py:

python
Copy
from setuptools import setup

setup(
    name="meu_pacote",
    version="0.1",
    packages=["meu_pacote"],
)
🔹 Resumo
Pacote = Pasta com __init__.py + módulos.

Usado para organizar, reutilizar e distribuir código.

Pacotes locais vs. pacotes instaláveis (via pip).

Quer um exemplo passo a passo de como criar um pacote simples? 😊

