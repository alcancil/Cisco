# Índice

- [Índice](#índice)
  - [05 - Exemplo Prático - PIM Dense Mode](#05---exemplo-prático---pim-dense-mode)
    - [Explicação do Cenário](#explicação-do-cenário)

## 05 - Exemplo Prático - PIM Dense Mode

### Explicação do Cenário

Agora que vimos a teoria é hora de praticar. A primeira coisa que precisa ser dita que o **multicast é um serviço** e, portanto, precisamos aplicar ele em um cenário que já está pronto e funcional.  

![cenário](Imagens/cenario.png)  

Nesse cenário estamos utilizando **seis roteadores**.  

Sim, isso mesmo — os “hosts” são, na verdade, **roteadores disfarçados de hosts**, e por isso não realizaremos muitas configurações neles.  

Nos demais roteadores, que estão interligados entre si, foi configurado apenas o protocolo de roteamento dinâmico **OSPF**, garantindo que todas as redes já possuam **conectividade IP completa** antes de ativarmos o multicast.  

O que precisamos entender aqui é que o **PIM Dense Mode** funciona segundo o princípio **“flood and prune”**.  
Mas o que isso significa?  

Quando o processo de comunicação multicast se inicia, o protocolo PIM envia o tráfego multicast por todos os caminhos possíveis (flood), **até descobrir quais roteadores possuem receptores interessados** naquele grupo multicast.  
Os caminhos que **não possuem hosts interessados** são posteriormente **“podados” (pruned)** da árvore de distribuição, otimizando o fluxo.  

Nesse exemplo, o **Host01 (Server)** será a **fonte** da comunicação multicast, enquanto apenas o **Host03** será o **receptor** interessado nesse tráfego.  
