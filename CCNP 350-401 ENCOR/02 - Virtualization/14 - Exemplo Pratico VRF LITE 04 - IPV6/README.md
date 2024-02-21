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

Aqui podemos ver que eu deixei as interfaces e0/2 e e0/3 dos dois roteadores na tabela de roteamento global. Portanto, só as outras interfaces que foram alocadas nas VRFs. Nesse momento, agora falta somente a parte de roteamento, que eu optei pelo OSPF single área. <br></br>