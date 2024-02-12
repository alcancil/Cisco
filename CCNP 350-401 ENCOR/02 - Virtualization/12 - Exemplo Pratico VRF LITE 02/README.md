# 12 - Exemplo Pratico VRF LITE 02

Aqui não vou me alongar muito nas explicações e vou direto a prática. Para esse segundo exemplo vou utilizar o mesmo cenário doe exemplo anterior.

![CENÁRIO](Imagens/01.png) <br></br>

No exemplo anterior eu criei duas VRFs em cada roteador e escolhi utilizar rotas estáticas como meio de roteamento. Mas sabemos que para a parte de roteamento podemos utilizar protocolos dinâmicos para isso. Então, como parte da pratica, vou remover as configurações e vou começar do zero. <br></br>
Então vamos entrar no roteador 01 e mostrar as configurações das vrfs e as suas tabelas de roteamento. <br></br> 

<table>
       <tr>
           <td width="33%"><img src="Imagens/R01/01.png"></img></td>
           <td width="33%"><img src="Imagens/R01/02.png"></img></td>
           <td width="33%"><img src="Imagens/R01/03.png"></img></td>
       </tr>
</table>

Agora vamos remover as rotas estáticas e as vrfs.<br></br>

<table>
       <tr>
           <td width="50%"><img src="Imagens/R01/04.png"></img></td>
           <td width="50%"><img src="Imagens/R01/05.png"></img></td>
       </tr>
</table>

Então agora devemos remover as vrfs. Note que ao retirarmos as vrfs de R01, automaticamente nos é apresentada a mensagem de que os ips são removidos das interfaces e com isso, as interfaces perdem também as associações com as vrfs.<br></br>

<table>
       <tr>
           <td width="50%"><img src="Imagens/R01/06.png"></img></td>
           <td width="50%"><img src="Imagens/R01/07.png"></img></td>
       </tr>
</table>

O mesmo processo deverá ser realizado em R02.<br></br>
Bom, como agora temos os roteadores configurados na condição inicial (sem VRFs, só com a tabela de roteamento global), então vamos configurar as VRFs 1 e 2 nos roteadores R01 e R02. Sim esse processo já foi feito anteriormente e não muda em nada, mas como trata-se de prática, quantos mais praticamos, mais fixamos os conceitos e comandos. Então vamos-lá. <br><br>

<table>
       <tr>
           <td width="50%"><img src="Imagens/R01/08.png"></img></td>
           <td width="50%"><img src="Imagens/R01/09.png"></img></td>
       </tr>
</table>

Novamente, devemos proceder com os mesmos comandos em R02.<br></br>
Veja como ficou em R02.<br></br>

![R02](Imagens/R02/01.png) <br></br>

Deixo aqui uma cópia do arquivo com a resolução . [LAB(RESOLVIDO)](Arquivos/vrf(resolvido).zip)
