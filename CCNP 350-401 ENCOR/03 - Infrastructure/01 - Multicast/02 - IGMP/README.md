# 02 - Internet Group Management Protocol

Esse é o protocolo utilizado para os hosts se juntarem aos grupos de multicast. Atualmente existem 3 versões desse protocolo: **IGMPv1** definida na RFC 1112 que raramente é utilizada, 
**IGMPv2** definida na RFC 2236 que é a mais comum de ser encontrada e **RFC 3376** definida na RFC 3376. <br></br>

![IGMP](Imagens/igmp.png)


## IGMP Versão 02

Agora para falar sobre o tipo de comunicação **unicast** é preciso se fazer uma pequena revisão. Então primeiramente vamos observar os tipos de comunicação existentes.

| UNICAST                         | BROADCAST                            | MULTICAST                                     |
|---------------------------------|--------------------------------------|-----------------------------------------------|
|  | ![BROADCAST](Imagens/broadcast.png)  | ![MULTICAST](Imagens/multicast.png)           |


