# Python - Básico 02

Agora que vimos o básico, vamos avançar um pouco mais e dar sequência nos estudo de Python.  

## Estruturas de dados - Listas, Tuplas, Set (conjunto) e Dicionários

Estas são estruturas capazes de armazenar dados.

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> tupla_produtos = ("Mercedes", "Ferrari", "Porche", "Jaguar")
    >>> set_produtos = {"Mercedes", "Ferrari", "Porche", "Jaguar"}
    >>> dic_produtos = {"Mercedes" : 20000, "Ferrari" : 100000, "Porche" : 500000, "Jaguar"  : 9000000}
    >>> type(lista_produtos)
    <class 'list'>
    >>> type(tupla_produtos)
    <class 'tuple'>
    >>> type(set_produtos)
    <class 'set'>
    >>> type(dic_produtos)
    <class 'dict'>
    >>>  
```
### Listas

As listas são as estruturas mais flexíveis. Elas podem armazenários vários tipos de dados (strings, números, objetos, etc.). Elas podem ser manipuladas, ou seja, podem ser adicionados ou removidos itens da lista.  
**OBS:** nas listas, os itens podem ser do mesmo tipo ou de tipos misturados.  
Cada item da lista tem uma posição, ou seja, cada item recebe um índice que pode ser acessado.  

#### Exemplo 01

```Python
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche', 'Jaguar']
    >>> print(lista_produtos[0])
    Mercedes
    >>> print(lista_produtos[2])
    Porche
    >>>
```  

Como podemos observar, os índices são representados entre [ ]. Os indices começam sempre em **0** e vão crescendo da esquerda para a direita. Mas se quisermos utilizar indices negativos, como -1 por exemplo, então os índices caminham da esquerda para  direita. 

### Exemplo 02

```Python
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche', 'Jaguar']
    >>> print(lista_produtos[0])
    Mercedes
    >>> print(lista_produtos[2])
    Porche
    >>> print(lista_produtos[-1])
    Jaguar
    >>> print(lista_produtos[-2])
    Porche
    >>>  
```

## Estruturas de controle (if, else, elif)


