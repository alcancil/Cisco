# 02 - SSH (Secure Shell)

Se você preferir instalar o OpenSSH Server no Windows 11 usando o modo gráfico (interface do usuário), siga os passos abaixo:

1. Abrir as Configurações do Windows
Pressione Win + I para abrir as Configurações do Windows.

2. Acessar "Apps"
No menu à esquerda, clique em "Apps".

Em seguida, clique em "Recursos opcionais".

3. Adicionar um Recurso Opcional
Role para baixo e clique em "Ver recursos" (ou "Adicionar um recurso").

Na lista de recursos, procure por "OpenSSH Server".

Marque a caixa ao lado de "OpenSSH Server" e clique em "Avançar".

Aguarde a instalação ser concluída.

4. Iniciar o Serviço OpenSSH Server
Após a instalação, você precisará iniciar o serviço OpenSSH Server manualmente.

Pressione Win + R, digite services.msc e pressione Enter.

No Gerenciador de Serviços, localize o serviço chamado "OpenSSH SSH Server".

Clique com o botão direito sobre ele e selecione "Iniciar".

Para garantir que o serviço inicie automaticamente com o Windows, clique com o botão direito novamente, selecione "Propriedades" e defina o "Tipo de inicialização" como "Automático".

5. Configurar o Firewall para Permitir Conexões SSH
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

