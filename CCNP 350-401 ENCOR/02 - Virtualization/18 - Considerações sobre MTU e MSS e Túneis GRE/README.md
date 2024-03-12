# 18 - Considerações sobre MTU e MSS e Túneis GRE

**MTU = Maximum Transmission Unit (Uniddade Máxima de Transmissão)** <br></br>
**MSS = Maximum Segment Size (Tamanho Máximo de um Segmento)**

## MTU

Quando falamos de MTU, precisamos ter em mente que existem diferentes tipos de MTU que seguem o modelo OSI. <br></br>
Então quando falamos MTU, normalmente estamos falando de **camada 02**, ou seja, estamos falando do tamanho máximo em bytes da quantidade de dados que um quadro pode ter. <br></br>
Mas não existe uma negociação no meio, esse é um parâmetro que é configurado nas portas de roteadores, switches, etc. <br></br>

![MTU](/Imagens/mtu.png) <br></br>