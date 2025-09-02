- [01 - Multicast](#01---multicast)
  - [Faixas de Endereçamento IP](#faixas-de-endereçamento-ip)
    - [**IPV4**](#ipv4)
    - [**IPV6**](#ipv6)
    - [🔧 Verificação de Suporte Multicast em Equipamentos](#-verificação-de-suporte-multicast-em-equipamentos)
  - [Cisco IOS - Verificar se multicast está habilitado:](#cisco-ios---verificar-se-multicast-está-habilitado)
  - [Switch - Verificar IGMP Snooping:](#switch---verificar-igmp-snooping)
  - [Problemas de não utilizar o multicast](#problemas-de-não-utilizar-o-multicast)
  - [Endereçamento Multicast](#endereçamento-multicast)
    - [🎯 Casos de Uso Reais](#-casos-de-uso-reais)
    - [Próximo Tópico: Detalhes do Multicast](#próximo-tópico-detalhes-do-multicast)

# 01 - Multicast

Para falar sobre o tipo de comunicação **multicast** é preciso fazer uma pequena revisão. Então primeiramente vamos observar os tipos de comunicação existentes.

| UNICAST                         | BROADCAST                            | MULTICAST                                     |
|---------------------------------|--------------------------------------|-----------------------------------------------|
|![UNICAST](Imagens/unicast.png)  | ![BROADCAST](Imagens/broadcast.png)  | ![MULTICAST](Imagens/multicast.png)           |

Como podemos observar, quando o tráfego vai de um emissor para um receptor podemos chamar de **unicast**, ou seja, é um tráfego direto. Um exemplo que podemos citar desse tipo de comunicação é a ligação telefônica por exemplo, ou mesmo quando se faz um acesso via ssh para algum equipamento.  

Depois temos o **broadcast**. Diferente do primeiro tipo de comunicação, esse é um tipo de comunicação onde um envia e todos recebem. Podemos citar o exemplo do protocolo arp onde os equipamentos precisam mapear o endereço mac com o endereço IP. Para o protocolo arp poder descobrir a quem pertence um endereço IP por exemplo, ele faz um "flood" para todos os equipamentos na rede e com isso a comunicação se dá de forma conhecida por **broadcast**.

Agora se analisarmos bem esses dois tipos de comunicação iremos perceber que no unicast a comunicação se dá de uma forma mais eficiente pois ela entrega os pacotes somente para o destinatário escolhido. Já no broadcast, todos recebem os pacotes independentemente se eles precisam ou não receber tal pacote. Isso faz com que o host que receba o pacote tenha que analisar o mesmo, verificar se ele é o destinatário e se não for, descartar o mesmo. Essa forma de comunicação não é muito eficiente pois em ambientes muito grandes ocupa banda muitas vezes desnecessárias e faz com que o host tenha que processar o pacote e consumir memória e processador.  

Com base nessa limitação, foi desenvolvido o **multicast**. Agora, nesse tipo de comunicação, existe uma fonte de envio de dados mas somente um grupo, ou grupos de hosts que irão receber esses dados. Com isso, o consumo de banda do meio é utilizada de forma mais eficiente e não força quem não tem que fazer parte da conversa receber dados indesejados.  

**💡 Exemplo Prático de Eficiência:** 

```text
Cenário: 1000 usuários assistindo o mesmo stream de vídeo (10 Mbps)

Unicast:     10 Mbps × 1000 usuários = 10.000 Mbps (10 Gbps)
Multicast:   10 Mbps × 1 stream = 10 Mbps total

Economia de banda: 99,9%
```

## Faixas de Endereçamento IP

### **IPV4**

| Classe de IP             | Faixa de Endereçamento         |
|--------------------------|--------------------------------|
| Classe A                 | 0.0.0.0 a 127.255.255.255      |  
| Classe B                 | 128.0.0.0 a 191.255.255.255    |
| Classe C                 | 192.0.0.0 a 223.255.255.255    |
| **Classe D (Multicast)** | **224.0.0.0 a 239.255.255.255**|
| Classe E (Reservado)     | 240.0.0.0 a 247.255.255.255    |

### **IPV6**

| Tipo de Endereço    |  Faixa de Endereçamento | Descrição                                                                                                                          |
| ------------------   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------|
| Unicast Global       |  2000::/3           | Usado para comunicação unicast na Internet. É equivalente aos endereços públicos no IPv4.                                               |
| Unicast Link-Local   |  FE80::/10          | Usado para comunicação dentro de um link (como em uma LAN). Esses endereços são configurados automaticamente em cada interface de rede. |
| Unicast Unique Local |  FC00::/7          | Endereços para redes privadas (semelhante a 192.168.0.0/16 no IPv4).                                                                    |
| **Multicast**        |  FF00::/8           | Usado para comunicação multicast.                                                                                                       |
| Anycast               | Derivado de unicast | Endereços unicast atribuídos a vários nós, mas roteados para o mais próximo.                                                            |
| Loopback                  | ::1            | Endereço para a própria máquina (equivalente a 127.0.0.1 no IPv4).                                                                      |
| Endereço Não Especificado | ::          | Indica ausência de endereço (usado como fonte em algumas situações, como durante a autoconfiguração).                                   |
| Reservado             |4000::/2, 6000::/3 e outras faixas | Reservado pela IETF para uso futuro.                                                                                      |
| Embedded IPv4         | ::FFFF:0:0/96 e 2002::/16 | Usado para compatibilidade com IPv4, como no caso de NAT64 (endereço mapeado para IPv4) ou redes 6to4.                            |

**Destaques sobre a tabela:**  

- **Unicast Global:** Utilizado para endereços roteáveis na Internet.
- **Link-Local:** Necessário para operações básicas dentro de uma rede local; todos os dispositivos IPv6 têm um endereço link-local automaticamente.
- **Multicast:** Substitui a funcionalidade de broadcast no IPv6.  
- **Loopback:** Para testes internos no dispositivo.  

Dois pontos importantes sobre multicast em camadas 2 e 3:

- **Camada 2 (Switches):** Utilizam IGMP Snooping para "escutar" as mensagens IGMP entre hosts e roteadores, criando uma tabela de quais portas têm hosts interessados em cada grupo multicast.

- **Camada 3 (Roteadores):** Gerenciam os grupos multicast localmente via IGMP e fazem o roteamento inter-redes via PIM (Protocol Independent Multicast).  

### 🔧 Verificação de Suporte Multicast em Equipamentos

## Cisco IOS - Verificar se multicast está habilitado:

```ios
Router# show ip multicast
Multicast Routing: enabled
Multicast Multipath: disabled
Multicast Route limit: No limit
Multicast Fallback group mode: Sparse
```

## Switch - Verificar IGMP Snooping:  

```ios
Switch# show ip igmp snooping
Global IGMP Snooping configuration:
IGMP snooping                : Enabled
IGMPv3 snooping              : Enabled
Report suppression           : Enabled
TCN solicit query            : Disabled
TCN flood query count        : 2
```

O IGMP funciona entre hosts e roteadores dentro de uma rede local, mas quando é necessário enviar tráfego multicast para outras redes, o protocolo PIM é responsável pelo roteamento inter-redes.

**Observação:** Existem outros protocolos multicast além do PIM (como DVMRP e MOSPF), porém o PIM se tornou o padrão da indústria para roteamento multicast.

![TOPOLOGIA](Imagens/topologia.png)  

- **Origem Multicast:** É o servidor que envia o tráfego multicast para o grupo.

- **FHR (First Hop Router):** É o roteador de "primeiro salto" que está diretamente conectado à origem. Ele recebe o tráfego multicast primeiro e inicia o processo de roteamento PIM.

- **Local Multicast Router:** Roteadores intermediários que participam da árvore PIM.

- **Switch Layer 2 com IGMP Snooping:** Dispositivo que usa o IGMP Snooping para aprender quais portas têm hosts interessados em um grupo multicast específico, evitando inundações de tráfego na rede local.

- **Hosts:** Recebem o tráfego multicast após enviarem uma Mensagem de Pedido IGMP (IGMP Join) para se juntar ao grupo.

## Problemas de não utilizar o multicast

Depois de entender isso, vamos analisar um cenário onde eu tenho um servidor de vídeos e que esteja transmitindo para a rede toda em **broadcast**. Agora vamos supor que em cada salto,
eu ocupe 10mbs de largura de banda.  

![TOPOLOGIA2](Imagens/topologia2.png)  

Como podemos perceber, o servidor de vídeos envia os pacotes para todos os computadores da rede. Vamos supor que o servidor de vídeos ocupe 10 Mbps para enviar os dados. Rapidamente podemos notar que a cada salto então teríamos que ter uma largura de banda 10 Mbps no mínimo para cada salto. Agora vamos imaginar que cada host resolva assistir a 5 vídeos ao mesmo tempo.  

Portanto teríamos que ter 50 Mbps de largura de banda, mesmo para os hosts não interessados. Isso é refletido em desperdício de banda e, outro ponto é que os hosts finais não interessados necessariamente precisam processar esses pacotes consumindo mais processador e memória.  

**📊 Comparação Quantitativa: Unicast vs Multicast**  

```text
Cenário: 100 usuários, vídeo 4K (25 Mbps cada)

┌─────────────────────────────────────────────────────┐
│ UNICAST (1:1)                                       │
│ ├─ Largura de banda total: 25 Mbps × 100 = 2.5 Gbps │
│ ├─ Links necessários: 100 conexões                  │
│ └─ Custo: MUITO ALTO                                │
│                                                     │
│ MULTICAST (1:N)                                     │
│ ├─ Largura de banda total: 25 Mbps × 1 = 25 Mbps    │
│ ├─ Links necessários: 1 conexão                     │
│ └─ Custo: BAIXO                                     │
│                                                     │
│ ECONOMIA: 99% de redução na banda                   │
└─────────────────────────────────────────────────────┘
```

Como podemos observar nas duas topologias apresentadas, temos duas situações: a comunicação em camada 2 e a comunicação em camada 3. Para a comunicação em camada 2, utilizaremos o **protocolo IGMP (Internet Group Management Protocol)** e em camada 3 o **protocolo PIM (Protocol Independent Multicast)** .  

**OBS:** O protocolo IGMP é ativado em switches e tem a função ***snooping*** ( no sentido de escuta em inglês), ou seja, ele trabalha com  requisições e envios de informações. Já o protocolo ***PIM*** é ativado em roteadores.  

**🔄 Fluxo de Comunicação IGMP/PIM**  

```text
1. Host ─────[IGMP Join]────→ Switch ─────[IGMP Report]────→ Router
   │                             │                              │
   │                             ▼                              ▼
   │                      [IGMP Snooping]              [Multicast Route]
   │                         Table                           Table
   │                             │                              │
   └─────[Multicast Data]◄───────┴─────────[PIM Messages]◄──────┘
                                        (entre roteadores)
```

## Endereçamento Multicast

Como mencionado anteriormente, foram definidas faixas de endereços IPv4 e IPv6 para a comunicação multicast. Seguem as faixa de endereços definidas pela IANA.  

**IPv4**  

| Designação                                       | Faixa de endereços Multicast            | 🎨 |
|--------------------------------------------------|-----------------------------------------|----|
| Local network control block                      | 224.0.0.0 to 224.0.0.255                | 🟢 |
| Internetwork control block                       | 224.0.1.0 to 224.0.1.255                | 🟢 |
| Ad hoc block I                                   | 224.0.2.0 to 224.0.255.255              | 🟡 |
| Reserved                                         | 224.1.0.0 to 224.1.255.255              | 🔴 |
| SDP/SAP block                                    | 224.2.0.0 to 224.2.255.255              | 🟡 |
| Ad hoc block II                                  | 224.3.0.0 to 224.4.255.255              | 🟡 |
| Reserved                                         | 224.5.0.0 to 224.251.255.255            | 🔴 |
| DIS Transient Groups                             | 224.252.0.0 to 224.255.255.255          | 🟡 |
| Reserved                                         | 225.0.0.0 to 231.255.255.255            | 🔴 |
| Source Specific Multicast (SSM) block            | 232.0.0.0 to 232.255.255.255            | 🔵 |
| GLOP block                                       | 233.0.0.0 to 233.251.255.255            | 🟡 |
| Ad hoc block III                                 | 233.252.0.0 to 233.255.255.255          | 🟡 |
| Unicast-Prefix-based IPv4 Multicast Addresses    | 234.0.0.0 to 234.255.255.255            | 🔵 |
| Reserved                                         | 235.0.0.0 to 238.255.255.255            | 🔴 |
| Organization-Local Scope (Administratively scoped block) | 239.0.0.0 to 239.255.255.255    | 🟠 |

Legenda de Cores:

- 🟢 Endereços de controle bem conhecidos
- 🟡 Endereços de uso geral
- 🔴 Endereços reservados
- 🔵 Endereços SSM/Prefix-based
- 🟠 Endereços organizacionais

**💡 Exemplos Práticos de Endereços Bem Conhecidos**  

```text
224.0.0.1    - Todos os hosts na sub-rede
224.0.0.2    - Todos os roteadores na sub-rede  
224.0.0.5    - Roteadores OSPF (AllSPFRouters)
224.0.0.6    - Roteadores OSPF Designados
224.0.0.9    - Roteadores RIP v2
224.0.0.13   - Roteadores PIM
224.0.1.1    - Network Time Protocol (NTP)
```

**Teste prático - Verificar hosts interessados em grupos:**  

- **Host Linux**

```bash
# Linux - verificar grupos multicast que o host participa
netstat -g

# Resultado exemplo:
Interface       RefCnt Group
eth0           1      224.0.0.1
eth0           1      224.0.0.251  # mDNS
```

Para informações mais detalhadas e atualizadas, consulte o registro oficial da IANA:
[Registro oficial de endereços multicast IPv4 pela IANA](https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml)  

• **Local network control block (224.0.0.0/24):** Endereços de controle no bloco de rede local são utilizados pelos ***protocolos de controle de tráfego*** e não são encaminhados para domínios de broadcast. São de escopo local. Exemplos desses endereços são o ***todos os hosts nessa sub-rede (224.0.0.0.2) e todos os roteadores PIM (224.0.0.13)***  

• **Internetwork control block (224.0.1.0/24):** Esse é um bloco de endereços que pode ser transmitidos através da Internet. Exemplos incluem ***Network Time Protocol (NTP), (224.0.1.1), Cisco-RP-Announce (224.0.1.39), e Cisco-RP-Discovery (224.0.1.40).***  

• ***Organization-Local Scope (239.0.0.0/8):*** São endereços definidos na RFC 2365 e tem escopo local. São similares aos endereços da ***RFC 1918**.  

 Em outras palavras os administradores de redes estão livres para poder utilizá-los dentro do próprio domínio sem se preocupar com conflitos
 em outras redes.  

**🛠️ Configuração de Endereço Organizacional**  

```ios
! Exemplo de configuração usando endereço organizacional
Router(config)# interface gigabitEthernet 0/1
Router(config-if)# ip pim sparse-mode
Router(config-if)# ip multicast boundary 10  ! ACL para filtrar 239.x.x.x

! ACL exemplo para limitar escopo organizacional
Router(config)# access-list 10 deny 239.0.0.0 0.255.255.255
Router(config)# access-list 10 permit any
```

**IPv6**  

| **Endereço Multicast IPv6** | **Descrição**                                           | **Escopo Disponível**                               | 🎨 |
|-----------------------------|---------------------------------------------------------|-----------------------------------------------------|----|
| FF0X::1                     | Todos os nós                                            | Interface-local (1), Link-local (2)                 | 🟢 |
| FF0X::2                     | Todos os roteadores                                     | Interface-local (1), Link-local (2), Site-local (5) | 🟢 |
| FF0X::5                     | Roteadores OSPFv3 AllSPF                                | Link-local (2)                                      | 🟡 |
| FF0X::6                     | Roteadores OSPFv3 Designated                            | Link-local (2)                                      | 🟡 |
| FF0X::9                     | Roteadores RIP                                          | Link-local (2)                                      | 🟡 |
| FF0X::A                     | Roteadores EIGRP                                        | Link-local (2)                                      | 🟡 |
| FF0X::12                    | Todos os roteadores PIM                                 | Link-local (2)                                      | 🟢 |
| FF0X::16                    | Todos os roteadores RPL                                 | Link-local (2)                                      | 🟡 |
| FF0X::FB                    | mDNSv6                                                  | Todos os escopos                                    | 🟡 |
| FF0X::101                   | Todos os servidores NTP                                 | Todos os escopos                                    | 🟡 |
| FF0X::1:2                   | Todos os servidores e agentes de retransmissão DHCPv6   | Link-local (2)                                      | 🟡 |
| FF0X::1:3                   | Todos os servidores DHCPv6 no site                      | Site-local (5)                                      | 🟡 |
| FF0X::1:FFXX:XXXX           | Endereço multicast de nó solicitado                     | Link-local (2)                                      | 🔵 |

Legenda de Cores:  

- 🟢 Verde: Endereços fundamentais e essenciais para o funcionamento básico da rede
- 🟡 Amarelo: Protocolos específicos de roteamento e serviços de infraestrutura
- 🔵 Azul: Endereços multicast de nó solicitado (solicited-node)

**🔍 Verificação IPv6 Multicast na Prática**  

- Host Linux

```bash
# Linux - Ver grupos IPv6 multicast
ip -6 maddr show

# Exemplo de saída:
2: eth0
    inet6 ff02::1
    inet6 ff02::2
    inet6 ff02::1:ff00:1234
    inet6 ff01::1
```

- Equipamentos Cisco

```ios
# Cisco - Ver grupos IPv6 multicast
Router# show ipv6 mld interface gigabitEthernet 0/1

GigabitEthernet0/1 is up, line protocol is up
  Internet address is 2001:DB8:1::1/64
  MLD is enabled on interface
  Current MLD version is 2
  MLD query interval is 125 seconds
  MLD querier timeout is 255 seconds
  MLD max query response time is 10 seconds
```

- Notas:

```text

    O campo 'X' no endereço multicast representa o valor do campo de escopo, que define a abrangência do endereço multicast. Os valores possíveis para 'X' são:
        1: Interface-Local
        2: Link-Local
        5: Site-Local
        8: Organization-Local
        E: Global

    O endereço FF0X::1:FFXX:XXXX é utilizado para os endereços de nó solicitado, onde os últimos 24 bits correspondem aos últimos 24 bits do endereço unicast ou anycast do nó.
```

Para informações mais detalhadas e atualizadas, consulte o registro oficial da IANA:
[Registro oficial de endereços multicast IPv6 pela IANA](https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml)

### 🎯 Casos de Uso Reais

1. IPTV/Streaming de Vídeo  

```text
Cenário: Provedor de TV por IP com 10.000 assinantes
├─ Largura de banda por canal: 8 Mbps (HD)
├─ 100 canais disponíveis  
├─ Pico: 30% dos usuários assistindo simultaneamente

Sem Multicast:
└─ Banda necessária: 10.000 × 30% × 8 Mbps = 24.000 Mbps (24 Gbps)

Com Multicast:  
└─ Banda necessária: 100 canais × 8 Mbps = 800 Mbps

💰 Economia: 96,7% na largura de banda!
```

2. Distribuição de Software/Updates  

```text
Cenário: Empresa com 1.000 computadores, update de 2GB

Unicast tradicional:
├─ Tempo por download: 10 minutos  
├─ Downloads simultâneos: 50 (limitação do servidor)
└─ Tempo total: 1000/50 × 10 = 200 minutos (3h20m)

Multicast:
├─ Todos recebem simultaneamente
├─ Largura de banda: 1 × transmissão
└─ Tempo total: 10 minutos

⏱️ Redução de tempo: 95%
```

3. Dados Financeiros (Market Data)  

```text
Cenário: Bolsa de valores enviando cotações para brokers

Características:
├─ Latência crítica: < 1ms
├─ 500 símbolos sendo negociados
├─ 100 updates/segundo por símbolo  
├─ 200 brokers conectados

Benefícios do Multicast:
├─ ✅ Latência ultra-baixa (UDP + multicast)
├─ ✅ Mesmo dado para todos simultaneamente  
├─ ✅ Não há "vantagem" por velocidade de conexão
└─ ✅ Escalabilidade: adicionar broker não afeta performance
```  

---

### Próximo Tópico: Detalhes do Multicast  

 Para aprofundar a compreensão sobre como o roteamento multicast funciona na prática, incluindo os protocolos e as árvores de distribuição, continue para o próximo artigo.

[**02 - Multicast Detalhes e Fluxo de Tráfego**](./README%20-%20Copia%20(2).md)