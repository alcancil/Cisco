# 09 - Virtual Switching

Agora vamos falar sobre a virtualização de switches. Ela funciona com um software que faz a função de um switch físico. <br></br>
Então em um **Hypervisor do Tipo2**, temos as **vNics (virtual Network Cards)**, que como citado anteriormente tem as funções Host Only, NAT e Bridge. Já no **Hypervisor Tipo01**, bare metal, vamos ter os vSwitches e as vNics. <br></br>

![SERVER](Imagens/server.png) <br></br>

Agora para cada VM poder acessar uma placa de rede física, ela precisa passar por um switch virtual criado pelo Hypervisor. Cada switch virtual precisa ter uma placa de rede física para poder ter acesso á rede. <br></br>
**OBS:** é preciso lembrar também que existem os vSwitches em NFV, mas o foco aqui será o de vSwitches em Hypervisors do **TIPO 01**. <br></br>
Então os vSwitches permitem que as máquinas virtuais "conversem" entre si dentro de um ambiente virtual e também com redes físicas externas por meio de placas de rede físicas (pNics). Porém os vSwitches emulam switches layer 2. Isso quer dizer que eles executam funções de camada 2 e funcionam um pouco diferente de um switch real. Por exemplo, eles não possuem o protocolo Spanning Three que evita loops de camada 2 uma vez que aqui não é mais necessário. <br></br>

## Exemplos de Vswitch

- Cisco Nexus 1000 ve, Cisco Application Virtual Switch (AVS), Open Switch (OVS), vSphere Switch, etc.

Cada fabricante tem sua implementação de vswitch e dependem do que for implementado, ou seja, não são totalmente iguais aos switches físicos. É importante ressaltar também que cada vswitch não se comunica diretamente com outro vswitch. <br></br>

## Tipos de Vswitch

**vNetwork Standard Switch (vSwitch ou VSS)**

Como dito anteriormente, o vswitch é o software que emula um switch físico. Nesse tipo de vswitch padrão, os vswitchs são conectados aos **pot groups** para depois poder conectar as vms. Então, por exemplo, se tivermos 3 port groups, um com 4 portas, outro com 3 portas e mais um com 1 porta, podermoes conectar respectivamente 4, 3 e 1 máquinas virtuais por port-group. Porém dessa maneira, o vswitch só consegue acesso as redes virtuais. Então é preciso atrela as portas de uplink as portas de rede físicas para se ter acesso as redes externas físicas. <br></br>
Exemplos de vswitches vmware. <br></br>

![VSWITCH](Imagens/vswitch.png) <br></br>