# 20 - WEIGTHED-FAIR QUEIUING (WFQ), ROUND ROBIN (RR) e WEIGTHED ROUND ROBIN (WRR)

## WEIGTHED-FAIR QUEIUING (WFQ)

Divide o tráfego em filas no que é especificado e fornece o peso determinado para cada fila. <br></br>
existem filas reservadas para tráfegos de voz e vídeo, por exemplo que já possuem privacidade mais alta. <br></br>
Ou seja, criam as filas por usuário e depois faz a distribuição "justa" do tráfego. <br></br>

![WFQ](Imagens/wfq.png) <br></br>

## ROUND ROBIN (RR)

Cada fila recebe uma parcela igual da largura de banda. Ele atende os pacotes de forma circular conforme vão chegando; Pode gerar jitter.

![RR](Imagens/rr.png) <br></br>

## WEIGTHED ROUND ROBIN (WRR)

São filas criadas com base em necessidades específicas do usuário / aplicativo. São filas personalizadas. <br></br>

![CQ](Imagens/custom_queuing(cq).png) <br></br>