# Cisco

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

Sabe-se que a lurgura de banda é a quantidade de dados que você pode transferir em uma rede em um determinado período de tempo. Já o trougputh, é a taxa em que os dados são transmitidos. Geralmente essa taxa é medida em megabits por segundos (Mbps) ou em Gigabits por segundos (Gbps). Mas esse é um recurso muito importante dentro de uma rede e está ligado diretamente á capcidade dos equipamentos tais como roteadores, switches, etc. Então é importante que esse recurso seja utilizado de uma forma responsável para que esse recurso não se esgote rapidamente. <br></br>

Vamos imaginar o seguinte cenário: <br></br>

 ![ cenário](Imagens/cenario.png) <br></br>

Neste cenário, a rede 192.168.3.0/24 representa a rede de uma pequena empresa uma mesmo uma rede doméstica. A rede 172.16.0.0/24 representa um servidor ou mesmo a Internet. Agora imagine que todos quisem acessar a Internet ao mesmo tempo e que o usuário com o 192.168.3.11 resolvesse ver um video, baixar arquivos, escutar músicas e jogar online tudo ao mesmo tempo. O que aconteceria com o tráfego para os outros usuários ? <br></br>
Bem se nada for feito, esse usuário "guluso" irá acabar com toda a largura de banda disponível para todos. Esse tipo de situação pode gerar diversos problemas que vão desde escassez de largura de banda, a dificuldades em se realizar um telefonema que usa voz sobre ip, instabilidade em jogos online e por ai vai. <br></br>
Pensando nisso, podemos então limitar o uso de banda desse usuário, uma vez que seu ip é conhecido.<br></br>
Primeiro é interessante salientar que existe duas técnicas que fazem parte do recurso QoS (Quality Of Service) : Policing e Shapping. Ambas as técnicas visam modelar o fluxo de dados a partir de uma taxa definida, a CIR (Committed Info Rate), ou seja, define-se uma taxa de transmissão de dados e a técnica faz com que a taxa fique próxima da taxa definida. Observe o gráfico da técnica Policing. <br> </br>

![ cenário](Imagens/policing.png) <br></br>