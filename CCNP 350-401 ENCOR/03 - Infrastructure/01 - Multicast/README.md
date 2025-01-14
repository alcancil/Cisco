# 01 - Multicast

Agora como falar sobre um tipo de comunicação é preciso se fazer uma pequena revisão. Então primeiramente vamos observar os tipos de comunicação existentes.

| UNICAST                         | BROADCAST                            | MULTICAST                                     |
|---------------------------------|--------------------------------------|-----------------------------------------------|
|![UNICAST](Imagens/unicast.png)  | ![BROADCAST](Imagens/broadcast.png)  | ![MULTICAST](Imagens/multicast.png)           |

Como podemos observar, quando o tráfego vai de um emissor para um receptor podemos chamar de **unicast**, ou seja, é um trafego direto. Um exemplo que podemos citar desse tipo de comunicação é a ligação telefônica por exemplo, ou mesmo quando se faz um acesso via ssh para algum equipamento. <br></br>

Depois temos o **broadcast**. 

## MTUs acima do padrão - Jumbo Frames

 **1400 bytes**.