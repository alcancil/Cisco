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

Como podemos observar, os índices são representados entre [ ]. Os indices começam sempre em **0** e vão crescendo da esquerda para a direita. Mas se quisermos utilizar indices negativos, como -1 por exemplo, então os índices caminham da esquerda para  direita sendo que, **0** sempre é o primeiro item e -1 é sempre o último item. 

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

### Operações Comuns em Listas

1. Adicionar Itens  

    **.append():** Adiciona ao final.  

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche', 'Jaguar']
    >>> lista_produtos.append("Moto")
    >>> prnt(lista_produtos)
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche', 'Jaguar', 'Moto']
    >>>  
```

```Python

```

    dispositivos.append("R3")  # ["R1", "R2", "SW1", "FW1", "R3"]

    .insert(): Adiciona em posição específica.
    python
    Copy

    dispositivos.insert(1, "LB1")  # ["R1", "LB1", "R2", "SW1", "FW1"]

3. Remover Itens

    .remove(): Remove pelo valor.
    python
    Copy

    dispositivos.remove("SW1")  # Remove "SW1"

    .pop(): Remove pelo índice (ou o último se não especificado).
    python
    Copy

    dispositivos.pop(0)  # Remove "R1"

    del: Remove por índice ou fatia.
    python
    Copy

    del dispositivos[1:3]  # Remove do índice 1 ao 2

4. Ordenação

    .sort(): Ordena a lista original.
    python
    Copy

    dispositivos.sort()  # ["FW1", "LB1", "R1", "R2"]

    sorted(): Retorna uma nova lista ordenada (sem alterar a original).
    python
    Copy

    ordenados = sorted(dispositivos)

5. Outras Operações Úteis

    Tamanho da lista:
    python
    Copy

    len(dispositivos)  # Retorna 4

    Verificar existência:
    python
    Copy

    if "R1" in dispositivos:
        print("R1 está na lista!")

    Fatiamento (slicing):
    python
    Copy

    print(dispositivos[1:3])  # ["R2", "SW1"]



## Estruturas de controle (if, else, elif)


