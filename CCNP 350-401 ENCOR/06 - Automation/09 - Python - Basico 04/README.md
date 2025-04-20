# Python - Básico 04

Antes de avançarmos, precisamos ver um pouco sobre **Operadores Lógicos**

## Operadores Lógicos

Em Python, os operadores lógicos são usados para combinar ou inverter expressões condicionais, sendo essenciais para controle de fluxo (if, while, etc.) e automação de redes. Aqui estão os principais:
📌 Operadores Lógicos Básicos

| Operador	| Nome	| Exemplo	                 |  Descrição                                              |
|-----------|-------|----------------------------|---------------------------------------------------------|
|   and	    |  E    | x > 5 and x < 10           | Retorna True se ambas as condições forem verdadeiras.   |
|   or      |  OU   | y == "up" or y == "active" | Retorna True se pelo menos uma condição for verdadeira. |
|   not     |  NÃO  | not interface_down         | Inverte o valor booleano (True vira False e vice-versa).|






## Estruturas de controle (if, else, elif)














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

## Operações Principais com Dicionários
#### 1. Acessando Valores

```Python
    >>> dispositivos = {
...             "R1": "192.168.1.1",
...             "SW1": "10.0.0.2",
...             "FW1": "172.16.0.1" 
...         }
    >>> print(dispositivos["R1"])
    192.168.1.1
    >>>
```

##### Método seguro (evita KeyError se a chave não existir)

```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...             "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1" 
    ... }
    >>> print(dispositivos.get("SW1", "Dispositivo não encontrado"))
    10.0.0.2
    >>> print(dispositivos.get("SW2", "Dispositivo não encontrado"))
    Dispositivo não encontrado
    >>>
```

#### 2. Adicionando/Atualizando Itens

##### Adiciona novo item

```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...              "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1" 
    ...         }
    >>> print(dispositivos["R1"])
    192.168.1.1
    >>> dispositivos["R2"] = "192.168.1.2"
    >>> print(dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2', 'FW1': '172.16.0.1', 'R2': '192.168.1.2'}
    >>>
```

##### Atualiza valor existente

```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...             "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1"
    ...         }
    >>> print(dispositivos["R1"])
    192.168.1.1
    >>> dispositivos["R1"] = "10.0.0.1"
    >>> print(dispositivos["R1"])
    10.0.0.1
    >>> 
```

#### 3. Removendo Itens

###### Remove um item específico

```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...             "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1"
    ...         }
    >>> del dispositivos["FW1"]
   >>> print(dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2'}
    >>> 
```

##### Remove e retorna o valor

```Python
    >>> dispositivos = {
    ...             "SW1": "10.0.0.2",
    ...             "R1": "192.168.1.1",
    ...             "FW1": "172.16.0.1"
    ...         }
    >>> ip_sw1 = dispositivos.pop("SW1")
    >>> print(dispositivos)
    {'R1': '192.168.1.1', 'FW1': '172.16.0.1'}
    >>>
```

##### Remove todos os itens

    ```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...             "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1"
    ...         }
    >>> dispositivos.clear()
    >>> print(dispositivos)
    {}
    >>>
```

### 5. Métodos Úteis

#### Combina dois dicionários

```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...             "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1"
    ...         }
    >>> print(dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2', 'FW1': '172.16.0.1'}
    >>> dispositivos.update({"LB1": "192.168.3.1", "DNS1": "8.8.8.8"})
    >>> print(dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2', 'FW1': '172.16.0.1', 'LB1': '192.168.3.1', 'DNS1': '8.8.8.8'}
    >>> 
```

#### Cria cópia segura

```Python
    >>> dispositivos = {
    ...             "R1": "192.168.1.1",
    ...             "SW1": "10.0.0.2",
    ...             "FW1": "172.16.0.1"
    ...         }
    >>> print(dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2', 'FW1': '172.16.0.1'}
    >>> dispositivos.update({"LB1": "192.168.3.1", "DNS1": "8.8.8.8"})
    >>> print(dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2', 'FW1': '172.16.0.1', 'LB1': '192.168.3.1', 'DNS1': '8.8.8.8'}
    >>> copia_dispositivos = dispositivos.copy()
    >>> print(copia_dispositivos)
    {'R1': '192.168.1.1', 'SW1': '10.0.0.2', 'FW1': '172.16.0.1', 'LB1': '192.168.3.1', 'DNS1': '8.8.8.8'}
    >>>
```

#### Listar chaves

```Python
>>> chaves = dispositivos.keys()
>>> print(chaves)
dict_keys(['R1', 'SW1', 'FW1', 'LB1', 'DNS1'])
```

#### Listar valores

```Python
    >>> valores = dispositivos.values() # Lista de valores
    >>> print(valores)
    dict_values(['192.168.1.1', '10.0.0.2', '172.16.0.1', '192.168.3.1', '8.8.8.8'])
    >>>
```




