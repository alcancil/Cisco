# 08 - LIMITE DE CONFIÂNÇA

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

![LIMITE](Imagens/00-cenario.png)

Vamos imaginar o cenário ilustrado. Imagine que o tráfego que entra na rede, está na camada de acesso, onde os hosts estão ligados. Então qual é o comportamento dos switches quanto ao tráfego que entra ? Bom quando um quadro vai atravessar os switches, pode ser confiável ou não. Então, o comportamento padrão dos switches é não confiar nos endpoints e ai, mesmo que o trafego entrante esteja com uma marcação COS e DSCP adequadas, o switch remarca esse tráfego para 0 antes de enviar o frame para dentro do switch. <br></br>
Sendo assim, o tráfego não é priorizado e fica marcado como best effort utilizado a lógica do algorítmo FIFO (First IN First Out), o primeiro que entra é o primeiro que sai. Mas e se desjámos alterar esse comportamento ? Vamos imaginar que no nosso cenário queremos confiar no tráfego do telefone ip, no sw01 e no sw02 e no sw03 não. <br></br>
A primeira coisa a se verificar é se no switch onde temos o telefone ip, se realmente possui uma vlan de voz. Aqui, nesse exemplo eu estarei utilizando a vlan padrão que é a VLAN 1. Então vamos acessar o switch 01 e verificar essa configuração. <br></br>

![LIMITE](Imagens/01-voice_vlan.png)
