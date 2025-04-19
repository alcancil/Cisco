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

#### 1. Acessar Elementos

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

#### 2. Fatiamento (Slicing)

Extrai uma sub-tupla:

```Python
    >>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
    >>> print(interfaces[1:3])
    ('GigabitEthernet0/1', 'GigabitEthernet0/2')
    >>>
```

#### 3. Concatenar Tuplas

Cria uma nova tupla combinando outras:

```Python
    >>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
    >>> interfaces_log = ("Loopback01", "Loopback02", "Loopaback03", "Loopback04")
    >>> print(interfaces + interfaces_log)
    ('GigabitEthernet0/0', 'GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3', 'Loopback01', 'Loopback02', 'Loopaback03', 'Loopback04')
    >>>
```

#### 4. Tamanho e Contagem

```Python
>>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
>>> vlans = ("10", "20", "30", "40", "50", "60","70", "80", "90", "100")
>>> print(len(interfaces))
4 # Retorna o número de itens dentro de interfaces
>>> print(vlans.count(100))
0 # Retornou 0 pois o valor precisar estar entre aspas
>>> print(vlans.count("90"))
1 # Retorna quantas vezes 90 está dentro da tupla vlans
>>> vlans1 = ("10", "20", "30", "40", "50", "60","70", "80", "90", "90", "90", "90", "100")
>>> print(vlans1.count("90"))
4 # Aqui retorna 4 vezes pois achou 4 vezes o item 90 dentro de vlans1
>>> 
```  

#### 5. Encontrar Índice de um Elemento

```Python
    >>> interfaces = ("GigabitEthernet0/0","GigabitEthernet0/1","GigabitEthernet0/2","GigabitEthernet0/3")
    >>> print(interfaces.index("GigabitEthernet0/2"))
    2 # Retorna o número do índice do elemento GigabitEthernet0/2
    >>>
```  

## Set

Set ou conjuntos também são parecidos com as listas porém as lista iniciam com [ ] e os **sets com { }** . Uma das características do set é que ele aceita letras, números, etc, porém ele não possui uma ordem. Então vamos supor que tenhamos um set e mandamos listar os elementos. Na primeira vez sai em uma ordem, na segunda em outra ordem e assim por diante. Outra característica é que dentro de um set não podem existir elementos com valores duplicados. Em set, também não existe a indexação do elemento como nas listas e tuplas.  

```Python
    >>> # Conjunto de VLANs
    >>> vlans = {10, 20, 30, 40}
    >>> # Conjunto de endereços IP
    >>> ips = set(["192.168.1.1", "10.0.0.1", "192.168.1.1"])  # Duplicado será removido
    >>> print(ips)  # Saída: {'10.0.0.1', '192.168.1.1'}
    {'10.0.0.1', '192.168.1.1'}
    >>>
```

## Operações Principais com Sets

#### 1. Adicionar e Remover Elementos

**.add():** Adiciona um elemento.

```Python
    >>> vlans = {10, 20, 30, 40}
    >>> vlans.add(50)
    >>> print(vlans)
    {40, 10, 50, 20, 30} # Adicionou a vlan 50 e imprimiu fora de ordem
    >>>
```

**.remove() ou .discard():** Remove um elemento (.discard() não gera erro se o elemento não existir).

```Python
    >>> vlans = {10, 20, 30, 40, 50}
    >>> vlans.remove(10)
    >>> print(vlans)
    {50, 20, 40, 30}
    >>> vlans.discard(99) # Não faz nada (sem erro)
    >>> print(vlans)
    {50, 20, 40, 30} 
    >>>
```

#### 2. Operações Matemáticas

**União (| ou .union()):**

```Python
    >>> vlan_switch1 = {10, 20, 30}
    >>> vlan_switch2 = {20, 40, 50}
    >>> todas_vlans = vlan_switch1 | vlan_switch2
    >>> print(todas_vlans)
    {50, 20, 40, 10, 30}
    >>>  
```

### 3. Interseção (& ou .intersection()):

```Python
>>> vlan_switch1 = {10, 20, 30}
>>> vlan_switch2 = {20, 40, 50}
>>> vlans_comuns = vlan_switch1 & vlan_switch2
>>> print(vlans_comuns)
{20}
>>>
```

#### 4. Diferença (- ou .difference()):

```Python
    >>> vlan_switch1 = {10, 20, 30}
    >>> vlan_switch2 = {20, 40, 50}
    >>> vlans_apenas_switch1 = vlan_switch1 - vlan_switch2
    >>> print(vlans_apenas_switch1)
    {10, 30}
    >>>
```

#### 5. Limpar o Set

```Python
    >>> vlans = {10, 20, 30, 40, 50}
    >>> print(vlans)
    {50, 20, 40, 10, 30}
    >>> vlans.clear()
    >>> print(vlans)
    set()
    >>>
```

## Dicionários

São estruturas que se parecem com listas mas trabalham com a estrutura de chave e valor. São declarados entre { }. Exemplo:

```Python
    # Dicionário de dispositivos e seus IPs
    dispositivos = {
        "R1": "192.168.1.1",
        "SW1": "10.0.0.2",
        "FW1": "172.16.0.1" 
    }
```

Agora quando vamos interagir com um dicionário, não vamos mais procurar um índice, e sim seu valor. Então podemos dizer que isso é uma especie bem reduzida de um banco de dados.  
Um exemplo clássico de um dicionário é uma lista telefônica. Vamos supor que eu precise saber o telefone de Jão. Então eu navego na lista até o nome João e depois vou ter o telefone dele.  



## Estruturas de controle (if, else, elif)


