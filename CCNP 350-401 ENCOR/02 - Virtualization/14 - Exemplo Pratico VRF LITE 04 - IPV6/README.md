# 14 - Exemplo Pratico VRF LITE 04 - IPV6

Agora eu estou utilizando o mesmo cenário anterior porém eu estou utilizando IPv6. Também nos hosts não vou mais "duplicar" os endereços IPv6, somente nas interfaces que ligam os roteadores. <br></br>  

![CENÁRIO](Imagens/01.png) <br></br>

No cenário temos configurado os hosts. Então vamos entrar nos equipamentos e criar as vrfs. <br></br>

<table>
      <tr>
          <td width="50%"><img src="Imagens/R01/01.png"></img></td>
          <td width="50%"><img src="Imagens/R02/01.png"></img></td>
      </tr>
</table>

Aqui eu defini duas VRFs, **VRF1 e VRF2** nos dois roteadores. Depois disso eu ativei o roteamento ipv6. Agora vamos colocar as interfaces nas respectivas VRFs e configurar seus IPs. <br></br>

<table>
      <tr>
          <td width="50%">ROTEADOR R01</td>
          <td width="50%">ROTEADOR R01</td>
      </tr>
      <tr>
          <td width="50%"><img src="Imagens/R01/02.png"></img></td>
          <td width="50%"><img src="Imagens/R01/03.png"></img></td>
      </tr>
      <tr>
          <td width="50%">ROTEADOR R02</td>
          <td width="50%">ROTEADOR R02</td>
      </tr>
      <tr>
          <td width="50%"><img src="Imagens/R02/02.png"></img></td>
          <td width="50%"><img src="Imagens/R02/03.png"></img></td>
      </tr>
</table>

Por questões de organização e estabilidade vou criar duas interfaces **LOOPBACK (Lo01 e Lo02)** nos dois roteadores e posteriormente vou associá-las as devidas VRFs. <br></br>

<table>
      <tr>
          <td width="50%">ROTEADOR R01</td>
          <td width="50%">ROTEADOR R02</td>
      </tr>
      <tr>
          <td width="50%"><img src="Imagens/R01/04.png"></img></td>
          <td width="50%"><img src="Imagens/R02/04.png"></img></td>
      </tr>
</table>

Nesse momento, agora falta somente a parte de roteamento, que eu optei pelo OSPF single área. <br></br>

## ROTEAMENTO OSPF SINGLE ÁREA

Agora vamos acessar os roteadores e realizar as configurações. <br></br>

<table>
      <tr>
          <td width="50%">ROTEADOR R01</td>
          <td width="50%">ROTEADOR R02</td>
      </tr>
      <tr>
          <td width="50%"><img src="Imagens/R01/05.png"></img></td>
          <td width="50%"><img src="Imagens/R02/05.png"></img></td>
      </tr>
</table>

Então vamos verificar as tabelas de roteamento. <br></br>

<table>
      <tr>
          <td width="50%">ROTEADOR R01</td>
          <td width="50%">ROTEADOR R02</td>
      </tr>
      <tr>
          <td width="50%"><img src="Imagens/R01/06.png"></img></td>
          <td width="50%"><img src="Imagens/R02/06.png"></img></td>
      </tr>
</table>