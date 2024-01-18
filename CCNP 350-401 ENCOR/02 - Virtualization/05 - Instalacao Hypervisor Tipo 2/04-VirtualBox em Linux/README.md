# 04 - VirtualBox em Linux

Agora vou demonstrar como realizar a instalação do virtualbox no Linux. Aqui eu escolhi a distribuição Debian 11, porém ela pode ser realizada em outras distribuições diferentes. Então fiquem atentos que algum comando ou outro poderá sofrer variações. Existem diversos tutoriais e uma ampla literatura disponível gratuitamente na Internet, e a intenção aqui é somente demonstrar graficamente um exemplo de uma instalação de um Hypervisor do tipo 2. <br><br>

![REDE](Imagens/01-placas_de_rede.png) <br></br>

Como podemos notar atráves do comando ip, agora temos quatro placas de rede físicas no sistema operacional, duas físicas **(eth0 e eth1)** e duas virtuais **(vmnet1 e a vmnet8)** criadas pelo Vmware Player. Mas antes de começarmos de fato a instalação do Hypervisor, precisamos resolver qualquer dependência que o software irá exigir. Então adicionar o repositório dos pacotes do virtualbox :

> - **Editar /etc/apt/sources.list e adicionar os componentes "contrib" e "non-free"**
> - **# Debian Oracle**
> - **deb http://download.virtualbox.org/virtualbox/debian buster contrib**

![DEPENDÊNCIAS](Imagens/02-dependencias.png)<br></br>

Feito isso precisamos baixar as chaves de criptografia dos repositórios. **OBS:** desde 2019 foi removido dos repositórios stable oficiais e só existe nos repositórios Unstable. Para contornar isso, então vamos baixar direto do fabricante, a oracle.  <br></br>

> - **sudo wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O /etc/apt/trusted.gpg.d/virtualbox-key.asc**
> - **sudo wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O /etc/apt/trusted.gpg.d/virtualbox-key-2.asc**
> - **sudo apt update**

![UPDATE](Imagens/03-update.png) <br></br>

Então vamos verificar as versões do VirtualBox disponíveis. <br></br>

> - **apt search virtualbox-**

![VERSÕES](Imagens/04-versoes.png) <br></br>

Na data deste artigo temos duas versões disponíveis do VirtualBox, a 6.1 e a 7.0. Então precisamos instalar o aplicativo de fato e vamos utilizar o gerenciador de pacotes apt. <br></br>

> - **sudo apt install virtualbox-7.0**

Ao final da instalação, podemos ver que o grupo **vboxusers** é criado. então precisamos adicionar nosso usuário a esse grupo.

> - **sudo adduser seuusuario vboxusers**

![USUÁRIOS](Imagens/05-users.png) <br></br>

Depois disso basta instalar o pacote de extensões. Então vamos baixar o pacote de extensões do site da oracle:

> - **sudo wget https://download.virtualbox.org/virtualbox/7.0.14/virtualbox-7.0_7.0.14-161095~Debian~bullseye_amd64.deb**

![WGET](Imagens/06-wget.png) <br></br>

Agora vamos baixar o binário com o comando wget:

>  **wget -c https://softwareupdate.vmware.com/cds/vmw-desktop/player/17.5.0/22583795/linux/core/VMware-Player-17.5.0-22583795.x86_64.bundle.tar**

**OBS:** aqui estou baixando a versão 17.5 Verifique a versão mais recente em: https://softwareupdate.vmware.com/cds/vmw-desktop/player/ 

![DOWNLOAD](Imagens/wget.png) <br></br>

Efetuado o download, precisamos descompactar os binários. <br></br>

> **tar -xvf VMware-Player-17.5.0-22583795.x86_64.bundle.tar**

![TAR](Imagens/tar.png) <br></br>

Depois de descompactado, vamos executar o script de instalação:

> sudo sh VMware-Player*

![SCRIPT](Imagens/script.png)

Agora é só abrir a aplicação e seguir as instruções. <br></br>

<table>
     <tr>
         <td width="33%"><img src="Imagens/vmware_player/01.png"></img></td>
         <td width="33%"><img src="Imagens/vmware_player/02.png"></img></td>
    </tr>
    <tr>
        <td width="33%"><img src="Imagens/vmware_player/03.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/04.png"></img></td>
    </tr>
    <tr>
        <td width="33%"><img src="Imagens/vmware_player/05.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/06.png"></img></td>
    </tr>
    <tr>
        <td width="33%"><img src="Imagens/vmware_player/07.png"></img></td>
        <td width="33%"><img src="Imagens/vmware_player/08.png"></img></td>
    </tr>
</table>

Até aqui a configuração do Vmware Player é muito semelhante a do windows porém, reparem na última tela. Ali tivemos que entrar em preferences e clicar em "download all components now". Isso é feito para baixar todos os drivers para todos os tipos de SO suportados pelo hypervisor. <br></br>

Esse é um conjunto de drivers do próprio hypervisor que permite as Máquinas Virtuais se comunicarem diretamente com o host e terem algumas melhorias como driver de vídeo. Com esse driver instalado é possível copiar algo para a memória do sistema operacional host e de dentro da máquina virtual regatar esse conteúdo com o comando "colar" do windows. <br></br>
Outro detalhe é que ao configurar o Vmware Player, ele vai exibir uma tela perguntado sobre a licença de uso do aplicativo. Aqui iremos escolher a opção: "for free non-comercial use" <br></br>

Nesse momento vamos voltar analisar as placas de rede do sistema operacional host através do comando **ip**. <br></br>

![REDE](Imagens/03-placas_de_rede.png) <br></br>

Percebam que nesse momento o Vmware criou duas placas de rede novas, a **vmnet1 e a vmnet8**. São essas as placas de rede vão permitir que as Máquinas Virtuais (VMs) possam interagir com o sistema operacional. Agora, para não ficar repetitivo, criei uma máquina virtual dentro do vmware player e vou analisar direto a parte de configuração das placas de rede. <br></br>

![REDE_VMS](Imagens/vmware_player/placas_de_rede.png) <br></br>

É aqui que podemos escolher como a placa de rede vai funcionar. Então temos as opções: 
> - **01 - Bridge:** aqui ela funciona como uma ponte. Ou marcamos a opção de replicar o endereço de IP da placa física ou, deixamos a placa obter um endereço automaticamente através do servidor DHCP da rede física. Essa opção é utilizada para as vms conseguirem sair para a Internet e conseguir "enxergar" as outras máquinas físicas da rede.
> - **02 - Nat:** esta opção serve para pegar o endereço de IP atribuído não roteável da VM e traduzir para um endereço de rede roteável, como os roteadores fazem com os endereços IPv4 das Lans. Essa opção normalmente é utilizada quando queremos que as Vms saiam para a Internet mas não enxerguem as máquinas físicas da rede real.
> - **03 - Host-only:** está opção serve para isolar a rede virtual da rede física. Então as vms se enxergam porém não conseguem sair para a Internet e nem conseguem conversar com as máquinas físicas da rede real.
