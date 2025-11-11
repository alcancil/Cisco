# Índice

- [Índice](#índice)
  - [08 - Exemplo Pratico - Pim Sparse Mode com Bootstrap Router IETF](#08---exemplo-pratico---pim-sparse-mode-com-bootstrap-router-ietf)
  - [🧾 Introdução](#-introdução)
  - [🎯 Objetivo do Laboratório](#-objetivo-do-laboratório)
    - [🧠 Explicação do Cenário](#-explicação-do-cenário)
    - [🌐 Do Dense Mode ao Sparse Mode](#-do-dense-mode-ao-sparse-mode)
      - [🧩 1️⃣ O papel do Bootstrap Router (BSR)](#-1️⃣-o-papel-do-bootstrap-router-bsr)
    - [🧭 Resumo dos Papéis no BSR](#-resumo-dos-papéis-no-bsr)
    - [🛰️ O que é o RP (Rendezvous Point)](#️-o-que-é-o-rp-rendezvous-point)
      - [🌳 2️⃣ O comportamento do PIM Sparse Mode](#-2️⃣-o-comportamento-do-pim-sparse-mode)
      - [🔹 3️⃣ O papel do IGMP Join](#-3️⃣-o-papel-do-igmp-join)
      - [🔀 4️⃣ Como o DR encontra o RP correto](#-4️⃣-como-o-dr-encontra-o-rp-correto)
      - [🛰️ 5️⃣ Quando a fonte começa a transmitir](#️-5️⃣-quando-a-fonte-começa-a-transmitir)
  - [🌐 Topologia do Laboratório](#-topologia-do-laboratório)
    - [🔍 Testes Preliminares](#-testes-preliminares)
    - [Onde o PIM deve ser ativado](#onde-o-pim-deve-ser-ativado)
    - [📘 No nosso cenário](#-no-nosso-cenário)
  - [🧩 Como funciona o Bootstrap Router (BSR)](#-como-funciona-o-bootstrap-router-bsr)
    - [1️⃣ Os papéis no BSR](#1️⃣-os-papéis-no-bsr)
    - [2️⃣ Como ocorre a comunicação](#2️⃣-como-ocorre-a-comunicação)
    - [3️⃣ Critérios de eleição](#3️⃣-critérios-de-eleição)
  - [⚙️ Ativando o protocolo PIM Sparse Mode](#️-ativando-o-protocolo-pim-sparse-mode)
    - [🧩 Eleição automática do Designated Router (DR)](#-eleição-automática-do-designated-router-dr)
    - [💬 Entendendo as Mensagens PIM Hello](#-entendendo-as-mensagens-pim-hello)
      - [⚙️ Função prática das mensagens Hello](#️-função-prática-das-mensagens-hello)
      - [🧩 Estrutura simplificada da mensagem Hello](#-estrutura-simplificada-da-mensagem-hello)
      - [🔍 Exemplo de mensagens Hello no log](#-exemplo-de-mensagens-hello-no-log)
    - [⚙️ Configurando o Candidate RP e o Candidate BSR (Bootstrap Router)](#️-configurando-o-candidate-rp-e-o-candidate-bsr-bootstrap-router)
    - [🧩 1️⃣ Escolha dos equipamentos](#-1️⃣-escolha-dos-equipamentos)
    - [🧭 2️⃣ Função das interfaces Loopback](#-2️⃣-função-das-interfaces-loopback)
    - [🧰 3️⃣ Comandos de configuração](#-3️⃣-comandos-de-configuração)
    - [3️⃣ Captura e Observação via Wireshark](#3️⃣-captura-e-observação-via-wireshark)
    - [🧪 Realizando a captura](#-realizando-a-captura)
  - [✅ 4️⃣ Ativando o Receptor (IGMP Join) — R04](#-4️⃣-ativando-o-receptor-igmp-join--r04)
    - [✅ Configuração do IGMP Join em R04](#-configuração-do-igmp-join-em-r04)
  - [✅ 5️⃣ Observando a Formação da Árvore (\*,G)](#-5️⃣-observando-a-formação-da-árvore-g)
  - [✅ 6️⃣ Ativando a Fonte Multicast — R01/Server](#-6️⃣-ativando-a-fonte-multicast--r01server)
  - [✅ 7️⃣ Confirmando a Convergência do Domínio PIM-SM](#-7️⃣-confirmando-a-convergência-do-domínio-pim-sm)
  - [🧠 O papel do DR no processo multicast (com PIM-SM e Bootstrap Router)](#-o-papel-do-dr-no-processo-multicast-com-pim-sm-e-bootstrap-router)
  - [🚀 Quando o Servidor Inicia o Tráfego](#-quando-o-servidor-inicia-o-tráfego)
  - [🌳 Formação da Árvore Multicast — do IGMP Join ao PIM Register](#-formação-da-árvore-multicast--do-igmp-join-ao-pim-register)
    - [🧩 1️⃣ O início de tudo: o IGMP Join](#-1️⃣-o-início-de-tudo-o-igmp-join)
    - [🛰️ 2️⃣ O papel do DR (Designated Router)](#️-2️⃣-o-papel-do-dr-designated-router)
    - [⚙️ 3️⃣ O nascimento da árvore compartilhada (\*,G)](#️-3️⃣-o-nascimento-da-árvore-compartilhada-g)
    - [📡 4️⃣ A fonte começa a transmitir — PIM Register](#-4️⃣-a-fonte-começa-a-transmitir--pim-register)
    - [🔁 5️⃣ RP conecta as pontas e inicia o fluxo](#-5️⃣-rp-conecta-as-pontas-e-inicia-o-fluxo)
    - [⚙️ 6️⃣ A transição para a Árvore de Caminho Mais Curto (SPT)](#️-6️⃣-a-transição-para-a-árvore-de-caminho-mais-curto-spt)
    - [✅ Conclusão](#-conclusão)
  - [🧰 Validação e Troubleshooting do PIM Sparse Mode](#-validação-e-troubleshooting-do-pim-sparse-mode)
    - [1️⃣ Verificar os vizinhos PIM — show ip pim neighbor](#1️⃣-verificar-os-vizinhos-pim--show-ip-pim-neighbor)
    - [2️⃣ Confirmar o RP ativo — show ip pim rp mapping](#2️⃣-confirmar-o-rp-ativo--show-ip-pim-rp-mapping)
    - [3️⃣ Verificar os grupos IGMP — show ip igmp groups](#3️⃣-verificar-os-grupos-igmp--show-ip-igmp-groups)
    - [4️⃣ Validar a tabela de rotas multicast — show ip mroute](#4️⃣-validar-a-tabela-de-rotas-multicast--show-ip-mroute)
    - [5️⃣ Confirmar o RPF — show ip rpf](#5️⃣-confirmar-o-rpf--show-ip-rpf)
    - [6️⃣ Confirmar a recepção de tráfego multicast](#6️⃣-confirmar-a-recepção-de-tráfego-multicast)
    - [🧭 7️⃣ Diagnóstico rápido de problemas comuns](#-7️⃣-diagnóstico-rápido-de-problemas-comuns)
  - [🧾 Resumo Final — Fluxo do PIM Sparse Mode](#-resumo-final--fluxo-do-pim-sparse-mode)
  - [✅ Conclusão](#-conclusão-1)
  - [📘 Tabela de Comandos](#-tabela-de-comandos)
    - [R01 – Mapping Agent (MA)](#r01--mapping-agent-ma)
    - [📗 R02 – Candidate RP (C-RP)](#-r02--candidate-rp-c-rp)
    - [📙 R03 – Roteador de Trânsito (PIM-SM Participant)](#-r03--roteador-de-trânsito-pim-sm-participant)
    - [📒 R04 – Roteador com Receptor Multicast (Host02)](#-r04--roteador-com-receptor-multicast-host02)
    - [📕 R05 – Roteador com Host Não Inscrito (Host03)](#-r05--roteador-com-host-não-inscrito-host03)
    - [🖥️ SERVER – Fonte Multicast (Sender)](#️-server--fonte-multicast-sender)
    - [💻 HOST02 – Receptor Multicast](#-host02--receptor-multicast)
    - [🖥️ HOST03 – Host Não Inscrito](#️-host03--host-não-inscrito)

## 08 - Exemplo Pratico - Pim Sparse Mode com Bootstrap Router IETF  

## 🧾 Introdução

Este laboratório foi desenvolvido como parte do meu estudo para a certificação Cisco **CCNP ENCOR (350-401)**.  
O objetivo é compreender, de forma prática, o funcionamento do protocolo **PIM Sparse Mode (PIM-SM)** e sua aplicação em redes corporativas que exigem **distribuição eficiente e controlada de dados multicast**.  
  
Aqui demonstro o funcionamento do **roteamento multicast em modo PIM Sparse Mode**, simulando um ambiente Cisco onde apenas hosts interessados recebem o fluxo de dados.  
Diferente do PIM Dense Mode, o PIM-SM utiliza **Rendezvous Points (RP)** — pontos centrais de encontro entre fontes e receptores — para construir as árvores multicast de forma otimizada.  
  
Neste laboratório, substituímos o mecanismo **Auto-RP (proprietário Cisco)** pelo **Bootstrap Router (BSR)**, que é o **padrão definido pelo IETF (RFC 5059)** para descoberta e distribuição automática de RPs dentro de um domínio PIM-SM.  
O BSR elimina a dependência de grupos multicast proprietários (224.0.1.39 e 224.0.1.40) e realiza a eleição e divulgação dos RPs de forma totalmente integrada ao próprio protocolo PIM.  
  
💡 Embora o laboratório utilize apenas roteadores Cisco, o conceito e o funcionamento do **BSR são universais e compatíveis com ambientes multivendor**, já que seguem o padrão aberto do IETF.  
Isso torna o aprendizado aplicável a qualquer fabricante que implemente o **PIM-SM com suporte ao BSR**, como Juniper, Arista, Huawei, Nokia, entre outros.  
  
[IETF (RFC 5059)](https://datatracker.ietf.org/doc/html/rfc5059)  
  
## 🎯 Objetivo do Laboratório

O objetivo deste laboratório é compreender o funcionamento do **PIM Sparse Mode (PIM-SM)** e a formação das árvores multicast — a **Shared Tree** (baseada no RP) e a **Shortest Path Tree (SPT)** — utilizando o mecanismo **Bootstrap Router (BSR)** para descoberta automática do RP.  

Durante os testes, iremos observar:

- Como o domínio PIM realiza a **eleição do BSR** e dos **Candidate RPs**;
- Como as mensagens **Bootstrap** e **Candidate-RP-Advertisement** são trocadas;
- A **formação da árvore multicast** e a **validação do RPF (Reverse Path Forwarding)**;
- E como o PIM-SM opera sobre uma infraestrutura unicast previamente estabelecida com OSPF.

Assim, este laboratório demonstra na prática o funcionamento completo do PIM-SM em conformidade com o padrão **IETF**, destacando o papel do BSR na automação, interoperabilidade e escalabilidade de redes multicast.

### 🧠 Explicação do Cenário

Como mencionado anteriormente, nosso cenário já possui **roteamento unicast totalmente funcional** (via OSPF), permitindo que o foco agora seja o **tráfego multicast**.  

![cenário](Imagens/cenario.png)  

Nesse laboratório, utilizamos **oito roteadores**, sendo **três deles disfarçados de hosts** apenas para representar as fontes (senders) e receptores (receivers) multicast.  
Esses roteadores “host” não executam roteamento dinâmico — apenas participam dos grupos multicast por meio do IGMP.  

Os demais roteadores estão interligados e executam o **OSPF**, garantindo a convergência e conectividade IP entre todas as redes antes de habilitarmos o PIM.

---

### 🌐 Do Dense Mode ao Sparse Mode

Diferente do **PIM Dense Mode**, que utiliza o método *flood and prune* (inundação inicial e podas posteriores), o **PIM Sparse Mode (PIM-SM)** opera de forma seletiva:  
apenas interfaces com receptores interessados participam da árvore multicast.  

Para que isso funcione, o PIM-SM precisa de um **Rendezvous Point (RP)** — o ponto de encontro entre fontes e receptores multicast.  
É ele quem coordena a formação inicial da árvore compartilhada (*,G), permitindo que os fluxos sejam distribuídos de forma controlada e eficiente.

---

#### 🧩 1️⃣ O papel do Bootstrap Router (BSR)

Neste cenário, estamos utilizando o **Bootstrap Router (BSR)**, que é o **padrão IETF** para descoberta e distribuição automática de RPs em um domínio PIM-SM.  
O BSR substitui mecanismos proprietários como o **Auto-RP** da Cisco.  

👉 **Diferente do Auto-RP**, o BSR **não usa os grupos 224.0.1.39 ou 224.0.1.40**.  
Toda a comunicação entre os roteadores PIM (Candidate-RP, BSR e demais roteadores) ocorre por **mensagens PIM internas**, encapsuladas diretamente no protocolo, sem uso de grupos multicast adicionais.  

Nos equipamentos Cisco, esses grupos podem até aparecer na tabela de roteamento multicast — mas apenas por **compatibilidade com o Auto-RP**, sem função prática neste laboratório.

---

### 🧭 Resumo dos Papéis no BSR

| Função                     | Responsabilidade                                                                                | Comunicação                                           |
|----------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Candidate RP (C-RP)**    | Roteadores que se oferecem para atuar como RP, anunciando quais grupos multicast podem atender. | Enviam mensagens PIM *Candidate-RP-Advertisement (C-RP-Adv)* para o BSR. |
| **Bootstrap Router (BSR)** | Responsável por receber os anúncios dos C-RPs, eleger o(s) RP(s) e distribuir o mapeamento de grupos para todo o domínio PIM. | Envia mensagens *Bootstrap* (PIM Type 13) a todos os roteadores. |
| **Demais roteadores PIM**  | Escutam as mensagens Bootstrap e aprendem automaticamente quem é o RP de cada grupo multicast.   | Atualizam suas tabelas PIM dinamicamente.           |

Após a eleição, o **BSR ativo** envia periodicamente mensagens do tipo **Bootstrap** para todo o domínio, informando quais RPs estão disponíveis e quais grupos eles atendem.  
Com isso, os roteadores aprendem automaticamente o mapeamento (*Group → RP*) sem intervenção manual.  

---

### 🛰️ O que é o RP (Rendezvous Point)

- O **Rendezvous Point (RP)** é o ponto central do domínio PIM-SM.  
- Ele conecta as duas pontas do fluxo multicast:
  - **Fontes (senders)** que enviam tráfego;
  - **Receptores (hosts)** que expressam interesse (via IGMP Join).  
- O RP recebe registros das fontes (mensagens *PIM Register*) e *joins* dos receptores, formando inicialmente a **árvore compartilhada (*,G)**.  
- Depois, os roteadores podem otimizar o caminho migrando para a **árvore por fonte (S,G)** — a *Shortest Path Tree (SPT)*.  
  
👉 Em resumo, o RP atua como um ponto de encontro lógico — fundamental para o Sparse Mode, já que nesse modo o tráfego multicast **não é floodado automaticamente**.  

---

#### 🌳 2️⃣ O comportamento do PIM Sparse Mode
  
O **PIM Sparse Mode** trabalha sob o princípio da economia: ele **não envia tráfego multicast até que haja um receptor interessado**.  
Isso o torna ideal para redes grandes ou ambientes corporativos, onde o consumo de banda precisa ser controlado.  
  
Em vez de inundar o domínio com tráfego (como ocorre no Dense Mode), o PIM-SM constrói **árvores de distribuição seletivas** — chamadas **Shared Trees** — baseadas no RP.  
Essas árvores crescem sob demanda, acompanhando os roteadores onde os receptores estão conectados.  
  
---
  
#### 🔹 3️⃣ O papel do IGMP Join
  
Os receptores, representados aqui pelos hosts multicast, sinalizam interesse em participar de um grupo através do **IGMP (Internet Group Management Protocol)**.  
O host envia uma mensagem **IGMP Membership Report (Join)** ao roteador local, conhecido como **Designated Router (DR)**.  
  
O DR, ao receber esse pedido, entende que há um receptor desejando participar do grupo — por exemplo, **239.1.1.1** — e aciona o processo PIM para buscar o tráfego correspondente.  
  
---
  
#### 🔀 4️⃣ Como o DR encontra o RP correto  
  
O Designated Router precisa descobrir **quem é o RP responsável** pelo grupo solicitado.  
Essa informação pode ser aprendida de três formas:  

- Por configuração estática (`ip pim rp-address`);  
- Por mecanismos proprietários como o **Auto-RP**;  
- Ou, como neste laboratório, por meio do **Bootstrap Router (BSR)**.
  
Com base nesse conhecimento, o DR envia um **PIM Join** em direção ao RP — **seguindo a rota unicast normal**, sem flood.  
Cada roteador no caminho cria uma entrada **(*,G)** na tabela multicast, registrando que existe interesse ativo naquele grupo.  
  
Dessa forma, o domínio PIM constrói gradualmente uma árvore lógica (*,G) que conecta todos os receptores ao RP, aguardando o surgimento de uma fonte.  
  
---
  
#### 🛰️ 5️⃣ Quando a fonte começa a transmitir  
  
Assim que a fonte (por exemplo, o servidor 192.168.10.1) inicia o envio de pacotes multicast para o grupo 239.1.1.1, o roteador mais próximo dela — chamado **Source DR** — envia uma **mensagem PIM Register** diretamente ao RP.  
Essa mensagem pode conter o tráfego encapsulado ou apenas um aviso de que há uma nova fonte ativa.  
  
O RP, ao receber esse registro, associa a fonte ao grupo multicast e conecta as duas pontas:  

- Fontes → RP → Receptores.  

O fluxo de tráfego multicast passa então a percorrer a **árvore compartilhada (*,G)**.  
Com o tempo, os roteadores próximos aos receptores podem optar por **migrar para a Shortest Path Tree (SPT)**, formando um caminho direto até a fonte — eliminando a necessidade do RP no encaminhamento de dados.  
  
---
  
👉 **Resumo:**  
O **Bootstrap Router (BSR)** fornece um método padronizado, automático e **compatível com qualquer fabricante** para distribuição de RPs em domínios PIM-SM.  
Ele garante que todos os roteadores conheçam o RP correto para cada grupo, permitindo a construção dinâmica das árvores multicast com eficiência, escalabilidade e interoperabilidade.  

## 🌐 Topologia do Laboratório

A topologia deste laboratório é composta por **cinco roteadores principais (R01 a R05)** e **três hosts simulados (Server, Host02 e Host03)**.  
Os hosts são roteadores Cisco configurados de forma simplificada, apenas com IP e participação em grupos multicast via IGMP, simulando o comportamento de dispositivos finais.  
  
O protocolo **OSPF** garante a conectividade unicast entre todos os roteadores, enquanto o **PIM Sparse Mode (PIM-SM)** é utilizado para o roteamento multicast.  
Diferente dos exemplos anteriores, aqui implementamos o **Bootstrap Router (BSR)** como mecanismo padrão IETF de descoberta automática de RPs, substituindo o antigo Auto-RP da Cisco.  
  
Neste cenário, teremos dois roteadores candidatos a RP (**Candidate RPs**) e um roteador candidato a coordenar o processo (**Candidate BSR**).  
Durante o laboratório, será possível observar a **eleição automática do RP ativo** e simular **falha em um deles** para confirmar a **assunção automática do RP de backup**.  
  
---

**🔧 Endereçamento e Funções**  

| **Dispositivo** | **Interface** | **Endereço IP / Máscara Rede** | **Conexão / Função**                          |
|-----------------|---------------|--------------------------------|-----------------------------------------------|
| **R01**         | Loopback0     | 1.1.1.1 /32                    | Identificação / Router-ID OSPF                |
|                 | Fa0/0         | 192.168.10.254 /24             | LAN do Server — Gateway multicast             |
|                 | Fa0/1         | 10.0.0.1 /30                   | Link com R02 — PIM + OSPF                     |
|                 | Fa1/0         | 10.0.0.18 /30                  | Link com R05 — PIM + OSPF                     |
| **R02**         | Loopback0     | 2.2.2.2 /32                    | Identificação / Router-ID OSPF                |
|                 | Fa0/0         | 10.0.0.2 /30                   | Link com R01 — PIM + OSPF                     |
|                 | Fa1/0         | 10.0.0.5 /30                   | Link com R03 — PIM + OSPF                     |
| **R03**         | Loopback0     | 3.3.3.3 /32                    | Candidate RP — Identificação / Router-ID OSPF |
|                 | Fa0/0         | 10.0.0.6 /30                   | Link com R02 — PIM + OSPF                     |
|                 | Fa1/0         | 10.0.0.9 /30                   | Link com R04 — PIM + OSPF                     |
| **R04**         | Loopback0     | 4.4.4.4 /32                    | Identificação / Router-ID OSPF                |
|                 | Fa0/0         | 10.0.0.10 /30                  | Link com R03 — PIM + OSPF                     |
|                 | Fa1/0         | 10.0.0.13 /30                  | Link com R05 — PIM + OSPF                     |
|                 | Fa1/1         | 192.168.20.254 /24             | LAN do Host02 — Gateway multicast             |
| **R05**         | Loopback0     | 5.5.5.5 /32                    | Identificação / Router-ID OSPF                |
|                 | Fa0/0         | 10.0.0.14 /30                  | Link com R04 — PIM + OSPF                     |
|                 | Fa1/0         | 10.0.0.17 /30                  | Link com R01 — PIM + OSPF                     |
|                 | Fa0/1         | 192.168.30.254 /24             | LAN do Host03 — Gateway multicast             |
| **Server**      | Fa0/0         | 192.168.10.1 /24               | Fonte multicast (sender)                      |
| **Host02**      | Fa0/0         | 192.168.20.1 /24               | Receptor multicast (join-group 239.1.1.1)     |
| **Host03**      | Fa0/0         | 192.168.30.1 /24               | Host sem participação (sem join IGMP)         |

---

**🧭 Resumo da Lógica**  

- O **Server (192.168.10.1)** transmite tráfego multicast para o grupo **239.1.1.1**.  
- Apenas o **Host02 (192.168.20.1)** realiza **IGMP Join**, pedindo para receber o grupo multicast.  
- O **Host03 (192.168.30.1)** não participa, representando uma rede sem receptores.  
- O **PIM-SM** é habilitado em todos os roteadores, e o **R01** será configurado como **Candidate BSR**, enquanto o **R02** e o **R03** atuarão como **Candidate RPs**.  
- O domínio PIM irá eleger automaticamente um RP ativo com base nas mensagens Bootstrap enviadas pelo BSR.  
- Após a eleição, simularemos uma **falha no RP ativo** para observar a **eleição e promoção automática do RP de backup**.  
- O **RPF (Reverse Path Forwarding)** garantirá que o caminho de retorno até a fonte multicast siga o melhor trajeto OSPF.
  
Assim, poderemos observar não apenas o funcionamento da descoberta automática de RPs via BSR, mas também o comportamento dinâmico da **tolerância a falhas (failover)** entre múltiplos RPs.  

---

### 🔍 Testes Preliminares

Antes de ativar o multicast, é importante confirmar a **conectividade unicast** entre todos os dispositivos.  
  
Cada roteador possui uma **interface de Loopback** usada como **Router-ID** no OSPF:  

- R01 → 1.1.1.1/32  
- R02 → 2.2.2.2/32  
- R03 → 3.3.3.3/32  
- R04 → 4.4.4.4/32  
- R05 → 5.5.5.5/32  

Após o OSPF estar operacional, verifique a conectividade com **ping entre todas as loopbacks**.

![01](Imagens/01.png)

Se todos os roteadores se alcançam, a infraestrutura unicast está pronta.  
Lembre-se: o **PIM-SM** depende de uma **base unicast funcional** para realizar o **RPF check**.

---

Agora podemos ativar o **roteamento multicast** globalmente:

```ios
R01(config)#ip multicast-routing
```

Confirme que o recurso foi habilitado:  

```ios
R01#show ip multicast
  Multicast Routing: enabled
  Multicast Multipath: disabled
  Multicast Route limit: No limit
  Multicast Triggered RPF check: enabled
  Multicast Fallback group mode: Sparse
  Multicast DVMRP Interoperability: disabled
```

Com o roteamento multicast ativo, o próximo passo é habilitar o protocolo PIM nas interfaces participantes (LANs e links entre roteadores).  
Repita esse processo de R01 a R05, garantindo que todas as interfaces de roteamento participem do domínio PIM-SM.  

### Onde o PIM deve ser ativado

No modo **Sparse Mode (PIM-SM)**, o tráfego multicast não é disseminado automaticamente.  
Ele só é encaminhado por interfaces que **participam ativamente do domínio multicast**, seja porque há **hosts interessados (IGMP Join)** ou porque é necessário **alcançar o Rendezvous Point (RP)**.  
  
👉 Por isso, o PIM deve ser ativado em **todas as interfaces relevantes** da topologia, ou seja:  

- **Entre roteadores PIM vizinhos**, para formar adjacências e trocar mensagens PIM Join/Prune;  
- **Em interfaces conectadas a fontes (senders)** e receptores (receivers) multicast;  
- **Em interfaces de Loopback**, quando utilizadas como endereço de RP ou de Candidate BSR.

---

✅ **Resumo prático para ativação do PIM-SM**

| Situação                           | PIM deve ser ativado? | Motivo                                                                |
|------------------------------------|-----------------------|-----------------------------------------------------------------------|
| Interface entre roteadores         | ✅ Sim               | Necessário para formar vizinhanças PIM e trocar mensagens Join/Prune   |
| Interface com host receptor (IGMP) | ✅ Sim               | Permite ao roteador DR receber IGMP Reports e criar a árvore multicast |
| Interface com fonte multicast      | ✅ Sim               | O DR da fonte envia PIM Register ao RP                                 |
| Loopback usada como RP ou BSR      | ✅ Sim               | O endereço de Loopback precisa participar do domínio PIM               |
| Loopback apenas como Router-ID     | ⚙️ Opcional          | Pode ser omitido se não for usada no processo PIM                      |

---

🌀 **Observação sobre as Loopbacks**  

No PIM Sparse Mode, a **Loopback** pode representar funções lógicas importantes:  

- Se for usada como **endereço do RP** ou **Candidate BSR**, o PIM **deve ser ativado** nela.  
- Se for apenas o **Router-ID do OSPF**, a ativação do PIM é opcional.  

💡 Em ambientes de laboratório — como este — é prática comum **ativar o PIM em todas as interfaces loopback** para simplificar a topologia e garantir que elas participem do domínio multicast.  

---

### 📘 No nosso cenário

Vamos habilitar o **PIM Sparse Mode** em todas as interfaces de roteadores que participam do domínio multicast, incluindo:  

- Todas as interfaces ponto a ponto entre roteadores (R01–R02, R02–R03, R03–R04, R04–R05, R05–R01);  
- As interfaces conectadas às LANs dos hosts (Server, Host02 e Host03);  
- As interfaces de Loopback, tanto para fins de identificação OSPF quanto para uso do **BSR e dos Candidate RPs**.  

Antes de iniciar a configuração, é importante compreender como ocorre o **processo de eleição do RP** no mecanismo **Bootstrap Router (BSR)**, que substitui o Auto-RP proprietário da Cisco.

---

## 🧩 Como funciona o Bootstrap Router (BSR)

O **Bootstrap Router (BSR)** é o método **padrão IETF (RFC 5059)** utilizado pelo **PIM Sparse Mode (PIM-SM)** para automatizar a **descoberta e a distribuição de RPs** dentro de um domínio multicast.  
Diferente do Auto-RP, o BSR não utiliza grupos multicast reservados (como 224.0.1.39 e 224.0.1.40).  
Toda a comunicação ocorre por meio de mensagens **Bootstrap** e **Candidate RP Advertisement (C-RP Adv)** encapsuladas no próprio PIM.  
  
---
  
### 1️⃣ Os papéis no BSR

| Função            | Sigla     | Responsabilidade                                                                                              |
|-------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| **Candidate BSR** | **C-BSR** | Roteador que se candidata a coordenar o domínio PIM, recolhendo anúncios de RPs e distribuindo a lista final. |
| **Candidate RP**  | **C-RP**  | Roteador que se oferece para atuar como Rendezvous Point para um ou mais grupos multicast.                    |
  
---
  
### 2️⃣ Como ocorre a comunicação

1. **Os Candidate RPs (C-RPs)** enviam anúncios para o **Candidate BSR (C-BSR)** contendo os grupos multicast que desejam atender.  
2. O **C-BSR eleito como BSR ativo** consolida todas as informações recebidas e distribui periodicamente mensagens **Bootstrap** para todo o domínio.  
3. Cada roteador PIM-SM recebe essas mensagens e atualiza sua tabela local de RPs disponíveis.  
  
👉 Assim, todos os roteadores aprendem automaticamente **quem é o RP ativo** para cada grupo multicast, sem necessidade de configuração manual.  
  
---

### 3️⃣ Critérios de eleição

Se houver mais de um **Candidate BSR**, a eleição é determinada com base nos seguintes critérios:  
  
1. **Prioridade configurada** (menor prioridade vence);  
2. Em caso de empate, o **maior endereço IP** da interface candidata é usado como critério de desempate.  
  
De forma semelhante, se houver múltiplos **Candidate RPs**, o domínio poderá alternar entre eles conforme as políticas definidas pelo BSR.  
No nosso laboratório, isso será demonstrado ao **forçar a falha de um RP ativo**, permitindo observar o **failover automático para o RP de backup**.  
  
---

💡 **Resumo geral:**  
  
O **BSR** é o “cérebro” do domínio multicast, responsável por:  

- Eleger o **Rendezvous Point (RP)** ativo;  
- Distribuir os mapeamentos (*Group → RP*) para todos os roteadores;  
- Garantir a **redundância e continuidade** do serviço multicast em caso de falha de um RP.

---

Pronto — com os conceitos estabelecidos, o próximo passo é iniciar a configuração do **Candidate BSR (R01)** e dos **Candidate RPs (R02 e R03)** dentro da topologia.  

📊 **O que é automático e o que é manual**

| Ação                                     | Automático? | Quem decide                          |
|------------------------------------------|-------------|--------------------------------------|
| Definir quem é Candidate BSR             | ❌ Não     | Administrador                         |
| Definir quem é Candidate RP              | ❌ Não     | Administrador                         |
| Eleger o BSR ativo                       | ✅ Sim     | Protocolo PIM-SM                      |
| Eleger o RP (entre os candidatos)        | ✅ Sim     | BSR (com base nas mensagens C-RP Adv) |
| Distribuir o mapeamento (Group → RP)     | ✅ Sim     | BSR                                   |
| Aprender o RP e atualizar a tabela local | ✅ Sim     | Todos os roteadores PIM-SM            |

---

🧱 **Em projeto real (ou laboratório bem documentado)**

A definição de quem será **Candidate BSR** e **Candidate RP** deve estar prevista no projeto de rede.  
No nosso caso — com **cinco roteadores**, **topologia em anel** e **cenário educacional** — podemos seguir a seguinte estratégia:

| Função                      | Roteador             | Justificativa                                                                        |
|-----------------------------|----------------------|--------------------------------------------------------------------------------------|
| **Candidate BSR**           | **R01**              | Está próximo da fonte multicast (Server) e possui posição central no domínio PIM-SM. |
| **Candidate RP 1**          | **R02**              | Localização intermediária, favorece convergência e distribuição equilibrada.         |
| **Candidate RP 2 (Backup)** | **R03**              | Permite validar o failover automático caso o RP principal falhe.                     |
| **R04 / R05**               | Participantes PIM-SM | Aprendem automaticamente o RP via mensagens Bootstrap.                               |

---

⚙️ **O que o BSR faz automaticamente**

Após definir quem são os **Candidate BSRs** e **Candidate RPs**, o processo de eleição ocorre automaticamente:

1. O **Candidate BSR (R01)** envia mensagens **Bootstrap** para todo o domínio PIM.  
2. Os **Candidate RPs (R02 e R03)** enviam mensagens **C-RP Advertisement** ao BSR, informando os grupos multicast que desejam atender.  
3. O BSR compila todas as informações e distribui a tabela final de mapeamento (*Group → RP*) para todos os roteadores.  

Dessa forma, cada roteador PIM-SM aprende quem é o RP ativo para cada grupo multicast.  
Se um RP deixar de responder, o BSR detecta e remove automaticamente seu mapeamento, promovendo o RP de backup.

👉 **Ou seja:** o BSR automatiza o processo de **eleição, distribuição e failover** de RPs, mas a definição inicial dos candidatos ainda é feita pelo administrador.

---

## ⚙️ Ativando o protocolo PIM Sparse Mode

Com a base teórica clara, o próximo passo é ativar o **PIM Sparse Mode** em todas as interfaces que participam do domínio multicast (de R01 a R05).

```ios
R01#show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.10.254  YES NVRAM  up                    up
FastEthernet0/1            10.0.0.1        YES NVRAM  up                    up
FastEthernet1/0            10.0.0.18       YES NVRAM  up                    up
Loopback0                  1.1.1.1         YES NVRAM  up                    up

R01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.

R01(config)#int f0/0
R01(config-if)#ip pim sparse-mode
*Mar  1 02:00:05.663: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 192.168.10.254 on interface FastEthernet0/0

R01(config)#int f0/1
R01(config-if)#ip pim sparse-mode
*Mar  1 02:00:20.615: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.1 on interface FastEthernet0/1

R01(config)#int f1/0
R01(config-if)#ip pim sparse-mode
*Mar  1 02:00:36.563: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.18 on interface FastEthernet1/0

R01(config)#int lo0
R01(config-if)#ip pim sparse-mode
*Mar  1 00:18:25.859: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 1.1.1.1 on interface Loopback0
```

Agora que o PIM Sparse-Mode está habilitado, podemos verificar se o roteamento multicast foi corretamente ativado:  

```ios
R01#show ip multicast
  Multicast Routing: enabled
  Multicast Multipath: disabled
  Multicast Route limit: No limit
  Multicast Triggered RPF check: enabled
  Multicast Fallback group mode: Sparse
  Multicast DVMRP Interoperability: disabled
```

Em seguida, validamos a tabela de roteamento multicast:

```ios
R01#show ip mrout
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group
Outgoing interface flags: H - Hardware switched, A - Assert winner
Timers: Uptime/Expires
Interface state: Interface, Next-Hop or VCD, State/Mode

(*, 224.0.0.0), 00:10:57/00:02:04, RP 0.0.0.0, flags: SCL
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    FastEthernet0/0, Forward/Sparse, 00:10:57/00:02:04
```
  
Note que neste estágio ainda não há grupos específicos configurados — apenas as entradas padrão criadas ao ativar o PIM.  
As mensagens Bootstrap e Candidate RP Advertisement começarão a circular assim que configurarmos o Candidate BSR (R01) e os Candidate RPs (R02 e R03).  
  
💡 **Dica prática:**  
Ao capturar o tráfego PIM no Wireshark **(filtro ip.proto == 103)**, será possível visualizar as mensagens Bootstrap e C-RP Adv sendo trocadas entre os roteadores, comprovando que o domínio PIM-SM com BSR está operacional.  

### 🧩 Eleição automática do Designated Router (DR)

Ao ativar o **PIM Sparse Mode** nas interfaces, cada rede multicast local (LAN) com mais de um roteador realiza automaticamente a **eleição do Designated Router (DR)**.  
O DR é quem interage com os hosts — enviando **PIM Join** em direção ao RP quando há receptores, e **PIM Register** quando há fontes.
  
A eleição ocorre de forma simples:

- O roteador com o **maior IP ativo na rede** vence;
- Se ele falhar, os demais detectam a ausência de **PIM Hello** (a cada 30s por padrão) e reelegem automaticamente outro DR.

💡 Essa etapa é automática e ocorre **antes da descoberta do RP via Bootstrap Router**, portanto não é o foco deste laboratório.

### 💬 Entendendo as Mensagens PIM Hello

As mensagens **PIM Hello** são o ponto de partida de toda a comunicação entre roteadores PIM.  
Elas são trocadas periodicamente entre vizinhos para **formar e manter a vizinhança ativa** dentro do domínio multicast.

Essas mensagens também carregam informações importantes sobre o **modo de operação (Sparse, Dense, Bidir)**, **prioridade de DR** e **temporizadores** usados na rede.

---

#### ⚙️ Função prática das mensagens Hello

| Função                     | Descrição resumida                                                                                  |
|----------------------------|-----------------------------------------------------------------------------------------------------|
| **Descoberta de vizinhos** | Roteadores PIM trocam Hellos para reconhecer quem está na mesma LAN.                                |
| **Troca de parâmetros**    | Inclui Holdtime, DR Priority, modo PIM e outras opções de compatibilidade.                          |
| **Monitoramento**          | Se um roteador parar de enviar Hellos dentro do tempo limite (Holdtime), ele é considerado inativo. |

Essas trocas são automáticas e ocorrem no grupo **224.0.0.13** (PIM Routers) com **TTL 1**, limitadas ao enlace local.

---

#### 🧩 Estrutura simplificada da mensagem Hello

| Campo               | Função                                                                | Valor típico |
|---------------------|-----------------------------------------------------------------------|--------------|
| **Type**            | Identifica a mensagem PIM (Hello = 0x00)                              | 0x00         |
| **Holdtime**        | Tempo máximo sem receber Hellos antes de considerar o vizinho inativo | 105 segundos |
| **DR Priority**     | Define quem será o Designated Router na LAN (maior valor vence)       | 1 (padrão)   |
| **Generation ID**   | Valor aleatório que muda a cada reinício do roteador                  | Aleatório    |
| **Intervalo Hello** | Tempo entre Hellos enviados                                           | 30 segundos  |

💡 **Dica:**  
Você pode visualizar esses parâmetros facilmente no **Wireshark**, no campo `PIM Hello Options`.

---

#### 🔍 Exemplo de mensagens Hello no log

Logo após ativar o **PIM Sparse Mode** nas interfaces, é possível observar no log a troca de Hellos e a eleição automática de DR:

```ios
*Mar  1 02:00:36.563: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.18 on interface FastEthernet1/0
```
  
👉 Esse log mostra que o roteador 10.0.0.18 foi eleito Designated Router (DR) para a rede da interface FastEthernet1/0.  

🧭 **Resumo rápido**

| Tipo de mensagem            | Destino    | TTL | Finalidade principal                       |
|-----------------------------|------------|-----|--------------------------------------------|
| Hello                       | 224.0.0.13 | 1   | Estabelecer e manter vizinhança PIM        |
| Timeout (ausência de Hello) | —          | —   | Detectar falha e remover vizinho da tabela |
| Hello com DR Priority       | 224.0.0.13 | 1   | Eleger o DR na LAN automaticamente         |

💡 **Nota:**  
As mensagens Hello são as primeiras a aparecer na captura de pacotes PIM.  
Elas garantem que o domínio esteja operacional antes da troca das mensagens Bootstrap e Candidate-RP Advertisement, que analisaremos em seguida.  

<center><img src="Imagens/pacote01.png" alt="Pacote01" width="550" height="450"> </img> </center>  

Aqui vamos realizar a captura dos pacotes com o Whireshark. Então ligamos ele em R01 na interface F0/1 que se interliga com R02. Vamos utilizar o filtro `pim.type == 0`

![Pacote01](Imagens/02.png)  

### ⚙️ Configurando o Candidate RP e o Candidate BSR (Bootstrap Router)

Agora que o **PIM Sparse Mode** está ativo em todas as interfaces, o domínio multicast já pode iniciar o processo de **eleição automática do Rendezvous Point (RP)** por meio do **Bootstrap Router (BSR)** — o método **padrão IETF (RFC 5059)**.  

Diferente do Auto-RP (proprietário Cisco), o **Bootstrap Router** realiza toda a descoberta e distribuição de RPs **dentro do próprio protocolo PIM**, sem depender de grupos multicast adicionais (como 224.0.1.39 e 224.0.1.40).  

---

### 🧩 1️⃣ Escolha dos equipamentos

Para este laboratório, adotaremos a seguinte estrutura:  

| Função                        | Roteador | Loopback usada | Justificativa técnica                                                                                   |
|-------------------------------|----------|----------------|---------------------------------------------------------------------------------------------------------|
| **Candidate BSR**             | **R01**  | 1.1.1.1        | Próximo à fonte multicast (Server) e bem posicionado no domínio para distribuir as mensagens Bootstrap. |
| **Candidate RP 1 (Primário)** | **R02**  | 2.2.2.2        | Centralizado no domínio, ideal para otimizar convergência e formar a Shared Tree.                       |
| **Candidate RP 2 (Backup)**   | **R03**  | 3.3.3.3        | Redundância — permite observar o processo de eleição e failover do RP.                                  |

Assim, o R01 atuará como **coordenador (BSR)**, enquanto os roteadores R02 e R03 anunciarão suas candidaturas como **RPs**.  
  
---
  
### 🧭 2️⃣ Função das interfaces Loopback

No PIM Sparse Mode com BSR, as interfaces Loopback exercem papel importante, pois são usadas como **endereços lógicos de identificação (Router-ID)** e como **endereços de RP e BSR**.  
  
| Função da Loopback                                   | PIM deve estar ativo? | Motivo                                                                            |
|------------------------------------------------------|-----------------------|-----------------------------------------------------------------------------------|
| Loopback usada como **Candidate RP**                 | ✅ Sim               | Necessário para envio e recebimento de mensagens PIM (Register, Join, Bootstrap). |
| Loopback usada como **Candidate BSR**                | ✅ Sim               | O BSR utiliza a interface para enviar mensagens Bootstrap (PIM Type 13).          |
| Loopback usada apenas como Router-ID (sem papel PIM) | ⚙️ Opcional          | Pode permanecer sem PIM se não participar do tráfego multicast.                   |

💡 **Boa prática:**  
Em ambientes de estudo ou testes, mantenha o **PIM ativo em todas as loopbacks** — isso simplifica o troubleshooting e garante que o endereço lógico seja sempre alcançável via OSPF.  

---

### 🧰 3️⃣ Comandos de configuração

➡️ **No R01 (Candidate BSR):**

```ios
R01(config)#ip pim bsr-candidate loopback0 30
```

🔎 **Explicação:**

- **loopback0** → Interface usada como origem das mensagens Bootstrap (IP 1.1.1.1);
- **30** → Tamanho do hash mask usado para calcular o RP para cada grupo multicast (valor padrão típico);

Nenhum parâmetro de prioridade é aceito aqui..  

🧠 **Sobre a “prioridade” do BSR**

O Bootstrap Router (BSR) não tem prioridade configurável diretamente no IOS clássico.  
  
Se houver mais de um Candidate BSR, a eleição segue:  

- **Hash mask length (o maior valor vence)**;
- Se empatar, o **endereço IP mais alto vence**.

Portanto:  

Se quiser influenciar quem será o BSR, use um **hash-mask maior no roteador que você quer priorizar**.

```ios
R01(config)#ip pim bsr-candidate loopback0 30
R02(config)#ip pim bsr-candidate loopback0 20
```

→ **O R01 será eleito BSR, porque 30 > 20.**

💡 **Versões IOS XE / NX-OS**

Em plataformas mais novas **(IOS XE 17.x, NX-OS, ou IOS XR)**, algumas versões aceitam o parâmetro priority, mas no IOS tradicional (12.x, 15.x, ou em simuladores tipo EVE-NG, GNS3, CML), essa opção não existe.  
  
Então para fins de laboratório CCNP ENCOR (350-401), o comando correto é o clássico:  

```ios
ip pim bsr-candidate loopback0 30
```

🧰 **Resumo prático**  

| Função        | Comando correto                                       | Observação                                                     |
|---------------|-------------------------------------------------------|----------------------------------------------------------------|
| Candidate BSR | ip pim bsr-candidate loopback0 30                     | Define interface e máscara de hash; maior valor vence eleição  |
| Candidate RP  | ip pim rp-candidate loopback0 group-list 1 priority 5 | Aqui sim a prioridade é configurável                           |
| Verificação   | show ip pim bsr-router / show ip pim rp mapping       | Mostra quem foi eleito BSR e RP                                |

Exemplo:

➡️ **No R02 (Candidate RP Primário):**  

```
R02(config)#ip pim rp-candidate loopback0 group-list 1
R02(config)#access-list 1 permit 224.0.0.0 15.255.255.255
```

➡️ **No R03 (Candidate RP Secundário):**  

```ios
R03(config)#ip pim rp-candidate loopback0 group-list 1
R03(config)#access-list 1 permit 224.0.0.0 15.255.255.255
```

🔎 **Explicação:**

- **ip pim rp-candidate** anuncia o roteador como Candidate RP para o intervalo de grupos definidos;
- **group-list 1** especifica os grupos multicast válidos (no caso, todo o intervalo **224.0.0.0/4**);  
  
Esses anúncios serão enviados diretamente ao BSR por meio das mensagens C-RP Advertisement (**PIM Type 14**).  
  
🛰️ 4️⃣ **Fluxo esperado**

- O **R01 (Candidate BSR)** envia mensagens Bootstrap (**Type 13**) pelo domínio PIM-SM;
- Os **R02 e R03 (Candidate RPs)** enviam **C-RP Advertisements (Type 14)** ao BSR;
- O **BSR** compila as informações e distribui o mapeamento de grupos e RPs a todos os roteadores PIM;
  
Todos os roteadores passam a conhecer automaticamente quem é o RP ativo.  

### 3️⃣ Captura e Observação via Wireshark  

🧩 **Contexto da captura**

Após ativar o **PIM Sparse Mode** e configurar os papéis do **Bootstrap Router (BSR)** e dos **Candidate RPs**, o próximo passo é comprovar que as mensagens de sinalização estão circulando no domínio PIM-SM.  
  
Diferente do Auto-RP (que utiliza os grupos 224.0.1.39/40), o **BSR utiliza mensagens nativas do PIMv2** enviadas para o grupo **224.0.0.13 (ALL-PIM-ROUTERS)**.  
Aqui esperamos observar:  

| Tipo de Mensagem               | PIM Type | Quem envia              | Função                             |
|--------------------------------|----------|-------------------------|------------------------------------|
| **Bootstrap**                  | **9**    | BSR eleito (R01 ou R02) | Distribui o mapeamento de RPs      |
| **RP-Candidate Advertisement** | **4**    | R02 e R03               | Informam ao BSR que desejam ser RP |
| **PIM Hello**                  | **0**    | Todos                   | Mantém vizinhança e DR             |

---

### 🧪 Realizando a captura

📌 **Local ideal para captura:**  
  
**R01 – FastEthernet0/1 (ligação direta com R02)**  

📌 **Filtro recomendado:**  

```wireshark
pim.type == 4 or pim.type == 9
```
  
✅ PIM type 4 = anúncios dos RP candidates  
✅ PIM type 9 = mensagens Bootstrap emitidas pelo BSR eleito  
  
📸 **Captura real**  

Nesta captura vemos a mensagem PIM Type 9 (Bootstrap) contendo:  

- BSR Address
- BSR Priority
- Hash Mask Length
- Lista de RP Candidates
- Group-to-RP mapping
  
![Whireshark](Imagens/03.png)  

✅ **Validando a eleição REAL do BSR**
  
Somente um roteador pode ser o Bootstrap Router ativo.  
Mesmo que você configure múltiplos candidatos (como R01 e R02), o domínio escolhe apenas um.  

Para saber quem venceu a eleição, utilize:  

```ios
show ip pim bsr-router
```

O que observar na saída:  
  
| Campo                     | Significado                                       |
|---------------------------|---------------------------------------------------|
| Bootstrap router address  | IP da loopback do BSR eleito                      |
| Priority                  | Maior prioridade vence (se empate, maior IP)      |
| Hash mask length          | Fator usado na seleção determinística de RPs      |
| Next bootstrap message in | Temporização, prova de que a eleição está ativa   |

Então vamos executar em **R01**  

```ios
R01#show ip pim bsr-router
PIMv2 Bootstrap information
  BSR address: 2.2.2.2 (?)
  Uptime:      00:59:23, BSR Priority: 0, Hash mask length: 20
  Expires:     00:01:37
This system is a candidate BSR
  Candidate BSR address: 1.1.1.1, priority: 0, hash mask length: 30
R01#
```

✅ Se a saída mostrar R01 → R01 venceu  
✅ Se mostrar R02 → R02 venceu  
🎯 Esse é o único comando que revela o BSR real.  
  
✅ Interpretando o campo Hash Mask Length  
  
O campo Hash Mask Length é um dos elementos centrais do BSR, e quase ninguém explica direito.  
  
📌 **O que é o Hash Mask Length?**
  
O **Hash Mask Length** define como o domínio PIM distribui grupos multicast entre múltiplos RPs em cenários com dois ou mais RP Candidates.  
  
💡 Em outras palavras:  

- O Hash Mask é um “peso” usado para calcular qual RP será responsável por qual range de grupos.

🤓 **Como funciona internamente?**

- Para cada grupo multicast (ex: 239.1.1.1),
- O roteador aplica um cálculo hash no endereço do grupo,
- Usa o Hash Mask Length para reduzir o resultado,
- E esse valor final aponta para um RP específico.
  
✅ Com dois C-RPs (como R02 e R03), os grupos podem ser distribuídos entre eles.  
✅ Se apenas um RP existir, ele recebe todos os grupos.  
✅ Se o BSR mudar, o hash continua garantindo determinismo e estabilidade.  
  
📌 **Regra geral:**

- **Hash Mask Length maior** → distribuição mais granular
- **Hash Mask Length menor** → clusters maiores de grupos atribuídos ao mesmo RP  
  
Você provavelmente verá algo assim na mensagem capturada:  

```ios
Hash mask len: 20
```

🎯 **Significa:**  
> “Use os primeiros 20 bits do resultado do hash para decidir qual RP será usado.”
  
✅ **Confirmando o mapeamento no domínio**
  
Após analisar a captura, também podemos confirmar as decisões do BSR usando:

```ios
show ip pim rp mapping
```

Essa saída revela:  

- Qual RP está ativo
- A origem da informação (Bootstrap)
- Lista completa de RP-Candidates
- Tempo restante até expirar a eleição

Em nosso exemplo, vamos executar em R01:  

```ios
R01#show ip pim rp mapping
PIM Group-to-RP Mappings

Group(s) 224.0.0.0/4
  RP 2.2.2.2 (?), v2
    Info source: 2.2.2.2 (?), via bootstrap, priority 0, holdtime 150
         Uptime: 01:10:37, expires: 00:01:48
  RP 3.3.3.3 (?), v2
    Info source: 2.2.2.2 (?), via bootstrap, priority 0, holdtime 150
         Uptime: 01:09:54, expires: 00:01:32
R01#
```

Esta saída mostra que o domínio PIM-SM aprendeu dois ***Candidate RPs* (2.2.2.2 e 3.3.3.3)** através das mensagens de **Bootstrap**, indicando que o BSR está funcionando corretamente.  
Ambos os RPs são válidos para o range **224.0.0.0/4 e possuem prioridade 0**. Os timers de *uptime* e *expires* confirmam que as informações estão sendo atualizadas periodicamente pelo BSR.  

🧠 **Quando o RP realmente começa a participar?**  
  
Mesmo com BSR + RP Candidates funcionando, nada entra na tabela multicast ainda, porque o PIM-SM é orientado à demanda:  

- Sem IGMP Join → Sem árvore multicast → Sem uso do RP
- Somente quando Host02 enviar IGMP join para 239.1.1.1, o DR (R04):
  - cria o entry (*,G)
  - envia PIM Join até o RP
  - inicia a árvore compartilhada
  - e o fluxo multicast começa a ser construído
  
Depois disso:  

- O Server envia tráfego
- R01/R02 envia PIM Register ao RP
- RP conecta fonte a receptores
- A SPT pode surgir
- **show ip mroute passa a exibir (S,G) e (*,G)**

## ✅ 4️⃣ Ativando o Receptor (IGMP Join) — R04

Agora que o domínio PIM-SM já conhece o BSR, o RP principal (R02) e o RP backup (R03), podemos finalmente ativar **o primeiro receptor multicast real**.  
No PIM Sparse Mode, este é o momento em que tudo começa a acontecer: sem IGMP Join, a rede permanece silenciosa.

No nosso cenário, **o host interessado está conectado ao R04**, portanto R04 atuará como DR (Designated Router) da LAN 192.168.20.0/24.

### ✅ Configuração do IGMP Join em R04

```ios
R04(config)#interface FastEthernet1/1
R04(config-if)#ip igmp join-group 239.1.1.1
```

✅ **Confirmando que o IGMP Join foi processado**  

```ios
R04#show ip igmp groups
```

Saída em R04:  

```ios
R04#show ip igmp groups
IGMP Connected Group Membership
Group Address    Interface                Uptime    Expires   Last Reporter   Group Accounted
239.1.1.1        FastEthernet1/0          00:46:15  00:02:50  192.168.20.254
224.0.1.40       Loopback0                00:56:17  00:02:58  4.4.4.4
R04#
```

Isso confirma que existe um receptor na rede e que o R04 está participando do domínio multicast como DR desta LAN.  

## ✅ 5️⃣ Observando a Formação da Árvore (*,G)

Assim que R04 registra o interesse pelo grupo, ele envia **PIM Join na direção do RP (2.2.2.2)**.  
O RP passa a saber que existe um receptor interessado.  

No RP (R02):  

```ios
R02#show ip mroute 239.1.1.1
```

Saída típica:

```ios
R02#show ip mroute 239.1.1.1
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group
Outgoing interface flags: H - Hardware switched, A - Assert winner
 Timers: Uptime/Expires
 Interface state: Interface, Next-Hop or VCD, State/Mode

(*, 239.1.1.1), 00:48:42/00:03:04, RP 2.2.2.2, flags: S
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:48:42/00:03:04

R02#
```
  
✅ Isto indica que a Shared Tree (*,G) está sendo criada corretamente.  
✅ O RP já sabe que há um receptor atrás de R04.  
✅ O PIM Join percorreu o caminho R04 → R03 → R02.  

## ✅ 6️⃣ Ativando a Fonte Multicast — R01/Server
  
Com o receptor ativo, agora precisamos da fonte para iniciar o tráfego.  
O servidor multicast está conectado ao R01 (192.168.10.0/24).  

No Server:  

```ios
Server(config)#interface FastEthernet0/0
Server(config-if)#ip igmp static-group 239.1.1.1
```

Em R01 também precisamos fazer o join-grpup na interface **F0/0** que está ligada no server.

```ios
R01(config)#int f0/0
R01(config-if)#ip igmp join-group 239.1.1.1
```

Em seguida, verifique no R01:

```ios
R01#show ip mroute 239.1.1.1
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group
Outgoing interface flags: H - Hardware switched, A - Assert winner
 Timers: Uptime/Expires
 Interface state: Interface, Next-Hop or VCD, State/Mode

(*, 239.1.1.1), 00:00:05/00:02:54, RP 2.2.2.2, flags: SJCL
  Incoming interface: FastEthernet0/1, RPF nbr 10.0.0.2
  Outgoing interface list:
    FastEthernet0/0, Forward/Sparse, 00:00:05/00:02:54

R01#
```
  
✅ Agora temos a árvore de origem (S,G).  
✅ O tráfego está fluindo R01 → R02 → R03 → R04 → Host.  
✅ O PIM Register já foi enviado do DR da fonte para o RP.  

## ✅ 7️⃣ Confirmando a Convergência do Domínio PIM-SM

Neste ponto, todo o domínio multicast está ativo.  
Execute nos roteadores principais:  

📌 **R01, R02, R03, R04 e R05**

```ios
show ip mroute 239.1.1.1
show ip pim rp mapping
show ip pim neighbor
```
  
O que você deve ver:  
  
- Entradas (*,G) em todo o domínio
- Entrada (S,G) começando no R01 e propagando para o RP
- RPF correto em cada salto
- Interfaces corretas listadas na OIL (Outgoing Interface List)
  - RP ativo = R02
  - RP candidato backup = R03
  
✅ Neste ponto, a rede multicast está totalmente funcional  
✅ O tráfego está fluindo corretamente  
✅ A Shared Tree (*,G) e a Source Tree (S,G) estão construídas  
✅ Estamos prontos para testar falhas do RP  

## 🧠 O papel do DR no processo multicast (com PIM-SM e Bootstrap Router)

O **Designated Router (DR)** é o primeiro roteador a detectar o interesse de um host por um grupo multicast.  
No nosso cenário, o **Host02**, conectado à interface **FastEthernet1/0 de R04**, será o receptor interessado no grupo **239.1.1.1**.  

Para observar o comportamento do IGMP e a atuação do DR, vamos habilitar o debug no **R04**:

```ios
R04#debug ip igmp
IGMP debugging is on
R04#
```

Agora, no **Host02**, adicionamos o host ao grupo multicast:  

```ios
HOST02(config)#int f0/0
HOST02(config-if)#ip igmp join-group 239.1.1.1
```

Voltando ao **R04**, podemos observar o roteador detectando o join do host e criando a entrada multicast local:  

```ios
R04#
*Mar  1 00:02:01.643: IGMP(0): Received v2 Query on FastEthernet0/0 from 10.0.0.9
R04#
*Mar  1 00:02:05.567: IGMP(0): Send v2 general Query on FastEthernet0/1
*Mar  1 00:02:06.567: IGMP(0): Send v2 general Query on FastEthernet1/0
*Mar  1 00:02:06.567: IGMP(0): Set report delay time to 2.4 seconds for 239.1.1.1 on FastEthernet1/0
R04#
*Mar  1 00:02:07.575: IGMP(0): Send v2 general Query on Loopback0
*Mar  1 00:02:07.575: IGMP(0): Set report delay time to 7.9 seconds for 224.0.1.40 on Loopback0
R04#
*Mar  1 00:02:09.579: IGMP(0): Send v2 Report for 239.1.1.1 on FastEthernet1/0
*Mar  1 00:02:09.579: IGMP(0): Received v2 Report on FastEthernet1/0 from 192.168.20.254 for 239.1.1.1
*Mar  1 00:02:09.583: IGMP(0): Received Group record for group 239.1.1.1, mode 2 from 192.168.20.254 for 0 sources
*Mar  1 00:02:09.583: IGMP(0): Updating EXCLUDE group timer for 239.1.1.1
*Mar  1 00:02:09.583: IGMP(0): MRT Add/Update FastEthernet1/0 for (*,239.1.1.1) by 0
R04#
*Mar  1 00:02:15.579: IGMP(0): Send v2 Report for 224.0.1.40 on Loopback0
*Mar  1 00:02:15.579: IGMP(0): Received v2 Report on Loopback0 from 4.4.4.4 for 224.0.1.40
*Mar  1 00:02:15.583: IGMP(0): Received Group record for group 224.0.1.40, mode 2 from 4.4.4.4 for 0 sources
*Mar  1 00:02:15.583: IGMP(0): Updating EXCLUDE group timer for 224.0.1.40
*Mar  1 00:02:15.583: IGMP(0): MRT Add/Update Loopback0 for (*,224.0.1.40) by 0
*Mar  1 00:02:15.583: IGMP(0): Received v2 Report on Loopback0 from 4.4.4.4 for 224.0.1.40
*Mar  1 00:02:15.583: IGMP(0): Received Group record for group 224.0.1.40, mode 2 from 4.4.4.4 for 0 sources
R04#
*Mar  1 00:02:15.583: IGMP(0): Updating EXCLUDE group timer for 224.0.1.40
*Mar  1 00:02:15.583: IGMP(0): MRT Add/Update Loopback0 for (*,224.0.1.40) by 0
```

O **R04, atuando como Designated Router (DR)** da rede local, aprendeu que há um receptor interessado no grupo 239.1.1.1.  
A partir daí, ele envia uma mensagem **PIM Join em direção ao RP eleito via Bootstrap Router (BSR)**, seguindo o melhor caminho unicast (RPF) até o RP.  
  
Neste momento, começa a se formar a árvore compartilhada, representada como **(*,G), onde “*” significa “todas as fontes possíveis” e “G” é o grupo multicast (239.1.1.1)**.  
  
💡 **Quando a fonte (Server) entra na comunicação**
  
Nosso Server (192.168.10.1), conectado à LAN de R01, será a fonte multicast.  
Como o servidor é um roteador disfarçado de PC, simularemos o envio de tráfego com um join-group e um ping multicast.  

```ios
SERVER(config)#int f0/0
SERVER(config-if)#ip igmp join-group 239.1.1.1
SERVER#ping 239.1.1.1
```

Ao enviar o tráfego multicast, o roteador da fonte **(DR da LAN do Server, no caso o R01)** gera uma mensagem PIM Register unicast para o RP — informando que existe uma fonte ativa enviando para o **grupo G.**  

O **RP (eleito pelo BSR)** passa então a conhecer:  

- A **fonte (S)** que envia para o grupo;
- Os receptores que solicitaram o grupo.
- O RP conecta as duas pontas e o tráfego multicast começa a fluir no domínio.

🌳 **Formação da Árvore Multicast (*,G) — A Shared Tree**

Até este ponto, já temos:  

- O **R01** como Bootstrap Router (BSR) ativo;
- O **R02** e o R03 como Candidate RPs (RP principal e backup);
- Todos os roteadores do domínio conhecem o RP eleito via mensagens Bootstrap.
  
Quando o **Host02 (192.168.20.1) se inscreve no grupo 239.1.1.1**, o R04 (DR da LAN) envia um PIM Join em direção ao RP (2.2.2.2), seguindo a rota unicast aprendida via OSPF.  
  
🔹 Assim nasce a primeira árvore multicast, a **Shared Tree (*,G)**, que conecta os receptores ao RP.  
  
Podemos confirmar a criação dessa árvore em R04:  

```ios
R04#show ip mroute 239.1.1.1
```

Saída

```ios
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group
Outgoing interface flags: H - Hardware switched, A - Assert winner
 Timers: Uptime/Expires
 Interface state: Interface, Next-Hop or VCD, State/Mode

(*, 239.1.1.1), 00:10:09/00:02:00, RP 2.2.2.2, flags: SJCL
  Incoming interface: FastEthernet0/0, RPF nbr 10.0.0.9
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:10:09/00:02:00
```

🧠 **Análise da saída:**

- **(*,G)** → entrada da árvore compartilhada (ainda sem fonte específica).
- **RP 2.2.2.2** → indica o RP eleito via Bootstrap Router.
- **Incoming interface** → interface usada para alcançar o RP (via RPF).
- **Outgoing interface list** → interface que conduz o tráfego até o receptor (Host02).
  
💬 **Conclusão até aqui**  
  
- O domínio multicast já tem um **RP dinâmico** aprendido via Bootstrap Router.
- O **R04 (DR)** estabeleceu a **árvore (*,G)** em direção ao RP.
- O **Server (R01) e o Host02 (R04)** agora participam ativamente do **grupo 239.1.1.1.**
- O próximo passo será observar a migração para a árvore SPT (Shortest Path Tree) — quando o tráfego passa a fluir diretamente entre a fonte e os receptores, sem depender do RP.
 
## 🚀 Quando o Servidor Inicia o Tráfego

Quando o **Server (192.168.10.1)** começa a enviar tráfego multicast para o grupo **239.1.1.1**, o roteador **R01 (Designated Router da LAN do Server)** detecta esse fluxo e envia uma mensagem **PIM Register** diretamente ao **RP eleito (2.2.2.2)** — que foi aprendido dinamicamente via **Bootstrap Router (BSR)**.  

Esse registro informa:  

- A **fonte (S = 192.168.10.1)**  
- O **grupo (G = 239.1.1.1)**  
  
O RP, ao receber o *Register*, cria uma nova entrada **(S,G)** na sua tabela multicast e conecta as duas pontas da comunicação:  

- os receptores que já haviam enviado o **PIM Join** (R04 → RP);  
- e a fonte recém-descoberta (R01 → RP).  

🔎 **Verificação prática**

No **RP (R02)**, podemos validar com:

```ios
R02#show ip mroute 239.1.1.1
```

Saída esperada  

```ìos
(*, 239.1.1.1), 00:01:12/00:02:54, RP 2.2.2.2, flags: SJCL
  Incoming interface: FastEthernet0/0, RPF nbr 10.0.0.1
  Outgoing interface list:
    FastEthernet0/1, Forward/Sparse, 00:01:12/00:02:54

(S, 239.1.1.1), 00:00:35/00:02:34, Source 192.168.10.1, flags: SJ
  Incoming interface: FastEthernet0/0, RPF nbr 10.0.0.1
  Outgoing interface list:
    FastEthernet0/1, Forward/Sparse, 00:00:35/00:02:34
```

💡 **Resumo do que aconteceu:**  

1. O receptor **(Host02)** enviou o Join → criou-se o **(*,G)**.
2. A fonte **(Server)** enviou tráfego → gerou o Register e criou o **(S,G)**.
3. O **RP** uniu as duas pontas → o tráfego multicast começou a fluir.

---

⚡ **Migração para a Shortest Path Tree (SPT)**  

Depois que o tráfego multicast estabiliza, o roteador receptor **(R04)** pode identificar que existe um caminho mais curto diretamente até a fonte **(192.168.10.1)**, sem precisar passar pelo RP.  
  
Nesse momento, ele envia um novo **PIM Join (S,G)** em direção à fonte, e o tráfego passa a seguir pela **SPT (Shortest Path Tree)** — a árvore mais eficiente e direta entre a fonte e os receptores.  

O RP continua existindo, mas agora apenas como referência para novos receptores que entrarem no grupo.  
O tráfego ativo flui diretamente pela SPT, reduzindo latência e uso de recursos na rede.  

---

🧩 **Propagação e Aprendizado do RP no PIM-SM com Bootstrap Router**

Diferente do **Auto-RP (proprietário Cisco)**, o Bootstrap Router (BSR) segue o padrão IETF RFC 5059 e dispensa grupos multicast especiais como 224.0.1.39 e 224.0.1.40.  
Em vez disso, o BSR distribui as informações de Candidate RPs usando mensagens **Bootstrap (PIM Type 4)**, enviadas em modo unicast hop-by-hop entre roteadores PIM.  

🔹 **Em resumo:**  
  
- O **BSR (em nosso caso o R01)** é responsável por divulgar quem são os Candidate RPs e qual deles foi eleito para cada grupo.
- Os **Candidate RPs (R02 e R03**) enviam anúncios **C-RP Advertisement (PIM Type 9) para o BSR**.
- O **BSR** processa essas mensagens, decide o RP ativo, e repassa a todos os roteadores PIM-SM do domínio.

💡 **Isso elimina a necessidade do comando ip pim autorp listener, que só existe em ambientes Auto-RP (Cisco Proprietário).**  
  
✅ **Validação do funcionamento do BSR**
  
Após configurar o domínio multicast com o BSR e os Candidate RPs, todos os roteadores aprendem automaticamente quem é o RP ativo.  
Podemos validar de duas formas principais:  
  
1️⃣ **Exibir o RP aprendido**  
  
```ios
R04#show ip pim rp mapping
```

Saída esperada:

```ios
PIM Group-to-RP Mappings

Group(s) 224.0.0.0/4
  RP 2.2.2.2 (?), v2
    Info source: 1.1.1.1 (?), via bootstrap, priority 0, holdtime 150
         Uptime: 00:11:22, expires: 00:02:33
  RP 3.3.3.3 (?), v2
    Info source: 1.1.1.1 (?), via bootstrap, priority 0, holdtime 150
         Uptime: 00:11:10, expires: 00:02:30
```

2️⃣ **Validar o Bootstrap Router ativo**  

```ios
R04#show ip pim bsr-router
```

Saída esperada:  

```ios
PIMv2 Bootstrap information
  BSR address: 1.1.1.1 (?), priority: 10, hash mask length: 30
  Candidate RPs:
    2.2.2.2, group prefix: 224.0.0.0/4, priority: 0, holdtime: 150
    3.3.3.3, group prefix: 224.0.0.0/4, priority: 0, holdtime: 150
```

🧠 **Como interpretar o campo Hash Mask Length**
  
O campo Hash Mask Length é usado pelo BSR para determinar qual RP será escolhido quando há vários Candidate RPs que cobrem o mesmo intervalo de grupos.  
Ele funciona como um "filtro de seleção" — quanto menor o valor, maior o agrupamento de grupos multicast sob o mesmo RP.  

| Hash Mask | Significado prático                           | Efeito                    |
|-----------|-----------------------------------------------|---------------------------|
| 0         | Todos os grupos usam o mesmo RP               | Menor granularidade       |
| 30        | Cada RP pode atender faixas menores de grupos | Maior equilíbrio de carga |
  
💡 **Em laboratórios simples, o valor padrão (30) é suficiente. Em redes grandes, ajustar o hash mask permite balancear grupos multicast entre múltiplos RPs.**  
  
🔍 **Captura de mensagens Bootstrap no Wireshark**  
  
Para visualizar a troca de mensagens entre os roteadores no domínio, use o filtro:  

```Whireshark
pim.type == 4 or pim.type == 9
```

- **Type 4:** Mensagens Bootstrap (enviadas pelo BSR)
- **Type 9:** Candidate RP Advertisements (enviadas pelos RPs candidatos)
  
Com isso, é possível ver no Wireshark as mensagens de eleição e distribuição do RP, confirmando que o domínio PIM-SM com BSR está operacional.  

💬 **Conclusão**

- O tráfego multicast agora flui endereçando o RP dinâmico (via BSR).
- Os receptores e fontes se conectam automaticamente através da árvore compartilhada (*,G).
- O domínio migra para a árvore otimizada (S,G), eliminando dependência do RP para o fluxo ativo.
- O Bootstrap Router (BSR) garante que a eleição e redistribuição dos RPs sejam automáticas e interoperáveis entre diferentes fabricantes.

---

Alterar Daqui

---

🧰 **Captura no Wireshark**  
  
Para confirmar a propagação das mensagens Auto-RP, realize a captura nas interfaces de trânsito entre o Mapping Agent **(R01)** e os roteadores intermediários **(R03, R04)**.  
  
Locais sugeridos para captura:

| Equipamento                  | Interface      | Motivo
|------------------------------|----------------|----------------------------------------------------------------------|
| R01 (Mapping Agent)          | Fa0/1          | Origem das mensagens Auto-RP Discovery (224.0.1.39)                  |
| R02 (Candidate RP)           | Fa0/0          | Envio dos anúncios Auto-RP Announce (224.0.1.40)                     |
| R03 (roteador intermediário) | Fa0/0 ou Fa0/1 | Validação de que os pacotes Auto-RP estão atravessando o domínio PIM |
| R04 (DR do Host)             | Fa0/0          | Verificar se o listener permitiu o recebimento das mensagens Auto-RP |  

**Filtro recomendado:**  

```whireshark
ip.dst == 224.0.1.39 || ip.dst == 224.0.1.40
```
  
🔍 **O que observar:**
  
| Tipo de mensagem            | Origem  | Destino                  | Descrição                                                         |
|-----------------------------|---------|--------------------------|-------------------------------------------------------------------|
| Auto-RP Announcement        | R02     | 224.0.1.40               | R02 anuncia-se como RP candidato                                  |
| Auto-RP Discovery           | R01     | 224.0.1.39               | R01 (Mapping Agent) distribui o mapeamento do RP                  |
| Encaminhamento via Listener | R03/R04 | 224.0.1.39 ou 224.0.1.40 | Indica que o listener está retransmitindo os pacotes pelo domínio |  

**R01 - Interface F0/1**  

![Whireshark](Imagens/05.png)  

**R02 - Interface F1/0**  

![Whireshark](Imagens/06.png)  

**R03 - Interface F0/0**  

![Whireshark](Imagens/07.png)  

**R04 - Interface F0/0**  

![Whireshark](Imagens/08.png)  

✅ **Conclusão**

O comando **ip pim autorp listener** é indispensável para inicializar corretamente um domínio PIM Sparse Mode que utiliza Auto-RP.  
  
Ele garante que:

- Todos os roteadores aprendam quem é o RP (resolvendo o paradoxo do ovo e da galinha);
- As mensagens Auto-RP (224.0.1.39 e 224.0.1.40) cheguem a todos os pontos da rede;
- O domínio PIM esteja sincronizado antes da formação da árvore multicast (*,G) e (S,G).
  
💡 **Resumo rápido:**  
  
Sem o autorp listener, roteadores distantes do Mapping Agent podem nunca aprender o RP, e o multicast simplesmente não se forma.  

## 🌳 Formação da Árvore Multicast — do IGMP Join ao PIM Register  
  
Com o domínio PIM Sparse Mode devidamente sincronizado e todos os roteadores já conhecendo o Rendezvous Point (RP) através do Auto-RP e do autorp listener, finalmente podemos observar a formação da árvore multicast.  
  
Essa é a parte mais visual e importante do laboratório, pois mostra o fluxo completo de como uma sessão multicast é criada e otimizada.  
  
### 🧩 1️⃣ O início de tudo: o IGMP Join

A comunicação multicast só é iniciada quando há um receptor interessado.  
Sem receptores, nenhum tráfego é enviado — esse é o grande diferencial do modo Sparse Mode.  
  
O processo começa no host (no nosso caso, um roteador simulando um PC) que deseja receber o fluxo multicast.  

📍 Comando no HOST02:

```ios
interface FastEthernet0/0
 ip igmp join-group 239.1.1.1
```  

- Esse comando simula o **IGMP Report** (mensagem enviada pelos hosts para participar de um grupo multicast).
- O roteador conectado ao host (chamado de Designated **Router – DR**) registra essa informação e sabe que há um receptor interessado em **239.1.1.1**.

### 🛰️ 2️⃣ O papel do DR (Designated Router)

O DR é o primeiro roteador no caminho que “ouve” o IGMP Join do host.  
Ao receber o pedido, ele precisa fazer com que o tráfego chegue até esse receptor — mas como ele faz isso?  
  
Como o PIM Sparse Mode não faz flood, o DR precisa “subir” até o Rendezvous Point (RP).  

👉 Então o DR consulta a tabela PIM e verifica quem é o RP responsável pelo grupo 239.1.1.1, informação aprendida via Auto-RP:  

```ios
show ip pim rp mapping
```

- Se o RP for, por exemplo, 2.2.2.2 (R02), o DR enviará uma mensagem PIM Join na direção do RP, utilizando a rota unicast normal (via OSPF).  
  
### ⚙️ 3️⃣ O nascimento da árvore compartilhada (*,G)

Durante o caminho até o RP, cada roteador cria uma entrada na tabela multicast, indicando que há um receptor interessado naquele grupo.  
Essas entradas têm o formato:  

```ios
(*, 239.1.1.1)
```

O asterisco (*) indica que o receptor ainda não conhece a fonte — ele está apenas interessado no grupo.  

- Esse caminho reverso é conhecido como Shared Tree, ou árvore compartilhada.  
  
✅ **Agora o RP já sabe que há receptores interessados no grupo 239.1.1.1.**  

Você pode verificar essa estrutura com o comando:  

```ios
show ip mroute 239.1.1.1
```

Exemplo em R03:  

```ios
R03#show ip mroute 239.1.1.1
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group
Outgoing interface flags: H - Hardware switched, A - Assert winner
 Timers: Uptime/Expires
 Interface state: Interface, Next-Hop or VCD, State/Mode

(*, 239.1.1.1), 01:18:31/00:02:42, RP 2.2.2.2, flags: SF
  Incoming interface: FastEthernet1/0, RPF nbr 10.0.0.5
  Outgoing interface list:
    FastEthernet0/0, Forward/Sparse, 01:18:31/00:02:42

R03#
```

### 📡 4️⃣ A fonte começa a transmitir — PIM Register

Agora, o servidor multicast (R01) começa a enviar tráfego para o grupo **239.1.1.1.**  
  
O roteador diretamente conectado à fonte (também um DR) detecta que está recebendo tráfego multicast sem receptores ainda conhecidos.  
Para resolver isso, ele encapsula o tráfego dentro de uma mensagem PIM Register e envia diretamente ao RP (R02), via unicast.  
  
💡 **Essa é a primeira etapa da comunicação — o RP “descobre” a fonte.**  

### 🔁 5️⃣ RP conecta as pontas e inicia o fluxo

O RP agora conhece dois lados:

- **As fontes (S)** — aprendidas via mensagens PIM Register.
- **Os receptores (R)** — aprendidos via mensagens PIM Join.
  
Ele então conecta essas duas informações e cria as entradas:  

```ios
(S, 239.1.1.1)
(*, 239.1.1.1)
```

A partir desse momento, o RP começa a reenviar o tráfego multicast pela árvore compartilhada (*,G) até o DR do receptor.
Os pacotes multicast fluem normalmente até o host.

✅ **O multicast agora está funcional!**  

### ⚙️ 6️⃣ A transição para a Árvore de Caminho Mais Curto (SPT)

Após o fluxo se estabilizar, o roteador receptor percebe que há um caminho mais direto entre ele e a fonte (sem passar pelo RP).  
  
Então, ele envia um novo PIM Join diretamente em direção à fonte, criando a árvore SPT (Shortest Path Tree).
A árvore agora passa a ser baseada em **(S,G)**, e o RP deixa de encaminhar esse tráfego.  
  
Esse comportamento otimiza o caminho e reduz o delay, criando a estrutura:  

```ios
(S, 239.1.1.1)
```

Então vamos no SERVER e realizar um ping para o grupo 239.1.1.1  

```ios
SERVER#ping 239.1.1.1 repeat 100
```  

Em R01 execute o comando:  

```ios
SERVER#ping 239.1.1.1 repeat 100

Type escape sequence to abort.
Sending 100, 100-byte ICMP Echos to 239.1.1.1, timeout is 2 seconds:

Reply to request 0 from 192.168.10.1, 4 ms
Reply to request 0 from 192.168.20.1, 176 ms
Reply to request 1 from 192.168.10.1, 4 ms
Reply to request 1 from 192.168.20.1, 128 ms
Reply to request 2 from 192.168.10.1, 4 ms
Reply to request 2 from 192.168.20.1, 112 ms
Reply to request 3 from 192.168.10.1, 4 ms
Reply to request 3 from 192.168.20.1, 116 ms
Reply to request 4 from 192.168.10.1, 4 ms
Reply to request 4 from 192.168.20.1, 132 ms
Reply to request 5 from 192.168.10.1, 4 ms
Reply to request 5 from 192.168.20.1, 120 ms
Reply to request 6 from 192.168.10.1, 4 ms
Reply to request 6 from

...saída omitida...
```  
  
```ios
R01#show ip mroute 239.1.1.1
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT, M - MSDP created entry,
       X - Proxy Join Timer Running, A - Candidate for MSDP Advertisement,
       U - URD, I - Received Source Specific Host Report,
       Z - Multicast Tunnel, z - MDT-data group sender,
       Y - Joined MDT-data group, y - Sending to MDT-data group
Outgoing interface flags: H - Hardware switched, A - Assert winner
 Timers: Uptime/Expires
 Interface state: Interface, Next-Hop or VCD, State/Mode

(*, 239.1.1.1), 01:58:37/stopped, RP 2.2.2.2, flags: SJCF
  Incoming interface: FastEthernet0/1, RPF nbr 10.0.0.2
  Outgoing interface list:
    FastEthernet0/0, Forward/Sparse, 01:58:37/00:02:32

(192.168.10.1, 239.1.1.1), 00:00:16/00:03:17, flags: FT
  Incoming interface: FastEthernet0/0, RPF nbr 0.0.0.0, Registering
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:00:17/00:03:12
    FastEthernet0/1, Forward/Sparse, 00:00:17/00:03:12

R01#  
```  

### ✅ Conclusão

O PIM Sparse Mode constrói a árvore multicast de forma inteligente e otimizada, somente quando há receptores interessados.  
O processo completo ocorre em três fases:  

| Etapa                                               | Descrição                            |
|-----------------------------------------------------|--------------------------------------|
| 1️⃣ Descoberta e sincronização (Auto-RP + Listener) | Define o RP e garante o domínio PIM   |
| 2️⃣ Formação da Shared Tree (*,G)                   | Ligação dos receptores ao RP          |
| 3️⃣ Transição para SPT (S,G)                        | Ligação direta entre receptor e fonte |  

## 🧰 Validação e Troubleshooting do PIM Sparse Mode

Após configurar todo o domínio PIM-SM, habilitar o Auto-RP (com Listener) e realizar os joins multicast, é hora de validar a formação da árvore multicast e confirmar se o tráfego está fluindo corretamente.  
  
Esta é a parte final e mais importante do laboratório — onde garantimos que cada elemento **(IGMP, PIM, RP e RPF)** está operando de forma integrada.

### 1️⃣ Verificar os vizinhos PIM — show ip pim neighbor

O primeiro passo é garantir que os roteadores realmente formaram vizinhança PIM nas interfaces corretas.  
  
📍 Execute em todos os roteadores:  

```ios
show ip pim neighbor
```

📘 **Saída esperada:**  

```ios
PIM Neighbor Table
Neighbor Address     Interface          Uptime/Expires    Ver/Mode
10.0.0.2             FastEthernet0/0    00:02:13/00:01:46 v2/Sparse
10.0.0.6             FastEthernet0/1    00:02:10/00:01:50 v2/Sparse
```

🔍 **Interpretação:**

- Todos os vizinhos devem aparecer em modo Sparse.
- Se não houver vizinhos, revise o comando ip pim sparse-mode nas interfaces.
- Sem vizinhança, o PIM não forma a árvore multicast.  

### 2️⃣ Confirmar o RP ativo — show ip pim rp mapping

O próximo passo é verificar se todos os roteadores aprenderam quem é o RP através do Auto-RP.  
  
📍 Execute em cada roteador:  

```ios
show ip pim rp mapping
```

📘 **Saída esperada**:  

```ios
Group(s) 224.0.0.0/4
  RP 2.2.2.2 (?), v2
    Info source: 1.1.1.1 (?), via Auto-RP
    Uptime: 00:00:42, expires: 00:01:17
```  

🔍 **Interpretação:**  
  
- O campo RP mostra o IP do Candidate RP (R02).
- Info source mostra o Mapping Agent (R01).
- O campo via Auto-RP confirma que o aprendizado foi feito automaticamente.
- Se aparecer “No RP mapping information”, o problema é na propagação das mensagens Auto-RP → verifique ip pim autorp listener.  

### 3️⃣ Verificar os grupos IGMP — show ip igmp groups

Agora, valide se os hosts realmente aderiram ao grupo multicast.  

📍 No roteador conectado ao Host02:  

```ios
show ip igmp groups
```

📘 **Saída esperada:**
  
```ios
Group Address    Interface       Uptime    Expires   Last Reporter   Group Mode
239.1.1.1        FastEthernet1/0 00:02:18  00:02:05  192.168.20.1    IGMPv2
```

🔍 **Interpretação:**  

- O endereço 239.1.1.1 confirma que o host se juntou ao grupo.
- O roteador local atua como Designated Router (DR).
- Se o grupo não aparecer, o host não enviou IGMP Join → revise ip igmp join-group 239.1.1.1.  

### 4️⃣ Validar a tabela de rotas multicast — show ip mroute

Este é o comando mais importante do laboratório .  
Ele mostra como o roteador está encaminhando o tráfego multicast.  

📍 Execute em todos os roteadores do caminho:  

```ios
show ip mroute 239.1.1.1
```

📘 **Saída esperada (Shared Tree ativa):**  

```ios
(*, 239.1.1.1), uptime: 00:00:56, RP 2.2.2.2, flags: SJCL
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:00:52/00:02:08
```

📘 **Após a fonte começar a transmitir:**  

```ios
(S, 239.1.1.1), uptime: 00:00:31, flags: T
  Incoming interface: FastEthernet0/1, RPF nbr 10.0.0.9
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:00:27/00:02:32
```

🔍 **Interpretação:**  

| Campo               | Significado                                |
|---------------------|--------------------------------------------|
| (*,G)               | Árvore compartilhada (receptores → RP)     |
| (S,G)               | Árvore específica (fonte → receptores)     |
| RP                  | Endereço do Rendezvous Point               |
| Incoming interface  | Caminho reverso até a fonte (RPF)          |
| Outgoing interfaces | Interfaces pelas quais o tráfego é enviado |  

💡 **Se a entrada (S,G) aparecer, significa que o SPT (Shortest Path Tree) foi formado com sucesso.**  

### 5️⃣ Confirmar o RPF — show ip rpf

O **Reverse Path Forwarding (RPF)** garante que o tráfego multicast está sendo recebido pelo caminho correto de volta à fonte.

📍 Execute no roteador receptor (por exemplo, R04):  

```ios
show ip rpf 192.168.10.1
```

📘 **Saída esperada:**  

```ios
RPF information for ? (192.168.10.1)
  RPF interface: FastEthernet0/0
  RPF neighbor: 10.0.0.1
  RPF route/mask: 10.0.0.0/30
  RPF type: unicast
  RPF recursion count: 0
```  

🔍 **Interpretação:**

- O RPF deve apontar para o roteador correto no caminho até a fonte.  
- Se o RPF falhar, o tráfego não será encaminhado — o roteador descarta o pacote multicast.  

### 6️⃣ Confirmar a recepção de tráfego multicast

Por fim, envie tráfego da fonte (Server / R01) para o grupo 239.1.1.1 e verifique se os receptores o recebem.  
  
📍 **No Server (R01):**  

```ios
ping 239.1.1.1 repeat 5
```

📍 **No Host02:**  

```ios
debug ip mpacket
```

📘 **Saída esperada:**

```ios
00:00:24: IP multicast packet received from 192.168.10.1 (239.1.1.1), 28 bytes
```
  
✅ Se o host receber o pacote multicast, o laboratório está 100% funcional.  

### 🧭 7️⃣ Diagnóstico rápido de problemas comuns

| Sintoma                                  | Causa provável                 | Solução                                         |
|------------------------------------------|--------------------------------|-------------------------------------------------|
| show ip pim rp mapping vazio             | Mensagens Auto-RP não propagam | Adicione ip pim autorp listener                 |
| show ip mroute sem (*,G)                 | Nenhum IGMP Join recebido      | Verifique o join-group no host                  |
| Tráfego chega ao RP, mas não ao receptor | Falha de RPF                   | Verifique show ip rpf e tabela de rotas unicast |
| Pacotes “Malformed” no Wireshark         | Captura truncada               | Aumente Snaplen para 65535                      |
| DR incorreto no domínio LAN              | Vizinhança PIM instável        | Verifique show ip pim neighbor e prioridade DR  |  

## 🧾 Resumo Final — Fluxo do PIM Sparse Mode

| Etapa | Descrição                       | Comando de validação      |
|-------|---------------------------------|---------------------------|
| 1️⃣   | Formação das vizinhanças PIM     | show ip pim neighbor     |
| 2️⃣   | Descoberta do RP (Auto-RP)       | show ip pim rp mapping   |
| 3️⃣   | Adesão do host ao grupo          | show ip igmp groups      |
| 4️⃣   | Criação da Shared Tree (*,G)     | show ip mroute           |
| 5️⃣   | Registro da fonte (PIM Register) | show ip mroute no RP     |
| 6️⃣   | Transição para SPT (S,G)         | show ip mroute + flags T |
| 7️⃣   | Validação do RPF                 | show ip rpf <source>     |  

## ✅ Conclusão
  
Com esses testes, você conclui a validação completa do PIM Sparse Mode, cobrindo:

- Eleição e distribuição do RP (Auto-RP + Listener)
- Formação da árvore multicast (*,G → S,G)
- Confirmação de IGMP, PIM, RPF e fluxo multicast ativo

## 📘 Tabela de Comandos

### R01 – Mapping Agent (MA)

| **Seção**                | **Comando / Configuração**                                                                     | **Descrição**                                            |
|--------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| **Global**               | `ip multicast-routing`                                                                         | Habilita o roteamento multicast globalmente              |
|                          | `ip pim autorp listener`                                                                       | Permite escutar mensagens Auto-RP em interfaces não PIM  |
|                          | `ip pim send-rp-discovery Loopback0 scope 16`                                                  | Define R01 como **Mapping Agent (MA)** no domínio PIM-SM |
| **Interface Loopback0**  | `ip address 1.1.1.1 255.255.255.255`<br>`ip pim sparse-mode`                                   | Identificação do roteador e ativação PIM na Loopback     |
| **Fa0/0 (LAN Server)**   | `ip address 192.168.10.254 255.255.255.0`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Gateway do servidor multicast                     |
| **Fa0/1 (Link com R02)** | `ip address 10.0.0.1 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point`     | Conexão P2P com R02                               |
| **Fa1/0 (Link com R05)** | `ip address 10.0.0.18 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point`    | Conexão P2P com R05                               |
| **OSPF**                 | `router ospf 100`<br>`router-id 1.1.1.1`<br>`network 1.1.1.1 0.0.0.0 area 0`<br>`network 10.0.0.0 0.0.0.3 area 0`<br>`network 10.0.0.16 0.0.0.3 area 0`<br>`network 192.168.10.0 0.0.0.255 area 0`                                                                                      | Configuração OSPF para conectividade unicast      |
| **Função no Auto-RP**    | **Mapping Agent (MA)**                                                      | Responsável por ouvir anúncios e distribuir o RP ativo (grupo 224.0.1.39)  | 

### 📗 R02 – Candidate RP (C-RP)

| **Seção**                | **Comando / Configuração**                                                                        | **Descrição**                                      |
|--------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **Global**               | `ip multicast-routing`                                                                            | Habilita o roteamento multicast globalmente        |
|                          | `ip pim autorp listener`                                                                | Permite escutar anúncios Auto-RP mesmo em interfaces não PIM |
|                          | `ip pim send-rp-announce Loopback0 scope 16`                                                      | Define R02 como **Candidate RP (C-RP)**            |
| **Interface Loopback0**  | `ip address 2.2.2.2 255.255.255.255`<br>`ip pim sparse-mode`                                      | Identificação e habilitação PIM                    |
| **Fa0/1 (Link com R01)** | `ip address 10.0.0.2 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Conexão P2P com R01                                |
| **Fa1/0 (Link com R03)** | `ip address 10.0.0.5 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Conexão P2P com R03                                |
| **OSPF**                 | `router ospf 100`<br>`router-id 2.2.2.2`<br>`network 2.2.2.2 0.0.0.0 area 0`<br>`network 10.0.0.0 0.0.0.3 area 0`<br>`network 10.0.0.4 0.0.0.3 area 0` | Configuração OSPF unicast |
| **Função no Auto-RP**    | **Candidate RP (C-RP)**                                                                | Envia anúncios para o grupo 224.0.1.40, oferecendo-se como RP |

### 📙 R03 – Roteador de Trânsito (PIM-SM Participant)

| **Seção**                | **Comando / Configuração**                                                                        | **Descrição**                                         |
|--------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Global**               | `ip multicast-routing`                                                                            | Habilita o roteamento multicast globalmente           |
|                          | `ip pim autorp listener`                                                                        | Permite escutar mensagens Auto-RP em interfaces não PIM |
| **Interface Loopback0**  | `ip address 3.3.3.3 255.255.255.255`<br>`ip pim sparse-mode`                                      | Identificação do roteador e ativação do PIM           |
| **Fa0/0 (Link com R04)** | `ip address 10.0.0.9 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Conexão P2P com R04                                   |
| **Fa1/0 (Link com R02)** | `ip address 10.0.0.6 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Conexão P2P com R02                                   |
| **OSPF**                 | `router ospf 100`<br>`router-id 3.3.3.3`<br>`network 3.3.3.3 0.0.0.0 area 0`<br>`network 10.0.0.4 0.0.0.3 area 0`<br>`network 10.0.0.8 0.0.0.3 area 0`   | Configuração OSPF para roteamento unicast |
| **Função no Auto-RP**    | **Participante do domínio PIM-SM**                                                  | Aprende automaticamente o RP via grupo 224.0.1.39 (Auto-RP Mapping) |

### 📒 R04 – Roteador com Receptor Multicast (Host02)

| **Seção**                | **Comando / Configuração**                                                                         | **Descrição**                                        |
|--------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------|
| **Global**               | `ip multicast-routing`                                                                             | Habilita o roteamento multicast globalmente          |
|                          | `ip pim autorp listener`                                                                           | Permite escutar anúncios Auto-RP                     |
| **Interface Loopback0**  | `ip address 4.4.4.4 255.255.255.255`<br>`ip pim sparse-mode`                                       | Identificação lógica e ativação do PIM               |
| **Fa0/0 (Link com R03)** | `ip address 10.0.0.10 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Conexão P2P com R03                                  |
| **Fa0/1 (Link com R05)** | `ip address 10.0.0.13 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Conexão P2P com R05                                  |
| **Fa1/0 (LAN Host02)**   | `ip address 192.168.20.254 255.255.255.0`<br>`ip pim sparse-mode`                              | Interface que conecta o host receptor multicast (Host02) |
| **OSPF**                 | `router ospf 100`<br>`router-id 4.4.4.4`<br>`network 4.4.4.4 0.0.0.0 area 0`<br>`network 10.0.0.8 0.0.0.3 area 0`<br>`network 10.0.0.12 0.0.0.3 area 0`<br>`network 192.168.20.0 0.0.0.255 area 0` | Configuração OSPF para conectividade completa |
| **Função no Auto-RP**    | **Participante com receptor multicast** |                          Recebe grupos via IGMP Join (Host02 – 239.1.1.1) e encaminha PIM Join em direção ao RP |

### 📕 R05 – Roteador com Host Não Inscrito (Host03)

| **Seção**               | **Comando / Configuração**                                                                            | **Descrição**                                      |
|-------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **Global**              | `ip multicast-routing`                                                                                | Habilita o roteamento multicast globalmente        |
|                         | `ip pim autorp listener`                                                                              | Permite escutar mensagens Auto-RP nas interfaces   |
| **Interface Loopback0** | `ip address 5.5.5.5 255.255.255.255`<br>`ip pim sparse-mode`                                          | Identificação do roteador e ativação do PIM        |
| **Fa0/0 (LAN Host03)**  | `ip address 192.168.30.254 255.255.255.0`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point` | Interface conectada ao Host03 (não inscrito em grupos multicast) |
| **Fa0/1 (Link com R04)** | `ip address 10.0.0.14 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point`   | Conexão P2P com R04                                |
| **Fa1/0 (Link com R01)** | `ip address 10.0.0.17 255.255.255.252`<br>`ip pim sparse-mode`<br>`ip ospf network point-to-point`   | Conexão P2P com R01                                |
| **OSPF**                 | `router ospf 100`<br>`router-id 5.5.5.5`<br>`network 5.5.5.5 0.0.0.0 area 0`<br>`network 10.0.0.12 0.0.0.3 area 0`<br>`network 10.0.0.16 0.0.0.3 area 0`<br>`network 192.168.30.0 0.0.0.255 area 0` | Configuração OSPF para conectividade total |
| **Função no Auto-RP**    | **Participante PIM-SM (sem receptor multicast)**                                     | Atua apenas como roteador de passagem; não há IGMP Join em sua LAN |

### 🖥️ SERVER – Fonte Multicast (Sender)

| **Seção**               | **Comando / Configuração**                                                | **Descrição**                                                         |
|-------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Global**              | `ip multicast-routing`                                                    | Habilita o roteamento multicast no servidor                           |
| **Fa0/0 (LAN com R01)** | `ip address 192.168.10.1 255.255.255.0`<br>`ip igmp join-group 239.1.1.1` | Interface do servidor multicast; envia tráfego para o grupo 239.1.1.1 |
| **Rota padrão**         | `ip route 0.0.0.0 0.0.0.0 192.168.10.254`                                 | Define R01 como gateway padrão (Designated Router da LAN do servidor) |
| **Função no cenário**   | **Fonte multicast (S = 192.168.10.1)**                     | Envia tráfego multicast para o grupo 239.1.1.1; origem do fluxo multicast no domínio |

### 💻 HOST02 – Receptor Multicast

| **Seção**                         | **Comando / Configuração**                                                | **Descrição**                                                        |
|-----------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Interface Fa0/0 (LAN com R04)** | `ip address 192.168.20.1 255.255.255.0`<br>`ip igmp join-group 239.1.1.1` | Host inscrito no grupo multicast 239.1.1.1 (receptor)                |
| **Rota padrão**                   | `ip route 0.0.0.0 0.0.0.0 192.168.20.254`                                 | Define R04 como gateway padrão                                       |
| **Função no cenário**             | **Receptor Multicast (Receiver)**             | Envia relatórios IGMP (Join) para o grupo 239.1.1.1, solicitando participação no fluxo multicast |

### 🖥️ HOST03 – Host Não Inscrito

| **Seção**                         | **Comando / Configuração**                | **Descrição**                                                                                       |
|-----------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Interface Fa0/0 (LAN com R05)** | `ip address 192.168.30.1 255.255.255.0`   | Host não inscrito em grupos multicast                                                               |
| **Rota padrão**                   | `ip route 0.0.0.0 0.0.0.0 192.168.30.254` | Define R05 como gateway padrão                                                                      |
| **Função no cenário**             | **Host sem participação multicast** | Serve como referência para uma rede sem receptores (verificação do comportamento do PIM-SM sem IGMP Join) |
