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

![TÚNEL](Imagens/tunel.png) <br></br>