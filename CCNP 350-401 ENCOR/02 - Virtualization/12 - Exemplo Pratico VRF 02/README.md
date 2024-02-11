# 12 - Exemplo Pratico VRF 02

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

Deixo aqui uma cópia do arquivo com a resolução . [LAB(RESOLVIDO)](Arquivos/vrf(resolvido).zip)
