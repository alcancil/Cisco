# Python - Ambientes Virtuais

Antes de começarmos a escrever nossos códigos, precisamos entender o que são os ambientes virtuais e porque devemos utilizá-los.  
Bom se lembrarmos que na parte que passamos pelo gerenciador de pacotes PIP, quando vamos utilizá-lo recebemos uma mensagem de erro que por padrão nos impede de utilizar o PIP. Mas o que realmente é essa mensagem ? Na verdade isso não é um erro e sim um aviso de boas práticas, e sendo "boas práticas", podemos modificar ese comportamento e passar a utilizar o PIP direto no sistema. <br></br>
No caso vimos que o Linux nos trouxe a mensagem, mas o Windows não. Mas a mensagem serve para qualquer um dos sistemas operacionais. O que acontece é que muitas vezes quando vamos desenvolver nossos código precisamos utilizar alguma biblioteca ou mesmo algum pacote. No caso de distribuições Linux Debian, o sistema utiliza o gerenciador de pacotes **apt**. Já no windows, recentemente foi introduzido o **winget**. <br></br>  
Então se repararmos, temos dois gerenciadores de pacote: um oficial para o sistema e outro para o Python. Acontece que os gerenciadores de pacote utilizam as suas fontes oficiais onde armazenam seu pacotes e pode ser que existam pacotes do sistema que possa gerar conflitos com pacotes do Python. Obviamente não queremos esse tipo de comportamento.  
Outro problema comum é que podemos escrever um código em uma máquina e depois queremos enviar para outra pessoa que irá utilizar em outra máquina para analisar, terminar ou mesmo completar esse mesmo código. Então é interessante que essa pessoa tenha também os mesmos pacotes necessários instalados no seu ambiente para que o código posso rodar sem problemas. Isso é chamado de requisitos do código. <br></br> 
Então, os ambientes virtuais nada mais são do que a virtualização de um ambiente em que podemos explicitar os requisitos e depois enviar para outras pessoas com isso protegendo o sistema operacional e que não falte nada para se executar o código.  
  
Resumindo:  

Por Que Usar Ambientes Virtuais?  
    ✔**Isolar Dependências :** Evita que bibliotecas de um projeto (ex: telnetlib v1.0) conflitem com as de outro (ex: telnetlib v2.0).
    ✔**Reproducibilidade   :** Garante que seu código funcione em qualquer máquina (com as mesmas versões de bibliotecas).  
    ✔**Sem Poluir o Python Global :** Instalações ficam restritas ao ambiente do projeto, sem afetar o sistema.  

## Windows

Agora vamos ver como criar, ativar, desativar e remover ambientes virtuais no Windows.  
1. Vamos abrir o terminal do Windows. 
2. Agora vamos listar os pacotes instalados pelo Pip no sistema operacional com o comando: **pip list**

![VENV](Imagens/Windows/01.png)  

Como podemos observar, temos várias bibliotecas e dependências instaladas no windows.  

3. Vamos criar a pasta **projetos** e vamos entrar nela
4. Dentro da pasta vamos criar nosso ambiente virtual com o comando: **python -m venv meu_ambiente Obs:** é a biblioteca **venv** quem cria os ambientes virtuais.  

| ![VENV](Imagens/Windows/02.png) | ![VENV](Imagens/Windows/03.png) |
|---------------------------------|---------------------------------|  

Como podemos observar, após inserirmos o comando uma pasta é criada com o nome do ambiente fornecido, nesse caso **meu_ambiente**. Dentro dessa pasta ficam todas as bibliotecas e dependências do projeto que vamos criar.  

Vou deixar aqui a documentação oficial sobre ambientes virtuais em Python: https://docs.python.org/3/library/venv.html

**Arrumar**  

    
🛠️ Como Ativar/Desativar (Linux e Windows)
1. Criar um Ambiente Virtual
Linux/macOS:
bash
Copy

python3 -m venv meu_ambiente  # Cria a pasta "meu_ambiente"

Windows:
cmd
Copy

python -m venv meu_ambiente

2. Ativar o Ambiente
Linux/macOS (Terminal):
bash
Copy

source meu_ambiente/bin/activate

Windows (CMD/PowerShell):
cmd
Copy

meu_ambiente\Scripts\activate

💡 Dica: No PowerShell, pode ser necessário executar:
powershell
Copy

Set-ExecutionPolicy Unrestricted -Scope Process  # Permite scripts
.\meu_ambiente\Scripts\Activate.ps1

3. Verificar se Está Ativo

O prompt mostrará o nome do ambiente:
Copy

(meu_ambiente) usuario@maquina:~$

4. Instalar Bibliotecas (Ex: telnetlib)
bash
Copy

pip install telnetlib3  # Dentro do ambiente ativo

5. Desativar o Ambiente
bash
Copy

deactivate  # Funciona em Linux e Windows

📂 Estrutura de Pastas

Após criar o ambiente, você terá:
Copy

meu_ambiente/
├── bin/           # (Linux) Scripts de ativação
├── Scripts/       # (Windows) Scripts de ativação
├── Lib/           # Bibliotecas instaladas
└── pyvenv.cfg     # Configurações do ambiente

💡 Dicas Avançadas

    Requisitos (requirements.txt)

        Para salvar as bibliotecas do ambiente:
        bash
        Copy

        pip freeze > requirements.txt

        Para reinstalá-las em outro lugar:
        bash
        Copy

        pip install -r requirements.txt

    Ferramentas Alternativas

        virtualenv: Mais antigo, mas flexível.

        conda: Usado em ciência de dados (Anaconda).

    VS Code Integration

        Se usar VS Code, selecione o interpretador do ambiente virtual:
        Ctrl + Shift + P > Python: Select Interpreter > Escolha o Python do ambiente.

⚠️ Problemas Comuns

    "Comando não encontrado" (Linux):
    Instale o pacote python3-venv:
    bash
    Copy

    sudo apt install python3-venv  # Debian/Ubuntu

    Erros no Windows:

        Se activate não funcionar, tente:
        cmd
        Copy

        .\meu_ambiente\Scripts\activate.bat

📚 Fontes para Aprofundar

    Documentação Oficial: venv

    Tutorial: Gerenciando Ambientes (Real Python)

Pronto! Agora você pode criar ambientes isolados para testar scripts de automação como telnetlib sem medo. Quer um exemplo de como usar o ambiente virtual num projeto de automação de redes? 🚀
New chat


| ![VSCODE](Imagens/Linux/01.png) | ![VSCODE](Imagens/Linux/02.png) | 
|---------------------------------|---------------------------------|
| 01                              | 02                              |
| ![VSCODE](Imagens/Linux/03.png) | ![VSCODE](Imagens/Linux/04.png) |
| 03                              | 04                              |
| ![VSCODE](Imagens/Linux/05.png) | ![VSCODE](Imagens/Linux/06.png) |
| 05                              | 06                              |
| ![VSCODE](Imagens/Linux/07.png) |                                 |
| 07                              |                                 |

Feito isso, o restante das otimizações e instalações de extensões é igual as realizadas em windows.  