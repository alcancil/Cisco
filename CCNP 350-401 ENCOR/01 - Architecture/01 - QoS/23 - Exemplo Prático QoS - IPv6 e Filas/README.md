# 23 - Exemplo Prático QoS - IPv6 e Filas

Até aqui eu demonstrei como marcar, escolher a técnica de QoS (Policer ou Shapper) e como dar prioridade ou mesmo limitar a banda de um fluxo de dados. Mas como mostrado na teoria, podemos escolher também em que tipo de fila que vamos colocar os tráfegos. Aqui vou utilizar o seguinte cenário: <br></br>

![CENÁRIO](Imagens/cenario.png) <br></br>

Nesse exemplo vou estar utilizado IPv6 na faixa 2001:DB8:: /64 que é a faixa reservada para documentações (essa faixa de endereços não e deve ser utilizada na prática). Então vou escolher 3 tipos de fluxos de dados: SSH, TFTP e ICP. Também estarei utilizando a marcação pelo NBAR. As configurações de QoS serão aplicadas no roteador **ISP** tanto na interface **E0/0, no sentido de input,** quanto na interface **E0/1**, no sentido de **output**. <br><br>

Então vamos analisar mais de perto a interface E0/0 como o comando: **show interface 0/0**. Observem a saída: <br></br>

![INTERFACE_E0/0](Imagens/interface_e0_0.png) <br></br>

