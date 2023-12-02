# 06 - Marcação em Layer 2

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

Agora que mostrei os mecanismos de QoS disponíveis, está na hora de falarmos um pouco mais sobre marcação. Como QoS é um assunto muito extenso, estou tentando contextualizar um pouco da teoria e mesclar com exemplos práticos para tentar elucidar melhor as coisas. Então vamos olhar um pouco sobre a marcação em layer 2. <br></br>
Ela é chamada de **CoS (Class of Service)** e ela utiliza alguns campos do quadro Ethernet 802.1Q, que é um padrão IEE onde são especificadas as Vlans. Nesse tipo de quadro temos dois campos: **TPID (Tag Protocol Identifier)** e **TCI (Tag Control Information)** que são inseridos nesse frame Ethernet no campo de endereço de origem. <br></br>

![CLASSIFICAÇÃO](Imagens/quadro_ethernet.png) <br></br>

* O valor do **TPID** é um campo de 16 bits com o valor **0x8100** que identifica como sendo um gardo 802.1Q tageado.
* O campo **TCI** possui 16 bits e é formado por 3 campos:
    * **Priority Code Point (PCP)** com 3 bits
    * **Drop Eligible Indicator (DEI)** com 1 bit
    * **Vlan Identificator (Vlan ID)** com 12 bits 









| DESCRITOR DE TRÁFEGO                  | DESCRIÇÃO                                                                                                    |
|---------------------------------------|------------------------------------------------------------------------------------------------------------- |
| INTERNO                               | Grupos de Qos (Tem Significado Local para o roteador)                                                        |
| LAYER 1                               | Interface física, sub interface ou rota                                                                      |
| LAYER 2                               | MAC Addres e bits 802.1 Q / P, Classe de Serviços (COS)                                                      |
| LAYER 2.5                             | Bits MPLS Experimental (ExP)                                                                                 |
| LAYER 3                               | Differentiated Services Code Points (DSCP), IP Precedence (IPP) e endereço IP de origem / destino            |
| LAYER 4                               | Portas TCP ou UDP                                                                                            |
| LAYER 7                               | Next Generation Network Based Application Recognition (NBAR2)                                                |

![NBAR01](Arquivos/01-nbar_mqc.pdf) <br></br>
![NBAR02](Arquivos/02-nbar_protocol_discovery.pdf) <br></br>
