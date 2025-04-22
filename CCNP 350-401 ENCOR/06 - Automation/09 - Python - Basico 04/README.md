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

### Múltiplas Condições - if + elif + else

Agora, imagine que queremos testar mais de uma condição. O que poderíamos fazer ?  
Nesse caso existe o **elif** que serve para colocar mais de uma condição.  

#### Exemplo 01

```Python
    >>> tipo_trafego = "voice"
    >>> if tipo_trafego == "voice":
    ...     print("Prioridade: Alta (QoS 5).")
    ... elif tipo_trafego == "video":
    ...     print("Prioridade: Média (QoS 4).")
    ... elif tipo_trafego == "data":
    ...     print("Prioridade: Baixa (QoS 1).")
    ... else:
    ...     print("Prioridade não definida.")
    ... 
    Prioridade: Alta (QoS 5).
    >>>
```

#### Exemplo 02

```Python
    >>> tipo_trafego = "video"
    >>> if tipo_trafego == "voice":
    ...     print("Prioridade: Alta (QoS 5).")
    ... elif tipo_trafego == "video":
    ...     print("Prioridade: Média (QoS 4).")
    ... elif tipo_trafego == "data":
    ...     print("Prioridade: Baixa (QoS 1).")
    ... else:
    ...     print("Prioridade não definida.")
    ... 
    Prioridade: Média (QoS 4).
    >>>
```

### if com operadores lógicos

#### Exemplo 01

```Python
    >>> interface = "Serial0/0"
    >>> status = "UP"
    >>> if interface == "Serial0/0" or status == "Down":
    ...     print("Interface identificada !")
    ... else:
    ...     print("Interface não identificada!")
    ... 
    Interface identificada !
    >>>
```

Nesse exemplo, utilizamos o **operador lógico or**. Nesse caso, **se (if)** uma condição ou outra for **True (Verdadeira)** então faça a ação, **senão (else)** tome a segunda opção. Então não precisamos que as duas condições sejam verdadeiras, basta que somente uma seja verdadeira.

#### Exemplo 02

```Python
    >>> interface = "Serial0/0"
    >>> if interface == "Serial0/0" or "Serial0/1" or "Serial0/2":
    ...     print("Interface encontrada !")
    ... else:
    ...     print("Interface não encontrada !")
    ... 
    Interface encontrada !
```

```Python
    >>> interface = "Serial0/0"
    >>> if interface == "Serial1/0" or "Serial1/1" or "Serial1/2":
    ...     print("Interface encontrada !")
    ... else:
    ...     print("Interface não encontrada !")
    ... 
    Interface encontrada !
    >>>
```

Como esses dois exemplos distintos deu o mesmo resultado ?  
Se analisarmos, os códigos são bem parecidos mas existe uma diferença importante. Aparentemente quando analisamos os dois códigos, quando vemos as linhas:  

```Python
    >>> if interface == "Serial0/0" or "Serial0/1" or "Serial0/2":  
    ou
    >>> if interface == "Serial1/0" or "Serial1/1" or "Serial1/2":
```
a nossa tendência é imaginar que o Python da seguinte maneira:  

#### Primeira linha:
"Se a interface **é igual a** "Serial1/0" ou **é igual a** "Serial0/1" ou **é igual a** "Serial0/2":
    então imprima "Interface encontrada !"  
uma vez que o valor de interface é Serial0/0.

#### Segunda linha:
Já nessa linha, a nossa tendencia é achar que a condição **if** não será atendida e já iremos cair em :
```Python
    ... else:
        ...     print("Interface não encontrada !")
```
o que não acontece.  

Isso se deve ao fato de que o Python pode receber um valor vazio ou cheio.

### Condições if aninhadas







Sintaxe Básica
python
Copy

if condição1:
    if condição2:
        # Executa se condição1 E condição2 forem True
    else:
        # Executa se condição1 for True, mas condição2 for False
else:
    # Executa se condição1 for False

🌐 Exemplo Prático (Automação de Redes)

Suponha que você queira validar:

    Se um dispositivo está acessível.

    Se está executando OSPF.

    Se a interface principal está ativa.

