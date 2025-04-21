# Python - Básico 04

Antes de avançarmos, precisamos ver um pouco sobre **Operadores Lógicos**

## Operadores Lógicos

Em Python, os operadores lógicos são usados para combinar ou inverter expressões condicionais, sendo essenciais para controle de fluxo (if, while, etc.) e automação de redes. Aqui estão os principais:

### Operadores Lógicos Básicos

| Operador	| Nome	| Exemplo	                 |  Descrição                                              |
|-----------|-------|----------------------------|---------------------------------------------------------|
|   ==      | IGUAL | x == 100                   | A variável x é igual a 5
|   and	    |  E    | x > 5 and x < 10           | Retorna True se ambas as condições forem verdadeiras.   |
|   or      |  OU   | y == "up" or y == "active" | Retorna True se pelo menos uma condição for verdadeira. |
|   not     |  NÃO  | not interface_down         | Inverte o valor booleano (True vira False e vice-versa).|  

### Operadores Bit a Bit (Para Tarefas Avançadas)

Embora não sejam estritamente "lógicos", são úteis em redes para manipulação de máscaras e flags:  

| Operador | Nome  |  Exemplo	        |  Descrição                               |
|----------|-------|--------------------|------------------------------------------|
|    &     |  AND  |  flags & 0b1000    |  Comparação bit a bit (E).               |
|    \|    |  OR   |  flags \| 0b0010	|  Comparação bit a bit (OU).              |
|    ^     |  XOR  |  mask ^ 0b11110000	|  Retorna 1 onde os bits forem diferentes.|

## Estruturas de controle (if, else, elif)

Essas são estruturas que servem para realizar ações se passarem em algumas condições. Como assim ? Ao invés de realizarmos um código que vai executar tudo linha a linha de foma linear, o código testa uma condição e se atender essa condição ele executa uma, ou algumas ações.  
Mas e o que o acontece se a condição não for atendida ? Bom, por padrão o código não faz nada, ou seja, ele passa por essa estrutura, testa a condição e ao terminar o teste ele volta exatamente para a próxima linha após os testes.  
Agora se queremos que o código teste uma condição e se não passar na condição execute uma ação, ai devemos executar o else.   
Podemos traduzir o "if" e o "else" como "se" e "senão". Então uma condição poderia ficar assim: " Se nome_interface é igual a Ethernet0/0 então escreva Interface encontrada ".  
Podemos pensar assim, "Se condição 1 for atendida, execute ação 1 Senão execute ação 2". Vamos a alguns exemplos.

### Sintaxe básica

```Python
    if condição1:
    # Código se condição1 for True
```   

#### Exemplo 01

```Python
    >>> interface = "Serial0/0"
    >>> if interface == "Serial0/0" :
    ...     print(interface)
    ... 
    Serial0/0
    >>>
```  

Vamos analisar a estrutura. Nesse exemplo temos a primeira condição que podemos ler dessa maneira: "Se a variável **interface** for igual a **Serial0/0**" ai vem a ação: "Mostre o conteúdo da variável **Serial0/0".  
Perceba que a ação, no nosso caso **print(interface)**, na está escrita na mesma direção de if. Ele tem espaço, um **tab**. Esse espaço se chama **indentação** que deve ser consistente. Então tudo o que estiver dentro desse espaço va estar dentro dessa condição. Quando a condição acaba, o código volta a ser escrito sem o tab. Então dentro das ações, podemos ter uma ou mais ações.  

#### Exemplo 02

```Python
    >>> interface = "Serial0/0"
    >>> if interface == "Serial0/0" :
    ...     print(interface) # Ação 01
    ...     print("A condição é true") # Ação 02
    ... 
    Serial0/0
    A condição é true
    >>>
```  

#### Exemplo 03

```Python
    >>> interface = "Serial0/1"
    >>> if interface == "Serial0/0" :
    ...     print(interface)
    ... 
    >>>
```

Aqui podemos ver que o código não retorna nada. Mas o porque disso ?  
Isso acontece pois agora a condição é **false** e depois da condição não temos mais nada no código. Então, nesse caso, o código não retorna nada.  

### Escolha Binária - if + else

Quando usar: Quando há apenas duas opções possíveis (True/False).

#### Exemplo 01 
    
```Python
    >>> login_sucesso = "verdade"
    >>> if login_sucesso == "verdade":
    ...     print("Login efetuado com sucesso!")
    ... else:
    ...     print("Login não efetuado!")
    ... 
    Login efetuado com sucesso!
    >>> 
```  

#### Exemplo 02

```Python
    >>> if login_sucesso == "falso":
    ...     print("Login efetuado com sucesso!")
    ... else:
    ...     print("Login não efetuado!")
    ... 
    Login não efetuado!
    >>>
```