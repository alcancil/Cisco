# 04 - Problemas

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

No artigo anterior, eu contextualizei um pouco sobre o surgimento das redes e como surgiram os seus problemas. Então quando se fala em aplicar QoS é por conta de uma real necessidade. <br></br>
Quando pacotes trafegam pela Internet, eles utilizam um modelo chamado de Best Effort, ou melhor esforço, ou seja, nenhum tipo de trafego vai receber algum tipo de tratamento ou priorização. Então nos momentode congestionamento de uma rede, esses pacotes vão ficar a mercê da capacidade de processamento dos roteadores e da disponibilidade da largura de banda do link local. Então como visto anteriormente, podem ocorrer diversos problemas tais como latência, jitter, escassez de banda e até mesmo perca de pacotes. <br></br>
Mas o quer dizer essa monte de nomes esquisitos e o que realmente isso afeta dentro de uma rede ? Bom, vou tentar explicar aqui. Então vamos lá. <br></br>

**01. LATÊNCIA** <br></br>

Latência pode-se dizer que é o sinônimo de atraso, pois é o tempo que um pacote leva para sair de um ponto ao outro e é medido em ms. <br></br>

**02. JITTER** <br></br>

Jitter é muito parecido com a Latência mas ele é mais importante quando se trata de aplicções em tempo real como voz e vídeo por exemplo. O Jitter é variação do atraso e também é medido em milessegundos. <br></br>

**03. PERCA DE PACOTES** <br></br>

Quando os pacotes atingem um tamanho maior que o seu tamanho máximo de transmissão, ele precisa ser fragmentado e depois enviado fragmento a fragmento através do meio de transmissão. Acontece que o equipamento que recebe esses pacotes possuie uma fila, um buffer, de armazenamento desses pacotes. E ai esse buffer tem um limite. Depois que os pacotes chegam nesse buffer, eles precisam ser ordenados e encaminhados para dentro do equipamento. Se esse buffer atingir seu limite e estiver cheio, isso faz com alguns pacotes sejam perdidos e com isso, o mesmo pacote precisa ser retransmitido até que consiga chegar ao seu destino.

**04. ESCASSEZ DE LARGURA DE BANDA** <br></br>

Largura de banda é a capacidade de transmissão dentro de um meio e é medida em bits po segundo. A largura de banda disponível entre a origem e o destino é *igual a cpacidade do link com menor largura de banda* . Vamos ver um exemplo: <br></br>

![Largura de Banda](Imagens/Largura.png) <br></br>

Nesse caso se a matriz quizesse conversar com o escritório, teríamos uma largura de banda disponível de 1 Mbps. Por mais que o plano de Intrente fosse maior e temos um link de 10 Mbps com a Internet, a largura de banda disponível sempre será a menor no circuito todo. <br></br>

### Problemas <br></br>

Então os principais problemas sentidos seriam fala fora de sincronia em um vídeo, voz metalizada em uma ligação, eco numa ligação, travamentos de aplicativos, etc. Esses são os sintomas que os usuários na sua maioria irão relatar. 





















No inicio quando foram criadas as redes, o tráfego de vídeo, voz e dados possuíam um circuito dedicado para cada tipo de tráfego. 

![Redes](Imagens/Sem_QoS.png) <br></br>

Observe o cenário: <br></br>

![Cenário](Imagens/cenario.png) <br></br>
