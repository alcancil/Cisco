# 10 - EXEMPLO PRÁTICO DE QoS

Agora vamos imaginar o seguinte cenário: <br></br>

![WIFI_QoS](Imagens/01-cenario.png)

Aqui irei simular uma pequena empresa que se conecta a sua central passando pela Internet, representada aqui pelo roteador ISP. Então aqui teremos 3 fluxos de tráfego: o trafego HTTP, o tráfego TFTP e o tráfego do ICMP. Como esse somente é um exemplo, vamos dizer que o tráfego HTTP é critico para a empresa e queremos dar prioridade maior para esse tipo de tráfego. Em seguida, vamos dar uma prioridade menor ao tráfego FTP e por fim, a menor prioridade será dada ao tráfego ICMP. <br></br>
Aqui temos que seguir alguns passos para realizara aconfiguração do QoS que são:
1. Criar um **CLASS MAP** - Selecionar o tráfego importante
2. Criar uma **Policy MAP** - Definir o que fazer com o tráfego
3. Aplicara política em uma interface.
Então a recomendação aqui é que o QoS seja configurado em cada equipamento em que o fluxo fora trafegar. <br></br>
Primeiro irei realizar a captura dos pacotes de redes em alguns pontos para podermos analisar como estão os pacotes. Para isso, irei utilizar a ferramenta wireshark de código aberto que é um sniffer de pacotes. Então irei posicionar o Wireshark na interface G0/0 do roteador ISP e nesse momento irei realizar um acesso HTTP, TFTP e um PIMG (ICMP) do host 192.168.10.10 . <br></br>

<tr >
     <td> <img src="Imagens/wireshark/01-Sem_QoS_ICMP.png" alt="Image" heigth="600" width="600"></img> </td>
     <td> <img src="Imagens/wireshark/02-Sem_QoS_HTTP.png" alt="Image" heigth="600" width="600"></img> </td>
     <td> <img src="Imagens/wireshark/03-Sem_QoS_TFTP.png" alt="Image" heigth="600" width="600"></img> </td>
</tr>

![Análise](Imagens/wireshark/01-Sem_QoS_ICMP.png) 
![Análise](Imagens/wireshark/02-Sem_QoS_HTTP.png)
![Análise](Imagens/wireshark/03-Sem_QoS_TFTP.png) 


