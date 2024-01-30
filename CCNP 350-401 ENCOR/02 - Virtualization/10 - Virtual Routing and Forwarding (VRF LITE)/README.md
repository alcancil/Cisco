# 10 - Virtual Routing and Forwarding (VRF LITE)

O VRF é uma tecnologia de virtualização **em layer 3**. Ele cria **roteadores virtuais** dentro de um roteador físico. <br></br>
É uma tecnologia semelhante as vlans sendo que vlans atuam em camada 2 segregando as portas do switch em determinadas vlans (cria lans virtuais). Já o VRF segrega **caminhos / rotas layer 3**, ou seja, ele cria **tabelas de roteamento diferentes**. Cada tabela de roteamento representa um **roteador virtual**. <br></br>

![VRF](Imagens/vrf.png) <br></br> 

Perceba que quando criamos VRFs, são criadas nova tabelas de roteamento porém, a tabela de roteamento que inicia no roteador permanece é chama de **Global**. <br></br>