# 21 - Gerenciamento de Congestionamento Enfileiramento Atual

As técnicas de algoritmos mais atuais são as recomendadas para as redes mais atuais (e que suportam o MQC) combinando as melhores práticas com suporte aos algoritmos legados. Eles são indicados para tráfego em tempo real, com largura de banda sensível a delays e garantia de delay sem esgotar os outros tipos de tráfego. Os algoritmos recomendados são: <br></br>

| FILAS ATUAIS                               | FILAS ATUAIS                                                                                                                    |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------|
| Class Based Weighted Fair Queuing ( CBWFQ) | CBWFQ habilita a criação de 256 filas, servido 256 tipos de tráfego. Cada fila é associada com uma banda estabelecida na classe |
| Low Latency Queuing (LLQ)                  | LLQ é o CBWFQ combinado com o PQ e foi desenvolvido para atender os requisitos de tráfego em tempo real, como voz e vídeo       |

## CBWFQ COM LLQ

- O CBWFQ combinado com o LLQ cria as filas onde as classes de tráfego são classificadas
- As filas CBWFQ são agendadas com um agendador CBWFQ que garante a largura de banda de cada classe. O LLQ sempre cria uma fila com alta prioridade que é atendida primeiro.
- Durante os períodos de congestionamento as classes LLQ são monitoradas para prevenir que o PQ esgote a banda das classes CBWFQ não prioritárias (como a PQ legada faz)
- Quando o LLQ é configurado, o monitoramento da taxa precisa especificar a quantidade fixa de largura de banda assim como o percentual de largura de banda na interface
- O LLQ permite que duas classes de tráfego diferentes sejam marcadas e então diferentes taxas de monitoramento podem se aplicadas para diferentes tipo s de tráfego de alta prioridade. Por exemplo, tráfego de voz pode ser monitorado durante os tempos de congestionamento para 10 mbps, enquanto que para vídeo seja monitorado para 100 mbps. Isso não é possível quando se utiliza somente uma classe de tráfego e um único policer.

![FLUXOGRAMA](Imagens/fluxograma)