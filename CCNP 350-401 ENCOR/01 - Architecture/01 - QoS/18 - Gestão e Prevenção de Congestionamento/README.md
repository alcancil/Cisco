# 18 - Gestão e Prevenção de Congestionamento

O gerenciamento de congestionamento envolve a combinação de enfileiramento e agendamento. <br></br>
- **Queuing (também conhecido como buffering)** é o armazenamento temporário dos pacotes em excesso (buffer)
- Queuing é ativado quando uma interface de saída está congestionada e é desativado quando acaba o congestionamento
> - O congestionamento é detectado pelo algoritmo de enfileiramento quando ocorre um enfileiramento na camada de hardware / layer 1 presente nas interfaces físicas, conhecido como **transmit ring (Tx-Ring ou TxQ)** e eles estão cheios 
> - Quando o Tx-Ring esvazia, isso indica que não existem mais congestionamentos e é desativado
- O congestionamento pode ocorrer por uma dessas duas razões:
> - A interface de entrada é mais rápida do que a de saída
> - A interface de saída está recebendo pacotes de múltiplas interfaces de entrada

## TÈCNICAS LEGADAS DE ENFILEIRAMENTO

- Quando o congestionamento está ocorrendo, as filas enchem e os pacotes podem ser reordenados por algum algoritmo de enfileiramento e, então, os pacotes de maior prioridade saem mais rápido que os de baixa prioridade.
- Um algoritmo de agendamento (Scheduling) decide qual será o próximo pacote a ser transmitido. O Scheduling sempre fica ativo, mesmo quando a interface enfrenta congestionamento.
- Existem vários algoritmos de enfileiramento, mas a maioria não é adequado para as redes modernas. Os algoritmos que precedem a arquitetura MQC incluem: <br></br>

|                          LEGACY QUEUING                         |
| :----------------------------- | :----------------------------- | 
| First In First Out (FIFO)      | Weighted Round Robin (Wrr)     |
| Priority Queuing (PQ)          | Round Robin                    |
| Custom Queuing                 | Weigted Fair Queuing (WFQ)     |