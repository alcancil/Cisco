# 01 - Multicast

Agora como falar sobre um tipo de comunicação é preciso se fazer uma pequena revisão. Então primeiramente vamos observar os tipos de comunicação existentes.

| UNICAST                         | BROADCAST                            | MULTICAST                                     |
|---------------------------------|--------------------------------------|-----------------------------------------------|
|![UNICAST](Imagens/unicast.png)  | ![BROADCAST](Imagens/broadcast.png)  | ![MULTICAST](Imagens/multicast.png)           |

Como podemos observar, quando o tráfego vai de um emissor para um receptor podemos chamar de **unicast**, ou seja, é um trafego direto. Um exemplo que podemos citar desse tipo de comunicação é a ligação telefônica por exemplo, ou mesmo quando se faz um acesso via ssh para algum equipamento. <br></br>

Depois temos o **broadcast**. Diferente do primeiro tipo de comunicação, esse é um tipo de comunicação onde um envia e todos recebem. Podemos citar o exemplo do protocolo arp onde os equipamentos precisam mapear o endereço mac com o endereço IP. Para o protocolo arp poder descobrir a quem pertence um endereço IP por exemplo, ele faz um "flood" para todos os equipamentos na rede e com isso a comunicação se dá de forma conhecida por **broadcast**. <br></br>

Agora se analisarmos bem esses dois tipos de comunicação iremos perceber que no unicast a comunicação se dá de uma forma mais eficiente pois ela entrega os pacotes somente para o destinatário escolhido. Já no broadcst, todos recebe os pacotes independentemente se eles precisam ou não receber tal pacote. Isso faz com que o host que receba o pacote tenha que analisar o mesmo, verificar se ele é o destinatário e se não for, descartar o mesmo. Essa forma de comunicação não é muito eficiente pois em ambientes muito grandes ocupa banda muitas vezes desnecessárias e faz com que o host tenha que processar o pacote e consumir memória e processador. <br></br>

Pensando nisso, foi desenvolvido o **multicast**. Agora, nesse tipo de comunicação, existe uma fonte de envio de dados mas somente um grupo, ou grupos de hosts que irão receber esses dados. Com isso, o consumo de banda do meio é utilizada de forma mais eficiente e não força quem não tem que fazer parte da conversa receber dados indesejados. <br></br>

## MTUs acima do padrão - Jumbo Frames

 **1400 bytes**.