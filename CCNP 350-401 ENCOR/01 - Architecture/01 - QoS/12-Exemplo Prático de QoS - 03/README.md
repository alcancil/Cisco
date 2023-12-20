# 12 - EXEMPLO PRÁTICO DE QoS 03
 
Sei que parece um pouco repetitivo, mas agora vou adicionar as classes restantes: TFTP e ICMP. Então mais uma vez vou partir do mesmo cenário: <br></br>

![CENAÁRIO](Imagens/01-cenario.png)

Então agora vamos acessar o roteador R01 e completar o que falta por primeiro. Depois iremos partir para o roteador R02. Mais uma vez, lembre-se dos passos para implemntar QoS:<br></br> 

1. Criar um **CLASS MAP** - Selecionar o tráfego importante
2. Criar uma **Policy MAP** - Definir o que fazer com o tráfego
3. Aplicara política em uma interface.

Então novamente vou começar criando as access-lists, tanto de ida e de volta,  para selecionar o tráfego interessante. Também vou aproveitar e criar uma acl para o tráfego SSH<br></br>

|      |  COMANDOS                                                                             |
| :--: | ------------------------------------------------------------------------------------- | 
| 01   | R01(config)# ip access-list extended TFTP                                             |
| 02   | R01(config-ext-nacl)#permit udp 192.168.10.0 0.0.0.255 host 192.168.20.11 eq tftp     |
| 03   | R01(config-ext-nacl)#deny   udp any any eq tftp                                       |
| 04   | R01(config-ext-nacl)#permit ip any any                                                |
| 05   | R01(config-ext-nacl)#exit                                                             |
| 06   | R01(config)# ip access-list extended SSH                                              |
| 07   | R01(confug-ext-nacl)# permit tcp 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255 eq 22  |
| 08   | R01(config-ext-nacl)# exit

Agora vamos criar as class-maps **CLASS-MAP TFTP**  e **CLASS-MAP SSH**. <br></br>

|      |  COMANDOS                                                                        |
| :--: | -------------------------------------------------------------------------------- | 
| 01   | R01(CONFIG)#class-map match-any TFTP                                             |
| 02   | R01(config-cmap)# match access-group name TFTP                                   |
| 03   | R01(config-cmap)# match dscp af31                                                |
| 04   | R01(config-cmap)# exit                                                           |
| 05   | R01(config)#class-map match-any SSH                                              |
| 06   | R01(config-cmap)# match access-group name SSH                                    |
| 07   | R01(config-cmap)# match dscp cs2                                                 |
| 08   | R01(config-cmap)# exit

Vamos agora ao passo **2. Criar uma **Policy MAP** - Definir o que fazer com o tráfego**. <br></br>

|      |  COMANDOS                                                                        |
| :--: | -------------------------------------------------------------------------------- | 
| 01   | R01(config)#policy-map QoS                                                       |
| 02   | R01(config-pmap)# class TFTP                                                     |
| 03   | R01(config-pmap-c)# police cir percent 20                                        |
| 04   | R01(config-pmap-c)# conform-action transmit                                      |
| 05   | R01(config-pmap-c)# exceed-action drop                                           |
| 06   | R01(config-pmap-c)# violate-action drop                                          |
| 07   | R01(config-pmap-c)#  set dscp af11                                               |
| 08   | R01(config-pmap-c)# exit                                                         |
| 09   | R01(config-pmap-c)# class SSH                                                    |
| 10   | R01(config-pmap-c)# police cir percent 10                                        |
| 11   | R01(config-pmap-c)# conform-action transmit                                      |
| 12   | R01(config-pmap-c)# exceed-action drop                                           |
| 13   | R01(config-pmap-c)# violate-action drop                                          |
| 14   | R01(config-pmap-c)# set dscp cs2                                                 |
| 15   | R01(config-pmap-c)# exit                                                         |

**OBS:** aqui eu não criei uma classe chamada TFTP-VOLTA e nem SSH-VOLTA pois o trafego TFTP utiliza portas altas aleatórias para o trafego de volta. Já para o de ida ele utiliza a porta **69**. Como atendeu o match de ida, na volta não há nada que esteja marcando o trafego para outra classe e, sendo assim, manterá marcação escolhida. O mesmo ocorre para o tráfego ssh, que utiliza a porta 22 no servidor e porta aleatórias no client. <br></br>

Perceba que agora somente eu adicionei mais uma classe a política **QoS** e não preciso fazer mais nada referente as interfaces pois essas políticas já estão aplicadas. Segue a captura do trafego **TFTP** no sentido de ida, **interface G0/0** e volta, **interface G0/1**
<table>
    <tr>
        <td width="50%" align="center"> Captura tráfego TFTP IDA</td>
        <td width="50%" align="center"> Captura tráfego TFTP VOLTA</td>
    </tr>
    <tr >
        <td width="50%"> <img src="Imagens/wireshark/01-TFTP_R01_G0_0.png"></img> </td>
        <td width="50%"> <img src="Imagens/wireshark/02-TFTP_R01_G0_1.png"></img> </td>
    </tr>
</table>

Perceba que agora terminamos de configurar o roteador R01 e ainda falta terminar o roteador R02. Então vamos seguir os mesmos 3 passos faltantes.<br></br>


Deixo aqui dois arquivos. O primeiro contendo as configurações iniciais de roteaemneto chama de ![01-QoS(Zerado).zip](Arquivos/01-QoS(Zerado).zip) e outro com as configurações realizadas em R01 chamado ![02-QoS_(R02).zip](Arquivos/02-QoS_(R02).zip). Estes arquivos podem ser importados no EVE-NG. **OBS:** favor se atentar as interfaces pois devido a imagem utilizadas, elas sempre iniciam desligadas, mesmo salvando a configuração para estarem ligadas. <br></br>
Também deixei o arquivo ![R02.txt](Arquivos/R02.txt) contendo todas as configurações de R01. <br></br>
