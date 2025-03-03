# 01 - Revisão

Para podermos realizar a automação de processos, primeiro precisamos entender como fazer o acesso aos equipamentos de rede e depois, conseguiremos fazer isso de forma automática.
Então vamos fazer uma breve revisão dos principais protocolos de rede para acesso aos equipamentos. <br></br>

No início, quando surgiram as redes, não existia nenhum padrão. Com isso, o crescimento se deu de forma desordenada e cada fabricante desenvolvia os protocolos conforme sua necessidade,
ou seja, as coisas não eram compatíveis entre si. Então isso tornava uma rede "isolada" de outra pois cada rede ficava dependente de um único fabricante sem poder escolher outro. <br></br>

Foi então que em 1984, a ISO (International Organization for Standardization) lançou o modelo de referência OSI (Open Systems Interconnection). Esse é um modelo de referência que visa padronizar e trazer interoperabilidade para que as redes sejam desenvolvidas independente do fabricante. <br></br>

Porém, depois de algum tempo surgiu o padrão TCP/IP que é uma pilha de protocolos. Então, por mais que já existisse o modelo anterior, o mercado adotou e implementou o TCP/IP porém, 
como os equipamentos são referenciados através do modelo OSI, os dois coexistem até hoje.

# MODELO OSI

![OSI](Imagens/osi.png)


**Camada 7 : Aplicação**

    Interface entre o usuário e a rede.
    Proporciona serviços como e-mail, navegação na web, transferência de arquivos.
    Exemplos de protocolos: HTTP, HTTPS, FTP, SMTP, POP3, IMAP, Telnet, SSH, DNS.

**Camada 6 : Apresentação**

    Responsável por tradução, criptografia e compactação de dados.
    Converte formatos de arquivos entre sistemas diferentes.
    Exemplos de formatos e protocolos: SSL/TLS, JPEG, GIF, MP3, MPEG, ASCII, Unicode.

**Camada 5 : Sessão**

    Controla o estabelecimento, manutenção e encerramento de sessões de comunicação entre dispositivos.
    Garante a sincronização e o gerenciamento das conexões.
    Exemplos de protocolos: RPC, NetBIOS, PPTP, SIP.

**Camada 4 : Transporte**

    Fornece comunicação confiável ou não entre dispositivos.
    Controla o fluxo de dados e pode realizar a retransmissão de pacotes perdidos.
    Protocolos principais: TCP (confiável, orientado à conexão) e UDP (rápido, sem conexão).

**Camada 3 : Rede**

    Responsável pelo roteamento e endereçamento dos pacotes de dados entre redes diferentes.
    Define os caminhos para a entrega eficiente dos pacotes.
    Protocolos e tecnologias: IP, ICMP, ARP, RIP, OSPF, BGP.

**Camada 2 : Enlace de Dados**

    Controla o acesso ao meio físico e a detecção/correção de erros na transmissão.
    Organiza os dados em quadros antes da transmissão.
    Dividida em duas subcamadas: LLC (Logical Link Control) e MAC (Media Access Control).
    Exemplos de protocolos e tecnologias: Ethernet, Wi-Fi (802.11), PPP, VLAN (802.1Q), ARP.

**Camada 1 : Física**

    Responsável pela transmissão de bits no meio físico (cabos, ondas de rádio, fibra óptica).
    Define características elétricas e mecânicas da conexão.
    Exemplos de tecnologias: Cabo UTP, Fibra Óptica, Bluetooth, Wi-Fi, RS-232, DSL.

# MODELO TCP/IP

![TCP_IP](Imagens/tcp_ip.png)

<br></br>

**Camada 4 : Aplicação**

    Corresponde às camadas de Aplicação, Apresentação e Sessão do modelo OSI.
    Oferece serviços de rede diretamente para as aplicações do usuário.
    Exemplos de protocolos: HTTP, HTTPS, FTP, SMTP, POP3, IMAP, Telnet, SSH, DNS, SNMP.

**Camada 3 : Transporte**

    Responsável pela comunicação fim a fim entre dispositivos.
    Garante a entrega confiável dos dados ou o envio rápido sem conexão.
    Protocolos principais: TCP (confiável, orientado à conexão) e UDP (rápido, sem conexão).

**Camada 2 : Internet**

    Equivalente à camada de Rede do modelo OSI.
    Define endereçamento, roteamento e empacotamento dos dados para envio entre redes diferentes.
    Protocolos e tecnologias: IP, ICMP, ARP, RIP, OSPF, BGP.

**Camada 1 : Acesso à Rede**

    Combina as camadas de Enlace de Dados e Física do modelo OSI.
    Define como os dados são transmitidos fisicamente pelo meio de comunicação.
    Exemplos de tecnologias: Ethernet, Wi-Fi (802.11), PPP, VLAN (802.1Q), DSL, Fibra Óptica.


Aqui vale notar que algumas camadas dos dois modelos são iguais. Já o modelo TCP/IP tem a camada **APRESENTAÇÂO, camada 4**, que é referente as camadas **APLICAÇÃO, APRESENTAÇÂO e SESSÂO** do modelo
OSI, ou seja, **as camadas 7, 6 e 5**. A **camada 4** do OSI é igual a **camada 3** do modelo TCP/IP. <br></br>
Agora a **camada 3** do OSI é igual a **camada 2** do TCP/IP porém uma é chamada de REDE e a outra de INTERNET. <br></br>
Já a **camada 1** do modelo TCP/IP engloba as camadas **3, 2, 1** do modelo OSI. <br></br>