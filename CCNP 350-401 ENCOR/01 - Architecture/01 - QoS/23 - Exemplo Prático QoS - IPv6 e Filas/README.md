# 22 - RED X WRED

As técnicas de gerenciamento de congestionamento monitoram as cargas de tráfego para antecipar e evitar o congestionamento descartando pacotes. <br></br>
o mecanismo padrão de descarte de pacotes é o **Tail Drop**
- O Tail Drop trata todos os tráfegos por igual e não diferencia entre as classes de serviço. Quando a fila de buffer de saída está cheia, todos os pacotes que tentam entrar são descartados, independentemente de sua prioridade.
- O Tail Drop deve ser evitado para tráfego **TCP** pois pode causar uma sincronização global de **TCP** o que resulta num significante sub-utilização do link.
- Uma melhor abordagem é a utilização de um mecanismo chamado **Random Early Detection (RED)**
- O RED prove a prevenção de congestionamento através do descarte aleatório de pacotes antes que a fila do buffer fique cheia.
- Descartar pacotes de uma vez, como TAIL DROP, evita a sincronização global de fluxos TCP
- O RED monitora o buffer a fundo e realiza o descarte antecipado de pacotes quando o limite mínimo é ultrapassado.

## WRED - WEIGHTED RED

- É uma melhoria do RED implementada pela CISCO
- A diferença entre o RED e o WRED é que a aleatoriedade de descarte dos pacotes pode ser manipulada através dos pesos nos tráfegos utilizando o IP Precedence (IPP) ou DSCP.
- Os pacotes com os menores valores de IPP, são descartados mais agressivamente do que os de maiores valores de IPP.
- Por exemplo, IPP 3 tem que sofrer um maior descarte do que um IPP 5 ou o DSCP AFx3 deve sofrer um maior descarte do que o AFx2, e o AFx2 de ser mais descartado do que um AFx1
- O WRED pode ser utilizado para configurar os bits **IP EXPLICIT NOTIFICATION (ECN)** para indicar que o congestionamento está ocorrendo durante o trânsito. O ECN é uma extensão do WRED que permite que a sinalização do ECN - ENABLED seja enviada aos endpoints instruindo eles a diminuírem a taxa de transmissão de pacotes.