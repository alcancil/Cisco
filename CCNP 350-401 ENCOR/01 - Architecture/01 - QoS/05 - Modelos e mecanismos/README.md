# 05 - Modelos e mecanismos QoS

Este tópico faz parte do ítem **1.5 Interpret wired and wireless QoS configurations** do blueprint do exame. <br></br>

Bom, até aqui eu demonstrei um caso de limitação de banda com o uso de 2 técnicas e expliquei os problemas existentes por falta da aplicação dos mecanismos de QoS. Mas existem 3 modelos de QoS. Vamos analisá-los: <br></br>

<table>
       <tr color="blue">
           <th> MODELO </th> </td>  <th> SIGNIFICADO </th>
       </tr>
       <tr>
           <td> MELHOR ESFORÇO </td> <td> É o modelo padrão utilizado para todos os tipos de tráfegos que não necessitam de algum tipo de tratamento.</td>
       </tr>
       <tr>    
           <td> SERVIÇOS INTEGRADOS (IntServ) </td> <td> é a reserva de banda feita fim-a-fim</td>
        </tr>
        <tr>
           <td> DIFERENCIAÇÃO DE SERVIÇOS (DiffServ) </td> <td> É feito por saltos e a rede identifica as classes que requerem tratamento diferenciaciado </td> 
       </tr>  
</table>

Agora repare na saída. <br></br>

![PING](Imagens/ping_delay.png) <br></br>

Agora podemos perceber que o tempo de resposta aumentou. Agora ele fica em uma média de 102 ms. Então esse é um atraso adicionado no tempo de resposa, ou seja, é o **Delay** <br></br>
Por fim, vou alterar o NETem para termos um delay de 50 ms e uma variação de 20 ms. Ou seja, nosso **jitter** será de 20 ms . <br></br>

<table>
       <tr>
           <td> <img src = "Imagens/netem_03.png"> </img> </td>  <td> <img src = "Imagens/netem_04.png"> </img> </td>
       </tr>  
</table>

![PING](Imagens/ping_normal.png) <br></br>
