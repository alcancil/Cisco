# 17 - Exemplo Prático - Tuneis GRE 01

Vamos imaginar a seguinte situação: estamos na empresa XPTO e precisamos ter comunicação com a filial através da Internet. O problema aqui é que ambas as partes, matriz e filial possuem somente redes utilizando o protocolo IPv4 e a empresa que fornece o link de Internet agora só funciona com o protocolo IPv6. Uma solução seria se utilizar os Tuneis GRE. Vamos analisar o cenário.<br></br>

![CENÁRIO](Imagens/cenario.png) <br></br>

Como podemos notar, o link da operadora só possui IPv6 e a matriz / filial só IPv4. Basicamente o que iremos fazer é criar um túnel GRE entra Matriz Filial e ele vai transportar o IPv4 dentro do Túnel GRE, ou seja, para os usuários é como se o tráfego passasse por R01 e fosse direto para R02 com comunicação IPv4. <br></br>

![FLUXO](Imagens/fluxo.png) <br></br>

Mas como essa mágica é feita se temos somente uma rede IPv4 e a Operadora IPv6 ?  Simples, o GRE encapsula o pacote original e assim, o pacote encapsulado é suportado pelo túnel. <br><br> 

![ENCAPSULADO](Imagens/encapsulado.png) <br></br>

Então vamos as configurações. Vamos acessar primeiro o roteador R01. Aqui vou assumir que o endereçamento de IP das interfaces já está configurada e que vamos configurar o default gateway para a interface de saída com a Internet, a interface E0/1. <br></br>

![ROTA_DEFAULT](Imagens/R01/01.png) <br></br>

E agora vamos criar a interface túnel. <br></br>

![TÚNEL](Imagens/R01/02.png) <br></br>

Percebam que aqui eu indico a origem **(tunnel source)** como sendo a interface com saída para a Internet, a **E0/1**. Como destino eu indiquei o endereço IPv6 do roteador R04 da filial que está ligado na Internet. Então aqui temos origem e destino do túnel. Como vamos atravessar o tráfego pela Internet que somente é em IPv6, temos que fornecer o comando **tunnel mode gre ipv6** para ele entender que irá passar pelo IPv6. E depois eu configurei o endereço IPv4 dessa interface, ou seja, o túnel será formado em IPv4 mas está passando pela Internet em IPv6. <br></br>

Como podemos notar, ele exibe a Informação de que a interface Tunnel0 fica ativa mesmo não tendo a outra ponta do Túnel configurada. Também podemos confirmar através do comando **show ip interface brief**. <br></br>

![INTERFACE](Imagens/R01/03.png) <br></br>

Então agora o que falta é fazer o mesmo no outro lado do túnel, ou seja, fazer o mesmo em R04. Então vamos lá. <br></br>

![ROTA_DEFAULT](Imagens/R04/01.png) <br></br> 

Primeiro configuramos a rota padrão para a interface que está com saída para Internet. Agora vamos configurar a interface Tunnel0. <br></br>

![TÚNEL](Imagens/R04/02.png) <br></br>

Da mesma forma que configuramos em R01, aqui definimos a interface **tunnel source** como sendo a **E0/1** que tem a saída para Internet. Como destino **(source detination)** eu indico o IPv6 do roteador R01 da matriz. Também precisamos indicar o modo do túnel como **tunnel mode gre ipv6**. <br></br>

Então vamos verificar o status da interface tunel0. <br></br>

![INTERFACE](Imagens/R04/03.png) <br></br>

Bom, agora é possível se pingar os endereços dos túneis mas não os endereços internos da Matriz e Filial. Ainda falta a parte de roteamento. Para isso eu escolhi o protocolo OSPF como protocolo de roteamento. Então vamos configurar as duas pontas do túnel. <br></br>

<Table>
      <TR>
          <Td width="50%"><img src="Imagens\R01\04.png"> </img> </Td>
          <Td width="50%"><img src="Imagens\R04\04.png"> </img> </Td>
      </TR>
</Table>