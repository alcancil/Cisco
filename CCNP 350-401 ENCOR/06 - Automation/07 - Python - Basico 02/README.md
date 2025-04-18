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
## Listas

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

### 1. Adicionar Itens  

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

 **.insert():** Adiciona em posição específica.

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche', 'Jaguar']
    >>> lista_produtos.insert(2, "Caminhonete")
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Caminhonete', 'Porche', 'Jaguar']
    >>> lista_produtos.insert(-1, "Lancha")
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Caminhonete', 'Porche', 'Lancha', 'Jaguar']
    >>>  
```  

### 2. Remover Itens

**.remove():** Remove pelo valor.
    
```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche', 'Jaguar']
    >>> lista_produtos.remove("Porche")
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Jaguar']
    >>>
```

**.pop():** Remove pelo índice (ou o último se não especificado).

### Exemplo 01

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> lista_produtos.pop(0)
    'Mercedes'
    >>> print(lista_produtos)
    ['Ferrari', 'Porche', 'Jaguar']
    >>>
```  

### Exemplo 02

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> lista_produtos.pop()
    'Jaguar'
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche']
    >>>  
```

**del:** Remove por índice ou fatia.

### Exemplo 01
    
```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> del lista_produtos[1] # Remove o item de índice 1
    >>> print(lista_produtos)
    ['Mercedes', 'Porche', 'Jaguar']
    >>>  
```  

### Exemplo 02

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> del lista_produtos[-1] # Remove o último item de índice -1 
    >>> print(lista_produtos)
    ['Mercedes', 'Ferrari', 'Porche']
    >>>  
```

### Exemplo 03

```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> del lista_produtos[1:3] # Remove do índice 1 ao 2
    >>> print(lista_produtos)
    ['Mercedes', 'Jaguar']
    >>>  
```  

### 3. Ordenação

**.sort():** Ordena a lista original.
    
```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> lista_produtos.sort()
    >>> print(lista_produtos)
    ['Ferrari', 'Jaguar', 'Mercedes', 'Porche']
    >>>  
```  

### 4. Tamanho da lista:
    
```Python
    >>> lista_produtos = ["Mercedes", "Ferrari", "Porche", "Jaguar"]
    >>> len(lista_produtos)
    4
    >>>
```  

## Tuplas

As tuplas são bem parecidas com listas. Então são estruturas que recebem valores que podem ser diferentes, repetidos, em ordem ou mesmo fora de ordem. A diferença é que são imutáveis, ou seja, não se pode alterar uma tupla. Ela funciona assim pois existem estruturas em Python que precisam retornar certas quantidades de valores, por exemplo, uma função. Imagine que você precise entrar somente dois valores nessa função e ela te retorne quatro valores. Nesse caso pode ser utilizada uma tupla para armazenar esses valores e garantir que não sejam alterados.  

**Sintaxe Básica**

Tuplas são definidas por parênteses () (ou sem parênteses, apenas com vírgulas):  

# Tupla de interfaces de roteador
interfaces = ("GigabitEthernet0/0", "GigabitEthernet0/1", "Serial0/0/0")  

# Tupla sem parênteses (válido)  
vlans = 10, 20, 30


#### E o que não se pode fazer com TUPLAS ?  

* Não se pode adicionar ou remover itens uma vez que ela é imutável
* Não se pode fazer uma ordenação direta com **.sort()** . Para isso é necessário se utilizar **.sorted()** que irá te retornar uma lista ordenada.

### Operações com Tuplas

1. Acessar Elementos

Funciona como listas (índices começam em 0):

```Python
    >>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
    >>> type(interfaces)
    <class 'tuple'>        
    >>> print(interfaces[0]) # Imprime o primeiro item
    GigabitEthernet0/0
    >>> print(interfaces[-1]) # Imprime o último item
    GigabitEthernet0/3
    >>>  
```

2. Fatiamento (Slicing)

Extrai uma sub-tupla:

```Python
    >>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
    >>> print(interfaces[1:3])
    ('GigabitEthernet0/1', 'GigabitEthernet0/2')
    >>>
```

3. Concatenar Tuplas

Cria uma nova tupla combinando outras:

```Python
    >>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
    >>> interfaces_log = ("Loopback01", "Loopback02", "Loopaback03", "Loopback04")
    >>> print(interfaces + interfaces_log)
    ('GigabitEthernet0/0', 'GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3', 'Loopback01', 'Loopback02', 'Loopaback03', 'Loopback04')
    >>>
```

4. Verificar Existência
python

if "GigabitEthernet0/0" in interfaces:
    print("Interface encontrada!")

5. Desempacotamento

Atribui elementos a variáveis:
python

interface1, interface2, interface3 = interfaces
print(interface2)  # Saída: "GigabitEthernet0/1"

6. Tamanho e Contagem
python

print(len(interfaces))  # Saída: 3 (número de elementos)
print(vlans.count(20))  # Saída: 1 (quantas vezes o valor 20 aparece)

7. Encontrar Índice de um Elemento
python

print(interfaces.index("Serial0/0/0"))  # Saída: 2

🚫 O Que Não é Possível Fazer com Tuplas?

    Adicionar/Remover Itens: Tuplas são imutáveis!
    python

interfaces.append("Loopback0")  # Erro: AttributeError
interfaces[0] = "FastEthernet0/0"  # Erro: TypeError

Ordenação Direta:
Tuplas não têm método .sort(). Use sorted() para criar uma nova lista ordenada:
python

sorted_interfaces = sorted(interfaces)  # Retorna uma lista!













## Estruturas de controle (if, else, elif)


