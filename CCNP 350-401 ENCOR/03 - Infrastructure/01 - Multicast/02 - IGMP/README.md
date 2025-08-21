# Índice

- [Índice](#índice)
  - [02 - Internet Group Management Protocol](#02---internet-group-management-protocol)
  - [Aplicações](#aplicações)
  - [IGMPv1](#igmpv1)
  - [IGMPv2](#igmpv2)
  - [IGMPv3](#igmpv3)
  - [Referências](#referências)

## 02 - Internet Group Management Protocol

Esse protocolo permite que hosts e roteadores adjacentes estabeleçam comunicação multicast em redes IP, otimizando o uso de banda e a transmissão de pacotes. O multicast pode ter um único ou vários remetentes e destinatários. Ele é utilizado em redes IPv4 e em redes IPv6 é utilizado o Multicast Listener Discovery (MLD) que é um protocolo que gerência membros multicast IPv6.  

O **IGMP (Internet Group Management Protocol)** é o protocolo responsável por permitir que os hosts informem ao roteador local sua intenção de ingressar ou sair de grupos multicast.  

Ele opera na **Camada 3 (Rede) do modelo OSI**, mas sua função está voltada principalmente **ao controle e gerenciamento de grupos multicast**. O IGMP atua dentro de **uma sub-rede,** funcionando como um protocolo de vizinhança entre os hosts e o roteador multicast conectado ao mesmo segmento.

Dessa forma, o roteador consegue identificar quais grupos multicast possuem membros ativos naquela rede local, garantindo que o tráfego seja encaminhado apenas para os segmentos onde realmente há receptores interessados.

Sem o IGMP, roteadores e switches não teriam como saber com precisão onde entregar o tráfego multicast, o que resultaria em desperdício de banda e, em cenários mais críticos, em inundações desnecessárias de tráfego na rede.

Atualmente existem 3 versões desse protocolo: **IGMPv1** definida na RFC 1112 que raramente é utilizada, **IGMPv2** definida na RFC 2236 que é a mais comum de ser encontrada na **RFC 3376** e **IGMPv3** que é definida na rfc RFC 3376.  

## Aplicações

- **Streaming:** o IGMP é muito utilizado em streaming de áudio e vídeo onde uma pessoa transmite um único fluxo de comunicação para um grupo em específico.
- **Jogos Online:** esse também é um uso comum para esse protocolo onde hoje em dia cada vez mais os usuários de jogos se tornaram mais exigentes e com a utilização do IGMP a comunicação se dá de forma mais eficiente.
- **Videoconferência:** essa é uma modalidade de comunicação que vem se tornando cada vez mais popular e exige também um uso mais eficiente de banda.  

## IGMPv1

![IGMP](Imagens/igmpv1.png)  

- **VERSÃO:** Campo configurado em 1. Versão do protocolo.
- **TIPO:** 1 para consulta de associação e relatório de associação de destinatário.  
- **NÃO UTILIZADO:** campo não utilizado preenchido com zeros.
- **CHECKSUM:** campo de 16 bits 1 que complementa a soma da mensagem IGMP. É o mesmo algoritmo utilizado pelo TCP/IP
- **ENDEREÇO DE GRUPO:** O campo de endereço do grupo é zero quando enviado e ignorado quando recebido na mensagem de consulta de associação. Em uma mensagem de relatório de associação, o campo de endereço do grupo utiliza o endereço do grupo de hosts IP do grupo que está sendo relatado

## IGMPv2

![IGMP](Imagens/igmpv2.png)  

As mensagens IGMPv2 são encapsuladas no protocolo **IP com a marcação de número 2** e possuem um TTL (Time To Live) igual a 1, limitando seu alcance à rede local. Quando o pacote chega ao próximo salto, o TTL é decrementado para 0 e descartado.

- **TIPO:** esse campo indica **5** tipos de mensagens IGMP diferentes:
  - **1 - Relatório de adesão versão 2:** essa é uma mensagem com o valor *0x16* que é enviada para os destinatários para se juntar ao grupo IGMP ou uma resposta de consulta feita pelos destinatários. É referida como IGMP join.
  - **2 - Relatório de adesão versão 1:** é uma mensagem com o valor 0x12 para fins de compatibilidade com o IGMPv1.
  - **3 - Consulta geral de associação:** é uma mensagem com o valor 0x11 enviada para todos os hosts de 224.0.0.1 para verificar se existem hosts nessa sub-rede. Ela seta o campo de endereço de grupo para 0.0.0.0
  - **4 - Consulta específica do grupo:** é uma mensagem com o valor 0x11 e é uma mensagem de resposta para o endereço que pediu para sair do grupo. O endereço do grupo é o IP de destino
endereço do pacote IP e o campo de endereço do grupo.
  - **5 - Tempo máximo de resposta:** Este campo é definido apenas em geral e mensagens de consulta de associação específicas de grupo (tipo valor 0x11); isto especifica o tempo máximo permitido antes de enviar um
relatório de resposta em unidades de um décimo de segundo. Em todos as outras mensagens, é definido como 0x00 pelo remetente e ignorado pelos destinatários.
- **CHECKSUM:** campo de 16 bits 1 que complementa a soma da mensagem IGMP. É o mesmo algoritmo utilizado pelo TCP/IP
- **ENDEREÇO DE GRUPO:** Este campo é definido como 0.0.0.0 nas mensagens de consulta geral e é definido para o endereço do grupo em configurações de mensagens específicas do grupo. As mensagens de relatório de adesão contém
o endereço do grupo que está sendo reportado neste campo; as mensagens de saída do grupo contém o endereço do grupo que está sendo deixado neste campo.  

**OBS:**  
    **Tipos**

    0x11 for Membership Query
    0x12 for IGMPv1 Membership Report
    0x16 for IGMPv2 Membership Report
    0x22 for IGMPv3 Membership Report
    0x17 for Leave Group  

Quando um destinatário quer receber um fluxo multicast, ele envia um relatório de adesão não solicitado para o roteador local, para o grupo que ele deseja se juntar.  

O termo oficial é ‘relatório de adesão não solicitado’. No entanto, é comum ouvir a expressão IGMP Join, por ser mais simples de usar — embora não seja o termo padronizado.  

Então o roteador local envia uma mensagem PIM Join em direção á origem para solicitar um fluxo multicast. Quando o roteador local começa a receber o fluxo multicast, ele envia de volta o fluxo para a sub-rede que o destinatário está.  

Logo após, o roteador começa a enviar mensagens de consulta de associação para a sub-rede, com o endereço de todos os hosts 224.0.0.1 para descobrir quais são os hosts presentes.
Essas mensagens de consulta gerais possuem um tempo padrão de resposta de 10 segundos por padrão.  

Em resposta a essas consultas, os destinatários configuram um timer entre 0 e 10 segundos. Quando esse timer expira, os destinatários enviam de volta um relatório de adesão informando a qual
grupo pertencem. Se um destinatário receber o relatório de outro destinatário para um dos grupos ao qual pertence enquanto estiver com um timer em execução, ele interrompe seu
timer para o grupo especificado e não envia um relatório; isso serve para suprimir relatórios duplicados.  

Quando um destinatário quer deixar o grupo, ele envia uma mensagem para o endereço 224.0.0.2 ( endereço all-routers group) se ele for o último destinatário a responder as consultas.
Caso contrário, ele pode sair do grupo de forma silenciosa pois neste caso deve existir algum outro destinatário na sub-rede.  

Quando a mensagem de saída do grupo é recebida pelo roteador, ela segue com uma consulta de associação específica do grupo para o grupo endereço multicast para determinar se há
algum destinatário interessado no grupo restante na sub-rede. Se não existir outro, então o remove o estado de IGMP do grupo.  

Mas pode ocorrer que nessa sub-rede exista tenha mais do que somente um roteador. Nesse caso ocorrerá uma eleição para ver quem vai responder as consultas IGMP. Então os roteadores
enviam mensagens de consultas genéricas de adesão contendo o endereço do seu IP com destino para 224.0.0.1 . Quando um roteador recebe uma mensagem dessas, ele compara o endereço IP
da mensagem com o endereço IP da sua própria interface de rede. O roteador **com o menor endereço IP** então é eleito como o roteador que irá responder as consultas IGMP dessa sub-rede.
Nesse momento, os outros roteadores iniciam um timer que reinicia toda a vez que ele recebe uma mensagem de consulta de adesão do roteador que venceu a eleição.  

Se por algum motivo o roteador que venceu a eleição para de enviar as mensagens, uma nova eleição ocorre. Um roteador que não responde as consultas, espera o dobro do tempo, que por
padrão é 60 segundos, e se ele não receber nenhuma consulta nesse intervalo, ele aciona uma nova eleição de IGMP.  

[IGMPv2 - Animação](https://alcancil.github.io/Cisco/CCNP%20350-401%20ENCOR/03%20-%20Infrastructure/01%20-%20Multicast/02%20-%20IGMP/Arquivos/igmpv2.html)

## IGMPv3

O IGMPv3 evolui em relação à versão 2 ao permitir identificar a origem desejada do tráfego multicast, possibilitando que os destinatários apliquem filtros de origem e escolham de quais fontes receber o tráfego.  

Essa versão foi desenvolvida para coexistir junto das outras. A diferença da versão 3 para 2 é que na versão 3 foram acrescentados novos campos na consulta de adesão e um novo tipo de
mensagem IGMP chamado relatório de associação da versão 3 para oferecer suporte à filtragem de origem.  

IGMPv3 oferece suporte a aplicativos que sinalizam fontes explicitamente do qual desejam receber tráfego. Com IGMPv3, os destinatários sinalizam a intenção de se associar a um endereço
de grupo multicast usando um relatório de associação nos dois modos a seguir:

- **MODO DE INCLUSÂO:** nesse modo, o destinatário anuncia a adesão para um endereço de grupo de multicast e fornece uma lista (include list) de endereços de fontes de quem ele deseja receber o tráfego
- **MODO DE EXCLUSÂO:** nesse modo, o destinatário anuncia a adesão para um endereço de grupo de multicast e fornece uma lista (exclude list) de endereços de quem ele não receber o tráfego.
Para receber o tráfego de todas as fontes, que é o comportamento do IGMPv2, o destinatário utiliza **o modo de exclusão de adesão com um uma lista de exclusão vazia**

![IGMP](Imagens/igmpv3.png)  

- **CÓDIGO MÁXIMO DE RESPOSTA :** Este campo é ignorado para tipos de mensagens diferentes de consulta de associação. Para o tipo de consulta de adesão, é o tempo máximo permitido antes de enviar um relatório de resposta. O valor está em unidades de 0,1 segundos.
- **CHECKSUM :** campo de 16 bits 1 que complementa a soma da mensagem IGMP. É o mesmo algoritmo utilizado pelo TCP/IP.
- **ENDEREÇO DE GRUPO :** É definido como 0 ao enviar uma consulta geral. Caso contrário, endereço multicast para consultas específicas de grupo ou de origem.
- **RESV :** É configurado em 0 e é ignorado quando recebido
- **S FLAG :** Representa o sinalizador Suprimir processamento do lado do roteador. Quando o sinalizador está definido, ele indica a supressão das atualizações de timer que os roteadores multicast realizam ao receber qualquer consulta.
- **QRV :** Representa a variável de robustez do consultor (querier). Os roteadores continuam recuperando o valor QRV da consulta recebida mais recentemente como seu próprio valor até que o QRV recebido mais recentemente seja zero.
- **QQIC :** Representa o código de intervalo de consulta do consultor.
- **NÚMERO DE FONTES :** Representa o número de endereços de origem presentes na consulta. Para consulta geral ou consulta específica de grupo, este campo é zero e para consulta específica de grupo e origem, este campo é diferente de zero.
- **ENDEREÇO DE ORIGEM[N] :** Representa o endereço IP unicast para N campos.

[IGMPv3 - Animação](https://alcancil.github.io/Cisco/CCNP%20350-401%20ENCOR/03%20-%20Infrastructure/01%20-%20Multicast/02%20-%20IGMP/Arquivos/igmpv3.html)

## Referências

| RFC   | Título                                                                 | Link                                                    |
|-------|------------------------------------------------------------------------|---------------------------------------------------------|
| RFC 1112 | Host Extensions for IP Multicasting           | [https://www.rfc-editor.org/rfc/rfc1112](https://www.rfc-editor.org/rfc/rfc1112) |
| RFC 2236 | Internet Group Management Protocol, Version 2 | [https://www.rfc-editor.org/rfc/rfc2236](https://www.rfc-editor.org/rfc/rfc2236) |
| RFC 3376 | Internet Group Management Protocol, Version 3 | [https://www.rfc-editor.org/rfc/rfc3376](https://www.rfc-editor.org/rfc/rfc3376) |
