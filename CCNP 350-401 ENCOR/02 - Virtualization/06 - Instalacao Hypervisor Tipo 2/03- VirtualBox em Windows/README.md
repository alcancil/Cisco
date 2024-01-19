# 01 - VirtualBox em Windows

Agora vou demonstrar como realizar a instalação do VirtualBox no Windows. Ele é da empresa Oracle e pode ser obtido em : https://www.virtualbox.org/wiki/Downloads . Ele é bem parecido com o Vmware Player citado anteriormente. <br><br>

Então vamos analisar novamente como estão as nossas placas de rede no windows. <br></br>

![REDE](Imagens/01-placas_de_rede_vmware.png) <br></br>

Aqui podemos notar que temos 1 placa de rede física e mais duas virtuais, que foram criadas no exemplo anterior onde instalamos o Vmware Player. Então vou copiar o instalador do VirtaulBox do site e guardar em uma pasta no hd do sistema operacional host, o sistema físico. <br></br>

![SOFTWARE](Imagens/02-software.png) <br></br>

Agora é clicar no arquivo executável e seguir as instruções. <br></br>

<table>
     <tr>
         <td width="33%"><img src="Imagens/virtualbox/01.png"></img></td>
         <td width="33%"><img src="Imagens/virtualbox/02.png"></img></td>
    </tr>
    <tr>
        <td width="33%"><img src="Imagens/virtualbox/03.png"></img></td>
        <td width="33%"><img src="Imagens/virtualbox/04.png"></img></td>
    </tr>
    <tr>
        <td width="33%"><img src="Imagens/virtualbox/05.png"></img></td>
        <td width="33%"><img src="Imagens/virtualbox/06.png"></img></td>
    </tr>
</table>

Como podemos ver, a instalação deu uma mensagem de aviso que está faltando Python Core / win32api . Agora o virtualbox possui uma integração com a linguagem de programação python, porém como não temos esse programa instalado, então o hypervisor perde essas funcionalidades. Para resolvermos isso, precisamos instalar o python e logo após a win32api. Então vamos baixar o python em: https://www.python.org/downloads/ e vamos salvar o executável na mesma pasta que baixamos o virtualbox. <br></br> 

Vamos executar o instalador quando começar a instalação, marcar a opção de adicionar o python ao path do sistema operacional. <br></br>

![PYTHON](Imagens/python/01.png) <br></br>

Bom aqui instalamos o python porém ainda não temos a api do python instalado. Vamos abrir o cmd e verificar a instalação do python. <br></br>

![VERSÂO](Imagens/python/02.png) <br></br>

Agora vamos abrir o cmd e executar o seguinte comando: **py -m pip install pywin32**

![API](Imagens/python/03.png) <br></br>

Agora só falta instalarmos o Extension Pack, que são os drivers de aprimoramento do virtualbox. Então vamos ir ao link https://download.virtualbox.org/virtualbox/7.0.14/Oracle_VM_VirtualBox_Extension_Pack-7.0.14.vbox-extpack e salvar o aplicativo na mesma pasta onde salvamos o virtualbox. <br></br>

![EXTENSION](Imagens/virtualbox/07.png) <br></br>

Vamos clicar no arquivo e ao executar será perguntado se desejamos instalar o pacote de extensões no virtualbox. Vamos clicar em sim. <br></br>

![EXTENSION](Imagens/virtualbox/08.png) <br></br>

Então irá abrir uma tela com os termos de utilização do programa. Devemos descer o texto até o final e depois clicar em concordar. <br></br>

![EXTENSION](Imagens/virtualbox/09.png) <br></br>

Pronto, agora terminamos de instalar o virtualbox e suas dependências. <br></br>

Como feito no vmware, já criei uma máquina virtual e vamos analisar as placas de rede. <br></br>

![REDE_VMS](Imagens/virtualbox/10.png) <br></br>

É aqui que podemos escolher como a placa de rede vai funcionar. Então temos as opções: 
> - **01 - Bridge:** aqui ela funciona como uma ponte. Ou marcamos a opção de replicar o endereço de IP da placa física ou, deixamos a placa obter um endereço automaticamente através do servidor DHCP da rede física. Essa opção é utilizada para as vms conseguirem sair para a Internet e conseguir "enxergar" as outras máquinas físicas da rede.
> - **02 - Nat:** esta opção serve para pegar o endereço de IP atribuído não roteável da VM e traduzir para um endereço de rede roteável, como os roteadores fazem com os endereços IPv4 das Lans. Essa opção normalmente é utilizada quando queremos que as Vms saiam para a Internet mas não enxerguem as máquinas físicas da rede real.
> - **03 - Host-only:** está opção serve para isolar a rede virtual da rede física. Então as vms se enxergam porém não conseguem sair para a Internet e nem conseguem conversar com as máquinas físicas da rede real.

Temos mais algumas opções, mas essencialmente são as mesmas.