python
Copy

dispositivo_acessivel = True
ospf_ativado = True
interface_up = False

if dispositivo_acessivel:
    if ospf_ativado:
        if interface_up:
            print("Dispositivo operacional com OSPF e interface ativa.")
        else:
            print("ALERTA: Interface principal inativa!")
    else:
        print("OSPF não está ativado.")
else:
    print("Dispositivo inacessível.")

Saída:
Copy

ALERTA: Interface principal inativa!

✅ Quando Usar If Aninhados?

    Validações em Etapas: Quando uma condição depende da anterior (ex: só verifica OSPF se o dispositivo estiver acessível).

    Hierarquia de Decisões: Em cenários com múltiplos níveis de condições (ex: redes, segurança, QoS).

    Legibilidade Controlada: Se o aninhamento for limitado a 2-3 níveis e facilitar a compreensão.

❌ Quando Evitar If Aninhados?

    Muitos Níveis de Aninhamento:

        Código fica difícil de ler e manter (conhecido como "Arrow Anti-Pattern" ou "efeito flecha").

        Exemplo problemático:
        python
        Copy

        if cond1:
            if cond2:
                if cond3:
                    if cond4:  # <- Difícil de acompanhar!
                        print("Ok")

    Condições Independentes:

        Se as condições não dependem umas das outras, use if separados.

        ❌ Ruim:
        python
        Copy

        if dispositivo == "R1":
            if ip == "192.168.1.1":  # Condição não relacionada!
                print("R1 com IP 192.168.1.1")

        ✅ Melhor:
        python
        Copy

        if dispositivo == "R1" and ip == "192.168.1.1":
            print("R1 com IP 192.168.1.1")

🛠 Alternativas a If Aninhados
1. Operadores Lógicos (and, or)

Use para condições simples e relacionadas:
python
Copy

if dispositivo_acessivel and ospf_ativado and interface_up:
    print("Dispositivo operacional.")
elif dispositivo_acessivel and not ospf_ativado:
    print("OSPF desativado.")

2. Funções Separadas

Encapsule lógicas complexas em funções para melhor legibilidade:
python
Copy

def verificar_dispositivo(acessivel, ospf, interface):
    if not acessivel:
        return "Dispositivo inacessível."
    if not ospf:
        return "OSPF desativado."
    if not interface:
        return "Interface inativa."
    return "Dispositivo operacional."

print(verificar_dispositivo(True, True, False))

3. Dicionários para Mapeamento

Útil para substituir múltiplos elif:
python
Copy

acoes = {
    "up": "Interface ativa",
    "down": "Interface inativa",
    "shutdown": "Interface desligada"
}

status = "down"
print(acoes.get(status, "Status desconhecido"))

4. Early Returns

Em funções, retorne cedo para evitar aninhamento:
python
Copy

def backup_dispositivo(dispositivo):
    if not dispositivo["acessivel"]:
        return "Falha: dispositivo inacessível."
    if not dispositivo["backup_habilitado"]:
        return "Backup não habilitado."
    # Lógica principal aqui...
    return "Backup concluído."

💡 Dicas para o CCNP ENCOR

    Máximo de 2-3 Níveis: Se precisar de mais, refatore para funções ou lógicas booleanas.

    Comente Condições Complexas: Explique o propósito de cada nível.

    Teste Cada Condição Separadamente: Facilita a depuração.

📚 Exemplo Refatorado (Sem Aninhamento Excessivo)
python
Copy

# Versão legível com early returns e operadores lógicos
def verificar_dispositivo(acessivel, ospf, interface):
    if not acessivel:
        return "Dispositivo inacessível."
    if not ospf:
        return "OSPF desativado."
    return "Interface ativa." if interface else "Interface inativa."

print(verificar_dispositivo(True, True, False))

Saída:
Copy

Interface inativa.

⚡ Quando Aninhar é Aceitável?

    Em validações curtas (ex: verificar um JSON aninhado).

    Quando a lógica é claramente hierárquica (ex: redes → dispositivo → interface).