# 21 - Gerenciamento de Congestionamento Enfileiramento Atual

As técnicas de algoritmos mais atuais são as recomendadas para as redes mais atuais (e que suportam o MQC) combinando as melhores práticas com suporte aos algoritmos legados. Eles são indicados para tráfego em tempo real, com largura de banda sensível a delays e garantia de delay sem esgotar os outros tipos de tráfego. Os algoritmos recomendados são: <br></br>

| FILAS ATUAIS                               | FILAS ATUAIS                                                                                                                    |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------|
| Class Based Weighted Fair Queuing ( CBWFQ) | CBWFQ habilita a criação de 256 filas, servido 256 tipos de tráfego. Cada fila é associada com uma banda estabelecida na classe |
| Low Latency Queuing (LLQ)                  | LLQ é o CBWFQ combinado com o PQ e foi desenvolvido para atender os requisitos de tráfego em tempo real, como voz e vídeo       |

