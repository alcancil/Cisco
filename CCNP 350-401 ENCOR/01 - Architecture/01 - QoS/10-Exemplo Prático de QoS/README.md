# 10 - EXEMPLO PRÁTICO DE QoS

Agora vamos imaginar o seguinte cenário: <br></br>

![WIFI_QoS](Imagens/01-cenario.png)

Aqui irei simular uma pequena empresa que se conecta a sua central passando pela Internet, representada aqui pelo roteador ISP. Então aqui teremos 3 fluxos de tráfego: o trafego HTTP, o tráfego FTP e o tráfego do ICMS. Como esse somente é um exemplo, vamos dizer que o tráfego HTTP é critico para a empresa e queremo dar prioridade maior para esse tipo de tráfego. Em seguida, vamos dar uma prioridade menor ao tráfego FTP e por fim, ao tráfego ICMP. <br></br>
Aqui temos que seguir alguns passos para realizara aconfiguração do QoS que são:
1. Criar um **CLASS MAP** - Selecionar o tráfego importante
2. Criar uma **Policy MAP** - Definir o que fazer com o tráfego
3. Aplicara política em uma interface.
Então a recomendação aqui é que o QoS seja configurado em cada equipamento em que o fluxo fora trafegar.

