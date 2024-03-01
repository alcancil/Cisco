# 16 - TÚNEIS GRE (GENERIC ROUTING ENCAPSULATION)

Vamos pensar agora em tempos um pouco distantes onde as empresas com matriz e filial queriam se comunicar. Então cada ponta dessas empresas tinham que serem ligadas através de cabos diretos com links dedicados. <br></br>
Então as empresas solicitavam as operadoras esse tipo de ligação. Isso era caro e difícil de se manter. <br></br>
Percebendo esse cenário, o fabricantes pensaram da seguinte maneira: "Porque ao invés de se passar um cabo direto entre matriz e filial não se desenvolve algo que substitua isso e aproveite o link de Internet uma vez que as duas partes interessadas já possuem o link de Internet ?" <br></br>
Com esse pensamento em mete e com o passar do tempo, os links de Internet foram se popularizando e os custos diminuindo. Com isso, a CISCO desenvolveu os **Túneis GRE que estão descritos na rfc 4213.** <br></br>
Então, um túnel nada mais é a abstração do cabo, ou seja, é como se um "cabo virtual" fosse ligado no roteador da matriz e chegasse no roteador da filial. Com isso os custos caem pois agora não existe mais a necessidade de um cabo direto e os links de Internet são aproveitados. <br></br>
Mas aí é criado um outro problema: **segurança**. Como de início foi pensado só no túnel, não existe nenhum tipo de criptografia e o tráfego passa em modo transparente, ou seja, o tráfego vai acessar a Internet e quem estiver no mesmo meio pode interceptar essa comunicação e conseguir ver o tráfego. A solução para esse tipo de problema é a utilização do protocolo **IPSEC** sobre o túnel, pois ele vai criptografar os dados, e mesmo que o tráfego seja interceptado, a conversa não pode ser vista. <br></br>

## GRE: Generic Routing Encpasulation 

O GRE foi desenvolvido pela CISCO e está descrita na **RFC 4213**. Ele não provê segurança. <br></br>
Os pacotes enviados através do GRE são encapsulados por um novo cabeçalho e colocados no túnel com o endereço de destino final do túnel.<br></br>

![TÚNEL](Imagens/gre.png) <br></br>

Então como podemos observar nas figuras, o pacote pode passar por vários roteadores ao longo do caminho até chegar ao seu destino final. <br></br>
Porém quando utilizamos o GRE, formamos um túnel com início em um roteador terminando em outro, como em uma mtariz e filial. Esse é o nosso **overlay**, que fica sobre o **underlay**. Aos olhos do usuário final, isso é transparente, ou seja, se o usuário executar um **tracert**, será mostrado somente as interfaces dos roteadores que formam o túnel mas por trás disso, o pacote pode estar passando por um caminho complexo. <br></br>
Com isso podemos notar que o GRE adiciona um overhead no cabeçalho IP original e é necessário ficar atento ao tamanho do mtu do pacote agora. Ele encapsula o pacote original e acrescenta dois campos: **IP e GRE**.<br></br>
No destino, os pacotes são descapsulados e continuam seu caminho pelo cabeçalho original. <br></br>

![TÚNEL](Imagens/tunel.png)<br></br>

Se os pacotes forem trafegar pela Internet, é necessário se ter IPs roteáveis nas pontas. O túnel também pode ser formado na Internet. <br></br>

