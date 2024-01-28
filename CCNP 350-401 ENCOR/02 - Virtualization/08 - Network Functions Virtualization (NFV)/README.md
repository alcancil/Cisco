# 08 - Network Functions Virtualization (NFV)

Estas são as virtualizações de funções de rede (NFV - NETWORK FUNCTIONS VIRTUALIZATION), ou seja, são estruturas baseadas em normas da ETSI (European Telecomunications Standards Institute). <br></br>

![NFV](Imagens/NFV.png) <br></br>

Na abordagem tradicional nós temos todos os equipamentos (apliences) que fornecem uma função ou mais como os roteadores, switches, load balancer, etc. Mas estes são equipamentos físicos que ficam juntos dentro de um rack. <br></br>
Então resumidamente NFV é transformar essas funções de rede físicas em virtuais dentro de um servidor. Mas não pense que isso é igual a virtualização tradicional. Aqui os servidores são x86 mais "poderosos" onde as funções de rede são executadas como módulos de software em servidores x86. <br></br>
Isso segue um framework desenvolvido pela ETSI e no final temos uma infra-estrutura **NFV** ou **NFVI (Network Functions Virtualization Infrastructure)** e normalmente é executado em um hypervisor como uma vm. Isso permite ter ambientes mais homogeneos e escaláveis. <br></br>
Os VNFs normalmente executam funções de camadas **4 á 7** mas também podem executar as camadas 2 e 3, como em routers e switches. <br></br>
Também podem ser utilizados em nuvem. <br></br>

## Elementos de uma NFVI

- **Virtualized Infrastructure Manager (VIM):** essa é a parte inicial do framework onde acontece a abstração do hardware físico. Então aqui temos os recursos de hardware físico onde é instalado o Hypervisor. Em cima do Hypervisor é que acontece a abstração do hardware físico. Exemplo: rede virtual, storage virtual, Vm, etc.
- **Gerentes de elementos (EMS - Elemente Manager):** esses são os gerentes das funções de rede. Por exemplo, podemos ter um EMS gerenciando um VNF1(Vm1), um VNF2(DNS), um VNF3(Acelerador de Rede), depois um EMS2 gerenciando um VNF2(Firewall), um ENS3 gerenciando um VNF3(VM2) e assim por diante.
- **Operations Support System (OSS) / Bussiness Support System (BSS):** esse é o elemento que fornece as redes para as demais redes menores. É o elemento que está no topo do Framework e que lida com a maior carga do Framework inteiro. Até a parte de cobrança dos serviços é ele quem fornece. Por exemplo, um provedor de serviços fornece a rede para os demais clientes. Então imagine que esse provedor possua milhares de clientes. Ou seja, uma rede fornecendo redes para os demais clientes. É nesse nível que o OSS / BSS trabalha. <br></br>

![OSS/BSS](Imagens/oss_bss.png) <br></br>

## CISCO Enterprise Network Functions Virtualization (ENFV)

Essa é a solução enterprise da Cisco para poder virtualizar nas empresas. São suportados por essa solução:

- Cisco Integrated Services Virtual Router (ISRv)
- Cisco Adaptative Security Virtual Applience (ASAv)
- Cisco Firepower Next-Generation Firewall virtual (NGFWv)
- Viptela vEdge e cEdge para Sd-Wan
- Cisco virtual Wide Area Application Services (vWAAS)
- Cisco Virtual Wirelles Lan controlers (vWLCs)
- ThousandEyes
- Fortinet
- Palo Alto
- Info Vista
- Ctera
- Windows Server
- Linux Server

![DNA_CENTER](Imagens/dna.png) <br></br>

Essa é a plataforma da CISCO que traz uma rede convencional (com várias "caixas", cada uma com uma função) para o "novo mundo" onde existe um servidor x86 ou algum dispositivo semelhante onde dentro vão existir várias máquinas virtuais VNFs. <br></br>

![NOVO](Imagens/velho_novo.png) <br></br>

## Exemplos de equipamentos CISCO

- **Tradicional:** Cisco 4000 series ISR, Cisco Catalyst 9000 series - Com serviços centralizados e serviços físicos conservadores.

<table>
      <tr>
           <td width="50%"><img src="Imagens/Equipamentos/tradicional/4000.png"></img></td>
           <td width="50%"><img src="Imagens/Equipamentos/tradicional/9000.png"></img></td>
      </tr>
      <tr>
           <td align="center">Cisco 4000 ISR</td>
           <td align="center">Cisco Catalyst 9000</td>
      </tr>
</table>

- **Enterprise:** 4000 ISR + UCS Eseries (Possui router físico com serviços virtuais), Enterprise Network Compute System (ECS) e UCS Series CSP series (Roteador virtual e serviços virtuais).

<table>
      <tr>
           <td width="50%"><img src="Imagens/Equipamentos/enterprise nfv/ucs.png"></img></td>
           <td width="50%"><img src="Imagens/Equipamentos/enterprise nfv/5000.png"></img></td>
      </tr>
      <tr>
           <td align="center">4000 series + UCS ESeries</td>
           <td align="center">Cisco 5000 Series Enterprise Network Compute System</td>
      </tr>
</table>

**OBS:** O Cisco Enterprise NFVIS possui uma interface gráfica onde pode-se configurar as opções. É ele que vai fazer a parte de abstração. Também possui um cli.

## Riscos da Virtualização de Funções de rede

- **Os controles de segurança não são eficazes:** a virtualização de componentes de rede aumenta sua vulnerabilidade a novo tipos de ataques em comparação com equipamentos físicos bloqueados em um datacenter.
- **O malware é difícil de isolar e conter:** é mais fácil para o malware viajar entre componentes virtuais que estão todos em execução em uma máquina virtual do que entre componentes de hardware que podem ser isolados ou separados fisicamente
- **O tráfego de rede é menos transparente:** as ferramentas tradicionais de monitoramento de tráfego tem dificuldade em detectar anomalias potencialmente maliciosas no tráfego de rede que viaja de leste a oeste entre máquinas virtuais, portanto o NFV requer soluções de segurança mais refinadas.
- **Camadas complexas exigem múltiplas formas de segurança:** os ambientes de virtualização de função de rede são inerentemente complexas, com múltiplas camadas que são difíceis de proteger com políticas de segurança abrangentes.

## Benefícios

- **Pagamento pelo uso:** os modelos NFV de pagamento conforme o uso podem reduzir custos porque as empresas pagam apenas pelo que precisam, ou o que consomem.
- **Menos dispositivos:** como NFV é executado em máquinas virtuais em vez de máquinas físicas, são necessários menos dispositivos e os custos operacionais são mais baixos.
- **Escalabilidade:** dimensionar a arquitetura de rede com máquinas virtuais é mais rápido e fácil e não requer a compra de mais hardware.

Agora deixo dois links para quem desejar se aprofundar mais sobre o assunto. O primeiro é a apresentação da cisco sobre o que é NFV. O segundo é o guia do NFV que dá uma visão geral e ensina como instalar o Cisco NFV.

https://www.cisco.com/c/en/us/solutions/service-provider/network-functions-virtualization-nfv/index.html <br></br>
https://www.cisco.com/c/en/us/td/docs/routers/nfvis/get_started/nfvis-getting-started-guide.html <br></br>
