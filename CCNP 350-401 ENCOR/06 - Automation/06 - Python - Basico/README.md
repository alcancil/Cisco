# Python - Básico

Como esse é um tópico do Blueprint da certificação CCNP-ENCORE 350-401 da Cisco (6.1 - Interpret basic Python components and scripts), a intenção aqui não é ser um curso de Python.  
Então vou começar pelo básico e ir avançando para alguns scripts que julgo serem úteis para o dia a dia de trabalho. Dito isso vamos começar. Aqui vale ressaltar que vou seguir utilizando o Linux Mint, mas como demonstrado, os códigos servem para Windows também.  

## O Shell do Python

Quando instalamos o Python, por padrão ele instala um shell, ou seja um prompt para podermos executar nossos códigos. Ele é mais limitado do que um IDE como o Vscode e server para testes rápidos ou mesmo para que está iniciando no mundo do Python. Vamos então chamar o nosso shell. Para isso vamos digitar **python3** no terminal.  

```python
    alcancil@linux:~$ python3
    Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
```    
Para sairmos podemos digitar **quit()** ou **exit()** ou mesmo pressionar **ctrl+d**  

```python
    alcancil@linux:~$ python3
    Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> quit()
    alcancil@linux:
```  
```python
    alcancil@linux:~$ python3
    Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()
    alcancil@linux:
```  
Para verificarmos a versão do python instalado, digite **python3 --version**  

```python
    alcancil@linux:~$ python3 --version
    Python 3.12.3
    alcancil@linux:~$
```  
**OBS:** para limpar a tela pressione **ctrl+l**  
**OBS2:** como estamos no shell, o python interpreta o código linha a linha e já vai apresento resultado na tela. Um pouco diferente do resultado de uma IDE mais completa.  

