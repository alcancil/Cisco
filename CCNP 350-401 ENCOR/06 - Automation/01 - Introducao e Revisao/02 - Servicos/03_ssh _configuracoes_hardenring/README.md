# 03 - SSH (Secure Shell) - Configurações e Hardenering

Agora vamos olhar os arquivos de configuração do ssh. Aqui podemos configurar quais usuários são permitidos, qual porta o ssh irá utilizar e etc. Aqui vou dar enfoque a segurança pois como é sabido, o ssh utiliza por padrão a porta 22. Com isso existem diversos tipos de de ataque, então a ideia é diminuir a superfície de ataque. <br> </br>


Mas o que é Hardening (endurecer)? <br></br>

Hardening é o processo de reforçar a segurança de um sistema, reduzindo vulnerabilidades e minimizando superfícies de ataque. No caso do SSH, isso significa configurar o serviço para ser mais seguro, prevenindo acessos não autorizados e protegendo contra ataques como brute force e MITM (Man-in-the-Middle). <br></br>

## 🔹 1. Hardening SSH no Linux
 
Passo a passo para reforçar a segurança do SSH no Linux (Debian, Ubuntu, CentOS, Rocky Linux, etc.) <br></br>

Editar a Configuração do SSH

**sudo nano /etc/ssh/sshd_config**

1. Altere as seguintes configurações:   
   > **Port 2222** - Alterar a porta padrão (evita scanners automatizados). Escolha uma porta entre 1024-65535  
   > **SyslogFacility AUTH** - Define o tipo de log (geralmente AUTH para logs de autenticação).  
   > **LogLevel INFO** - aqui definimos os níveis de log que queremos obter.  
   > **PermitRootLogin no** - Desativa login como root  
   > **PubkeyAuthentication yes** - Impedir autenticação por senha (usar apenas chaves)  
   > **AuthorizedKeysFile .ssh/authorized_keys** - define o caminho e o nome do arquivo das chaves autorizadas  
   > **PasswordAuthentication no** - Impedir autenticação por senha (usar apenas chaves)  
   > **ClientAliveInterval 300** - Define tempo de timeout. A cada 300 segundos (5 minutos), o servidor envia um pacote de keep-alive para verificar se o cliente ainda está ativo       
   > **ClientAliveCountMax 2** - Aqui é definido quantas vezes quantas vezes o servidor envia os pacotes keep-alive sem receber resposta, ou seja duas vezes seguidas. 
   > **AllowUsers usuario1 usuario2** - Permite apenas usuários específicos          
   > **KexAlgorithms curve25519-sha256,ecdh-sha2-nistp521,ecdh-sha2-nistp384** - Restringe o uso de certos algoritmos inseguros  
   > **Ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com** - Restringe o uso de certos algoritmos inseguros  
   > **MACs hmac-sha2-512,hmac-sha2-256** - Restringe o uso de certos algoritmos inseguros  
   > **Protocol 2** - Habilitar apenas versões seguras do protocolo SSH   

  **OBS:** para podermos ter logs do ssh, temos que ter instalado um serviço de logs no sistema. Geralmente o utilizado em linux é o **rsyslog**. Então verificar se ele está instalado e rodando.
  **OBS2:** o caminho dos logs em sistemas Debian / Ubuntu ficam em **/var/log/auth.log**. Já em distribuições baseadas em Red Hat/CentOS os logs ficam em **/var/log/secure**.   
  **OBS3:** Os possíveis níveis de log são:  
  > * **QUIET:** Logs mínimos.  
  > * **FATAL:** Apenas erros fatais.  
  > * **ERROR:** Erros.  
  > * **INFO:** Informações gerais (recomendado).
  > * **VERBOSE:** Mais detalhes.  
  > * **DEBUG:** Logs detalhados (use apenas para depuração).  
  
Deixo aqui um exemplo do arquivo **sshd_config** com as configurações aplicadas. [sshd_config](Arquivos/sshd_config)  

