# 11 - Exemplo Pratico VRF 01

Agora vamos praticar e para isso vou demonstrar em alguns exemplos práticos o funcionamento da tecnologia VRF. <br></br>

![CENÁRIO](Imagens/01.png) <br></br>

No cenário eu estou interligando dois roteadores, simulando a situação de sobrepor endereços IPv4 nas interfaces dos mesmos roteadores. Essa situação também ira acontecer nos hosts. Em cenários normais isso não é possível pois o roteador possui somente uma tabela de roteamento nativa. Então vamos dar uma olhada na tabela de roteamento de R01. <br></br>

![R01](Imagens/01.png) <br></br>

Bom, como não não temos nada configurado, aqui temos somente a tabela de roteamento sem nenhuma rota instalada nela. Então vou atribuir um endereço IP á interface e0/1 do roteador e mostrar a tabela de roteamento após isso. <br></br>

![TABELA](Imagens/02.png) <br></br>

