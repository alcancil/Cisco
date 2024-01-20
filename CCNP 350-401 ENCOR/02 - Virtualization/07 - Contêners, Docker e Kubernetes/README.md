# 07 - Contêners, Docker e Kubernetes

Uma Máquina Virtual é uma emulação de um Sistema Operacional completo de um espaço virtual que comparei como uma "caixa" dentro desse so. <br></br>
Só que nesse conceito temos que ter um sistema operacional completo. Agora imagine que queremos somente "subir" alguns serviços ou aplicações somente. Então precisaríamos ter uma VM para cada serviço / aplicação ? Se analisarmos bem, até um certo tempo atrás era o que existia <br></br>
Com isso em mente foi criado o conceito de contêiner. Então ao invés de instalarmos um Hypervisor, depois criar uma Vm com um SO completo para depois subirmos a aplicação / serviço, agora instalamos um **contêiner engine.** Agora o conceito muda um pouco. Esse contêiner engine é instalado sobre um so e dai ele reserva um espaço com todas as bibliotecas e arquivos necessários para rodar a aplicação /serviço. <br></br>

