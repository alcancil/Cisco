# 07 - Contêners, Docker e Kubernetes

<table>
     <tr>
          <td width="30%" align="middle"><img src="Imagens/conatainer_simples.png"></img></td>
          <td width="10%" align="middle"><img src="Imagens/x.png"></img></td>
          <td width="20%" align="middle"><img src="Imagens/docker.png"></img></td>
          <td width="10%" align="middle"><img src="Imagens/x.png"></img></td>
          <td width="20%" align="middle"><img src="Imagens/kubernets.png"></img></td>
     </tr>
<table>

Uma Máquina Virtual é uma emulação de um Sistema Operacional completo de um espaço virtual que comparei como uma "caixa" dentro desse so. <br></br>
Só que nesse conceito temos que ter um sistema operacional completo. Agora imagine que queremos somente "subir" alguns serviços ou aplicações somente. Então precisaríamos ter uma VM para cada serviço / aplicação ? Se analisarmos bem, até um certo tempo atrás era o que existia <br></br>
Com isso em mente foi criado o conceito de contêiner. Então ao invés de instalarmos um Hypervisor, depois criar uma Vm com um SO completo para depois subirmos a aplicação / serviço, agora instalamos um **contêiner engine.** Agora o conceito muda um pouco. Esse contêiner engine é instalado sobre um so e dai ele reserva um espaço com todas as bibliotecas e arquivos necessários para rodar a aplicação /serviço. <br></br>

Com isso, os containers ficam mais leves e podem se medidos em megabytes uma vez que não precisam subir um so completo a cada vez que precisar rodar a aplicação / serviço. O container já aproveita o so que está de pé servindo como host e com isso eles se tronam mais rápidos. <br></br>

![CONTAINER](Imagens/cointainer.png) <br></br>

Existem várias empresas que fornecem o Container Engine porém uma das mais populares é o Docker. Ele fornece uma pçataforma que permite criar, implantar e executar os containers de forma fácil e eficiente. Ele também fornece a opção de realizar snpashots dos mesmos. <br></br>
Então os containers são utilizados para empacotar funções individuais que realizam tarefas especificas, os chamados **micro serviços**. <br></br>

![MICROSERVIÇOS](Imagens/microservicos.png) <br></br>

Então agora fica mais fácil de escalar / aumentar o ambiente de produção. <br></br>
Conforme vão surgindo as necessidades, ao invés de subir uma vm completa é mais fácil subir um container com as aplicações ou serviços necessários. <br></br>
**OBS:** os containers podem estar dentro de uma vm completa ou mesmo de um so guest completo instalado no hardware. <br></br>
Mas conforme vão crescendo o número de containers, a gerência pode ficar complicada. Então, o Docker é indicado para ambientes menores. Já para ambientes maiores foi criado o Kubernets. <br></br>

![ARUITETURA](Imagens/arquitetura_kubernets.png) <br></br>

Agora com o Kubernetes é possível administrar vários Dockers ao mesmo tempo. <br></br>
**OBS:** aqui também existe a parte da rede. Então é preciso se atentar que cada container pode ter um endereço IP. Logo é preciso seguir as boas práticas com um bom plano de endereço IP no uso do Docker e do Kubernet.

Para saber mais, deixo o site oficial do [DOCKER](https://www.docker.com/) e do [KUBERNETES](https://kubernetes.io/pt-br/)

- https://www.docker.com/
- https://kubernetes.io/pt-br/ 