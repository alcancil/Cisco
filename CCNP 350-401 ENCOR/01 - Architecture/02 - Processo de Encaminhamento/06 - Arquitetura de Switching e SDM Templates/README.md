# 06 - Arquitetura de Switching e SDM Templates

O processador de rotas (RP) é responsável por aprender a topologia da rede e construir a rooute table (RIB). <br></br>
Uma falha no RP pode ocasionar em um reset nos protocolos de roteamento e adjacências. Durante a falha, é preferível "esconder" essa falha e permitir que o roteador continue encaminhando pacotes utilizando a CEF e suas entradas do que causar o descarte temporário de pacotes. <br></br>
O **statful switchover (sso)** é um recurso de redundância que permite um roteador CISCO com dois RPs sincronizarem a configuração do control plane. O processo de espelhar as informações entre os RFs é chamado de **checkpointing**. Os roteadores com o sso habilitado sempre fazem o checkpoint das line cards e dos estados dos protocolos de camada 2. Durante o switchover o RP que está em standby assume o controle imediatamente.

## SDM Templates

O número de endereços MAC que um switch necessita, comparado com o número de rotas que ele suporta depende do local onde ele está na rede. A memória para as tabelas **TCAM** são estaticamente alocadas durante o processo de boot do switch. Quando uma seção do hardware está cheia, todo o processamento excedente é enviado para a CPU. Isso impacta negativamente a performance do switch. <br></br>
Os indices de alocação entre várias tabelas TCAM são armazenadas e podem ser modificadas com o **SDM (Switching Database Manager templates)**. O template sdm pode ser configurado em switches da linha catalyst 9.000 com o comando **sdm prefer {vlan | advanced}**. O switch precisa ser reiniciado com o comando **reload**.