# 14 - POLICING X SHAPPING

Agora preciso fazer uma pausa para falar um pouco mais dessas duas técnicas de QoS: **Policing** e **Shapping**. Elas são duas técnicas parecidas mas que trabalham um pouco diferente. No **Policing** definimos uma taxa para monitaramento e o que passar dessa taxa é descartado ou remarcado. Já no **Shapping** o que passa dessa taxa é enfileirado e a transmissão para, e começa a transmitir desse buffer, depois retorna a transmissão e por ai adiante. 

![POLICING](Imagens/policing.png) <br></br>
![SHAPPING](Imagens/shapping.png) <br></br>

**OBS:** A recomendação de uso para o uso do shapping **é na interface de saída**. <br></br>

Para isso são utilizados alguns algorítmos e alguns tipo de filas para se utilizar essas duas técnicas. <br></br>

## MARKDOWN

Como dito anteriormente, o policer fica monitorando uma taxa de transmissão e quando essa taxa é excedida ele ou descrta ou trafego ou remarca com uma prioridade menor.<br></br>
Por exemplo, um tráfego excedente que está marcado com o valo **AFx1** deve ser rebaixado com o valor **AFx2** ou mesmo **AFx3**, baixando a prioridade em 2 classes. <br></br>
Depois de remarcar / rebaixar a prioridade do tráfego, os mecanismos que evitam o congestionamento, como um DSCP - baseado no WRED (Weighted Random Early Detection), devem ser configurados para descartar mais agressivamente tráfegos marcados com **AFx3** do que **AFx2**. E o **AFx2** deve ser mais descartado do que **AFx1** e menos que o **AFx3** <br></br>

## TOKEN BUCKET ALGORITHMS

Os Policers e os Shappers são baseados em algorítmos de **token buccket**. Então vou citar alguns termos para demonstrar como esse tipo de algorítmo funciona: 
- **Commited Information Rate (CIR)**: essa é a taxa monitorada, definida no controle de tráfego. É medida em bits por segundo.
- **Commited Time Interval (TC)**: O intervalo de tempo, em milessegundos (ms) dividido pela rajada / pico de tráfego (BC). **TC** pode ser calculado pela fórmula: **TC = (BC[bits]) / CIR[bps] x 1000**
- **Cmmited Burst Size (BC)**: o tamanho máximo do CIR token bucket, medido em bytes, e o máximo montante de tráfego que pode ser cálculado atráves da fórmula **BC = CIR x (TC / 1000)**
- **TOKEN**: um único token representa **1 byte ou 8 bits**

**OBS:** <br></br>
- **TC** é o número de segmentos que será dividido em um segundo
- **BC** é o número de bits permitidos para serem enviados por TC
- **CIR** é a taxa que quer manter

![INTERFACE](Imagens/int_100_mbps.drawio.png) <br></br>
