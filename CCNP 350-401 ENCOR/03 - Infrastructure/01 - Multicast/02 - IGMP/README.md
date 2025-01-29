# 02 - Internet Group Management Protocol

Esse é o protocolo utilizado para os hosts se juntarem aos grupos de multicast. Atualmente existem 3 versões desse protocolo: **IGMPv1** definida na RFC 1112 que raramente é utilizada, 
**IGMPv2** definida na RFC 2236 que é a mais comum de ser encontrada e **RFC 3376** definida na RFC 3376. <br></br>

![IGMP](Imagens/igmp.png) <br></br>

A mensagens são encapsulados dentro do protocolo  **IP com a marcação de número 2** . Ela possui um TTL (Time To Live) de 1, ou seja, essas mensagens tem escopo local. Só conseguem ser encaminhadas 
para os roteadores locais e não são roteadas para outras redes uma vez que para o próximo salto o TTL é decrementado para 0 e a mensagem é descartada. <br></br>

* **TIPO:** esse campo indica **5** tipos de mensagens IGMP diferentes:
    * **1 - Relatório de adesão versão 2:** essa é uma mensagem com o valor *0x16* que é enviada para os receptores para se juntar ao grupo IGMP ou uma resposta de consulta feita pelos receptores. É referida como IGMP join.
    * **2 - Relatório de adesão versão 1:** é uma mensagem com o valor 0x12 para fins de compatibilidade com o IGMPv1.
    * **3 - Consulta geral de associação:** é uma mensagem com o valor 0x11 enviada para todos os hosts de 224.0.0.1 para verificar se existem hosts nessa sub-rede. Ela seta o campo de endereço de grupo para 0.0.0.0
    * **4 - Consulta específica do grupo:** é uma mensagem com o valor 0x11 e é uma mensagem de resposta para o endereço que pediu para sair do grupo. O endereço do grupo é o IP de destino
endereço do pacote IP e o campo de endereço do grupo.
    * **5 - Tempo máximo de resposta:** Este campo é definido apenas em geral e mensagens de consulta de associação específicas de grupo (tipo valor 0x11); isto especifica o tempo máximo permitido antes de enviar um
relatório de resposta em unidades de um décimo de segundo. Em todos as outras mensagens, é definido como 0x00 pelo remetente e ignorado pelos receptores.
* **TEMPO MÁXIMO DE RESPOSTA:**