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

Isso se deve ao fato de que o Python pode receber um valor vazio ou cheio. Como assim ? Vamos analisar um pequeno exemplo que vai clarear o erra cometido.  

```Python
    >>> interface = " "
    >>> if interface == " ":
    ...     print("Valor vazio!!!")
    ... else:
    ...     print("Valor cheio!!!")
    ... 
    Valor vazio!!!
    >>>
```

Como podemos notar, o valor de **interface** é **" "**, ou seja, vazio. Como a condição if ficou verdadeira, pois o valor é vazio, então ele escreve **Valor vazio!!!**. Se a interface tivesse algum valor, a condição if seria **falsa** e a ação seria a que estava em **else:**.  
Voltando no trecho:  
```Python
    >>> if interface == "Serial0/0" or "Serial0/1" or "Serial0/2":  
    ou
    >>> if interface == "Serial1/0" or "Serial1/1" or "Serial1/2":
```
a condição sempre será verdadeira. Veja só utilizamos o condicional **==** uma vez e depois **or "Serial0/1" or "Serial0/2"**, ou seja estamos dizendo variável **Serial0/0** ou variável **Serial0/2** e não estamos analisando mais o conteúdo da variável interface. Uma maneira de corrigir isso seria:

```Python
    >>> interface = "Serial0/0"
    >>> if interface == "Serial1/0" or interface == "Serial1/1" or interface == "Serial1/2":
    ...     print("Interface encontrada !")
    ... else:
    ...     print("Interface não encontrada !")
    ... 
    Interface não encontrada !
    >>>
```

Porém, aqui podemos combinar o uso de listas para ficar mais claro o nosso código:  

```Python
    >>> interface = "Serial0/0"
    >>> if interface == ("Serial1/0", "Serial1/1", "Serial1/2"):
    ...     print("Interface encontrada !")
    ... else:
    ...     print("Interface não encontrada !")
    ... 
    Interface não encontrada !
    >>>
```

### Condições if aninhadas

Agora vamos imaginar a seguinte situação. Queremos validar algumas condições do tipo:  

1. O equipamento está ativo ?
2. O equipamento é um roteador ou um switch layer3 ?
3. O protocolo OSPF está ativo ?
4. A interface principal está ativa ?
5. Existe uma interface Loopback ativa ?

Certo, então vamos escrever um código somente utilizando o **if** e o **else**. Depois iremos analisar o código gerado.

```Python
    # Variáveis de exemplo (modifique para testar diferentes cenários)
    equipamento_ativo = True
    tipo_equipamento = "roteador"
    ospf_ativo = True
    interface_principal_ativa = False
    loopback_ativa = True

    # Validação ruim com ifs aninhados
    if equipamento_ativo:
      print("1. Equipamento está ativo")
        if tipo_equipamento == "roteador":
            print("2. É um roteador")
            if ospf_ativo:
                print("3. OSPF está ativo")
                if interface_principal_ativa:
                    print("4. Interface principal está ativa")
                    if loopback_ativa:
                        print("5. Loopback ativa encontrada")
                    else:
                        print("5. Nenhuma loopback ativa encontrada")
                else:
                    print("4. Interface principal inativa")
                    if loopback_ativa:
                        print("5. Loopback ativa encontrada")
                    else:
                        print("5. Nenhuma loopback ativa encontrada")
            else:
                print("3. OSPF inativo")
                if interface_principal_ativa:
                    print("4. Interface principal está ativa")
                else:
                    print("4. Interface principal inativa")
        else:
            if tipo_equipamento == "switch_layer3":
                print("2. É switch layer3")
                if ospf_ativo:
                    print("3. OSPF está ativo")
                else:
                    print("3. OSPF inativo")
    else:
        print("1. Equipamento inativo")
        if tipo_equipamento == "roteador":
            print("2. É um roteador (mas está inativo)")
        else:
            print("2. É switch layer3 (mas está inativo)")
```

Ufa, terminamos o código. Mas ele está correto seguindo as boas práticas ? Vamos analisar.  
Dá pra perceber que este código está ruim, mas porquê ?  

| Problemas Encontrados                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Uso excessivo de **if**. (Muitos **if** aninhados)                                                                                    |
| 2. Dificuldade de manutenção. Uma simples alteração nesse código pode se tornar quase impossível de reverter até para quem o desenvolveu |
| 3. Baixa legibilidade. Esse código está muito difícil de entender                                                                        |
| 4. Como esse código está complexo, pode ser que ele não cubra todas as possibilidades.                                                   |
| 5. Podem existir mais problemas não observados e descritos.                                                                              |

Mas e como é possível ajustar um código desses ?  

| Boas Práticas                                           |
|---------------------------------------------------------|
| 1. Evite Aninhamento Excessivo (Níveis Máximos: 2-3)    |
| 2. Use "Early Return" para Simplificar                  |
| 3. Combine Condições com Operadores Lógicos (and, or)   |
| 4. Use Estruturas de Dados para Substituir Múltiplos if |
| 5. Comente Condições Complexas                          |

#### 1. Evite Aninhamento Excessivo (Níveis Máximos: 2-3)

**Problema:**
Múltiplos níveis de aninhamento tornam o código difícil de ler e manter ("Arrow Anti-Pattern").

**Solução:**

    Limite a 2-3 níveis de profundidade.
    Use funções auxiliares para dividir a lógica.

Exemplo Ruim (4+ níveis):

```Python

    if condição1:
        if condição2:
            if condição3:
                if condição4:  
                    print("Ok")
```

Exemplo Melhor (2 níveis):

```Python

    def validar_condição3(condição3, condição4):
        if condição3 and condição4:
            print("Ok")

    if condição1 and condição2:
        validar_condição3(condição3, condição4)
```














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