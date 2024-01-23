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

