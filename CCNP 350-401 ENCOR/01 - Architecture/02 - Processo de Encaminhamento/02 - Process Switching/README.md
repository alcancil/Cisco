# 02 - Process Switching

Este tópico faz parte do item **Describe hardware and software switching mechanisms such as CEF, CAM, TCAM, FIB, RIB, and adjacency tables** do blueprint do exame. <br></br>

Process Switching, também conhecido como software Switching ou Slow Path é um mecanismo de switching em que a CPU fica responsável pelo switching de pacotes. É o método mais tradicional porém mais lento pois feito através de software. <br></br>
Existem alguns casos onde é necessário se utilizar esse método. Os tipos de pacotes que necessitam do Process Switching são:
- Pacotes originado ou destinados no / para o roteador (utilizando controle de tráfego ou pacotes de roteamento)
- Pacotes que são muito complexos para o hardware tratar (Pacotes IP com as opções IP)
- Pacotes que requerem informações extra que normalmente não é conhecida (Ex. Arp) <br></br>
O software switching é muito mais lento que o switching feito pelo hardware. O processo NET IO foi desenvolvido para lidar com uma pequena porcentagem do tráfego tratado pelo sistema. Os pacotes são sempre tratados pelo hardware quando possível. <br></br>
A tabela de roteamento também conhecida como **Routing Information Base (RIB)**; é gerada a partir das informações dos protocolos de roteamento dinâmicos, das rotas diretamente conectadas e das rotas estáticas. A tabela ARP é formada através de informação do protocolo ARP.