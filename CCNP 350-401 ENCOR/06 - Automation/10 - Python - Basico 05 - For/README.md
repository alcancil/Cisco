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

* <nome variável> : aqui o Python precisa de uma variável que irá ser utilizada na Iteração (repetição). Essa variável pode ser qualquer nome. 
* <iterável> : são os dados que vão ver utilizados no loop. Podem ser palavras, listas, dicionários, etc.
**OBS:**  existe uma convenção de que se a variável não vai ser utilizado em mais lugar algum do código utiliza-se **_** para demonstrar que a variável esta sendo utilizado somente nessa parte do código.  

Então vamos voltar ao nosso exemplo. Aqui utilizamos uma lista como o **iterável** do nosso loop. Então na sintaxe podemos ler da seguinte forma:  

```Go    
    para variavel em lista:     
        faça a ação01
        faça a ação02
        ...
    fim do loop
```

Agora vamos imaginar a seguinte situação: queremos imprimir na tela 100 itens. Teríamos que ter uma lista com 200 itens ? Para isso existe a função **range**. 

```Python
    >>> for interface in range(100):
    ...     print("Ethernet0/",interface)
    ... 
    Ethernet0/ 0
    Ethernet0/ 1
    Ethernet0/ 2
    Ethernet0/ 3
    Ethernet0/ 4
    Ethernet0/ 5
    Ethernet0/ 6
    ...
    Ethernet0/ 99
    >>>
```

O range funciona assim: ele começa no item 0 e vai até o 99, ai ele atinge os 100 itens. Então esse é um recurso interessante para utilizarmos.

Agora que aprendemos o que é o Loop for e sua sintaxe básica, vamos analisar alguns exemplos de como podemos utilizar o **for**.

1. Iterar em Listas (Exemplo: VLANs, Interfaces)

```Python
    >>> vlans = [10, 20, 30, 40]
    >>> for vlan in vlans:
    ...     print(f"Configurando Vlan {vlan}")
    ... 
    Configurando Vlan 10
    Configurando Vlan 20
    Configurando Vlan 30
    Configurando Vlan 40
    >>> 
```

Aqui é interessante observar o uso do print. Como podemos notar temos uma letra **f** agora dentro dos parênteses. Essa é uma nova forma de utilizar o print, são as chamadas **f strings**. Esse recurso foi introduzido no Python 3.6 e portanto só funciona nele ou em versões superiores.  
Essa é uma nova forma de formatação que nos permite inserir variáveis e expressões diretamente em strings utilizando chaves { }.  

**Sintaxe**  

```Python
    f"Texto {variável} mais texto"
```

Com esse novo método temos algumas vantagens.

* **Legibilidade**
  
```Python
    # Método antigo (format())
    print("Configurando VLAN {}".format(vlan))

    # Método ruim (concatenação)
    print("Configurando VLAN " + str(vlan))

    # F-string (recomendado)
    print(f"Configurando VLAN {vlan}")
```

* **Performance:** F-strings são mais rápidas que outras formas de formatação.

* **Expressões Diretas:** Você pode incluir operações dentro das chaves:

```Python
    print(f"Total de VLANs: {len(vlans)}")
```

2. Iterar em Dicionários (Exemplo: Dispositivos e IPs)

```Python
    >>> dispositivos = {"R1": "192.168.1.1", "SW1": "10.0.0.1", "FW1": "172.16.0.1"}
    >>> for nome, ip in dispositivos.items():
    ...     print(f"{nome} -> IP: {ip}")
    ... 
    R1 -> IP: 192.168.1.1
    SW1 -> IP: 10.0.0.1
    FW1 -> IP: 172.16.0.1
    >>>
```
Percebam que aqui no for foram utilizadas duas variáveis pois o dicionário trabalha com chave e valor.

3. Iterar em Strings (Exemplo: Processar Comandos)

```Python
    >>> comando = "show ip interface brief"
    >>> for caractere in comando:
    ...     if caractere == " ":
    ...             print("[ESPAÇO]")
    ...     else:
    ...             print(caractere)
    ... 
    s
    h
    o
    w
    [ESPAÇO]
    i
    p
    [ESPAÇO]
    i
    n
    t
    e
    r
    f
    a
    c
    e
    [ESPAÇO]
```

4. Usar range() para Repetições Numéricas

```Python
    >>> for i in range(5):
    ...     print(f"Enviando pacote ICMP {i + 1}/5")
    ... 
    Enviando pacote ICMP 1/5
    Enviando pacote ICMP 2/5
    Enviando pacote ICMP 3/5
    Enviando pacote ICMP 4/5
    Enviando pacote ICMP 5/5
    >>> 
```

