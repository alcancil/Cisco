# 15 - Single Rate Two-Color Marker / Policers

Existem diferentes algorítmos de policing, incluindo o Single Rate Two-Color Marker / Policer, Single Rate Three-Color Marker / Policer (SRTCM). O Single Rate Two-Color Marker model é baseado no algorítmo Single Token Bucket Algorithm. Para esse tipo de policer, o tráfego pode estar de acordo com exceder o CIR. O Marking Down ou descarte pode ser aplicado em cada um dos casos. <br></br>

![SINGLE-COLOR](Imagens/Single_rate_two_colors.png) <br></br>

- O tráfego acima da linha pontilhada no lado esquerdo representa o tráfego excedente ao **CIR** e sofre **Mark Down**
- O tráfego acima da linha pontilhada no lado direito representa o tráfego excedente ao **CIR e que foi descartado**

O Single-Rate Three Color Policer é baseado na **RFC 3637.** <br></br>
Esse tipo de policer usa dois token buckets, a aí o tráfego pode ser classificado como em conformidade, excedente ou violando o CIR. As acções de Mark Down ou Descarte podem ser aplicadas em cada um dos 3 estados. <br></br>
O primeiro token bucket opera muito parecido com o sistema Single-Rate Two Color, com pequenas diferenças. <br></br>
- Se existirem tokens sobrando no bucket nos períodos de pouca ou nenhuma atividade, ao invés de descartar o excesso, o algorítmo coloca esses tokens em um segundo bucket para ser utilizado nos picos de tráfego que ultrapassem o CIR. 
- Os token que são armazenados nesse segundo bucket são chamados de **excess burst (Be)** e, o Be é o número máximo de bits que pode exceder o valor de BC.

O tráfegi pode ser classificado em 3 cores ou estados: <br></br>