# 01 - Vmware ESXI

Aqui a instalação segue a de um software comum. Devemos iniciar o computador e dar o boot através da mídia de instalação. Feito isso, é só seguir as etapas de instalação. <br></br>

<table>
       <tr>
            <td width="50%"><img src="Imagens/ESXI/01.png"></img></td>
            <td width="50%"><img src="Imagens/ESXI/02.png"></img></td> 
       </tr>
       <tr>
            <td width="50%"><img src="Imagens/ESXI/03.png"></img></td>
            <td width="50%"><img src="Imagens/ESXI/04.png"></img></td> 
       </tr>
       <tr>
            <td width="50%"><img src="Imagens/ESXI/05.png"></img></td>
            <td width="50%"><img src="Imagens/ESXI/06.png"></img></td> 
       </tr>
       <tr>
            <td width="50%"><img src="Imagens/ESXI/07.png"></img></td>
            <td width="50%"><img src="Imagens/ESXI/08.png"></img></td> 
       </tr>
       <tr>
            <td width="50%"><img src="Imagens/ESXI/09.png"></img></td>
            <td width="50%"><img src="Imagens/ESXI/10.png"></img></td> 
       </tr>
</table>

Bom, como podemos ver na última imagem, o ESXI já pegou um endereço de IP que foi fornecido através de um servidor DHCP. Então cabe aqui ressaltar que essa é a parte de rede que vamos utilizar para administrar o Hypervisor. Nesse momento, vou pressionar **F2 (Customize System/View Logs)** para analisarmos as opções. Veja, aqui estou mostrando somente um exemplo da instalação de Hypervisor do tipo 1 e portanto o enfoque será somente na parte das configurações de rede. <br></br>

![SENHA](Imagens/11.png) <br></br>

Como podemos ver, ele funciona como um Sistema Operacional completo, com usuários cadastrados. Então para podermos realizar as devidas alterações / configurações, precisamos fornecer o usuário administrador com sua respectiva senha. Feito isso, vamos navegar entre as diversas opções que aparecem no menu até chegarmos em: **"Configure Management Network" <br></br>

![INTERFACE_DE_GERÊNCIA](Imagens/12.png) <br></br>

Aqui iremos configurar as opções da Interface de Gerência do Hypervisor. Podemos escolher configurar o endereço IPv4 / IPv6 manualmente ou via DHCP, colocar a interface em uma Vlan e configurar a parte do DNS para que os outros hosts possam encontrar o ESXI através do nome FQDN.

![REDE](Imagens/13.png) <br></br>

Para acessarmos o ESXI propriamente dito, agora precisamos ir em outro terminal, abrir o navegador e digitar o endereço de rede fornecido pelo DHCP, como no exemplo. <br></br>
**OBS:** aqui estou deixando na configuração padrão a rede gerência por se tratar de um mero exemplo mas, o recomendado quando se for utilizar um tipo de Hypervisors desses o recomendado é se utilizar um IP Fixo.

![ACESSO](Imagens/14.png) <br></br>

Como não configuramos nada, o navegador irá tentar realizar um acesso via HTTPS seguro, porém como não temos nenhum certificado configurado para esse tipo de acesso, vamos clicar em **aceitar o risco e continuar** para prosseguirmos. <br></br>

![ROOT](Imagens/15.png) <br></br>

Novamente aqui devemos informar o usuário administrador e a senha. Notem que são dois acessos diferentes. Aqui vamos ter o acesso de utilização do Hypervisor. Aqui podemos criar as VMs, discos virtuais e configurar a rede das VMs, que é diferente da rede gerência. <br></br>

![ROOT](Imagens/16.png) <br></br>

Vamos clicar na guia **NETWORKING** para podermos analisar as opções que irão aparecer.

![NETWORKING](Imagens/17.png) <br></br>

Aqui temos as seguintes opções:

> - **Port Groups**
> - **Virtual Switches**
> - **Physical Nics**
> - **VMKernel NICS**
> - **TCP/IP STACKS**
> - **Firewall Rules**

**OBS:** como boa prática a ser seguida, você nunca deve misturar o tráfego de redes lan que utilizam o protocolo Ethernet com o tráfego de redes de Storages que utilizam o protocolo iscsi dentro do mesmo switch. Isso pode gerar problemas e deixar o tráfego muito lento. Então utilize switchs separados para cada tipo de tráfego.

## Port GROUPS

Podemos pensar que um Port Group é como se fosse uma porta virtual com um conjunto específico de configurações aplicadas sobre ela. Eles são responsáveis por conectar as máquinas virtuais aos vSwitches.<br></br>
Para os port groups funcionarem, é necessário que eles tenham portas de uplink, que representam as conexões entre as placas de rede físicas e os vSwitches do host ESXi. Dessa forma, os port groups são associados a uma VLAN específica, e o tráfego flui através das NICs físicas.<br></br>
**OBS:** É possível associar mais de uma placa de rede física a um vSwitch para fornecer redundância de uplink. <br></br>
É possível observar que nas configurações podemos especificar em qual vswitch o port group está associado, configurar a parte de segurança, realizar um nic teaming e até mesmo realizar um traffic shapping. <br></br>

<table>
       <tr>
            <td width="50%"><img src="Imagens/REDE_ESXI/port groups/1.png"></img></td>
            <td width="50%"><img src="Imagens/REDE_ESXI/port groups/2.png"></img></td> 
       </tr>
       <tr>
            <td width="50%"><img src="Imagens/REDE_ESXI/port groups/3.png"></img></td>
            <td width="50%"><img src="Imagens/REDE_ESXI/port groups/4.png"></img></td> 
       </tr>
</table>

## VIRTUAL SWITCHES

<table>
       <tr>
            <td width="50%"><img src="Imagens/REDE_ESXI/Vswitches/1.png"></img></td>
            <td width="50%"><img src="Imagens/REDE_ESXI/Vswitches/2.png"></img></td> 
       </tr>
       <tr>
            <td width="50%"><img src="Imagens/REDE_ESXI/Vswitches/3.png"></img></td>
            <td width="50%"><img src="Imagens/REDE_ESXI/Vswitches/4.png"></img></td> 
       </tr>
</table>
