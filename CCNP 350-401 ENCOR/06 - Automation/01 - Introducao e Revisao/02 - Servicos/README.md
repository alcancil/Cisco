# 02 - Serviços

Bom, agora que revisamos os modelos OSI e TC/IP vamos estudar os protocolos de acesso aos equipamentos. <br></br>

## Protocolo TELNET (TELECOMMUNICATION NETWORK)

O Telnet é um protocolo da camada de Aplicação (Modelo OSI e TCP/IP) que permite a comunicação remota entre computadores através de uma interface de linha de comando. Ele foi um dos primeiros protocolos utilizados para acesso remoto a sistemas e equipamentos de rede. <br></br>

**Principais Características do Telnet:**

    Acesso remoto: Permite que um usuário controle um computador ou dispositivo de rede remotamente.
    Baseado em texto: Utiliza comandos enviados via terminal.
    Utiliza TCP: Funciona sobre o protocolo TCP na porta 23.
    Sem criptografia: A comunicação ocorre em texto puro, expondo credenciais e comandos a ataques de interceptação (sniffing).
    Baixa segurança: Como não oferece criptografia, é vulnerável a ataques como MITM (Man-in-the-Middle) e captura de senhas.

**Funcionamento do Telnet:**

    O cliente Telnet inicia uma conexão com um servidor na porta 23/TCP.
    Após a conexão, o usuário pode autenticar-se (se necessário) e executar comandos remotamente.
    O servidor responde com a saída dos comandos, permitindo o controle do sistema remoto.

**Desvantagens e Alternativa Segura**

    Vulnerável a ataques: Como transmite dados em texto puro, qualquer pessoa que consiga interceptar o tráfego pode visualizar informações sensíveis.
    Não recomendado para redes públicas: Pode ser facilmente explorado por invasores.
    Alternativa segura: O SSH (Secure Shell) substituiu o Telnet, oferecendo criptografia e autenticação mais seguras.

## Instalação do Telnet

### Windows

| ![WINDOWS](Imagens/windows/01.jpg) | ![Img2](https://via.placeholder.com/50) | ![Img3](https://via.placeholder.com/50) | ![Img4](https://via.placeholder.com/50) |
|---|---|---|---|
| ![Img5](https://via.placeholder.com/50) | ![Img6](https://via.placeholder.com/50) | ![Img7](https://via.placeholder.com/50) | ![Img8](https://via.placeholder.com/50) |
| ![Img9](https://via.placeholder.com/50) | ![Img10](https://via.placeholder.com/50) | ![Img11](https://via.placeholder.com/50) | ![Img12](https://via.placeholder.com/50) |
| ![Img13](https://via.placeholder.com/50) | ![Img14](https://via.placeholder.com/50) | ![Img15](https://via.placeholder.com/50) | ![Img16](https://via.placeholder.com/50) |
