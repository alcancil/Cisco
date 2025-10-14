# Índice

- [Índice](#índice)
  - [05 - Exemplo Prático - PIM Dense Mode](#05---exemplo-prático---pim-dense-mode)
    - [Explicação do Cenário](#explicação-do-cenário)
    - [Testes Preliminares](#testes-preliminares)
    - [Onde o PIM deve ser ativado](#onde-o-pim-deve-ser-ativado)
  - [Função do DR no PIM Dense Mode](#função-do-dr-no-pim-dense-mode)
    - [Contexto: Por que o PIM precisa de um DR?](#contexto-por-que-o-pim-precisa-de-um-dr)
    - [Processo de Eleição do DR no PIM Dense Mode](#processo-de-eleição-do-dr-no-pim-dense-mode)
    - [Função prática do DR no PIM Dense Mode](#função-prática-do-dr-no-pim-dense-mode)
    - [Resumo rápido](#resumo-rápido)
  - [Endereço Multicast 224.0.0.13](#endereço-multicast-2240013)
    - [Revisão](#revisão)
    - [Resumo prático](#resumo-prático)
  - [Explicação da Tabela de roteamento multicast](#explicação-da-tabela-de-roteamento-multicast)

## 05 - Exemplo Prático - PIM Dense Mode

### Explicação do Cenário

Agora que vimos a teoria é hora de praticar. A primeira coisa que precisa ser dita que o **multicast é um serviço** e, portanto, precisamos aplicar ele em um cenário que já está pronto e funcional.  

![cenário](Imagens/cenario.png)  

Nesse cenário estamos utilizando **seis roteadores**.  

Sim, isso mesmo — os “hosts” são, na verdade, **roteadores disfarçados de hosts**, e por isso não realizaremos muitas configurações neles.  

Nos demais roteadores, que estão interligados entre si, foi configurado apenas o protocolo de roteamento dinâmico **OSPF**, garantindo que todas as redes já possuam **conectividade IP completa** antes de ativarmos o multicast.  

O que precisamos entender aqui é que o **PIM Dense Mode** funciona segundo o princípio **“flood and prune”**.  
Mas o que isso significa?  

Quando o processo de comunicação multicast se inicia, o protocolo PIM envia o tráfego multicast por todos os caminhos possíveis (flood), **até descobrir quais roteadores possuem receptores interessados** naquele grupo multicast.  
Os caminhos que **não possuem hosts interessados** são posteriormente **“podados” (pruned)** da árvore de distribuição, otimizando o fluxo.  

Nesse exemplo, o **Host01 (Server)** será a **fonte** da comunicação multicast, enquanto apenas o **Host03** será o **receptor** interessado nesse tráfego.  

### Testes Preliminares

Agora vamos acessar o SERVER e vamos garantir que existe comunicação entre todos os hosts.  
**OBS:** nos roteadores eu configurei interfaces de LOOPABCK. Então R01 tem o ip 1.1.1.1 /32, R02 tem o ip 2.2.2.2 /32 e R03 tem o ip 3.3.3.3 /32 .  

![01](Imagens/01.png)

Com isso, podemos ver que todos os hosts se alcançam e se comunicam. Mas o mais importante é observer a a tabela de roteamento para podermos entender um conceito simples.  

![02](Imagens/02.png)  

Essa é a tabela de roteamento em R01. Estamos acostumados a analisar essa tabela para verificarmos se o roteamento dinâmico está funcionando corretamente e não temos nenhum problema. Porém uma coisa que não é muito falada e que pode passar despercebida no primeiro momento é que essa tabela é como se fosse um bando de dados onde é feito o mapeamento da comunicação das redes que agora se dá em **unicast**. Ou seja, um host vai se comunicar diretamente com o outro, ou seja, comunicação de **um para um.**  

No nosso caso queremos ter a comunicação **de um para um grupo**, ou seja, **comunicação multicast**. Então nosso papel aqui é montar a árvore de comuniçação que já foi explicada anteriormente. Essa árvore é como se fosse uma tabela de roteamento só que agora multicast.  

Então a primeira coisa que precisamos verificar é se o **roteamento multicast está ativo** no equipamento.  

```ios
R01#show ip multicast  
  Multicast Routing: disabled  
  Multicast Multipath: disabled  
  Multicast Route limit: No limit  
  Multicast Triggered RPF check: enabled  
  Multicast Fallback group mode: Sparse  
  Multicast DVMRP Interoperability: disabled  
  Number of multicast boundaries configured with filter-autorp option: 0  
R01#  
```

Certo, como podemos ver, o roteamento multicast não está ativo. Então vamos ativar o mesmo.  

>R01(config)#ip multicast-routing  

Só para confirmar, vamos rodar o mesmo comando mais uma vez.  

```ios
R01#show ip multicast  
  Multicast Routing: enabled  
  Multicast Multipath: disabled  
  Multicast Route limit: No limit  
  Multicast Triggered RPF check: enabled  
  Multicast Fallback group mode: Sparse  
  Multicast DVMRP Interoperability: disabled  
  Number of multicast boundaries configured with filter-autorp option: 0  
R01#  
```

Agora que temos o roteamento multicast ativo, precisamos ativar o protocolo **PIM**. Esse protocolo deve ser ativado nas interfaces onde a comunicação ira ocorrer.  

### Onde o PIM deve ser ativado

No modo **Dense Mode (PIM-DM)**, o tráfego multicast é floodado por todas as interfaces que participam do domínio multicast.  

👉 Portanto, você deve ativar o PIM **em todas as interfaces que participam do caminho multicast** — ou seja, interfaces que interligam roteadores e também interfaces conectadas a redes com hosts (fontes ou receptores).  

✅ **Resumo da regra prática:**  

- Ative o PIM nas interfaces que têm roteadores vizinhos PIM e nas interfaces onde há fontes ou receptores multicast.  

🌀 **Sobre interfaces de Loopback (muito importante)**  

- Não é necessário ativar PIM em interfaces Loopback, a menos que ela seja usada como origem do tráfego multicast (por exemplo, um servidor multicast rodando em 1.1.1.1).  

- Por padrão, o PIM trabalha nas interfaces que realmente encaminham tráfego multicast (as físicas).  

- A Loopback costuma ser usada apenas como Router-ID, endereço de origem de OSPF/PIM, ou fonte lógica (RP) em cenários de Sparse Mode — não é o caso aqui.  

Portanto, no nosso cenário vamos entrar no roteador R01 vamos ativar o PIM em todas as interfaces que estão ativas e vão fazer parte do multicast.  

```ios
 R01>ena  
 R01#show ip int br  
  Interface                  IP-Address      OK? Method Status                Protocol  
  FastEthernet0/0            10.0.0.1        YES NVRAM  up                    up  
  FastEthernet0/1            10.0.0.9        YES NVRAM  up                    up  
  FastEthernet1/0            192.168.10.254  YES NVRAM  up                    up  
  Loopback0                  1.1.1.1         YES NVRAM  up                    up  
 R01#conf t  
 Enter configuration commands, one per line.  End with CNTL/Z.  
 R01(config)#int f0/0  
 R01(config-if)#ip pim dense-mode  
 R01(config-if)#  
 *Mar  1 03:53:26.735: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.1 on interface FastEthernet0/0  
 R01(config-if)#int f0/1  
 R01(config-if)#ip pim dense-mode  
 R01(config-if)#  
 *Mar  1 03:53:48.687: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.9 on interface FastEthernet0/1  
 R01(config-if)#ip pim  
 R01(config-if)#int f1/0  
 R01(config-if)#ip pim dense-mode  
 R01(config-if)#  
 *Mar  1 03:54:21.635: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 192.168.10.254 on interface FastEthernet1/0  
 R01(config-if)#  
```

Agora que ativamos o **PIM DENSE-MODE** podemos observar que nos é exibida uma mensagem de aviso (log nível 5)  
  
***Mar  1 03:54:21.635: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 192.168.10.254 on interface FastEthernet1/0**  
  
Essa mensagem se dá por conta do processo de eleição do **DR (Designated Router)**. Apesar dessa mensagem gerar uma dúvida, isso não tem nada a ver com o protocolo OSPF. Apenas ocorre uma coincidência nas nomenclaturas: **DR (Designated Router)** pois nos dois protocolos é mesma nomenclatura.  

## Função do DR no PIM Dense Mode

No PIM Dense Mode, a comunicação multicast funciona com o método Flood and Prune:

- Inicialmente, o tráfego multicast é enviado para todos os roteadores PIM;
- Os roteadores que não têm receptores interessados enviam mensagens Prune, pedindo para parar de receber o fluxo.
- O Designated Router é quem:
- Inicia o envio do fluxo multicast para a LAN;
- Coordena a poda (prune) quando não há interesse local;
- Evita duplicação de pacotes multicast quando há mais de um roteador conectado à mesma rede.  

### Contexto: Por que o PIM precisa de um DR?  

Em uma rede multiacesso (como um segmento Ethernet), podem existir vários roteadores PIM conectados à mesma sub-rede.  
Quando um host multicast envia tráfego para um grupo (ex: 239.1.1.1), todos os roteadores PIM na LAN recebem esse tráfego.  

- Se todos eles repassassem o fluxo multicast ao mesmo tempo, haveria duplicação de pacotes e loops.  
  
Por isso, o PIM precisa eleger um único roteador que será responsável por reencaminhar o tráfego multicast na LAN — esse é o Designated Router (DR).  

### Processo de Eleição do DR no PIM Dense Mode

A eleição é baseada nas mensagens PIM Hello, trocadas periodicamente entre os roteadores.

🔹 **Etapa 1 — Envio de mensagens Hello**

Todos os roteadores PIM em uma interface enviam mensagens Hello periodicamente (a cada 30 segundos por padrão).  
Essas mensagens contêm informações como:  

- IP da interface de origem
- Prioridade do DR (DR Priority)
- Temporizador de Hello  

O comando **debug ip pim ou show ip pim interface** permite ver esses parâmetros.

🔹 **Etapa 2 — Comparação dos parâmetros**

Ao receber Hellos dos vizinhos, cada roteador compara sua prioridade com as dos outros:  

- Maior prioridade vence.
- Por padrão, o valor é 1 em todos os roteadores.

Pode ser alterado com:  

> interface FastEthernet0/0
> ip pim dr-priority <valor>  

🔹 **Etapa 3 — Eleição e anúncio do DR**

Quando um roteador identifica que ele possui a maior prioridade (ou maior IP em empate), ele se declara DR.  
O Cisco IOS registra isso com mensagens como:  

> %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 192.168.10.254 on interface FastEthernet1/0

📘 Interpretação:  

- O campo from neighbor 0.0.0.0 indica que não havia DR anterior.
- O novo DR é o roteador cujo IP é 192.168.10.254 (o próprio).  

🔹 **Etapa 4 — Manutenção do DR**  

Enquanto o DR estiver ativo e enviando Hellos, os outros roteadores não tentam assumir o papel.  
Se o DR parar de enviar Hellos (por falha, interface down ou perda de conectividade), os demais roteadores detectam a ausência e refazem a eleição automaticamente.  

### Função prática do DR no PIM Dense Mode

O DR atua como ponto central para:  

- Registrar as fontes (quando há hosts multicast na LAN).
- Enviar os pacotes multicast iniciais no modo flood.
- Responder a mensagens IGMP vindas dos hosts receptores. 

Ou seja, o DR é quem fala com os hosts (via IGMP) e com os outros roteadores (via PIM).  

**🔍 Exemplo prático**

Imagine três roteadores PIM ligados à mesma rede 192.168.10.0/24:

| Roteador | IP da Interface | Prioridade PIM |
|----------|-----------------|----------------|
| R1       | 192.168.10.1    |       1        |
| R2       | 192.168.10.2    |       1        |
| R3       | 192.168.10.3    |       5        |

➡️ Resultado:  

O R3 será o Designated Router, pois tem maior prioridade (5).  
Se R3 cair, a eleição é refeita: o DR passa a ser R2 (maior IP entre os restantes).  

### Resumo rápido

| Etapa | Descrição                                                  |
|-------|------------------------------------------------------------|
| 1️⃣    | Todos enviam mensagens PIM Hello                           |
| 2️⃣    | Comparam prioridade (dr-priority)                          |
| 3️⃣    | Empate → vence o maior IP da interface                     |
| 4️⃣    | Roteador vencedor se torna o DR                            |
| 5️⃣    | DR é responsável pelo tráfego multicast e comunicação IGMP |
| 6️⃣    | Se o DR falhar → nova eleição automática                   |

Agora vamos confirmar isso com o **Whireshark** Vamos ligar ele na interface de R01 que está ligada ao nosso HOST01 (SERVER) e vamos procurar pelas mensagens Hello do protocolo PIM.  

![hello](Imagens/03.png)  

Como podemos ver, a mensagem **Hello** é originada do IP 192.168.0.254, que é o IP do nosso SERVER com origem para **224.0.0.13**  

## Endereço Multicast 224.0.0.13

| Campo               | Valor                                              |
|---------------------|----------------------------------------------------|
| Endereço IPv4       | 224.0.0.13                                         |
| Nome reservado      | ALL-PIM-ROUTERS                                    |
| Protocolo associado | Protocol Independent Multicast (PIM)               |
| Escopo              | Local-link (não é roteável)                        |
| Função              | Comunicação entre roteadores PIM no mesmo segmento |  

E dentro do pacote:  

- Option 19: DR Priority: 1
- Option 20: Generation ID: 488683522
- Option 21: State-Refresh: Version = 1, Interval = 0s

Essas opções são usadas justamente para o processo de eleição do DR e detecção de vizinhos.  

**🔍 O papel do endereço 224.0.0.13 em resumo**

| Função                           | Descrição                                                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Descoberta de vizinhos           | Os roteadores PIM enviam Hellos para 224.0.0.13 e escutam nesse grupo para saber quem mais está no mesmo segmento. |
| Eleição de DR                    | As mensagens Hello trocadas via 224.0.0.13 contêm o campo de prioridade que define quem será o DR.                 |
| Troca de informações de controle | Outras mensagens PIM (Join/Prune, Assert, Register Stop, etc.) também usam esse grupo.                             |
| Escopo local (não roteável)      | Pacotes para 224.0.0.13 nunca saem da rede local — são sempre TTL=1.                                               |  

### Revisão

A tabela abaixo mostra outros endereços multicast da faixa 224.0.0.x, usados por protocolos de roteamento e gerenciamento:

| Endereço   | Nome                  | Usado por                 |
|------------|-----------------------|---------------------------|
| 224.0.0.1  | All Hosts             | Todos os hosts multicast  |
| 224.0.0.2  | All Routers           | Todos os roteadores       |
| 224.0.0.5  | All OSPF Routers      | OSPF                      |
| 224.0.0.6  | OSPF DR/BDR Routers   | OSPF                      |
| 224.0.0.9  | RIPng Routers         | RIPng                     |
| 224.0.0.10 | EIGRP Routers         | EIGRP                     |
| 224.0.0.13 | All PIM Routers       | PIMv2                     |
| 224.0.0.18 | VRRP Routers          | VRRP                      |  

### Resumo prático

🔹 Quem envia: todo roteador com ip pim dense-mode (ou sparse, etc.) ativo em uma interface.  
🔹 Quem recebe: todos os roteadores PIM do mesmo segmento (escutando 224.0.0.13).  
🔹 TTL = 1: os pacotes nunca são roteados.  

Usado para:

- Descoberta de vizinhos PIM
- Eleição de DR
- Comunicação de controle  

Agora que entendemos, o inicio do processo, vamos analisar a tabela de roteamento multicast. Aqui é importante que esse é o ponto de criação de nossa árvore multicast.  
O comando fica:  

> R01#show ip mroute  

E o resultado é a saída:  

```ios
 IP Multicast Routing Table
 Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,  
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,  
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,  
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,  
       U - URD, I - Received Source Specific Host Report,  
       Z - Multicast Tunnel, z - MDT-data group sender,  
       Y - Joined MDT-data group, y - Sending to MDT-data group  
 Outgoing interface flags: H - Hardware switched, A - Assert winner  
 Timers: Uptime/Expires  
 Interface state: Interface, Next-Hop or VCD, State/Mode  
  
 (*, 224.0.1.40), 00:00:20/00:02:40, RP 0.0.0.0, flags: DCL  
  Incoming interface: Null, RPF nbr 0.0.0.0  
  Outgoing interface list:  
    FastEthernet0/0, Forward/Dense, 00:00:20/00:00:00  
  
 R01#  
```

## Explicação da Tabela de roteamento multicast

Como essa tabela é diferente da tabela de roteamento tradicional, vamos analisar suas entradas.  

🔹 Linha principal:  

```ios
(*, 224.0.1.40), 00:00:20/00:02:40, RP 0.0.0.0, flags: DCL 
```

- (*, 224.0.1.40) → É uma entrada (*,G), ou seja, “para qualquer origem (*), grupo 224.0.1.40”.  
Isso indica que qualquer fonte enviando para esse grupo será tratada por essa entrada (é o estado compartilhado).  
  
- 00:00:20/00:02:40 → Tempo desde que a entrada foi criada (uptime) e quanto tempo falta para expirar (expire time).  
  
- RP 0.0.0.0 → O RP (Rendezvous Point) é 0.0.0.0 porque o modo é PIM Dense Mode, que não usa RP (só o Sparse Mode usa RP).  
  
- flags: DCL  

Cada letra indica um estado:

  D → Dense-mode entry

  C → Connected (a origem está diretamente conectada)

  L → Local (o roteador faz parte do grupo — ou recebeu IGMP localmente)  

🔹 Próxima parte:  

```ios
Incoming interface: Null, RPF nbr 0.0.0.0  
```

- **Incoming interface: Null** → Ainda não há uma origem (S,G) conhecida enviando tráfego multicast. Ou seja, o roteador conhece o grupo, mas não sabe ainda de onde vem o fluxo.  
- **RPF nbr 0.0.0.0** → O Reverse Path Forwarding neighbor (vizinho RPF) não está definido, pois ainda não há rota multicast para a origem.  

🔹 Saídas (onde o tráfego será enviado):  

```ios
Outgoing interface list:  
  FastEthernet0/0, Forward/Dense, 00:00:20/00:00:00  
```

- O tráfego multicast (quando chegar) será encaminhado pela interface FastEthernet0/0.  
- Forward/Dense → indica que o tráfego será reenviado (forwarded) no modo dense-mode.  
- Timers → mostram há quanto tempo o estado está ativo e quando expira.  

💡 **Em outras palavras:**  
O roteador R01 está participando do grupo 224.0.1.40, aprendeu via IGMP local, ainda não recebeu tráfego multicast, mas já sabe por onde reenviar quando ele aparecer.  
  
**224.0.1.40 — Cisco RP-Announce (Auto-RP Announcement) - Grupo proprietário da Cisco**  

Esse endereço é usado pelo protocolo Cisco Auto-RP, que faz parte do PIM (Protocol Independent Multicast), modo Sparse.  
Mesmo que você esteja usando Dense Mode, os roteadores Cisco ainda escutam alguns grupos multicast padrão (como o 224.0.1.40), especialmente se o PIM estiver ativado — por isso ele aparece na tabela.  

🔹 **Função do grupo 224.0.1.40**  
  
- Utilizado por Candidatos a RP (Rendezvous Point) para anunciar suas informações a todos os roteadores.  
- Em outras palavras, roteadores que querem ser RP enviam suas mensagens de anúncio (RP-Announce) para o grupo 224.0.1.40.  
  
🔹 **Complemento: o 224.0.1.39**
  
- Esse é o outro grupo relacionado:  
224.0.1.39 — Cisco RP-Discovery (Auto-RP Discovery)  
É usado pelos roteadores para descobrir quem são os RPs disponíveis.  
Ou seja, os Mapping Agents escutam 224.0.1.40 e enviam informações no 224.0.1.39.  
  
**📘 Resumo prático**  

| Grupo      |Função                       | Descrição                                        |
|------------|-----------------------------|--------------------------------------------------|
| 224.0.0.13 | PIM Hello                   | Troca de mensagens entre roteadores PIM vizinhos |
| 224.0.1.39 | Auto-RP Discovery           | Distribui mapeamentos RP para os roteadores      |
| 224.0.1.40 | Auto-RP Announcement        | Roteadores candidatos a RP anunciam sua função   |
| 224.0.0.x  | Multicast de link-local     | Não roteável (apenas dentro do segmento local)   |
| 224.0.1.x  | Multicast global (roteável) | Pode atravessar roteadores                       |  

Para verificarmos em quais interfaces foram configurados o protocolo PIm, vamos executar o comando:

```ios
R01#show ip pim interface

Address          Interface                Ver/   Nbr    Query  DR     DR
                                          Mode   Count  Intvl  Prior
10.0.0.1         FastEthernet0/0          v2/D   0      30     1      10.0.0.1
10.0.0.9         FastEthernet0/1          v2/D   0      30     1      10.0.0.9
192.168.10.254   FastEthernet1/0          v2/D   0      30     1      192.168.10.254
R01#
```

Agora que demos o inicio da criação da nossa árvore, precisamos fazer as mesmas configurações nos outros roteadores R02 e R03.  
Vamos acessar R02 agora e aplicar os mesmos comandos nas interfaces.  

```ios
R02#conf t
R02(config)#ip multicast-routing
R02(config)#int f0/0
R02(config-if)#ip pim dense-mode
R02(config-if)#
*Mar  1 00:13:15.155: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.2 on interface FastEthernet0/0
R02(config-if)#int f0/1
R02(config-if)#ip pim dense-mode
R02(config-if)#
*Mar  1 00:13:36.107: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 192.168.20.254 on interface FastEthernet0/1
R02(config-if)#int f1/0
R02(config-if)#ip pim dense-mode
*Mar  1 00:13:44.023: %PIM-5-NBRCHG: neighbor 10.0.0.1 UP on interface FastEthernet0/0
R02(config-if)#
*Mar  1 00:13:53.055: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.5 on interface FastEthernet1/0
R02(config-if)#
```

Agora podemos notar que agora o roteador já conseguiu formar vizinhos. Isso é mostrado nas mensagens de log exibidas:  

```ios
*Mar  1 00:13:15.155: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.2 on interface FastEthernet0/0
```

Com isso já conseguimos verificar em R01 e R02 os vizinhos.  

- R01  

```ios
R01>ena
R01#show ip pim neighbor
PIM Neighbor Table
Mode: B - Bidir Capable, DR - Designated Router, N - Default DR Priority,
      S - State Refresh Capable
Neighbor          Interface                Uptime/Expires    Ver   DR
Address                                                            Prio/Mode
10.0.0.2          FastEthernet0/0          00:04:57/00:01:43 v2    1 / DR S
R01#
```
  
- R02  

```ios
R02#show ip pim neighbor
PIM Neighbor Table
Mode: B - Bidir Capable, DR - Designated Router, N - Default DR Priority,
      S - State Refresh Capable
Neighbor          Interface                Uptime/Expires    Ver   DR
Address                                                            Prio/Mode
10.0.0.1          FastEthernet0/0          00:06:02/00:01:37 v2    1 / S
R02#
```  