5. Loop Aninhado (Exemplo: Interfaces por Dispositivo)

```Python
    >>> dispositivos = {
    ...                     "R1": ["Gig0/0", "Gig0/1", "Loopback0"],
    ...                     "SW1": ["Vlan10", "Vlan20"]
    ... }
    >>> for dispositivo, interfaces in dispositivos.items():
    ...     print(f"\nInterfaces de {dispositivo}:")
    ...     for interface in interfaces:
    ...             print(f" - {interface}")
    ... 

    Interfaces de R1:
     - Gig0/0
     - Gig0/1
    - Loopback0

    Interfaces de SW1:
     - Vlan10
     - Vlan20
    >>>
```
### Métodos Break e Continue

Esses métodos são utilizados para para **(Break)** ou continuar **(continue)** um loop. 

**Break**

    Finaliza o loop antecipadamente quando uma condição é atendida.  
    Economiza recursos ao evitar iterações desnecessárias.  

#### Exemplo 

Parar ao Encontrar um Dispositivo Inacessível  

```Python
    >>> interfaces = {
    ...     "GigabitEthernet0/0": "up",
    ...     "GigabitEthernet0/1": "down",
    ...     "GigabitEthernet0/2": "up",
    ...     "GigabitEthernet0/3": "down",
    ...     "Serial0/0/0": "up"
    ... }
    >>> 
    >>> print("Iniciando verificação de status das interfaces...\n")
    Iniciando verificação de status das interfaces...
    >>> 
    >>> for interface, status in interfaces.items():
    ...     print(f"Verificando interface {interface}... Status: {status}")
    ...     
    ...     if status == "down":
    ...         print(f"\nALERTA: Interface {interface} está DOWN!")
    ...         print("Enviando notificação para a equipe de rede...")
    ...         print("Interrompendo verificação para priorizar esta interface.")
    ...         break  # Sai do loop quando encontra a primeira interface down
    ... else:
    ...     print("\nTodas as interfaces estão operacionais (UP).")
    ... 
    Verificando interface GigabitEthernet0/0... Status: up
    Verificando interface GigabitEthernet0/1... Status: down
    ALERTA: Interface GigabitEthernet0/1 está DOWN!
    Enviando notificação para a equipe de rede...
    Interrompendo verificação para priorizar esta interface.
    >>> print("\nAção corretiva deve ser tomada para a interface problemática.")

    Ação corretiva deve ser tomada para a interface problemática.
    >>>
```
Para nosso exemplo, aqui temos um código um pouco maior e podemos notar o uso de **for**, **if** e **else**. Então o interessante nesse caso é que vamos varrer dentro do nosso dicionario de interfaces com o comando **for** pelas interfaces atrás daquela que tenha o status **down**.  
Mas o objetivo desse código é gerar um alerta se for encontrado alguma interface no status down. Então, ao encontrar a primeira interface com esse status, qual seria o sentido de continuarmos buscando mais interfaces com esse mesmo status se o nosso objetivo já foi atingido ?  
Portanto utilizamos um **break** para pararmos essa busca imediatamente uma vez que essa condição for atingida. Então esse é o objetivo do uso de **break** em loops.  

**Continue**

    Pula para a próxima iteração do loop (sem interromper).  

#### Exemplo

