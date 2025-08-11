# 01 - Multicast

Agora para falar sobre o tipo de comunicação **unicast** é preciso se fazer uma pequena revisão. Então primeiramente vamos observar os tipos de comunicação existentes.

| UNICAST                         | BROADCAST                            | MULTICAST                                     |
|---------------------------------|--------------------------------------|-----------------------------------------------|
|![UNICAST](Imagens/unicast.png)  | ![BROADCAST](Imagens/broadcast.png)  | ![MULTICAST](Imagens/multicast.png)           |

Como podemos observar, quando o tráfego vai de um emissor para um receptor podemos chamar de **unicast**, ou seja, é um trafego direto. Um exemplo que podemos citar desse tipo de comunicação é a ligação telefônica por exemplo, ou mesmo quando se faz um acesso via ssh para algum equipamento. <br></br>

Depois temos o **broadcast**. Diferente do primeiro tipo de comunicação, esse é um tipo de comunicação onde um envia e todos recebem. Podemos citar o exemplo do protocolo arp onde os equipamentos precisam mapear o endereço mac com o endereço IP. Para o protocolo arp poder descobrir a quem pertence um endereço IP por exemplo, ele faz um "flood" para todos os equipamentos na rede e com isso a comunicação se dá de forma conhecida por **broadcast**. <br></br>

Agora se analisarmos bem esses dois tipos de comunicação iremos perceber que no unicast a comunicação se dá de uma forma mais eficiente pois ela entrega os pacotes somente para o destinatário escolhido. Já no broadcst, todos recebe os pacotes independentemente se eles precisam ou não receber tal pacote. Isso faz com que o host que receba o pacote tenha que analisar o mesmo, verificar se ele é o destinatário e se não for, descartar o mesmo. Essa forma de comunicação não é muito eficiente pois em ambientes muito grandes ocupa banda muitas vezes desnecessárias e faz com que o host tenha que processar o pacote e consumir memória e processador. <br></br>

Pensando nisso, foi desenvolvido o **multicast**. Agora, nesse tipo de comunicação, existe uma fonte de envio de dados mas somente um grupo, ou grupos de hosts que irão receber esses dados. Com isso, o consumo de banda do meio é utilizada de forma mais eficiente e não força quem não tem que fazer parte da conversa receber dados indesejados. <br></br>

## Faixas de Endereçamento IP

### **IPV4**

| Classe de IP             | Faixa de Endereçamento         |
|--------------------------|--------------------------------|
| Classe A	               | 0.0.0.0 a 127.255.255.255      |  
| Classe B	               | 128.0.0.0 a 191.255.255.255    |
| Classe C	               | 192.0.0.0 a 223.255.255.255    |
| **Classe D (Multicast)** | **224.0.0.0 a 239.255.255.255**|
| Classe E (Reservado)     | 240.0.0.0 a 247.255.255.255    |

<br></br>

### **IPV6**

| Tipo de Endereço	   |  Faixa de Endereçamento |	Descrição                                                                                                                          |
| ------------------   | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------|
| Unicast Global       |  2000::/3           | Usado para comunicação unicast na Internet. É equivalente aos endereços públicos no IPv4.                                               |
| Unicast Link-Local   |  FE80::/10	         | Usado para comunicação dentro de um link (como em uma LAN). Esses endereços são configurados automaticamente em cada interface de rede. |
| Unicast Unique Local |  FC00::/7	         | Endereços para redes privadas (semelhante a 192.168.0.0/16 no IPv4).                                                                    |
| **Multicast**	       |  FF00::/8           | Usado para comunicação multicast.                                                                                                       |
| Anycast              | Derivado de unicast | Endereços unicast atribuídos a vários nós, mas roteados para o mais próximo.                                                            |
| Loopback	                | ::1            | Endereço para a própria máquina (equivalente a 127.0.0.1 no IPv4).                                                                      |
| Endereço Não Especificado	| ::	         | Indica ausência de endereço (usado como fonte em algumas situações, como durante a autoconfiguração).                                   |
| Reservado	           |4000::/2, 6000::/3 e outras faixas | Reservado pela IETF para uso futuro.                                                                                      |
| Embedded IPv4	       | ::FFFF:0:0/96 e 2002::/16 | Usado para compatibilidade com IPv4, como no caso de NAT64 (endereço mapeado para IPv4) ou redes 6to4.                            |

**Destaques sobre a tabela:** <br></br>

* **Unicast Global:** Utilizado para endereços roteáveis na Internet.
* **Link-Local:** Necessário para operações básicas dentro de uma rede local; todos os dispositivos IPv6 têm um endereço link-local automaticamente.
* **Multicast:** Substitui a funcionalidade de broadcast no IPv6.
* **Loopback:** Para testes internos no dispositivo.
<br></br>

