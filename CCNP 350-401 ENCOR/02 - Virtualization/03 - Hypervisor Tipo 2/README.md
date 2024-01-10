# 03 - HYPERVISOR TIPO 02

Esse é o tipo de hypervisor que é conhecido como **hosted hypervisor**. Ele necessita de um computador com um sistema operacional (SO) completo já instalado e funcionando, ou seja, ele é instalado dentro de um sistema operacional. <br></br>
Ele é o tipo que é utilizado para testes de algumas vms, testes de alguns recursos e etc., mas ele é o menos escalável pois, como ele é instalado dentro de um so completo, ele compartilha recursos do próprio sistema operacional. Isso quer dizer que se alguma tarefa, por exemplo, uma renderização de vídeo, estiver ocupando muito CPU, esse recurso ficará em concorrência com a vm por muitas vezes deixando tudo mais lento. <br></br>

![HYPERVISOR](Imagens/hypervisor.png) <br></br>

