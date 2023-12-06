# 08 - LIMITE DE CONFIÂNÇA

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

![LIMITE](Imagens/00-cenario.png)

Vamos imaginar o cenário ilustrado. Imagine que o tráfego que entra na rede, está na camada de acesso, onde os hosts estão ligados. Então qual é o comportamento dos switches quanto ao tráfego que entra ? Bom quando um quadro vai atravessar os switches, pode ser confiável ou não. Então, o comportamento padrão dos switches é não confiar nos endpoints e ai, mesmo que o trafego entrante esteja com uma marcação COS e DSCP adequadas, o switch remarca esse tráfego para 0 antes de enviar o frame para dentro do switch. <br></br>
Sendo assim, o tráfego não é priorizado e fica marcado como best effort utilizado a lógica do algorítmo FIFO (First IN First Out), o primeiro que entra é o primeiro que sai. Mas e se desjámos alterar esse comportamento ? Vamos imaginar que no nosso cenário queremos confiar no tráfego do telefone ip, no sw03 e no sw04 e no sw05 não. Ou seja, o limite fica sendo a parte em rosa.<br></br>
A primeira coisa a se verificar é se no switch onde temos o telefone ip, se realmente possui uma vlan de voz. Aqui, nesse exemplo eu estarei utilizando a vlan padrão que é a VLAN 1. Então vamos acessar o switch 01 e verificar essa configuração. <br></br>

![LIMITE](Imagens/01-voice_vlan.png)

Agorva vamos configurar a Vlan de voz na porta f0/10 do switch SW01 para qua porta identifique esse tráfego será o do telefone IP. <br></br>

![LIMITE](Imagens/02-voice_vlan.png)

Uma vez que configuramos a porta f0/10 para aceitar o trafego do telefone IP e colocá-lo em uma vlna de voz, agora pode ativar o QoS em modo global. Para, podemos digitar: **sw03(config)# mls qos** . Com isso estamos ativando o QoS em modo global. Em seguida, vamos exibir como está configurado o QoS na interface F0/10, pois ela está no padrão do momento ativação do QoS em modo global. <br></br>

![LIMITE](Imagens/03-mls_qos.png)

Perceba que ele vem como não confiável. Como queremos que o switch confie em marcações em camada 2, maracção COS, temos que alterar esse comportamento. Então primeiro vamos alterar o padrão para confiar em marcação COS. <br></br>

![LIMITE](Imagens/04-mls_qos_cos.png)

![LIMITE](Imagens/05-mls_qos_cisco_phone.png)

![LIMITE](Imagens/06-mls_qos_voip.png)

![LIMITE](Imagens/07-mls_qos_voip_extend.png)
