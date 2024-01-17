# 05 - Instalação Hypervisor Tipo 2

Aqui vou dar o exemplo da instalação de dois hypervisors do Tipo 2 mais comuns do mercado. O Vmware Player e o VirtualBox. Ambos são gratuitos e podem ser obtidos no site dos próprios fabricantes. Antes de qualquer coisa, vamos analisar como está a parte de rede do nosso sistema operacional. Primeiro vamos analisar o microsoft windows<br></br>

![REDE](Imagens/01-placas_de_rede.png) <br></br>

Perceba que aqui só temos uma placa de rede que é a placa física. Então vamos entrar no site: https://customerconnect.vmware.com/en/downloads/details?downloadGroup=WKST-PLAYER-1750&productId=1377&rPId=111473 e vamos clicar na versão para windows. Irei salvar o arquivo na pasta c:\downloads. <br></br>

![DOWNLOADS](Imagens/vmware_player/01.png) <br></br>

Agora, aqui a instalação é como de um programa qualquer. Só vou alterar e deixar selecionado a opção para instalar o driver avançado de teclado. <br></br>

<table>
     <tr>
         <td width="33%"><img src="Imagens/vmware_player/01.png"></img></td>
         <td width="33%"><img src="Imagens/vmware_player/02.png"></img></td>
         <td width="33%"><img src="Imagens/vmware_player/03.png"></img></td>
    </tr>
    <tr>
        <td width="33%"><img src="Imagens/vmware_player/04.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/05.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/06.png"></img></td>
    </tr>
      <tr>
        <td width="33%"><img src="Imagens/vmware_player/07.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/08.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/09.png"></img></td>
    </tr>
</table>

Depois disso é necessário reiniciar o windows. <br></br>
Após reiniciar, podemos notar que ao lado do relógio aparece um ícone. <br></br>

![TOOLS](Imagens/vmware_player/vmware_tools.png) <br></br>

Esse é um conjunto de drivers do próprio hypervisor que permite as Máquinas Virtuais se comunicarem diretamente com o host e terem algumas melhorias como driver de vídeo. Com esse driver instalado é possível copiar algo para a memória do sistema operacional host e de dentro da máquina virtual regatar esse conteúdo com o comando "colar" do windows. <br></br>
Outro detalhe é que ao iniciar o Vmware Player, ele vai exibir uma tela perguntado sobre a licença de uso do aplicativo. Aqui iremos escolher a opção: "for free non-comercial use" <br></br>

![LICENÇA](Imagens/vmware_player/licenca.png) <br></br>

Nesse momento vamos voltar analisar as placas de rede do sistema operacional host. <br></br>
![REDE](Imagens/02-placas_de_rede_vmware.png) <br></br>

Percebam que nesse momento o Vmware criou duas placas de rede novas. São essas as placas de rede vão permitir que as Máquinas Virtuais (VMs) possam interagir com o sistema operacional. Agora, para não ficar repetitivo, criei uma máquina virtual dentro do vmware player e vou analisar direto a parte de configuração das placas de rede. <br></br>

![REDE_VMS](Imagens/vmware_player/placas_de_rede.png) <br></br>

É aqui que podemos escolher como a placa de rede vai funcionar. Então temos as opções: 
> - **01 - Bridge:** aqui ela funciona como uma ponte. Ou marcamos a opção de replicar o endereço de IP da placa física ou, deixamos a placa obter um endereço automaticamente através do servidor DHCP da rede física. Essa opção é utilizada para as vms conseguirem sair para a Internet e conseguir "enxergar" as outras máquinas físicas da rede.
> - **02 - Nat:** esta opção serve para pegar o endereço de IP atribuído não roteável da VM e traduzir para um endereço de rede roteável, como os roteadores fazem com os endereços IPv4 das Lans. Essa opção normalmente é utilizada quando queremos que as Vms saiam para a Internet mas não enxerguem as máquinas físicas da rede real.
> - **03 - Host-only:** está opção serve para isolar a rede virtual da rede física. Então as vms se enxergam porém não conseguem sair para a Internet e nem conseguem conversar com as máquinas físicas da rede real.
> - **04 - Custom:** essa opção serve para definirmos intervalos de endereços IPs.