Certo, mas precisamos lembrar de duas coisas importantes: os switches propagam broadacst e os roteadores não. Isso é importante de se lembrar pois o multicast vai 
funcionar de forma semelhante nesse aspecto. Então para se poder ter comunicação em ***unicast***, o switches formam os grupos em que os hosts irão participar e o roteador é 
quem gerencia os hosts. Porém essa comunicação fica somente na ***lan**, não vai para outras redes. Quem cria e gerencia esses grupos é a funcionalidade **IGMP SNOOP** . 
Mas se precisarmos enviar a comunicação para outras redes quem faz esse processo é o protocolo **PIM - Protocol Independent Multicast**. **OBS:** existem vários outros protocolos 
além do PIM, porém o mercado escolheu ele para utilizar no dia-a-dia. <br></br>

![TOPOLOGIA](Imagens/topologia.png) <br></br>

## Problemas de não utilizar o multicast

Depois de entender isso, vamos analisar um cenário onde eu tenho um servidor de vídeos e que esteja transmitindo para a rede toda em **broadcast**. Agora vamos supor que em cada salto,
eu ocupe 10mbs de largura de banda. <br> </br>

![TOPOLOGIA2](Imagens/topologia2.png) <br></br>

Como podemos perceber, o servidor de vídeos envia os pacotes para todos os computadores da rede. Vamos imaginar que o servidor de vídeos ocupe 10 Mbps para enviar os dados. Rapidamente
podemos notar que a cada salto então teríamos que ter uma largura de banda 10 Mbps no mínimo para cada salto. Agora vamos imaginar que cada host resolva assistir a 5 vídeos ao mesmo tempo.
Portanto teríamos que ter 50 Mbps de largura de banda, mesmo para os hosts não interessados. Isso é refletido em desperdício de banda e, outro ponto é que os hosts finais não interessados
necessariamente tem que processar esses pacotes consumindo mais processador e memória. <br></br>

Como podemos observar nas duas topologias apresentadas, temos duas situações: a comunicação em camada 2 e a comunicação em camada 3. Para a comunicação em camada 2 iremos utilizar o 
**protocolo IGMP (Internet Group Management Protocol)** e em camada 3 o **protocolo PIM (Protocol Independent Multicast)** . <br></br>

**OBS:** O protocolo IGMP é ativado em switches e tem a função ***snooping*** ( no sentido de escuta em inglês), ou seja, ele trabalha com  requisições e envios de informações. Já o protocolo 
***PIM*** é ativado em roteadores.

## Endereçamento Multicast

Como citado anteriormente, foram definidas faixas de endereço IPv4 e IPv6 para a comunicação multicast. Seguem as faixa de endereços definidas pela IANA. <br></br>

**IPv4** <br></br>

| Designation                                      | Multicast Address Range                 |
|--------------------------------------------------|-----------------------------------------|
| Local network control block                      | 224.0.0.0 to 224.0.0.255                |
| Internetwork control block                       | 224.0.1.0 to 224.0.1.255                |
| Ad hoc block I                                   | 224.0.2.0 to 224.0.255.255              |
| Reserved                                         | 224.1.0.0 to 224.1.255.255              |
| SDP/SAP block                                    | 224.2.0.0 to 224.2.255.255              |
| Ad hoc block II                                  | 224.3.0.0 to 224.4.255.255              |
| Reserved                                         | 224.5.0.0 to 224.251.255.255            |
| DIS Transient Groups                             | 224.252.0.0 to 224.255.255.255          |
| Reserved                                         | 225.0.0.0 to 231.255.255.255            |
| Source Specific Multicast (SSM) block            | 232.0.0.0 to 232.255.255.255            |
| GLOP block                                       | 233.0.0.0 to 233.251.255.255            |
| Ad hoc block III                                 | 233.252.0.0 to 233.255.255.255          |
| Unicast-Prefix-based IPv4 Multicast Addresses    | 234.0.0.0 to 234.255.255.255            |
| Reserved                                         | 235.0.0.0 to 238.255.255.255            |
| Organization-Local Scope (Administratively scoped block) | 239.0.0.0 to 239.255.255.255    |

Para informações mais detalhadas e atualizadas, consulte o registro oficial da IANA:
[Registro oficial de endereços multicast IPv4 pela IANA](https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml) <br></br>

• **Local network control block (224.0.0.0/24):** Endereços de controle no bloco de rede local são utilizados pelo ***protocolo de controle de tráfego*** e não
são encaminhados para domínios de broadcast. São de escopo local. Exemplos desses endereços são o ***todos os hosts nessa sub-rede (2240.0.0.2) e todos os roteadores PIM (224.0.0.13)***

• **Internetwork control block (224.0.1.0/24):** Esse é um bloco de endereços que pode ser transmitidos através da Internet. Exemplos incluem ***Network Time Protocol (NTP), (224.0.1.1), Cisco-RP-Announce***
 ***(224.0.1.39), e Cisco-RP-Discovery (224.0.1.40).***

• ***Organization-Local Scope (239.0.0.0/8):*** São endereços definidos na RFC 2365 e tem escopo local. São similares aos endereços da ***RFC 1918**.
 Em outras palavras os administradores de redes estão livres para poder utilizá-los dentro do próprio domínio sem se preocupar com conflitos
 em outras redes. 

