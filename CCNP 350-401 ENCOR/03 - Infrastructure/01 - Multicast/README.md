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