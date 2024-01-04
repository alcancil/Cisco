# 04 - Switching Distribuído e Centralizado

Este tópico faz parte do item **Describe hardware and software switching mechanisms such as CEF, CAM, TCAM, FIB, RIB, and adjacency tables** do blueprint do exame. <br></br>

Quando um processador de roteador (RP) está equipado com um "motor" de encaminhamento então ele pode tomar todas as decisões de encaminhamento sozinho. Isso é chamado de Arquitetura de encaminhamento centralizada. <br></br>
Na **Arquitetura Centralizada**, quando um pacote chega na interface de entrada, ele é transmitido para o motor de encaminhamento no processador de rotas (RP). O motor de encaminhamento analisa os cabeçalhos dos pacote e decide por qual interface de saída esse pacote vai sair e o coloca em uma única fila de saída. <br></br>
Se as line cards forem equipadas com o motor de encaminhamento, então ela pode tomar decisões de switching sem intervenção do RP, e isso é chamado de **Arquitetura Distribuida**. <br></br>
Em uma arquitetura distribuída, quando um pacote chega na placa de linha de entrada, ele é encaminhado para o motor de forwarding local. Então esse motor faz o lookup de pacotes e, se ele determinar que a saída é uma interface local, ele encaminha o pacote para a interface. <br></br>
Se for verificado que a interface de saída está em outra line card, o pacote é enviado através do switching fabric, diretamente para a line card de saída ignorando o RP. <br></br>