**IPv6** <br></br>

| **Endereço Multicast IPv6** | **Descrição**                               | **Escopo Disponível**                  |
|-----------------------------|---------------------------------------------|----------------------------------------|
| FF0X::1                     | Todos os nós                                | Interface-local (1), Link-local (2)    |
| FF0X::2                     | Todos os roteadores                         | Interface-local (1), Link-local (2), Site-local (5) |
| FF0X::5                     | Roteadores OSPFv3 AllSPF                    | Link-local (2)                         |
| FF0X::6                     | Roteadores OSPFv3 Designated                | Link-local (2)                         |
| FF0X::9                     | Roteadores RIP                              | Link-local (2)                         |
| FF0X::A                     | Roteadores EIGRP                            | Link-local (2)                         |
| FF0X::12                    | Todos os roteadores PIM                     | Link-local (2)                         |
| FF0X::16                    | Todos os roteadores RPL                     | Link-local (2)                         |
| FF0X::FB                    | mDNSv6                                      | Todos os escopos                       |
| FF0X::101                   | Todos os servidores NTP                     | Todos os escopos                       |
| FF0X::1:2                   | Todos os servidores e agentes de retransmissão DHCPv6   | Link-local (2)             |
| FF0X::1:3                   | Todos os servidores DHCPv6 no site          | Site-local (5)                         |
| FF0X::1:FFXX:XXXX           | Endereço multicast de nó solicitado         | Link-local (2)                         |


Notas:

    O campo 'X' no endereço multicast representa o valor do campo de escopo, que define a abrangência do endereço multicast. Os valores possíveis para 'X' são:
        1: Interface-Local
        2: Link-Local
        5: Site-Local
        8: Organization-Local
        E: Global

    O endereço FF0X::1:FFXX:XXXX é utilizado para os endereços de nó solicitado, onde os últimos 24 bits correspondem aos últimos 24 bits do endereço unicast ou anycast do nó.

Para informações mais detalhadas e atualizadas, consulte o registro oficial da IANA:
[Registro oficial de endereços multicast IPv6 pela IANA](https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml)

# Endereços de Camada 02 (Mac Address)

Para qualquer host pode responder a alguma requisição em redes IP, ele tem um endereço de camada 2 chamado de mac address que é único. Porém, agora como estamos em múlticast, os hosts
tem que responder a um endereço de grupo de múlticast para poderem fazer parte desse grupo. Como as placas de rede podem receber vários fluxos de comunicação ao mesmo 
tempo, é assim que eles conseguem identificar os fluxos multicast. Mas para tanto, foram criadas algumas regras. <br></br>

Primeiro precisamos lembrar que o mac address é um endereço de 12 dígitos em hexadecimal, com segmentos de 8 bits contendo no total 48 bits. Exemplo: 00:11:22:33:44:55 <br></br>

- Os **primeiros 24 bits** de um Mac Address de multicast sempre serão **01:00:5E**
- O primeiro bit mais à esquerda é conhecido como **individual/group bit (I/G)** e sempre que ele for o valor **1**, isso indica que ele é um multicast.
- O vigésimo quinto bit sempre será setado em **0**. Isso é feito para evitar ambiguidades e tentar manter o endereço de multicast em faixas menores.
- O restante dos outros **23 bits** é utilizado para calcular o resto do endereço de multicast.

Agora vamos a um exemplo de como funciona essa regra. Vamos transformar o endereço IP 239.255.1.1 .<br></br>

![IP](Imagens/ip.png) <br></br>

Certo agora aplicamos a regra. <br></br>

![FÓRMULA](Imagens/formula.png) <br></br>

E por fim agora é só converter a parte em Binário para Hexadecimal. <br></br>

![MAC](Imagens/mac.png) <br></br>

Agora vamos pensar um pouco. Se os 25 primeiro bits são fixos, isso não pode gerar algum tipo de problema ? Sim, podem existir sobreposições de endereços uma vez que somente os 23 
últimos bits vão variar. Vamos supor que eu tenha endereços que os 23 últimos bits seja iguais. Vamos ao exemplo: <br></br>

![SOBRE](Imagens/sobre.png) <br></br>

Esse tipo de problema pode fazer com que hosts que não sejam os alvos comecem a receber os tráfegos não solicitados e isso dificulta a gerência dos grupos multicast. Para solucionar esse
tipo de problema devemos fazer filtragem de pacotes com o uso de Vlans, ACLS e Firewalls controlando o fluxo de dados. <br></br>

Por outro lado, se pensarmos em IPv6, o espaçamento de endereços IP é infinitamente maior e esse tipo de problema é evitado. Então a recomendação é sempre se utilizar IPv6 quando puder.

## Multicast - Árvore de Distribuição

🌳 **[Ver Visualização Interativa da Árvore Multicast](Arquivos/multicast_tree.html)**