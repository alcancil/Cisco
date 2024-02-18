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

Agora é só configurarmos os endereços de ip nas interfaces, uma vez que já criamos as VRFs e já associamos as devidas interfaces. Veja como ficaram as VRFs depois de configurarmos os endereços IP. <br></br>

<table>
       <tr>
           <td width="50%">ROTEADOR R01</td>
           <td width="50%">ROTEADOR R02</td>
       </tr>
       <tr>
           <td width="50%"><img src="Imagens/R01/10.png"></img></td>
           <td width="50%"><img src="Imagens/R02/02.png"></img></td>
       </tr>
</table>

Até aqui confesso que é pura e simples repetição do laboratório anterior. Mas agora vamos entrar na parte de roteamento. Agora vou utilizar protocolos dinâmicos. <br></br>

## OPEN SHORTEST PATH (OSPF) SINGLE ÁREA

Agora vou demonstrar como realizar o roteamento através do OSPF single área. Aqui, o processo é quase o mesmo quando temos nenhuma VRF configurada.<br></br>
Então vamos acessar R01 e habilitar o OSPF nas interfaces **E0/0 e E0/1**. Também vamos definir as mesmas interfaces como sendo do tipo **point-to-point** pois não queremos ativar a eleição de DR e BR nesses links uma vez que não temos mais roteadores participando do processo. <br></br>

<table>
       <tr>
           <td width="50%"><img src="Imagens/ospf/R01/01.png"></img></td>
           <td width="50%"><img src="Imagens/ospf/R01/02.png"></img></td>
       </tr>
</table>

![R01](Imagens/ospf/R01/03.png)

Então o mesmo deverá ser feito em R02. <br></br>

<table>
       <tr>
           <td width="50%"><img src="Imagens/ospf/R02/01.png"></img></td>
           <td width="50%"><img src="Imagens/ospf/R02/02.png"></img></td>
       </tr>
</table>

![R02](Imagens/ospf/R02/03.png)

Podemos notar que agora o processo de adjacência está completo e os roteadores se tornaram vizinhos. <br></br> 

<table>
       <tr>
           <td width="50%"><img src="Imagens/ospf/R01/04.png"></img></td>
           <td width="50%"><img src="Imagens/ospf/R02/04.png"></img></td>
       </tr>
</table>

Mas ainda não completamos nosso cenário. Falta ainda habilitarmos o OSPF na interfaces **E0/2 e E0/3 em R01** e **E0/2 e E0/3 em R02**. Então vamos configurar os roteadores. <br></br>

<table>
       <tr>
           <td width="50%"><img src="Imagens/ospf/R01/05.png"></img></td>
           <td width="50%"><img src="Imagens/ospf/R02/05.png"></img></td>
       </tr>
</table>

Agora vamos verificar as tabelas de roteamento. <br></br>

![R01](Imagens/ospf/R01/06.png) <br></br>
![R02](Imagens/ospf/R02/06.png) <br></br>

Deixo aqui uma cópia do arquivo com a resolução . [LAB(RESOLVIDO)](Arquivos/vrf(resolvido).zip)
