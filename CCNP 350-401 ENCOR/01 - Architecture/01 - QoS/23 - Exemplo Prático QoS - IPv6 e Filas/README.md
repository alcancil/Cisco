# 23 - Exemplo Prático QoS - IPv6 e Filas

Até aqui eu demonstrei como marcar, escolher a técnica de QoS (Policer ou Shapper) e como dar prioridade ou mesmo limitar a banda de um fluxo de dados. Mas como mostrado na teoria, podemos escolher também em que tipo de fila que vamos colocar os tráfegos. Aqui vou utilizar o seguinte cenário: <br></br>

![CENÁRIO](Imagens/cenario.png) <br></br>

Nesse exemplo vou estar utilizado IPv6 na faixa 2001:DB8:: /64 que é a faixa reservada para documentações (essa faixa de endereços não e deve ser utilizada na prática). Então vou escolher 3 tipos de fluxos de dados: SSH, TFTP e ICP. Também estarei utilizando a marcação pelo NBAR. As configurações de QoS serão aplicadas no roteador **ISP** tanto na interface **E0/0, no sentido de input,** quanto na interface **E0/1**, no sentido de **output**. <br><br>

Então vamos analisar mais de perto a interface E0/0 como o comando: **show interface 0/0**. Observem a saída: <br></br>

![INTERFACE_E0/0](Imagens/interface_e0_0.png) <br></br>

Notem que nada foi feito quanto ao tipo de fila e a interface é automaticamente colocada no algoritmo FIFO. Então primeiro vamos configurar o QoS como feito até agora e depois vamos alterar esse comportamento. <br></br>

01. Escolher o tráfego interessante

| ROTEADOR ISP | COMANDOS                                   |
| ------------ | ------------------------------------------ |
| 01           | ISP(config)#class-map match-all TFTP       |
| 02           | ISP(config-cmap)# match protocol tftp      |
| 03           | ISP(config)#class-map match-all ICMP       |
| 04           | ISP(config-cmap)# match protocol ipv6-icmp |
| 05           | ISP(config)#class-map match-all SSH        |
| 06           | ISP(config-cmap)# match protocol ssh       |

02. Escolher a política a ser aplicada a cada tráfego interessante.

| ROTEADOR ISP | COMANDOS                                   |
| ------------ | ------------------------------------------ |
| 01           | ISP(config)#policy-map QoS                 |
| 02           | ISP(config-pmap)#class SSH                 |
| 03           | ISP(config-pmap-c)# set dscp cs6           |
| 04           | ISP(config-pmap)#class TFTP                |
| 05           | ISP(config-pmap-c)# set dscp af31          |
| 06           | ISP(config-pmap)#class ICMP                |
| 07           | ISP(config-pmap-c)# set dscp ef            |

03. Aplicar a política a interface e0/0

| ROTEADOR ISP | COMANDOS                                   |
| ------------ | ------------------------------------------ |
| 01           | ISP(config)# int e0/0                      |
| 02           | ISP(config-if)#service-policy input QoS    |

Então vamos analisar como ficaram nossas configurações até agora. <br> </br>

<table>
    <tr >
        <td width="33%"> <img src="Imagens/class_map.png"></img> </td>
        <td width="33%"> <img src="Imagens/policy_map.png"></img> </td>
        <td width="33%"> <img src="Imagens/policy_map_int_e0_0.png"></img> </td>
    </tr>
</table>

Antes de avançarmos vamos configurar as larguras de bandas para as interface **e0/0 e e0/1** pois as porcentagens de bandas reservadas para cada classe se baseia no comando **bandwith** aplicado na interface. <br></br>

| ROTEADOR ISP | COMANDOS                                   |
| ------------ | ------------------------------------------ |
| 01           | ISP(config)# int e0/0                      |
| 02           | ISP(config-if)#bandwidth 1000000           |
| 03           | ISP(config-if)# int e0/1                   |
| 04           | ISP(config-if)#bandwidth 1000000           |

Aqui configuramos as interfaces como 100Mbps. <br></br>

Como visto anteriormente, temos dois mecanismos de enfileiramento: **Congestion Management** e **Congestion Avoidance**. Então vamos tratar do primeiro. <br></br>

## Congestion Management

Agora aqui nesse momento temos as classes criadas e então queremos dar um tratamento diferenciado para cada fila, conforme o plano escolhido: <br></br>

> - SSH deverá ter 40% da banda
> - Tfp deverá ter 10% da banda
> - ICMP deverá ter 256 Kbps, e ser colocado na fila prioritária (LLC)
> - Configurar a class-default para usar WFQ
