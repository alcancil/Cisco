# 03 - MÉTODOS DE SWITCHING

Este tópico faz parte do item **Describe hardware and software switching mechanisms such as CEF, CAM, TCAM, FIB, RIB, and adjacency tables** do blueprint do exame. <br></br>

## Process Switching

![PSWITCHING](Imagens/process_switching.png) <br></br>

**OBS:** os pacote entram pela interface, vão para o dataplane, depois são encaminhados ao control plane e ai retornam para o data plane para saírem pela interface de saída. <br></br>

Então quando o quadro chega na cpu, ele precisa ser desmontado, verificar o IP de destino e depois comparar com a tabela de roteamento e ai verificar se tem alguma saída. Ai depois se tiver uma saída, precisa remontar o quadro. Se for ethernet, tem que fazer um ARP, achar o MAC de origem / destino, termina o quadro e após envia ele.

## Fast Switching

![FSWITCHING](Imagens/fast_switching.png) <br></br>