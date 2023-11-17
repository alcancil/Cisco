# 04 - Problemas

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

No artigo anterior, eu contextualizei um pouco sobre o surgimento das redes e como surgiram os seus problemas. Então quando se fala em aplicar QoS é por conta de uma real necessidade. <br></br>
Quando pacotes trafegam pela Internet, eles utilizam um modelo chamado de Best Effort, ou melhor esforço, ou seja, nenhum tipo de trafego vai receber algum tipo de tratamento ou priorização. Então nos momentode congestionamento de uma rede, esses pacotes vão ficar a mercê da capacidade de processamento dos roteadores e da disponibilidade da largura de banda do link local. Então como visto anteriormente, podem ocorrer diversos problemas tais como latência, jitter, escassez de banda e até mesmo perca de pacotes. <br></br>
Mas o quer dizer essa monte de nomes esquisitos e o que realmente isso afeta dentro de uma rede ? Bom, vou tentar explicar aqui. Então vamos lá. <br></br>

**01. LATÊNCIA** <br></br>

Latência pode-se dizer que é o sinônimo de atraso, pois é o tempo que um pacote leva para sair de um ponto ao outro e é medido em ms. Por exemplo, vamos imaginar que um usuário dentro da rede está jogando online. Então quando ele solicita que um pacote saia da rede e chegue no servidor do jogo, essa é a latencia. Vamos supor que seja de 20 ms<br></br>

**02. JITTER** <br></br>

Jitter é muito parecido com a Latência mas ele é mais importante quando se trata de aplicções em tempo real como voz e vídeo por exemplo. O Jitter é variação do atraso e também é medido em milessegundos. Vamos retomar o exemplo anterior do jogo online onde a latência tinha sido de 20 ms. Agora imagine que um segundo pacote saia da rede com uma latência de 50 Ms<br></br>
Então: **jitter = 50 ms - 20 ms = 30 ms** <br></br>

A recomendação é que o *jitter não ultrapasse os 30 ms* pois com mais de 30 ms  começamos a ter uma degradação na qualidade do sinal. <br></br>

**03. PERCA DE PACOTES** <br></br>

Quando os pacotes atingem um tamanho maior que o seu tamanho máximo de transmissão, ele precisa ser fragmentado e depois enviado fragmento a fragmento através do meio de transmissão. Acontece que o equipamento que recebe esses pacotes possuie uma fila, um buffer, de armazenamento desses pacotes. E ai esse buffer tem um limite. Depois que os pacotes chegam nesse buffer, eles precisam ser ordenados e encaminhados para dentro do equipamento. Se esse buffer atingir seu limite e estiver cheio, isso faz com alguns pacotes sejam perdidos e com isso, o mesmo pacote precisa ser retransmitido até que consiga chegar ao seu destino.

**04. ESCASSEZ DE LARGURA DE BANDA** <br></br>

Largura de banda é a capacidade de transmissão dentro de um meio e é medida em bits po segundo. A largura de banda disponível entre a origem e o destino é *igual a cpacidade do link com menor largura de banda* . Vamos ver um exemplo: <br></br>

![Largura de Banda](Imagens/Largura.png) <br></br>

Nesse caso se a matriz quizesse conversar com o escritório, teríamos uma largura de banda disponível de 1 Mbps. Por mais que o plano de Intrente fosse maior e temos um link de 10 Mbps com a Internet, a largura de banda disponível sempre será a menor no circuito todo. <br></br>

### Problemas <br></br>

Então os principais problemas sentidos seriam fala fora de sincronia em um vídeo, voz metalizada em uma ligação, eco em uma ligação, travamentos de aplicativos, lentidão, pixelização de vídeos, etc. Esses são os sintomas que os usuários na sua maioria irão relatar. É aqui que podemos notar a importância de se aplicar algum mecanismo de QoS. <br></br>

Agora vamos observar o cenário. Aqui eu estou aproveitando o mesmo cenário anterior, do tópico 03 - Auto QoS. Porém entre o switch 01 e o roteador 03 eu adicionei o *NETem*, que é uma aplicação Linux que foi desenvolvida para gerar alguns tipos de tráfego na rede. Aqui foi utilizada a versão para o emulador Gns3 e convertida para o Eve-Ng. Link para download  https://gns3.com/marketplace/appliances/netem . Mais informações sobre a aplicção podem ser obtidas em: https://wiki.linuxfoundation.org/networking/netem <br></br>

![NETem](Imagens/cenario.png) <br></br>

Então vou realizar um simples Ping no Windows do host **10.0.0.10** para o host **172.16.0.10**. Essa é uma ferramenta que utiliza o protocolo ICMP e, inicialmente ele envia um pacto Echo Request para um destino e, se encontrar esse destino recebe um pacote Echo Reply, que é a resposta. A principio, nenhum mecanismo de QoS foi configurado. <br></br>

![PING](Imagens/ping_normal.png) <br></br>

Analisando essa saída, podemos observar que o ping possue algumas colunas que mostram algumas informações que são: <br></br>

01. *Reply from 172.16.0.10* ou seja, aqui ele diz que recebeu uma reposta do host alvo
02. *bytes=32* tamanho do pacote medido em bytes
03. *time=1ms* esse é o tempo em que o pacote demorou para sair do destino e voltar para a origem, ou seja, essa é a **LATÊNCIA**
04. *TTL=127* TTL é a abreviação de Time To Live, ou o tempo de vida. Ou seja, esse é número máximo de saltos ou roteadores que o pacote pode trafegar. Sem esse campo, ele ficaria andando pela rede eternamente. <br></br>

Ao final do resultado do comando, são exibidas algumas estatísticas. É por aqui também que conseguimos medir o desempenho da rede. <br></br>
Agora vou ligar o NETem e simular um atraso na rede, um delay de 50 ms. Aqui cabe ressaltar que essa é uma aplicação muito simples de uso, ou seja só iniciar a máquina virtual e escolher os parâmetros desejados. <br></br> 

<table>
       <tr>
           <th img src = ![NETem](Imagens/netem_01.png) >&nbsp;</th>  <td> &nbsp; ![NETem](Imagens/netem_02.png) </td>
       </tr>  
</table>

<br></br>

