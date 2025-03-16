# 03 - SSH (Secure Shell) - Configurações e Hardenering

Agora vamos olhar os arquivos de configuração do ssh. Aqui podemos configurar quais usuários são permitidos, qual porta o ssh irá utilizar e etc. Aqui vou dar enfoque a segurança pois como é sabido, o ssh utiliza por padrão a porta 22. Com isso existem diversos tipos de de ataque, então a ideia é diminuir a superfície de ataque. <br> </br>


Mas o que é Hardening (endurecer)? <br></br>

Hardening é o processo de reforçar a segurança de um sistema, reduzindo vulnerabilidades e minimizando superfícies de ataque. No caso do SSH, isso significa configurar o serviço para ser mais seguro, prevenindo acessos não autorizados e protegendo contra ataques como brute force e MITM (Man-in-the-Middle). <br></br>

## 🔹 1. Hardening SSH no Linux
 
Passo a passo para reforçar a segurança do SSH no Linux (Debian, Ubuntu, CentOS, Rocky Linux, etc.) <br></br>

Editar a Configuração do SSH

**sudo nano /etc/ssh/sshd_config**

Altere as seguintes configurações:

* Desativar login como root  
    > **PermitRootLogin no**  
*  Permitir apenas usuários específicos  
    > **AllowUsers usuario1 usuario2**  
* Alterar a porta padrão (evita scanners automatizados)  
    > **Port 2222   # Escolha uma porta entre 1024-65535**  
* Impedir autenticação por senha (usar apenas chaves)  
    > **PasswordAuthentication no**  
    > **PubkeyAuthentication yes**  
* Habilitar apenas versões seguras do protocolo SSH  
    > **Protocol 2**  
* Definir tempo de timeout para desconectar sessões inativas  
    > **ClientAliveInterval 300**  
    > **ClientAliveCountMax 2**  
* Restringir o uso de certos algoritmos inseguros
    > **KexAlgorithms curve25519-sha256,ecdh-sha2-nistp521,ecdh-sha2-nistp384**  
    > **Ciphers aes256-gcm@openssh.com,aes128-gcm@openssh.com**  
    > **MACs hmac-sha2-512,hmac-sha2-256**  

2. Reiniciar o SSH para aplicar as mudanças  
    > **sudo systemctl restart ssh**  
3. Configurar Firewall  
Permita apenas a porta do SSH:  
    > **sudo ufw allow 2222/tcp**
    > **sudo ufw enable**  
4. Ativar Fail2Ban para proteção contra brute-force  
    > **sudo apt install fail2ban -y**  

    Crie um arquivo de configuração:  
        > **sudo nano /etc/fail2ban/jail.local**

Adicione:

[sshd]
enabled = true
port = 2222
maxretry = 3
bantime = 600

Reinicie o Fail2Ban:

sudo systemctl restart fail2ban

🔹 2. Hardening SSH no Windows

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

# 1️⃣ Alterar a porta padrão
Port 2222

# 2️⃣ Impedir login de administrador via SSH
PermitRootLogin no

# 3️⃣ Habilitar apenas chaves SSH
PasswordAuthentication no
PubkeyAuthentication yes

Salve e reinicie o SSH:

Restart-Service sshd

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