```Python
    [01] # Declaração das interfaces e estados em um dicionário
    [02] >>> interfaces = {
    [03] ...     "GigabitEthernet0/0": {"status": "up", "config": "correct", "admin": "up"},
    [04] ...     "GigabitEthernet0/1": {"status": "down", "config": "correct", "admin": "down"},
    [05] ...     "GigabitEthernet0/2": {"status": "up", "config": "incorrect", "admin": "up"},
    [06] ...     "GigabitEthernet0/3": {"status": "down", "config": "incorrect", "admin": "up"},
    [07] ...     "Loopback0": {"status": "up", "config": "correct", "admin": "up"}
    [08] ... }
    [09] >>> 
    [10] >>> print("Iniciando auditoria de configuração de interfaces...\n")
    [11] Iniciando auditoria de configuração de interfaces...
    [12]
    [13] >>> 
    [14] >>> for interface, data in interfaces.items():
    [15] ...     # Pular interfaces administrativamente desabilitadas
    [16] ...     if data["admin"] == "down":
    [17] ...         print(f"Pulando {interface} (administrativamente down)")
    [18] ...         continue  # Vai para a próxima iteração
    [19] ...         
    [20] ...     # Pular interfaces loopback (caso necessário)
    [21] ...     if interface.startswith("Loopback"):
    [22] ...         print(f"Pulando interface loopback {interface}")
    [23] ...         continue
    [24] ...             
    [25] ...     # Verificar apenas interfaces ativas com problemas
    [26] ...     if data["status"] == "up" and data["config"] == "incorrect":
    [27] ...         print(f"\nProblema encontrado na {interface}:")
    [29] ...         print(f" - Status: {data['status']}")
    [30] ...         print(f" - Configuração: {data['config']}")
    [31] ...         print("Aplicando configuração padrão...")
    [32] ... 
    [33] Pulando GigabitEthernet0/1 (administrativamente down)
    [35]
    [36] Problema encontrado na GigabitEthernet0/2:
    [37] - Status: up
    [38] - Configuração: incorrect
    [39] Aplicando configuração padrão...
    [40] Pulando interface loopback Loopback0
    [41] >>> print("\nAuditoria concluída para interfaces relevantes.")
    [42]
    [43] Auditoria concluída para interfaces relevantes.
    [44] >>>
````

Agora aqui o pensamento é o contrário do código anterior. Aqui queremos varrer nosso dicionário atrás das interfaces que estão no estado **down** e **admin**. Isso significa que essa interface está administrativamente desligada. Porém podemos reparar que se o segundo campo estiver como **correct** é porque essa interface foi definida para estar desligada no projeto.   


✅ Onde Aplicar o for em Automação de Redes?

    Configuração em Massa

        Aplicar a mesma configuração em múltiplas VLANs, interfaces ou dispositivos.
    python

for interface in ["Gig0/0", "Gig0/1", "Loopback0"]:
    print(f"interface {interface}\n description Configurada via Python")

Processamento de Saídas de Comandos

    Extrair informações de comandos como show ip interface brief.

python

output = ["Gig0/0  192.168.1.1  UP", "Gig0/1  10.0.0.1  DOWN"]
for linha in output:
    if "UP" in linha:
        print(f"Interface ativa: {linha.split()[0]}")

Testes de Conectividade

    Pingar uma lista de IPs.

python

ips = ["8.8.8.8", "192.168.1.1", "10.0.0.1"]
for ip in ips:
    os.system(f"ping -c 1 {ip}")

Filtrar Dados

    Separar interfaces ativas/inativas.

python

    interfaces = {"Gig0/0": "UP", "Gig0/1": "DOWN", "Loopback0": "UP"}
    for interface, status in interfaces.items():
        if status == "UP":
            print(f"{interface} está operacional")

❌ Onde Evitar o for?

    Quando Há Métodos Mais Diretos

        Use funções built-in como map(), filter(), ou list comprehensions para operações simples.
    python

    # Ruim:
    for ip in ips:
        ips_ativos.append(ip) if "UP" in ip else None

    # Melhor:
    ips_ativos = [ip for ip in ips if "UP" in ip]

    Processamento de Grandes Volumes de Dados

        Para arquivos muito grandes ou muitos dispositivos, prefira bibliotecas assíncronas (ex: asyncio) ou processamento em lotes.

    Operações que Podem Ser Vetorizadas

        Em bibliotecas como NumPy/Pandas, evite loops explícitos.

🛠 Melhores Práticas para for em Redes

    Use enumerate() para Acessar Índices
    python

interfaces = ["Gig0/0", "Gig0/1", "Loopback0"]
for idx, interface in enumerate(interfaces, start=1):
    print(f"Interface {idx}: {interface}")

Combine com break e continue

    break: Interrompe o loop (ex: ao encontrar um dispositivo inacessível).

    continue: Pula para a próxima iteração (ex: ignorar interfaces desativadas).

python

    for ip in ips:
        if not ping(ip):
            print(f"{ip} inacessível")
            break  # Sai do loop no primeiro falha

    Evite Loops Infinitos

        Sempre defina uma condição de saída clara.

🔍 Exemplo Completo: Backup de Configurações
python

dispositivos = ["R1", "R2", "SW1"]
for dispositivo in dispositivos:
    try:
        conexao = connect(dispositivo)
        backup = conexao.send_command("show running-config")
        with open(f"{dispositivo}_backup.txt", "w") as file:
            file.write(backup)
        print(f"Backup de {dispositivo} concluído!")
    except Exception as e:
        print(f"Falha no backup de {dispositivo}: {str(e)}")

Resumo

    Use for para:

        Iterar sobre listas, dicionários, strings.

        Automatizar configurações em massa.

        Processar saídas de comandos.

    Evite for quando:

        Operações podem ser feitas com métodos mais eficientes (ex: list comprehensions).

        Trabalhando com grandes volumes de dados (prefira processamento assíncrono).

Quer um exemplo específico para NAPALM ou Netmiko? Posso criar um script passo a passo! 🚀
New chat
