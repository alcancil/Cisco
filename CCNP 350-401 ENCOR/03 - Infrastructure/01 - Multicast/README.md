# 01 - Multicast

## MULTICAST

Agora como falar sobre um tipo de comunicação é preciso se fazer uma pequena revisão. Então primeiramente vamos observar os tipos de comunicação existentes.

| TIPOS DE COMUNICAÇÂO                                                                                                   |
|---------------------------------|--------------------------------------|-----------------------------------------------|
|![UNICAST](Imagens/unicast.png)  | ![BROADCAST](Imagens/broadcast.png)  | ![MULTICAST](Imagens/multicast.png)           |

Então como não há uma negociação, um lado do link não conhece o MTU do outro lado, e com isso, poderão existir MTUs diferentes. Nesse caso dizemos que quando essa situação ocorre temos **um mismatch de MTUs**. Com isso os pacotes são descartados e o contador **Giant** é acrescentado. <br></br>

## MTUs acima do padrão - Jumbo Frames

Bom sabemos o tamanho padrão do MTU é de 1500 bytes. Mas e se ocorrer uma necessidade de se transmitir informações maiores do que **1500 bytes?** <br></br>
Existem os frames chamados de ***Jumbo Frames***, ou seja, são frames **são frames maiores que 1500 bytes e vão até 9000 byes**. <br></br>
Esse tipo de necessidade é mais comum em data center. Para essa comunicação ocorrer, é necessário que esse tipo de frame seja configurado nas portas dos roteadores e switches e; os servidores e endpoints envolvidos também estejam configurados para utilizar os *jumbo frames*. <br></br>

![MTU1](Imagens/mtu1.png) <br></br>

## IP MTU

![MTU2](Imagens/mtu2.png) <br></br>

![CABEÇALHO](Imagens/cabecalho.png) <br></br>

Esse é um valor de camada 3, ou seja, é um valor que precisa ser ajustado conforme o tipo de protocolo que irá passar nas interfaces. <br></br>
Então no caso de um túnel GRE, precisam ser adicionadas dados dos cabeçalhos IP original. Por esse motivo, o tamanho do **IP MTU** fica menor que os 1500 bytes. <br></br>
Se esse valor não for ajustado e o IP MTU ficar acima dos 1500 bytes, ou o pacato é descartado ou ocorrerá fragmentação. Isso pode ser um problema pois existem equipamentos que não suportam a fragmentação. Isso pode até fazer com que o túnel GRE pare de funcionar se ocorrer. <br></br>

No exemplo, o MTU no túnel GRE foi configurado para **1400 bytes**. Então podemos observar que 1400 bytes é o tamanho total do pacote IP nesse túnel e que depois é **adicionado mais 24 bytes** do túnel GRE. Com isso, não ocorrerá fragmentação. <br></br>

## MSS - CAMADA 4

![MTU3](Imagens/mtu3.png) <br></br>

Agora como estamos na camada 4, quando a origem e o destino querem se comunicar, então eles realizam o hadnshake triplo para o tcp. <br></br>
Co isso, o valor de MSS é ajustado automaticamente para **1460**. Mas por que esse tamanho ? <br></br>
Bom sabemos que o MTU do quadro Ethernet é 1500 bytes. Então se o MSS for de **1460**, ainda faltam o cabeçalho IP e TCP. Então a conta fica assim: **20 bytes do IP + 20 bytes do TCP + 1460 MSS =** ***1500 bytes.***

## Ajustes no MSS

Quando o TCP começa a negociação ele pode ajustar automaticamente. Mas vamos analisar a situação: <br></br>

![MTU4](Imagens/mtu4.png) <br></br>

Agora nesse caso, entre os roteadores temos uma nuvem. Então precisamos ajustar o mss para suportar o cabeçalho do protocolo que atravessa a nuvem. Nesse caso, o mss ficou em 1432. Com isso, se realizarmos a soma: 20 bytes IP + 20 bytes TCP + 1432 MSS = **1472 bytes** Com isso sobra espaço para a nuvem utilizar algum outro protocolo ou mesmo algum outro túnel. <br></br>

## Comandos no CISCO IOS

* **MTU L2:** ***mtu valor-bytes***
* **MTU L3:** ***ip myu valor-bytes***
* **MSS:** ***tcp adjust-mss valor bytes***

Para o GRE, podemos configurar o MTU L3, MSS ou os dois em conjunto para evitar a fragmentação.