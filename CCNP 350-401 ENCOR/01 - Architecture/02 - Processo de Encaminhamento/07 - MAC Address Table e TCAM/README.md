# 07 - MAC Address Table e TCAM

Então aqui é importante relembrar que no início surgiram os computadores e suas aplicações. Ai veio a necessidade de se aproveitar melhor os recursos, ou seja, compartilham recursos e aplicações entre os equipamentos. Tudo era feito de forma isolada. <br></br>
Então foi inventado o HUB, que é o pai das redes. <br></br>

![HUB](Imagens/hub.png) <br></br>

E o que era um hub ? O HUB era uma caixa com um circuito interno e na sua frente ficavam as portas ethernet (RJ45 fêmea). Ele não possuía nenhum tipo de software de controle de tráfego, simplesmente recebida algum tráfego em uma das portas e depois repassava o mesmo tráfego nas demais. <br></br>
Mas todo o tráfego ocorria através de cabos de cobre. Esses cabos possuem 4 pares de cabos trançados internamente onde a comunicação era feita por 1 par inicialmente. Ou seja, um cabo do par transmite (tx) e o outro par recebe (rx). Isso era chamado de **half-duples**.
Mas com isso vieram os primeiros problemas. Primeiro não existia privacidade. Se o computador A quer falar com o B, mas na rede existem mais nós, todo mundo recebia a mesma "conversa". E, como a "conversa" era feita por 1 par de cabos de cobre, quando 1 fala, o outro tinha que ficar quieto escutando.<br></br>