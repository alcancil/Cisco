# Python - Básico 04

Agora vamos ver um pouco sobre estruturas de repetição. 

## For

Agora chegou a hora de vermos um pouco sobre estruturas de Loop. Imagine que tenhamos uma tarefa que se repetitiva e manual. Essas são estruturas utilizadas para repetir ações ou um bloco de ações até que atinja a uma certa condição.

```Python
    >>> lista = ["Ethernet0/0", "Ethernet0/1", "Ethernet0/2", "Ethernet0/0"]
    >>> for variavel in lista:
    ...     print(variavel)
    Ethernet0/0
    Ethernet0/1
    Ethernet0/2
    Ethernet0/0
    >>>
```

Nesse exemplo, temos uma lista de interfaces de um equipamento e queremos imprimir interface por interface. Para ficar mais claro, eu poderia ter impresso a lista inteira, mas no caso eu quero percorrer a lista inteira e imprimir item por item. Então nossa sintaxe ficou assim:  

```Python
    for <nome variável> in <iterável>:
        ação01
        ação02
        ...
```

* <nome variável> : aqui o Python precisa de uma variável que irá ser utilizada na Iteração (repetição). Essa variável pode ser qualquer nome. **OBS:**
* <iterável>