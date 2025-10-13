# Índice

- [Índice](#índice)
  - [05 - Exemplo Prático - PIM Dense Mode](#05---exemplo-prático---pim-dense-mode)
    - [Explicação do Cenário](#explicação-do-cenário)
    - [Testes Preliminares](#testes-preliminares)

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

### Testes Preliminares

Agora vamos acessar o SERVER e vamos garantir que existe comunicação entre todos os hosts.  
**OBS:** nos roteadores eu configurei interfaces de LOOPABCK. Então R01 tem o ip 1.1.1.1 /32, R02 tem o ip 2.2.2.2 /32 e R03 tem o ip 3.3.3.3 /32 .  

![01](Imagens/01.png)

Com isso, podemos ver que todos os hosts se alcançam e se comunicam. Mas o mais importante é observer a a tabela de roteamento para podermos entender um conceito simples.  

![02](Imagens/02.png)  

Essa é a tabela de roteamento em R01. Estamos acostumados a analisar essa tabela para verificarmos se o roteamento dinâmico está funcionando corretamente e não temos nenhum problema. Porém uma coisa que não é muito falada e que pode passar despercebida no primeiro momento é que essa tabela é como se fosse um bando de dados onde é feito o mapeamento da comunicação das redes que agora se dá em **unicast**. Ou seja, um host vai se comunicar diretamente com o outro, ou seja, comunicação de **um para um.**  

No nosso caso queremos ter a comunicação **de um para um grupo**, ou seja, **comunicação multicast**. Então nosso papel aqui é montar a árvore de comuniçação que já foi explicada anteriormente. Essa árvore é como se fosse uma tabela de roteamento só que agora multicast.  

Então a primeira coisa que precisamos verificar é se o **roteamento multicast está ativo** no equipamento.  

> R01#show ip multicast
>  Multicast Routing: disabled
>  Multicast Multipath: disabled
>  Multicast Route limit: No limit
>  Multicast Triggered RPF check: enabled
>  Multicast Fallback group mode: Sparse
>  Multicast DVMRP Interoperability: disabled
>  Number of multicast boundaries configured with filter-autorp option: 0
> R01#