2. Reiniciar o SSH para aplicar as mudanças  
    > **sudo systemctl restart ssh**  
3. Configurar Firewall  
Permita apenas a porta do SSH:  
    > **sudo ufw allow 2222/tcp**  
    > **sudo ufw enable**  

## Chave Públicas x Chaves Privadas

Certo chegamos em um ponto em que já configuramos o daemon ssh e precisamos entender como funcionam as chaves. Agora não iremos mais utilizar usuário e senha pois o acesso através de chaves é mais seguro e auxilia no processo de automação.  
A palavra chave vem de uma analogia a portas que precisam de chaves para fechar e abrir. Esse é um conceito utilizado em criptografia assimétrica. Uma chave nada mais é o resultado de um algoritmo que retorna caracteres como números, letras e bytes por exemplo e fica armazenado dentro de um arquivo.  
As chaves são geradas por algoritmos de criptografia assimétrica, como **RSA, ECDSA, ou Ed25519**. Esses algoritmos usam matemática avançada (como fatoração de números primos ou curvas elípticas) para criar um par de chaves que estão matematicamente relacionadas, mas não podem ser derivadas uma da outra de forma prática.  
Entendido o conceito de chaves, precisamos notar que existem dois tipos de chaves: **Pública e Privada**  
  * **Chave Pública:** Pode ser compartilhada livremente e é usada para criptografar dados ou verificar assinaturas.  
  * **Chave Privada:** Deve ser mantida em segredo e é usada para descriptografar dados ou criar assinaturas.  

<div style="text-align: center;">
  <img src="Imagens/chaves.png" alt="CHAVES">
</div>}  

## 🔹 2. Hardening SSH no Windows

📍 Passo a passo para reforçar a segurança do OpenSSH no Windows 10/11 e Windows Server.
✅ 1. Instalar o OpenSSH (caso não esteja instalado)

Add-WindowsCapability -Online -Name OpenSSH.Server

Inicie o serviço:

Start-Service sshd
Set-Service -Name sshd -StartupType Automatic

✅ 2. Editar Configuração do SSH no Windows

Abra o arquivo:

notepad C:\ProgramData\ssh\sshd_config

Modifique estas linhas:

1️⃣ Alterar a porta padrão  
Port 2222  
2️⃣ Impedir login de administrador via SSH
PermitRootLogin no  
3️⃣ Habilitar apenas chaves SSH  
**PasswordAuthentication no**  
**PubkeyAuthentication yes**  

Salve e reinicie o SSH:  

**Restart-Service sshd**

✅ 3. Configurar Firewall

New-NetFirewallRule -DisplayName "SSH Custom" -Direction Inbound -Protocol TCP -LocalPort 2222 -Action Allow

✅ 4. Auditar tentativas de login (Event Viewer)

Abra o Event Viewer e navegue até:
📍 Applications and Services Logs > Microsoft > Windows > OpenSSH > Operational

Ative o log de auditoria para rastrear tentativas de login suspeitas.
🔹 3. Hardening SSH em Equipamentos Cisco

📍 Passo a passo para reforçar a segurança do SSH em roteadores e switches Cisco.
✅ 1. Habilitar apenas SSH (desativar Telnet)

conf t
 line vty 0 4
 transport input ssh
 exit

✅ 2. Alterar a porta padrão do SSH

ip ssh port 2222 rotary 1
line vty 0 4
 rotary 1
 exit

✅ 3. Definir tempo máximo de inatividade

ip ssh time-out 300

✅ 4. Restringir número de tentativas de login

ip ssh authentication-retries 3

✅ 5. Habilitar apenas SSH versão 2

ip ssh version 2

✅ 6. Criar um usuário com senha segura

username admin privilege 15 secret SenhaForte123

✅ 7. Definir algoritmos seguros

ip ssh server algorithm encryption aes256-ctr
ip ssh server algorithm mac hmac-sha2-256






