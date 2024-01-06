# 07 - MAC Address Table e TCAM

Então aqui é importante relembrar que no início surgiram os computadores e suas aplicações. Ai veio a necessidade de se aproveitar melhor os recursos, ou seja, compartilham recursos e aplicações entre os equipamentos. Tudo era feito de forma isolada. <br></br>
Então foi inventado o HUB, que é o pai das redes. <br></br>

![HUB](Imagens/hub.png) <br></br>

E o que era um hub ? O HUB era uma caixa com um circuito interno e na sua frente ficavam as portas ethernet (RJ45 fêmea). Ele não possuía nenhum tipo de software de controle de tráfego, simplesmente recebida algum tráfego em uma das portas e depois repassava o mesmo tráfego nas demais. <br></br>
Mas todo o tráfego ocorria através de cabos de cobre. Esses cabos possuem 4 pares de cabos trançados internamente onde a comunicação era feita por 1 par inicialmente. Ou seja, um cabo do par transmite (tx) e o outro par recebe (rx). Isso era chamado de **half-duplex**.
Mas com isso vieram os primeiros problemas. Primeiro não existia privacidade. Se o computador A quer falar com o B, mas na rede existem mais nós, todo mundo recebia a mesma "conversa". E, como a "conversa" era feita por 1 par de cabos de cobre, quando 1 fala, o outro tinha que ficar quieto escutando.<br></br>
Mas como inicialmente o hub era só uma grande extensão, não tinha como o computador A saber quando o computador B estava transmitindo e vice - versa. Então, quando dois nós resolviam conversar ao mesmo tempo, ocorriam as colisões. Por isto que o Hub é considerado como um único **domínio de colisão** <br></br>.
Mas a colisão pode também ocorrer não somente no mesmo hub, pode ser que existam um ou mais hubs interligados e isso vai aumentar a probabilidade de colisões porém aumenta o tempo de recuperação. <br></rb>
Para resolver esse tipo de problema, foi implementado o algoritmo **CSMA/CD (Carrier Sense / Colision Detection)**. Então esse algoritmo verifica a portadora com múltiplo acesso e identifica a colisão. Ai quem "produziu" a colisão tem que esperar um tempo aleatório para depois poder voltar e enviar. Mas ainda existia o problema de enviar o tráfego para todo mundo. <br></br>
A primeira evolução que veio para o hub foram as **Bridges**. Ele é uma "caixa" com somente 2 portas ethernets, baseada em software, que foi desenvolvido justamente para "quebrar" um **domínio de colisão em dois** e com isso diminuir o número de colisões que ocorrem dentro da rede. <br></br>
