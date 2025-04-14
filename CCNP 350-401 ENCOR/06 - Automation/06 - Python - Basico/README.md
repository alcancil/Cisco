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

O Python segue o padrão REPL (Read-Eval-Print Loop):  
 
 ```Python
    >>> 200
    200
    >>> 
 ```

    Read: Lê a entrada (ex: 200).

    Eval: Avalia a expressão (calcula o valor).

    Print: Exibe o resultado (200).

    Loop: Repete o processo.

Isso é útil para testes rápidos e depuração.  

Para escrevermos algo na tela temos o comando **print** . Aqui preciso fazer uma observação. O Python aceita que quando precisamos entrar com algum argumento em algum comando como o print, podemos utilizar as aspas ´ ´ ou mesmo as aspas duplas " " . Mas não podemos misturar essas duas aspas e precisamos ser consistentes, se começamos com aspas simples ´´, é importante que continuemos a utilizar aspas simples. Para aspas duplas devemos seguir o mesmo conceito.  

```Python
    >>> print('Hello World!!')
    Hello World!!
    >>>  
 ```     
      ou

```Python
    >>> print("Hello World!!")
    Hello World!!
    >>> 
```  

## Variáveis

Agora que vimos como enviar dados para a saída padrão (tela), precisamos pensar no seguinte: e se quisermos armazenar esses valores para podermos utilizá-los depois ? Bom, para isso existem as **variáveis** que podem ser de vários tipos.  
**OBS:** para passarmos um valar para alguma variável, devemos primeiro declarar a mesma. Exemplo: **variável = valor** 
**Obs2:** para sabermos o tipo da variável podemos utilizar o comando **type**. Verifique os exemplos a seguir.

### Tipo Inteiro (int)

Essa é a variável do tipo inteiro, ou seja, são números decimais inteiros tanto positivos como negativos. 

```Python
    >>> a = 10
    >>> print(a)
    10
    >>> print(type(a))
    <class 'int'>
    >>>
```  

Nesse exemplo lê-se a recebe 10, imprima na tela o valor de a e na última linha imprima a classe da variável a . Então podemos notar que o comando **pint()** precisa de dois parênteses, um que abre e um que fecha. O mesmo vale para o comando **type()**  

### Tipo float - Ponto flutuante ou Decimal

São os números racionais que são resultantes de frações. São os números "quebrados"  

```Python
    >>> a = 1.48
    >>> b = 11.267
    >>> print(a)
    1.48
    >>> print(b)
    11.267
    >>> print(type(a),type(b))
    <class 'float'> <class 'float'>
    >>>
```  
Aqui eu aproveitei para demonstrar que ao utilizar o mesmo nome da **a** que foi utilizado para a variável do exemplo anterior, o valor que antes era 10 agora foi substituído por 1.48  

### Tipo Complexo

São os números complexos que são utilizados na sua grande maioria em cálculos científicos e geométricos. É composto em duas partes: a parte real e a parte imaginária. Ele tem o formato:  

```Python
    a+bj  

    a: Parte real (real).  

    b: Parte imaginária (imag).  

    j: Unidade imaginária.  
```

```Python
    Sintaxe
    z = a + bj  # Forma literal
    z = complex(a, b)  # Usando a função complex()
```

```Python
    >>> x = 7 + 100j
    >>> print(x.real)
    7.0
    >>> print(x.imag)
    100.0
    >>> print(type(x))
    <class 'complex'>
    >>> print(complex(3,7))
    (3+7j)
    >>>  
```

### Tipo String (Str)

É uma sequência de caracteres para armazenar texto em Python. São sempre inseridos entre aspas simples ' ' ou aspas duplas " ".

    ```Python
    >>> nome = 'Alexandre'
    >>> sobrenome = 'Silva'
    >>> print(nome)
    Alexandre
    >>> print(type(sobrenome))
    <class 'str'>
    >>> senha = ('51Ab!2@c')
    >>> print(senha)
    51Ab!2@c
    >>> 
    ```



# ARRUMAR

String (str)

É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.

Exemplos:


1
2
3
4
5


	

nome = 'Guilherme'
profissao = 'Engenheiro de Software'

print(type(profissao))
print(type(nome))


Saída:



<class 'str'>
<class 'str'>


Boolean (bool)

Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).

Na lógica computacional, podem ser considerados como 0 ou 1.

Exemplos:


1
2
3
4
5


	

fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))


Saída:



<class 'bool'>
<class 'bool'>


Listas (list)

Tipo de dado muito importante e que é muito utilizado no dia a dia do desenvolvedor Python!

Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.

Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos, veja alguns exemplo abaixo:


1
2
3
4
5


	

alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0] 

print(type(alunos))
print(type(notas))


Saída:



<class 'list'>
<class 'list'>


Aqui na Python Academy temos muito conteúdo sobre Listas para você ficar craque!

Para saber mais sobre Listas acesse nosso post sobre Listas, também nosso post sobre Manipulação de Listas, e nosso post completo sobre List Comprehensions.

Está curtindo esse conteúdo? :thumbsup:

Que tal receber 30 dias de conteúdo direto na sua Caixa de Entrada?