# 10 - Virtual Routing and Forwarding (VRF LITE)

O VRF é uma tecnologia de virtualização **em layer 3**. Ele cria **roteadores virtuais** dentro de um roteador físico. <br></br>
É uma tecnologia semelhante as vlans sendo que vlans atuam em camada 2 segregando as portas do switch em determinadas vlans (cria lans virtuais). Já o VRF segrega **caminhos / rotas layer 3**, ou seja, ele cria **tabelas de roteamento diferentes**. Cada tabela de roteamento representa um **roteador virtual**. <br></br>

![VRF](Imagens/vrf.png) <br></br> 

Perceba que quando criamos VRFs, são criadas nova tabelas de roteamento porém, a tabela de roteamento que inicia no roteador permanece é chama de **Global**. <br></br>
Porém as interfaces, tabelas de encaminhamento **são completamente isoladas** entre as VRFs, impedindo que o tráfego de uma VRF seja encaminhado para outra VRF. Então, inicialmente todas as interfaces **pertencem a tabela global inicialmente**. A partir do momento que indicamos em uma interface a qual VRF ela deve ingressar, ai ela passa a fazer parte somente desta VRF. <br></br>
Então as VRFs segregam o tráfego de camada 3. Vamos imaginar que queremos isolar o tráfego de uma empresa de seus colaboradores externos, ou mesmo se queremos isolar o tráfego de voz do tráfego de dados e do tráfego de vídeo também. Então podemos criar uma VRF para cad tipo de tráfego, ou departamento, por exemplo. <br></br>
As VRFs são de camada 3 e, portanto, são configuradas em: **interfaces, sub-interfaces e svis (switches layer3).** Não funcionam em switches layer 2. <br></br>