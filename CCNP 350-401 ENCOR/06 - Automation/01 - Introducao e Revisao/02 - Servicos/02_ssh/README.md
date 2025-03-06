# 02 - SSH (Secure Shell)

## Windows

Para instalar o OpenSSH Server no Windows 11 usando, siga os passos:

*  Clique em iniciar e clique em Configurações.

    ![SSH](Imagens/ssh/Windows/1.png)

* Em seguida, clique em "Recursos opcionais".
    ![SSH](Imagens/ssh/Windows/2.png)

* Adicionar um Recurso Opcional
Role para baixo e clique em "Exibir recursos" (ou "Adicionar um recurso").
    ![SSH](Imagens/ssh/Windows/3.png)

* Na lista de recursos, procure por "OpenSSH Server".
    ![SSH](Imagens/ssh/Windows/4.png)

* Marque a caixa ao lado de "OpenSSH Server" e clique em "Avançar".
    ![SSH](Imagens/ssh/Windows/5.png)

* Aguarde a instalação ser concluída.
    ![SSH](Imagens/ssh/Windows/6.png)

* Iniciar o Serviço OpenSSH Server
Após a instalação, você precisará iniciar o serviço OpenSSH Server manualmente.
Pressione Win + R, digite services.msc e pressione Enter.
No Gerenciador de Serviços, localize o serviço chamado "OpenSSH SSH Server".
Clique com o botão direito sobre ele e selecione "Iniciar".

Para garantir que o serviço inicie automaticamente com o Windows, clique com o botão direito novamente, selecione "Propriedades" e defina o "Tipo de inicialização" como "Automático".
| ![SSH](Imagens/ssh/Windows/7.png) | ![SSH](Imagens/ssh/Windows/8.png)  |
|-----------------------------------|------------------------------------|
| ![SSH](Imagens/ssh/Windows/9.png) | ![SSH](Imagens/ssh/Windows/10.png) |


* Configurar o Firewall para Permitir Conexões SSH

| ![SSH](Imagens/ssh/Windows/fw01.png) | ![SSH](Imagens/ssh/Windows/fw02.png) |
|--------------------------------------|--------------------------------------|
| ![SSH](Imagens/ssh/Windows/fw03.png) | ![SSH](Imagens/ssh/Windows/fw04.png) |
|--------------------------------------|--------------------------------------|
| ![SSH](Imagens/ssh/Windows/fw05.png) | ![SSH](Imagens/ssh/Windows/fw06.png) |
|--------------------------------------|--------------------------------------|
|![SSH](Imagens/ssh/Windows/fw07.png)  | ![SSH](Imagens/ssh/Windows/fw08.png) |
|--------------------------------------|--------------------------------------|
|![SSH](Imagens/ssh/Windows/fw09.png)  | ![SSH](Imagens/ssh/Windows/fw10.png) |


Abra o Firewall do Windows:

Pressione Win + S, digite "Firewall do Windows" e selecione "Firewall do Windows com Segurança Avançada".

No painel esquerdo, clique em "Regras de Entrada".

No painel direito, clique em "Nova Regra...".

Selecione "Porta" e clique em "Avançar".

Escolha "TCP" e insira a porta 22 (porta padrão do SSH). Clique em "Avançar".

Selecione "Permitir a conexão" e clique em "Avançar".

Marque todas as opções de perfil (Domínio, Privado e Público) e clique em "Avançar".

Dê um nome à regra, como "OpenSSH Server", e clique em "Concluir".

6. Verificar a Instalação
Abra o Prompt de Comando ou PowerShell e digite:

bash
Copy
ssh localhost
Se a instalação estiver correta, você será solicitado a inserir suas credenciais de usuário do Windows.

7. (Opcional) Configurar Chaves SSH
Se você quiser usar autenticação por chave SSH, crie ou adicione suas chaves SSH no diretório C:\Users\SeuUsuario\.ssh\.

