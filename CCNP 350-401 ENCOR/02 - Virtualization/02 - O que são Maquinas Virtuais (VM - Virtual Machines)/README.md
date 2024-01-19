# 01 - O que são Maquinas Virtuais (VM - Virtual Machines)

Este item faz parte do Bluprint do CCNP ENCORE 350-401 - 2.1.b Virtual machine <br></br>

Atualmente ouvimos muito falar no termo Máquinas Virtuais ou Virtual Machines (VMs) em inglês e, podemos ter a impressão de que isso é um termo novo. Mas esse termo foi inventado na década de 1960 pela empresa IBM. Naquela época não existiam os computadores pessoais (Personal Computers - PCs) do jeito que a gente conhece hoje em dia. Os computadoras eram chamdos de MainFrames e eram enormes. Ocupavam salas e salas. Eles funcionavam com um único arquivo batch (em lotes) onde todas as instruções eram escritas dentro desse arquivo. <br></br>
Na época existia o IBM mainframes System/360 porém como ele funcionava com um único arquivo em lotes, isso gerava um enorme problema. Toda vez que alguém precisava dar uma instrução para o mainframe ele tinha que fazer sozinho e de uma única vez. Não tinha como várias pessoas trabalharem juntos ao mesmo tempo.

<table>
      <tr>
           <td width="50%"><img src="Imagens/MainFrame/01.jpg"></img></td>
           <td width="50%"><img src="Imagens/MainFrame/02.jpg"></img></td>
      </tr>
       <tr>
           <td width="50%"><img src="Imagens/MainFrame/03.jpg"></img></td>
           <td width="50%"><img src="Imagens/MainFrame/04.jpg"></img></td>
      </tr>
</table>

Então com esse problema em mãos foi desenvolvido o sistema de VMs (Virtual MAchines) onde era feita uma abstração do hardware, ou seja agora um programa de controle (CP) emulava o hardware físico em pequenos espaços separados dentro do sistema operacional do MainFraime. Ou seja, o sistema de controle pega uma parte do hardware (Processador, Hd, Memória, etc) e divide através de software em outros hardwares emulando vários comutadores dentre um só MainFraime. Com esse tipo de tecnologia, era possível que uma ou mais pessoas pudessem trabalhar no mesmo hardware ao mesmo tempo. <br></br>

