# 08 - FIB (Forwarding Information Base) x RIB (Routing Information Base)

Em equipamentos CISCO, existe uma técnica de encaminhamento / switching dos pacotes que ja vem habilitada por padrão, que é o **CEF (CISCO EXPRESS FORWARDING)** <br></br>
Essa técnica permite encaminhar pacotes (em camada 3) através de hardware Asics que diminuem a carga na CPU. Com isso, o processo de roteamento pode deixar a cargo do processador tarefas como criptografia, QoS, etc. <br></br>
Apesar de ser proprietário da CISCO, os outros fabricantes também possuem sua implementação de CEF. <br></br>

![CEF](Imagens/cef.png) <br></br>

