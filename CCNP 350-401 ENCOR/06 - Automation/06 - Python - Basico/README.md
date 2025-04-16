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
**Obs2:** para sabermos o tipo da variável podemos utilizar o comando **type**.  

### Regras para os nomes das variáveis

Para criarmos variáveis precisamos segui algumas regras.  

* A variável precisa iniciar com uma letra ou com um underscore ( _ )  
* A variável não pode começar com um número  
* A variável pode conter somente caracteres alfa numéricos e underscore (A-z, 0-9 e _ )  
* A variável é do tipo "Case Sensitive", ou seja, ela diferencia letras maiúsculas de minúsculas
* A variável não pode ser nenhum nome reservado para a linguagem Python (Ex: type)   

Verifique os exemplos a seguir.

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

## Tipo Boolean (bool)

Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).  
Na lógica computacional, podem ser considerados como 0 ou 1.  

```Python
    >>> up=True
    >>> down=False
    >>> type(up)
    <class 'bool'>
    >>> type(down)
    <class 'bool'>
    >>> 
```


Qualquer valor pode ser convertido em booleano.  

```Python  
    # Valores considerados "False" (Falsy)  
    print(bool(0))         # False  
    print(bool(""))        # False (string vazia)  
    print(bool([]))        # False (lista vazia)  
    print(bool(None))      # False  
  
    # Valores considerados "True" (Truthy)  
    print(bool(1))         # True  
    print(bool("Cisco"))   # True  
    print(bool([1, 2]))    # True  
```  

Agora que aprendemos sobre os tipos de variáveis pode aparecer uma questão interessante: mas e se eu tiver um tipo de variável e precisar converte-la para outro tipo ? Isso é possível ? Sim.  Vamos ver alguns exemplos.  

**Exemplo 01**

```Python
    >>> x = 1
    >>> y = 3.4
    >>> z = 56j
    >>> type(x)
    <class 'int'>
    >>> type(y)
    <class 'float'>
    >>> type(z)
    <class 'complex'>
    >>> 
```  
Então temos um tipo **int**, um **float** e um **complex** . Vamos convertê-los:  

```Python
    >>> float(x)
    1.0
    >>> complex(y)
    (3.4+0j)
    >>> str(z)
    '56j'
    >>> 
```  
Podemos adicionar comentários ao nosso código e para isso basta utilizarmos o sinal de **#** antes do que desejarmos comentar. Então veja o exemplo anterior comentado.  

```Python
    #Convertendo de int para float
    >>> float(x)
    1.0
    #Convertendo de float para complex
    >>> complex(y)
    (3.4+0j)
    #convertendo de complex para string
    >>> str(z)
    '56j'
    >>> 
```  

**Obs:** até verificamos como definir um valor a uma variável e depois realizar a saída na tela dessa informação. Mas podemos realizar a entrada de valor nas variáveis também. Para isso existe o comando **input**  

```Python
    >>> nome = input()
    #Aqui o cursor fica piscando "esperando" que o usuário digite algum valor. A variável só irá receber o valor após o usuário digitar o valor e pressionar enter
    Alexandre
    >>> print(nome)
    Alexandre
    >>>
```  

## Python como calculadora  

O Python por si só realiza operações matemáticas. Então podemos dizer que ele funciona como uma espécie de calculadora rudimentar e não precisamos fazer muita coisa. Vamos a alguns exemplos:  

**Exemplo 01**
```Python
    >>> 1+1
    2
    >>> 2-1
    1
    >>> 3*3
    9
    >>> 5/2
    2.5
    >>> 
```  
Nesse exemplo realizamos as 4 operações básicas fundamentais: soma (+), subtração (-), multiplicação (*) e divisão (/).  

**Exemplo 02**
```Python
    # Realizando uma divisão por 0
    >>> 10/0
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    # Como não existe divisão por Zero, o Python irá retornar um erro
```  

**Exemplo 03**
```Python
    >>> 2-4
    -2
    >>> 5*-2
    -10
    >>> 3/12
    0.25
    >>> 5+(-5)
    0
    >>>
```  

**Exemplo 04**
```Python
    >>> a=1
    >>> b=2
    >>> a+b
    3
    >>> b-a
    1
    >>> a/b
    0.5
    >>> a*b
    2
    >>
```  

## Interação com o usuário 

Como demonstrado anteriormente, existe dentro do Python uma função chamada de **Input()** que é considerada built-in, ou seja, ela já vem pronta dentro do próprio Python. Essa função serve para ler os dados digitado pelo usuário no prompt.  Também podemos passar esses dados para alguma variável, por exemplo. Todos os dados que o usuário digitar são do tipo **string**.  

```Python
    >>> nome = input()
    Alexandre
    >>> Print(nome)
    >>> print(nome)
    Alexandre
    >>>
```  

Então, como podemos notar, nesse exemplo, passamos o valor do input() para a variável nome. Então o cursor fica esperando o usuário digitar, para depois armazenar o valor.  

```Python
    >>> nome = input("Olá, qual é o seu nome: ")
    Olá, qual é o seu nome: Alexandre
    >>>
```  
Nesse exemplo podemos notar que agora inserimos uma frase antes para ser mostrada ao usuário para ele saber o que digitar.  
Uma outra coisa interessante que podemos fazer com o "Python" é concatenar valores com o sinal de **+** .

```Python
    >>> nome = input()
    João
    >>> sobrenome = input()
    Silva
    >>> print('Seja bem vindo', nome + sobrenome)
    Seja bem vindo JoãoSilva
    >>> print('Seja bem vindo', nome, ' ' + sobrenome)
    Seja bem vindo João  Silva
>>>
```  
Nesse exemplo podemos observar que as variáveis **nome** e **sobrenome** recebem o valor digitado pelo usuário porém quando queremos retornar os valores na tela utilizamos a função **print()** concatenando as duas variáveis, **nome** + **sobrenome**. Porém, dessa maneira, os valores saem unidos. Uma solução como mostrado foi adicionar um valor em branco entre as variáveis.  
Agora, como citado, os valores que a função **input()** recebe são do tipo **str**. Veja o exemplo:  

```Python
    >>> peso = input()
    2
    >>> quantidade = 2
    >>> print('Se eu tenho ', quantidade, ' martelos, então seu peso será de ', peso * quantidade , ' kgs')
    Se eu tenho  2  martelos, então seu peso será de  22  kgs
    >>>
``` 
Ora, sabemos que 2 * 2 é igual a 4. Mas então porque o resultado ai foi de 22 ? Simples. Como já vimos, toda a entrada em um **imput()** é uma **string**. Então temos dois tipos de variáveis nesse exemplo: uma **sting** e uma do tipo **integer**. Para resolver esse problema precisamos transformar a string em integer.  

```Python
    >>> peso = int(input())
    2
    >>> quantidade = 2
    >>> print('Se eu tenho ', quantidade, ' martelos, então seu peso será de ', peso * quantidade , ' kgs')
    Se eu tenho  2  martelos, então seu peso será de  4  kgs
    >>>  
```  
 
