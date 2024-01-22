# 01 - O que são Maquinas Virtuais (VM - Virtual Machines)

Este item faz parte do Bluprint do CCNP ENCORE 350-401 - 2.1.b Virtual machine <br></br>

Atualmente ouvimos muito falar no termo Máquinas Virtuais ou Virtual Machines (VMs) em inglês e, podemos ter a impressão de que isso é um termo novo. Mas esse termo foi inventado na década de 1960 pela empresa IBM. Naquela época não existiam os computadores pessoais (Personal Computers - PCs) do jeito que a gente conhece hoje em dia. Os computadoras eram chamdos de MainFrames e eram enormes. Ocupavam salas e salas. Eles funcionavam com um único arquivo batch (em lotes) onde todas as instruções eram escritas dentro desse arquivo. <br></br>
Na época existia o IBM mainframes System/360 porém como ele funcionava com um único arquivo em lotes, isso gerava um enorme problema. Toda vez que alguém precisava dar uma instrução para o mainframe ele tinha que fazer sozinho e de uma única vez. Não tinha como várias pessoas trabalharem juntos ao mesmo tempo.
Agora deixo algumas imagens ilustrativas do IBM Mainframe System/360

<table>
      <tr>
           <td width="50%"><figure><img src="Imagens/MainFrame/01.jpg"><figcaption>Imagem sem especificação de autoria</figcaption></figure></img></td>
           <td width="50%"><img src="Imagens/MainFrame/02.jpg"><figcaption>Imagem sem especificação de autoria</figcaption></figure></img></td>
      </tr>
       <tr>
           <td width="50%"><img src="Imagens/MainFrame/03.jpg"><figcaption>Imagem sem especificação de autoria</figcaption></figure></img></td>
           <td width="50%"><img src="Imagens/MainFrame/04.jpg"><figcaption>Imagem sem especificação de autoria</figcaption></figure></img></td>
      </tr>
</table>

Então com esse problema em mãos foi desenvolvido o sistema de VMs (Virtual MAchines) onde era feita uma abstração do hardware, ou seja agora um programa de controle (CP) emulava o hardware físico em pequenos espaços separados dentro do sistema operacional do MainFraime. Ou seja, o sistema de controle pega uma parte do hardware (Processador, Hd, Memória, etc) e divide através de software em outros hardwares emulando vários comutadores dentre um só MainFraime. Com esse tipo de tecnologia, era possível que uma ou mais pessoas pudessem trabalhar no mesmo hardware ao mesmo tempo. <br></br>

## A evolução e popularização das VMS.

Como dito, as máquinas virtuais foram inventadas para solucionar um problema que os Mainframes tinham de uma só pessoa poder trabalhar com ele. Imagine, são equipamentos enormes e caros, então tinham que inventar uma maneira de otimizar o seu uso. Mas, a princípio, essa era uma tecnologia que ficou restrita a esse setor. <br></br>
Com o passar dos anos, veio o surgimento dos pcs, ou dos computadores pessoais. Agora as pessoas podiam comprar um computador e ter em casa um equipamento em tamanho menor, mas bem robusto. E foi assim por alguns anos: um computador com um sistema operacional instalado e vários aplicativos rodando ao mesmo tempo. <br></br>
Mas, mas uma vez a indústria percebeu que o uso desses equipamento poderiam ser melhorados e com isso surgiram os servidores. O que são os servidores ? Bom a princípio é todo o computador que consegue fornecer aplicativos ou serviços para outros utilizarem. Imagine que antes você comprava um computador, produzia uma carta ou algum documento e precisava mostrar isso para algum colega. Isso era inviável se a pessoa não caminhasse até esse computador. Ai surgiram as impressoras para contornar esse problema. Mas veja que ao mesmo tempo temos um outro problema. Uma impressora não era um equipamento tão acessível assim, e dessa forma se todos os equipamentos de uma empresa precisassem imprimir vários documentos ao mesmo tempo ? Teríamos que ter uma impressora por computador ? A resposta é não. Teríamos que ter um computador central que fornecia e gerencia o serviço de impressão, ai os restantes eram ligados a esse computador e, no momento que precisavam imprimir, a impressão passava por esse servidor central que gerenciava e fornecia o serviço de impressão. <br></br>
E esse comportamento ficou assim no mercado por vários anos. Mas isso começou a mudar quando as empresas começaram a se questionar sobres os custos de ter que se manter uma estrutura dessas. Vamos para para pensar um pouco. Legal temos um servidor que em tese acabou com o problema de impressão simultânea mas, e quanto aos custos de energia ? Porque vamos pensar novamente, não é sempre que todo mundo vai querer imprimir ao mesmo tempo. E o que isso significa ? Bom isso significa que temos que manter um servidor central, caro, ligado 100% do tempo todos os dias sem poder parar para nada.<br></br>

Com isso, as empresas foram notando que diversos servidores ao redor do mundo poderiam chegar a ter certos períodos em que seus equipamentos não estava nem sequer sendo utilizados, chegando mesmo a ter períodos em que ficavam 70% ou mais ociosos. Olhando para esse contexto, algumas empresas apareçam com a mesma solução que anteriormente era restrita somente aos mainframes, as vms. E o pensamento foi: "Então porque não passamos a utilizar as Máquinas Virtuais agora nos servidores ?". E foi o que começou a ser feito.<br></br>
Então, como surgiram vários fabricantes de Hypervisors, as empresas começaram a dimensionar melhor os equipamentos. Então o pensamento agora é assim: preciso de um serviço ou uma aplicação, então vemos quais são essas necessidades, dimensionamos os requisitos para esses aplicativos / serviços e imaginamos que isso vai ser uma máquina, igual quando dimensionamos um computador para determinado aplicativo. A diferença aqui é que, agora podemos montar um grande servidor um mais capacidade e dividi-lo em várias máquinas virtuais para poder utilizar melhor sua capacidade ao invés de termos que comprar um servidor para cada serviço / aplicação como era feitos tempos atrás. Com isso, a utilização desse grande servidor é otimizada, gasta-se menos energia e espaço.

# Vantagens

- É uma ótima opção para se realizar testes
- Podemos utilizar vários sistemas operacionais sobre o mesmo hardware
- Diminuição de custos com hardware
- Facilidade no gerenciamento, migração e replicação de ambientes 
- Maior disponibilidade uma vez que alguma falha de software irá afetar somente uma VM, a VM que esta executando a aplicação
- Testes de diversos sistemas operacionais sem precisar particionar o hd uma vez que o hd virtual agora é um arquivo
- Segurança. Uma vez que cada ambiente é isolado do outro, se ocorrer uma infecção em uma das vms, ela irá ficar contida dentro dessa vm sem afetar as demais.

# Desvantagens

- Gerenciamento: apesar de existir produtos capazes de gerenciarem os ambientes virtuais, eles precisam ser monitorados, configurados e salvos.
- Desempenho. Uma vez que se instala um software em cima de um sistema operacional, isso gera um concorrência de tarefas e pode comprometer o desempenho do sistema todo dependendo do número de máquinas virtuais criadas.
- Enorme utilização de Memória real já que agora temos que atender os requisitos das máquinas virtuais e das aplicações que irão rodar dentro delas

Deixo um link da própria Cisco com a descrição dela do que são máquinas virtuais. [VIRTUAl_MACHINES](https://www.cisco.com/c/en/us/solutions/computing/what-is-a-virtual-machine.html)<br></br>