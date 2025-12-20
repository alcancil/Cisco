# Índice

- [Índice](#índice)
  - [09 - Exemplo Pratico - SSM (Source-Specific Multicast) e IGMP v3](#09---exemplo-pratico---ssm-source-specific-multicast-e-igmp-v3)
  - [🧾 Introdução](#-introdução)
  - [🎯 Objetivo do Laboratório](#-objetivo-do-laboratório)
  - [📚 O que você vai aprender](#-o-que-você-vai-aprender)
  - [💼 Relevância prática](#-relevância-prática)
    - [🧠 Explicação do Cenário](#-explicação-do-cenário)
    - [🌐 Do PIM-SM ao Source-Specific Multicast (SSM)](#-do-pim-sm-ao-source-specific-multicast-ssm)
    - [🧩 1️⃣ Fontes e Receptores no Cenário](#-1️⃣-fontes-e-receptores-no-cenário)
    - [🧭 Estrutura do Roteamento](#-estrutura-do-roteamento)
    - [📡 Grupos Multicast e Fontes Definidas](#-grupos-multicast-e-fontes-definidas)
    - [🧩 Conclusão](#-conclusão)
    - [🛰️ O que muda no SSM (Source-Specific Multicast)](#️-o-que-muda-no-ssm-source-specific-multicast)
      - [🌳 1️⃣ O comportamento do PIM-SSM](#-1️⃣-o-comportamento-do-pim-ssm)
      - [🔹 2️⃣ O papel do IGMPv3](#-2️⃣-o-papel-do-igmpv3)
      - [🔀 3️⃣ Como o DR encontra a fonte (S)](#-3️⃣-como-o-dr-encontra-a-fonte-s)
      - [🛰️ 4️⃣ Quando a fonte começa a transmitir](#️-4️⃣-quando-a-fonte-começa-a-transmitir)
      - [📡 5️⃣ Vantagens do SSM sobre o PIM-SM](#-5️⃣-vantagens-do-ssm-sobre-o-pim-sm)
  - [🌐 Topologia do Laboratório](#-topologia-do-laboratório)
    - [🔍 Testes Preliminares](#-testes-preliminares)
    - [🧩 Principais diferenças do SSM em relação ao PIM-SM](#-principais-diferenças-do-ssm-em-relação-ao-pim-sm)
    - [🌍 Onde o PIM deve ser ativado](#-onde-o-pim-deve-ser-ativado)
    - [💡 Observação sobre as fontes multicast](#-observação-sobre-as-fontes-multicast)
    - [🔹 Exemplo com IGMPv3](#-exemplo-com-igmpv3)
    - [⚙️ Nosso cenário SSM com IGMPv3](#️-nosso-cenário-ssm-com-igmpv3)
    - [📡 Papel do IGMPv3 no SSM](#-papel-do-igmpv3-no-ssm)
    - [🔁 Funcionamento geral do SSM](#-funcionamento-geral-do-ssm)
    - [🧱 No nosso laboratório](#-no-nosso-laboratório)
  - [⚙️ Ativando o protocolo PIM-SSM (Source-Specific Multicast)](#️-ativando-o-protocolo-pim-ssm-source-specific-multicast)
    - [🔧 Configuração do PIM-SSM](#-configuração-do-pim-ssm)
  - [🧩 Eleição do Designated Router (DR)](#-eleição-do-designated-router-dr)
  - [💬 Mensagens PIM Hello](#-mensagens-pim-hello)
    - [⚙️ Configurando o PIM-SSM (Source-Specific Multicast)](#️-configurando-o-pim-ssm-source-specific-multicast)
    - [🧩 1️⃣ Definindo o intervalo de endereços SSM](#-1️⃣-definindo-o-intervalo-de-endereços-ssm)
    - [🧭 2️⃣ Habilitando o IGMPv3 nos roteadores](#-2️⃣-habilitando-o-igmpv3-nos-roteadores)
    - [🧰 3️⃣ Associando hosts e fontes multicast](#-3️⃣-associando-hosts-e-fontes-multicast)
    - [🧪 5️⃣ Captura e análise via Wireshark](#-5️⃣-captura-e-análise-via-wireshark)
    - [🎥 Configurando os servidores simulados (senders)](#-configurando-os-servidores-simulados-senders)
      - [🟩 Server01 – Transmitindo para 232.1.1.1 e 232.2.2.2](#-server01--transmitindo-para-232111-e-232222)
    - [🟦 Server02 – Transmitindo para 231.1.1.1 e 232.2.2.2](#-server02--transmitindo-para-231111-e-232222)
    - [Realizando testes - Simulando fluxo nos servidores](#realizando-testes---simulando-fluxo-nos-servidores)
  - [🛠️ Troubleshooting](#️-troubleshooting)
  - [🧩 O que aprendemos com este laboratório (SSM + IGMPv3)](#-o-que-aprendemos-com-este-laboratório-ssm--igmpv3)
  - [🎯 Principais aprendizados](#-principais-aprendizados)
  - [💡 Conclusões gerais](#-conclusões-gerais)
  - [🗺️ Fluxo conceitual do SSM (S,G)](#️-fluxo-conceitual-do-ssm-sg)
  - [📘 Tabela de Comandos](#-tabela-de-comandos)
    - [🖥️ Função	—	R01 atua como Designated Router (DR) para a LAN dos servidores](#️-funçãor01-atua-como-designated-router-dr-para-a-lan-dos-servidores)
    - [📗 R02 – Router de Núcleo / Intermediário do Domínio SSM](#-r02--router-de-núcleo--intermediário-do-domínio-ssm)
    - [📙 R03 – DR da LAN do Host + Roteador de Trânsito no SSM](#-r03--dr-da-lan-do-host--roteador-de-trânsito-no-ssm)
    - [📒 R04 – DR da LAN do Host02 + Roteador de Trânsito no SSM](#-r04--dr-da-lan-do-host02--roteador-de-trânsito-no-ssm)
    - [📕 R05 – Roteador de Trânsito + DR da LAN do Host03](#-r05--roteador-de-trânsito--dr-da-lan-do-host03)
    - [🖥️ SERVER – Fonte Multicast (Sender)](#️-server--fonte-multicast-sender)
    - [🖥️ SERVER02 – Fonte Multicast (Sender)](#️-server02--fonte-multicast-sender)
    - [💻 HOST02 – Receptor Multicast (IGMPv3 + SSM)](#-host02--receptor-multicast-igmpv3--ssm)
    - [🖥️ HOST03 – Receptor Multicast Secundário (SSM com múltiplas fontes)](#️-host03--receptor-multicast-secundário-ssm-com-múltiplas-fontes)

## 10 - Exemplo Pratico - PIM Biderecional Multicast

## 🧾 Introdução
  
**PIM Bidirectional (BIDIR) Multicast**  
  
Este laboratório foi desenvolvido como parte do meu estudo para a certificação Cisco CCNP ENCOR (350-401).  
O objetivo é compreender, de forma prática, o funcionamento do PIM Bidirectional (BIDIR), analisando seu comportamento em cenários com múltiplas fontes e múltiplos receptores, comuns em redes corporativas e ambientes de larga escala.  

O PIM BIDIR é uma variação do PIM Sparse Mode (PIM-SM) projetada para ambientes onde diversos dispositivos atuam simultaneamente como fontes e receptores de tráfego multicast.
Diferentemente do modelo tradicional do PIM-SM, o BIDIR não realiza a transição para Shortest Path Tree (SPT). Todo o tráfego multicast é sempre encaminhado por meio de um Rendezvous Point (RP), garantindo previsibilidade e simplicidade no plano de controle.  
  
Nesse modelo, o RP deixa de ser apenas um ponto de encontro inicial e passa a ser o núcleo permanente da árvore multicast, formando uma árvore bidirecional compartilhada (*,G). Isso reduz o estado multicast na rede e torna o BIDIR especialmente eficiente para aplicações como conferências, colaboração em grupo e serviços many-to-many.
  
💡 ***Um conceito fundamental no PIM BIDIR é o Designated Forwarder (DF).***  
Ao contrário do DR tradicional, o DF é eleito por interface, com base no custo até o RP e, em caso de empate, no endereço IP do roteador. O DF é responsável por encaminhar o tráfego multicast em direção ao RP, garantindo o fluxo correto dentro da árvore bidirecional.  
  
O IGMP, normalmente em sua versão v2, é utilizado para o gerenciamento de membros nos segmentos de acesso. Diferentemente do SSM, o BIDIR não exige que os receptores especifiquem a fonte, pois o modelo é baseado no grupo multicast (*,G), e não em pares (S,G).  
  
O laboratório a seguir demonstra como configurar e validar o PIM BIDIR em roteadores Cisco, incluindo:  

- Definição de RP estático
- Associação de grupos multicast ao modo BIDIR
- Eleição e validação do Designated Forwarder (DF)
- Análise da tabela multicast e do fluxo de tráfego
- Comportamento da rede em cenários de falha de link
  
Esse estudo evidencia como o PIM BIDIR simplifica o controle multicast em ambientes complexos, ao mesmo tempo em que mantém eficiência e escalabilidade.  

## 🎯 Objetivo do Laboratório

O objetivo deste laboratório é compreender o funcionamento do PIM Bidirectional (BIDIR) e seu comportamento em cenários multicast many-to-many, onde múltiplos dispositivos podem atuar simultaneamente como fontes e receptores.  
  
Durante os testes, iremos observar:  

- Como o PIM BIDIR opera a partir de uma árvore multicast compartilhada (*,G);
- O papel do Rendezvous Point (RP) como núcleo permanente da árvore multicast, sem transição para SPT;
- A eleição e a função do Designated Forwarder (DF) em cada enlace;
- O comportamento das tabelas mroute no modelo bidirecional;
- O processo de RPF (Reverse Path Forwarding) aplicado em direção ao RP;
- E a entrega eficiente do tráfego multicast em ambientes com múltiplas fontes e múltiplos receptores.

Dessa forma, o laboratório demonstra na prática como o PIM BIDIR simplifica o controle multicast, reduz o estado de roteamento e melhora a escalabilidade em redes corporativas e de grande porte.  

## 📚 O que você vai aprender

- Como configurar PIM BIDIR com RP estático em roteadores Cisco;
- Como associar grupos multicast específicos ao modo BIDIR;
- Como funciona a eleição do Designated Forwarder (DF) baseada no custo até o RP;
- Como o tráfego multicast é sempre encaminhado pela árvore compartilhada (*,G);
- Como validar o funcionamento do BIDIR por meio de comandos show ip pim e show ip mroute;
- Como simular um ambiente many-to-many multicast em laboratório.

### 💼 Relevância prática

O **PIM BIDIR** é amplamente utilizado em ambientes onde há grande número de participantes ativos, como:  
  
- Sistemas de conferência e colaboração em grupo
- Aplicações financeiras distribuídas
- Ambientes de controle e monitoramento
- Serviços multicast corporativos de larga escala  

Por manter uma árvore única e estável, o BIDIR reduz significativamente o overhead de sinalização e o consumo de memória nos roteadores, tornando-se uma solução eficiente para redes multicast complexas.  

## 🧠 Explicação do Cenário

Como mencionado anteriormente, o cenário já possui o roteamento unicast totalmente funcional (via OSPF), permitindo que o foco do laboratório seja exclusivamente o tráfego multicast utilizando PIM Bidirectional (BIDIR).  
  
A topologia em anel foi propositalmente escolhida para facilitar a observação de:  
  
- Eleição do Designated Forwarder (DF)
- Comportamento do tráfego multicast em condições normais
- Impacto de falhas de enlace no encaminhamento multicast

![cenário](Imagens/cenario.png)  

---

Alterar daqui

---

Neste laboratório, utilizamos **cinco roteadores Cisco (R01 a R05)**, além de **três hosts simulados** (SERVER, SERVER02 e HOSTS) que representam as **fontes e receptores multicast**.  
Os hosts são configurados apenas com **endereçamento IP e IGMPv3**, sem participar de roteamento dinâmico.  
Os roteadores intermediários executam **OSPF**, garantindo a convergência e a conectividade IP entre todas as sub-redes antes da ativação do PIM-SSM.

---

### 🌐 Do PIM-SM ao Source-Specific Multicast (SSM)

Diferente do **PIM Sparse Mode tradicional (PIM-SM)**, que depende de um **Rendezvous Point (RP)** para interligar fontes e receptores, o **SSM (Source-Specific Multicast)** elimina completamente o uso de RP.  
No modelo **(S,G)**, o receptor declara explicitamente de qual **fonte (S)** deseja receber o tráfego multicast associado a um determinado **grupo (G)**.

Esse método simplifica a operação e aumenta a segurança, pois:

- Apenas as fontes autorizadas transmitem o fluxo;
- O tráfego multicast é entregue **somente** aos receptores que expressaram interesse explícito em (S,G);
- Não há necessidade de configuração manual de RP nem de mecanismos como Auto-RP ou BSR.

O **SSM** é implementado em conjunto com o **IGMPv3**, que introduz a capacidade de inscrição seletiva em fontes.  
Assim, os hosts podem escolher exatamente de quais fontes desejam receber tráfego multicast — algo impossível nas versões anteriores (IGMPv1/v2).

---

### 🧩 1️⃣ Fontes e Receptores no Cenário

Neste cenário, temos **duas fontes multicast** e **um receptor**, distribuídos nas seguintes redes:

| Função         | Dispositivo | Rede/Sub-rede        | Interface  | Endereço IP        | Descrição                                      |
|----------------|-------------|----------------------|------------|--------------------|------------------------------------------------|
| **Fonte 1**    | SERVER      | 192.168.10.0/24      | fa0/0      | 192.168.10.1       | Envia tráfego multicast para o grupo 232.1.1.1 |
| **Fonte 2**    | SERVER02    | 192.168.40.0/24      | fa0/0      | 192.168.40.1       | Envia tráfego multicast para o grupo 232.2.2.2 |
| **Receptor 1** | HOST02      | 192.168.20.0/24      | fa0/0      | 192.168.20.1       | Participa de grupos multicast via IGMPv3       |
| **Receptor 2** | HOST03      | 192.168.30.0/24      | fa0/0      | 192.168.30.1       | Participa de grupos multicast via IGMPv3       |
| **Receptor 3** | (opcional)  | —                    | —          | —                  | Pode ser adicionado em qualquer outra sub-rede |

---

### 🧭 Estrutura do Roteamento

Todos os roteadores (R01 a R05) fazem parte de uma **única área OSPF (Área 0)**, garantindo o roteamento unicast completo antes da ativação do PIM.  
As redes de backbone e interconexão seguem o seguinte mapeamento:

| Link Ponto-a-Ponto | Rede / Máscara | Interface Local | Interface Remota |
|--------------------|----------------|-----------------|------------------|
| R01 – R02          | 10.0.0.0/30    | Fa0/1 (R01)     | Fa1/0 (R02)      |
| R02 – R03          | 10.0.0.4/30    | Fa1/0 (R02)     | Fa1/0 (R03)      |
| R03 – R04          | 10.0.0.8/30    | Fa0/0 (R03)     | Fa0/0 (R04)      |
| R04 – R05          | 10.0.0.12/30   | Fa0/1 (R04)     | Fa0/1 (R05)      |
| R05 – R01          | 10.0.0.16/30   | Fa1/0 (R05)     | Fa1/0 (R01)      |

---

### 📡 Grupos Multicast e Fontes Definidas

No SSM, cada receptor escolhe explicitamente a fonte de interesse, conforme a tabela abaixo:

| Grupo Multicast | Fonte (S)        | Descrição                                   | Receptores Interessados      |
|-----------------|------------------|---------------------------------------------|------------------------------|
| 232.1.1.1       | 192.168.10.1     | Tráfego multicast gerado pelo SERVER        | HOST02 e HOST03              |
| 232.2.2.2       | 192.168.40.1     | Tráfego multicast gerado pelo SERVER02      | HOST02 (exemplo)             |

Dessa forma, o domínio PIM forma **árvores diretas (Shortest Path Trees)** de cada receptor até sua fonte específica, eliminando qualquer dependência de RP.

---

### 🧩 Conclusão

Com esse modelo, o laboratório demonstra como o **SSM e IGMPv3** tornam o roteamento multicast mais previsível, seguro e escalável.  
A eliminação do RP e o uso explícito de (S,G) simplificam o controle de fluxos, tornando o ambiente ideal para **streaming, replicação de dados e aplicações em tempo real**.

### 🛰️ O que muda no SSM (Source-Specific Multicast)

Diferente do modelo **PIM Sparse Mode tradicional (PIM-SM)**, que depende de um **Rendezvous Point (RP)** para conectar fontes e receptores, o **SSM (Source-Specific Multicast)** elimina totalmente a necessidade de um ponto central de encontro.  

No SSM, o receptor informa explicitamente **qual fonte (S)** deseja ouvir, junto com o **grupo multicast (G)** — formando o par **(S,G)**.  
Isso simplifica o roteamento multicast e aumenta a segurança, já que **somente fluxos de fontes autorizadas** são encaminhados.  

Em outras palavras:

- O receptor diz: “quero receber o grupo **G = 232.1.1.1** vindo da fonte **S = 192.168.10.1**”;  
- O roteador local cria a rota (S,G) e forma a **árvore de distribuição direta (Shortest Path Tree)** até a fonte;  
- Nenhum RP, BSR ou Auto-RP é necessário.  

---

#### 🌳 1️⃣ O comportamento do PIM-SSM

O **PIM-SSM** segue o mesmo princípio de economia de banda do PIM-SM: **somente interfaces com receptores interessados** participam da árvore multicast.  
A diferença é que o **SSM trabalha sempre em modo por fonte (S,G)** — sem precisar construir árvores compartilhadas (*,G).  

Assim, o PIM inicia diretamente o caminho entre o receptor e a fonte específica, garantindo:

- **Baixa latência** (sem RP intermediário);  
- **Caminho otimizado** (SPT desde o início);  
- **Menos processamento e estado multicast** nos roteadores.  

---

#### 🔹 2️⃣ O papel do IGMPv3

O **IGMPv3** é essencial para o funcionamento do **SSM**.  
Ele introduz o conceito de **inscrição seletiva**, permitindo que um host indique explicitamente de qual fonte deseja receber o tráfego multicast.  

O processo funciona assim:

1. O host envia uma mensagem **IGMPv3 Membership Report**, informando o par **(S,G)** de interesse;  
2. O roteador diretamente conectado ao host (conhecido como **Designated Router – DR**) registra esse interesse;  
3. O DR, por sua vez, envia uma mensagem **PIM Join (S,G)** diretamente em direção à fonte **S**, utilizando a rota unicast normal para encontrá-la.  

Dessa forma, a árvore multicast é formada de forma **direta, seletiva e eficiente**.  

---

#### 🔀 3️⃣ Como o DR encontra a fonte (S)

No modelo SSM, **não há descoberta de RP** nem mensagens Bootstrap.  
O **Designated Router (DR)** usa sua **tabela de roteamento unicast** (aprendida via OSPF, no caso deste laboratório) para alcançar a fonte.  

Quando o DR recebe um pedido IGMPv3 indicando:

```ios
(S,G) = (192.168.10.1, 232.1.1.1)
```

ele simplesmente consulta sua rota para `192.168.10.1` e envia o **PIM Join (S,G)** seguindo esse caminho.  
Os roteadores intermediários criam entradas **(S,G)** em suas tabelas multicast, estabelecendo o caminho reverso até a fonte.  

---

#### 🛰️ 4️⃣ Quando a fonte começa a transmitir

Quando a fonte — por exemplo, o servidor `192.168.10.1` — envia pacotes multicast para `232.1.1.1`, os roteadores no caminho reconhecem o fluxo e o associam à árvore (S,G) existente.  
Os receptores que solicitaram esse fluxo começam imediatamente a receber os pacotes.  

Não há necessidade de registros, mensagens encapsuladas ou intermediação por RP.  
Todo o processo é **automático e direto**, pois o **PIM-SSM** já conhece exatamente quem é a fonte e quem são os receptores interessados.  

---

#### 📡 5️⃣ Vantagens do SSM sobre o PIM-SM

| Aspecto                     | PIM Sparse Mode (tradicional)        | Source-Specific Multicast (SSM)           |
|-----------------------------|--------------------------------------|-------------------------------------------|
| Dependência de RP           | Sim                                  | ❌ Não                                   |
| Tipo de árvore inicial      | Compartilhada (*,G)                  | Direta (S,G)                              |
| Controle sobre as fontes    | Limitado                             | Total — receptor escolhe a fonte          |
| Mensagens adicionais        | PIM Register, Bootstrap, RP-Adv      | Nenhuma (apenas PIM Join/Prune)           |
| Versão IGMP necessária      | IGMPv2                               | IGMPv3                                    |
| Segurança e escalabilidade  | Moderada                             | Alta — menos estados e fluxos indevidos   |

---

👉 **Resumo:**  
O **SSM (Source-Specific Multicast)** representa a evolução natural do multicast em redes IP.  
Ele remove completamente a complexidade do RP e do BSR, simplificando a operação e melhorando o desempenho.  
Em conjunto com o **IGMPv3**, o SSM fornece uma arquitetura **mais segura, previsível e escalável** — ideal para **aplicações de streaming, replicação de dados e videoconferência**.

## 🌐 Topologia do Laboratório

A topologia deste laboratório é composta por **cinco roteadores principais (R01 a R05)** e **quatro hosts simulados (Server, Server02, Host02 e Host03)**.  
Os hosts são roteadores Cisco configurados de forma simplificada, apenas com IP e participação em grupos multicast via IGMPv3, simulando o comportamento de dispositivos finais.  

O protocolo **OSPF** garante a conectividade unicast entre todos os roteadores, enquanto o **PIM-SSM (Source-Specific Multicast)** é utilizado para o roteamento multicast.  
Diferente dos modos Dense ou Sparse tradicionais, o **SSM elimina completamente a necessidade de um RP (Rendezvous Point)**.  
Neste modelo, o tráfego multicast é estabelecido diretamente entre **fonte (S)** e **receptor (G)**, criando pares (S,G) sem passar por um ponto central de encontro.  

---

**🔧 Endereçamento e Funções**  

| **Dispositivo**   | **Interface** | **Endereço IP / Máscara Rede** | **Conexão / Função**                                            |
|-------------------|---------------|--------------------------------|-----------------------------------------------------------------|
| **R01**           | Loopback0     | 1.1.1.1 /32                    | Identificação / Router-ID OSPF                                  |
|                   | Fa0/0         | 192.168.10.254 /24             | LAN do Server — Gateway multicast                               |
|                   | Fa0/1         | 10.0.0.1 /30                   | Link com R02 — PIM + OSPF                                       |
|                   | Fa1/0         | 10.0.0.18 /30                  | Link com R05 — PIM + OSPF                                       |
| **R02**           | Loopback0     | 2.2.2.2 /32                    | Identificação / Router-ID OSPF                                  |
|                   | Fa0/0         | 10.0.0.2 /30                   | Link com R01 — PIM + OSPF                                       |
|                   | Fa1/0         | 10.0.0.5 /30                   | Link com R03 — PIM + OSPF                                       |
| **R03**           | Loopback0     | 3.3.3.3 /32                    | Identificação / Router-ID OSPF                                  |
|                   | Fa0/0         | 10.0.0.6 /30                   | Link com R02 — PIM + OSPF                                       |
|                   | Fa1/0         | 10.0.0.9 /30                   | Link com R04 — PIM + OSPF                                       |
| **R04**           | Loopback0     | 4.4.4.4 /32                    | Identificação / Router-ID OSPF                                  |
|                   | Fa0/0         | 10.0.0.10 /30                  | Link com R03 — PIM + OSPF                                       |
|                   | Fa1/0         | 10.0.0.13 /30                  | Link com R05 — PIM + OSPF                                       |
|                   | Fa1/1         | 192.168.20.254 /24             | LAN do Host02 — Gateway multicast                               |
| **R05**           | Loopback0     | 5.5.5.5 /32                    | Identificação / Router-ID OSPF                                  |
|                   | Fa0/0         | 10.0.0.14 /30                  | Link com R04 — PIM + OSPF                                       |
|                   | Fa1/0         | 10.0.0.17 /30                  | Link com R01 — PIM + OSPF                                       |
|                   | Fa0/1         | 192.168.30.254 /24             | LAN do Host03 — Gateway multicast                               |
| **Server**        | Fa0/0         | 192.168.10.1 /24               | Fonte multicast (sender)                                        |
| **Server02**      | Fa0/0         | 192.168.40.1 /24               | Fonte multicast (sender)                                        |
| **Host02**        | Fa0/0         | 192.168.20.1 /24               | Receptor multicast                                              |
| **IGMPv3 joins:** | 01            | -                              | (192.168.10.1, 231.1.1.1) — fluxo do Server                     |
| **IGMPv3 joins:** | 01            | -                              | (192.168.10.1, 231.2.2.2) — fluxo do Server02                   |
| **Host03**        | Fa0/0         | 192.168.30.1 /24               | Receptor multicast                                              |
| **IGMPv3 joins:** | 01            | -                              | (192.168.10.1, 232.1.1.1) — fluxo do Server                     |
| **IGMPv3 joins:** | 01            | -                              | (192.168.10.1, 232.2.2.2) — fluxo do Server02                   |

**OBS:** como o SSM com IGMPv3 aceita múltiplas fontes, então aqui vamos simular que os **Host02 e Hos03** vão receber 02 fluxos cada, 1 de cada Server.

🎯 Intervalo Oficial de Endereços SSM (RFC 4607)

O Source-Specific Multicast (SSM) utiliza um intervalo de endereços multicast exclusivo e padronizado pelo IETF:  

> 232.0.0.0/8

Esse bloco — **também chamado de 232/8** — é reservado **exclusivamente para operações SSM** e deve ser utilizado sempre que o ambiente suportar **IGMPv3/PIM-SSM**. Ao usar esse intervalo, garantimos total conformidade com a RFC 4607, interoperabilidade entre fabricantes e comportamento previsível no roteamento multicast.  
Por esse motivo, neste laboratório adotaremos os grupos:  

- **232.1.1.1 para o Server01**
- **232.2.2.2 para o Server02**

📌 **Intervalo oficial do SSM (RFC 4607)**  

| Descrição               | Endereço        |
|-------------------------|-----------------|
| Início do intervalo SSM | 232.0.0.0       |
| Fim do intervalo SSM    | 232.255.255.255 |
| Máscara / Notação       | 232.0.0.0/8     |

Esses endereços atendem às boas práticas e refletem corretamente o funcionamento do SSM baseado em IGMPv3.  
  
---

**🧭 Resumo da Lógica**  

- O **Server (192.168.10.1)** é a **fonte multicast** (S) e envia tráfego para o grupo **232.1.1.1 (G)**.  
- O **Server02 (192.168.40.1)** é a **fonte multicast02** (S) e envia tráfego para o grupo **232.2.2.2 (G)**.
- O **Host02 (192.168.20.1)** participa utilizando **IGMPv3**, solicitando explicitamente os fluxos **(192.168.10.1, 232.1.1.1)** e **(192.168.40.1, 232.2.2.2)**.  
- O **Host03 (192.168.30.1)** participa utilizando **IGMPv3**, solicitando explicitamente os fluxos **(192.168.10.1, 232.2.2.2)** e **(192.168.40.1, 232.2.2.2)**.  
- O protocolo **PIM-SSM** é ativado em todas as interfaces participantes do domínio multicast (LANs e links de roteamento).  
- Os **roteadores não utilizam RP nem BSR**, pois no SSM o DR do receptor envia diretamente o **PIM Join (S,G)** na direção da fonte.  
- O **RPF (Reverse Path Forwarding)** assegura que o caminho de retorno até a fonte siga o melhor trajeto aprendido via OSPF.  

Assim, o laboratório demonstra a operação do **Source-Specific Multicast**, onde o encaminhamento multicast é estabelecido **somente entre fonte e receptor interessados**, sem dependência de mecanismos centralizados de controle.

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
Lembre-se: o **PIM-SSM** depende de uma **base unicast funcional** para realizar o **RPF check**.

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
Repita esse processo de R01 a R05, garantindo que todas as interfaces de roteamento participem do domínio **PIM-SSM**.  

---

### 🧩 Principais diferenças do SSM em relação ao PIM-SM

| Característica                    | PIM Sparse Mode (SM)                              | PIM Source-Specific Multicast (SSM)                  |
|-----------------------------------|---------------------------------------------------|------------------------------------------------------|
| Tipo de árvore                    | (*,G) e (S,G)                                     | Somente (S,G)                                        |
| Necessita de RP?                  | ✅ Sim                                           | ❌ Não                                               |
| Mecanismo de descoberta de fontes | RP/BSR (ou Auto-RP)                               | IGMPv3 (relato direto do receptor sobre a fonte)     |
| Complexidade de configuração      | Maior (eleição de RP, failover, distribuição)     | Menor (sem RP, sem Bootstrap)                        |
| Tempo de convergência             | Moderado                                          | Muito rápido — a árvore é criada direto com a fonte  |

---

### 🌍 Onde o PIM deve ser ativado

No modo **Source-Specific Multicast (PIM-SSM)**, o tráfego multicast é encaminhado **somente para receptores que solicitam explicitamente uma fonte e um grupo multicast** — ou seja, o modelo baseia-se na relação **(S,G)**, onde **S = Source** e **G = Group**.  
  
Diferente do **PIM-SM tradicional**, o SSM **não utiliza Rendezvous Point (RP)** nem Bootstrap Router (BSR).  
O roteamento multicast é direto entre os receptores e as fontes conhecidas, simplificando o domínio multicast e eliminando pontos de falha.

Embora o SSM dispense RP e Bootstrap, o PIM ainda precisa ser **ativado nas interfaces que participam do encaminhamento multicast**, garantindo que as mensagens PIM **Join/Prune** sejam trocadas corretamente entre roteadores.  

✅ **Ative o PIM Sparse Mode (modo SSM)** nas seguintes interfaces:

| Situação                           | PIM deve ser ativado? | Motivo                                                                 |
|------------------------------------|-----------------------|------------------------------------------------------------------------|
| Interface entre roteadores         | ✅ Sim               | Necessário para formar adjacências PIM e propagar as árvores (S,G)     |
| Interface com host receptor (IGMP) | ✅ Sim               | Permite ao DR receber IGMPv3 Reports com a fonte específica            |
| Interface com fonte multicast      | ✅ Sim               | O DR da fonte inicia o fluxo multicast diretamente para os receptores  |
| Loopback apenas como Router-ID     | ⚙️ Opcional          | Pode ser omitido, usada apenas para identificação OSPF                 |
  
---

### 💡 Observação sobre as fontes multicast

No SSM, as **fontes (senders)** não precisam registrar-se em nenhum RP.  
O tráfego flui diretamente das interfaces onde as fontes estão localizadas para as interfaces com receptores que enviaram *IGMPv3 Reports* solicitando explicitamente aquele fluxo.  

Isso elimina a dependência de mecanismos como **Register/Join** e simplifica o plano de controle multicast.  
  
Em um ambiente SSM (Source-Specific Multicast), o receptor não apenas informa o grupo multicast (G) que deseja receber, mas também as fontes específicas (S) das quais aceita tráfego.  
Essa característica é o que diferencia o IGMPv3 das versões anteriores, permitindo o chamado Source Filtering.  
  
No caso deste laboratório, há duas fontes ativas — SERVER e SERVER02 — enviando tráfego simultaneamente, ambas destinadas, por exemplo, ao mesmo grupo multicast **239.1.1.1**.  
  
Cada receptor pode então escolher:

- **Ouvir somente uma das fontes** (por exemplo, apenas o SERVER);
- **Ouvir as duas fontes simultaneamente** (SERVER e SERVER02);
- **Ou filtrar fontes indesejadas, mesmo que transmitam no mesmo grupo**.  
  
### 🔹 Exemplo com IGMPv3

Se o Host02 quiser receber tráfego das duas fontes, ele enviará um IGMPv3 Membership Report com dois pares (S,G):  

| Fonte (S)    | Grupo (G) | Descrição                     |
|--------------|-----------|-------------------------------|
| 192.168.10.1 | 232.1.1.1 | Fluxo proveniente do SERVER   |
| 192.168.40.1 | 232.2.2.2 | Fluxo proveniente do SERVER02 |

O roteador conectado ao **Host02 (o Designated Router)** registra ambos os pares e aciona o processo PIM-SSM, construindo **duas árvores independentes (S,G)** — uma para cada fonte.  
Dessa forma, o tráfego chega de cada servidor por caminhos otimizados, conforme o **RPF (Reverse Path Forwarding) determinado pelo OSPF.**  
  
💡 **Em resumo:**  
O SSM com IGMPv3 oferece controle total ao receptor sobre quais fontes deseja ouvir, permitindo topologias com múltiplos senders e eliminando completamente a dependência de um Rendezvous Point (RP).  

🎯 **Situação**

Você tem:  

- Server01 (192.168.10.10) transmitindo para o grupo **232.1.1.1**
- Server02 (192.168.40.10) transmitindo também **para o mesmo grupo 232.2.2.2 (ou pode ser outro, não importa)**
- Host01 quer receber **os dois fluxos multicast, um de cada servidor**.

🧠 **Como o SSM trata isso?**  

O **IGMPv3** trabalha com a relação **(S,G) — Source e Group.**  
Isso significa que cada fonte representa um fluxo separado, mesmo que **o grupo (G) seja o mesmo**.  
  
Então o Host01 vai enviar **dois IGMPv3 Reports**, um para cada fonte, assim:  

| Fluxo | Fonte (S)               | Grupo (G)  | Tipo de IGMPv3 Report |
|-------|-------------------------|------------|-----------------------|
| 1️⃣   | 192.168.10.10 (Server01) | 232.1.1.1  | INCLUDE (S,G)         |
| 2️⃣   | 192.168.40.10 (Server02) | 232.2.2.2  | INCLUDE (S,G)         |

🔁 **O que acontece no roteador (Designated Router)**  

- O roteador conectado ao Host01 recebe dois IGMPv3 Reports.
- Ele cria duas entradas separadas na sua tabela de multicast:
  - **(192.168.10.10, 232.1.1.1)**
  - **(192.168.40.10, 232.2.2.2)**
- O roteador envia duas mensagens **PIM Join (S,G)** em direção a cada fonte.
- **Duas árvores independentes (S,G)** são criadas — uma para cada fonte.
- O tráfego de ambas as fontes chega até o Host01, misturado no mesmo **grupo multicast (G), mas com origem diferente (S)**.

🔎 **Visualmente:**  

```text
         (S1,G) 192.168.10.10 → 232.1.1.1
         (S2,G) 192.168.40.10 → 232.2.2.2
               │
               ▼
          [Roteador DR]
               │
               ▼
             [Host01]
```
  
O Host01 vai receber dois fluxos simultâneos:  

- Um vindo da árvore (192.168.10.10, 232.1.1.1)
- Outro vindo da árvore (192.168.40.10, 232.2.2.2)

🧩 **E se o Host01 quiser apenas uma das fontes?**

Ele simplesmente envia um único IGMPv3 Report:  

```ios
INCLUDE { 232.1.1.1 : 192.168.10.10 }
```

🚫 **E se ele quiser bloquear uma das fontes?**

O IGMPv3 permite o **EXCLUDE mode**, em que o host pode dizer:  
  
> “Quero o grupo 232.1.1.1, mas exclua o tráfego vindo de 192.168.40.10.”

Isso é útil em cenários de redundância (duas fontes transmitindo o mesmo conteúdo).  
Mas no nosso laboratório, normalmente usamos **INCLUDE** mode, porque é o padrão simples do SSM.  

💬 **Resumo final**  

| Caso                      | IGMPv3 Report                                                      | Resultado                           |
|---------------------------|--------------------------------------------------------------------|-------------------------------------|
| Host quer apenas Server01 | INCLUDE { 232.1.1.1 : 192.168.10.10 }                              | Recebe só o fluxo do Server01       |
| Host quer apenas Server02 | INCLUDE { 232.2.2.2 : 192.168.40.10 }                              | Recebe só o fluxo do Server02       |
| Host quer os dois         | INCLUDE { (232.1.1.1, 192.168.10.10), (232.2.2.2, 192.168.40.10) } | Recebe ambos os fluxos              |
| Host quer excluir um      | EXCLUDE { 232.1.1.1 : 192.168.40.10 }                              | Recebe o grupo, mas ignora Server02 |

👉 **Em resumo:**

- No SSM, cada (S,G) é uma sessão multicast independente.
- O receptor pode selecionar, combinar ou excluir fontes de forma totalmente controlada, e o roteador cria uma árvore separada por fluxo (S,G).

### ⚙️ Nosso cenário SSM com IGMPv3

Nosso laboratório foi expandido para incluir **duas fontes multicast distintas**:

| Fonte       | Roteador conectado | Sub-rede             | Grupo multicast utilizado (exemplo)  |
|-------------|--------------------|----------------------|--------------------------------------|
| **SERVER**  | R01                | 192.168.10.0/24      | 232.1.1.1                            |
| **SERVER02**| R03                | 192.168.40.0/24      | 232.2.2.2                            |

Os receptores multicast (hosts simulados) enviam **mensagens IGMPv3** especificando exatamente qual fonte desejam escutar.  
Por exemplo, um host pode ingressar no grupo `232.1.1.1` proveniente de `192.168.10.10`, enquanto outro pode escutar o grupo `232.2.2.2` proveniente de `192.168.40.10`.

---

### 📡 Papel do IGMPv3 no SSM

O **IGMPv3** é fundamental para o funcionamento do SSM, pois ele introduz o conceito de **Source Filtering**, permitindo que um receptor defina **quais fontes deseja (INCLUDE mode)** ou **quais não deseja (EXCLUDE mode)**.  

No nosso caso, todos os receptores utilizam **INCLUDE mode**, ou seja, solicitam explicitamente o fluxo multicast de uma ou mais fontes conhecidas.

| Tipo de Mensagem                | Descrição                                                                        |
|---------------------------------|----------------------------------------------------------------------------------|
| **Membership Report (INCLUDE)** | Informa ao roteador local (Designated Router) o grupo e a(s) fonte(s) desejadas. |
| **Leave Group**                 | Indica que o host não quer mais receber o tráfego daquele grupo/fonte.           |

---

### 🔁 Funcionamento geral do SSM

1. O **receptor** envia um **IGMPv3 Report** informando o grupo e a fonte (S,G) desejada.  
2. O roteador de borda (Designated Router) cria a árvore SSM diretamente para a fonte — **sem RP**.  
3. O tráfego multicast é encaminhado da **fonte** ao **receptor** pela árvore (S,G).  
4. Se o receptor deixar o grupo, o roteador envia **PIM Prune (S,G)**, encerrando o fluxo.  

---

### 🧱 No nosso laboratório

O SSM será ativado em todos os roteadores e interfaces relevantes:

- **Entre os roteadores R01 a R05**, formando o domínio PIM-SSM;  
- **Nas interfaces LAN** conectadas às fontes multicast (**Server** e **Server02**);  
- **Nas interfaces LAN** conectadas aos receptores (Host02 e Host03);  
- **Nas Loopbacks**, apenas como *Router-ID* para OSPF (sem necessidade de PIM).  

Com isso, teremos um domínio totalmente funcional de **PIM-SSM com IGMPv3**, suportando múltiplas fontes e fluxos multicast independentes, sem depender de RP, Bootstrap ou Auto-RP.

---

🧩 **Resumo prático**

| Elemento                     | Função no cenário                                |
|------------------------------|--------------------------------------------------|
| **Server (192.168.10.10)**   | Fonte multicast principal (grupo 232.1.1.1)      |
| **Server02 (192.168.40.10)** | Segunda fonte multicast (grupo 232.2.2.2)        |
| **Host02 / Host03**          | Receptores multicast (enviam IGMPv3 Reports)     |
| **Roteadores R01–R05**       | Encaminham tráfego multicast via PIM-SSM         |
| **OSPF**                     | Mantém conectividade unicast entre os roteadores |
| **Sem RP / Sem BSR**         | O SSM elimina esses componentes completamente    |

---

💬 **Conclusão**

O uso de **SSM com IGMPv3** traz uma abordagem mais simples, escalável e segura para multicast.  
Cada receptor escolhe exatamente **de qual fonte** receberá o tráfego, eliminando a necessidade de RP, reduzindo o overhead de controle e tornando o comportamento multicast totalmente determinístico.

## ⚙️ Ativando o protocolo PIM-SSM (Source-Specific Multicast)

Com o ambiente unicast devidamente funcional e as bases teóricas sobre o **SSM e o IGMPv3** já estabelecidas, é hora de ativar o **PIM-SSM** nos roteadores do domínio multicast.  
O objetivo agora é permitir que cada receptor solicite fluxos específicos com base nas **fontes (S)** de interesse, sem depender de **Rendezvous Points (RP)** nem de mensagens Bootstrap.

Diferente do modelo anterior (PIM-SM com Bootstrap), o SSM é totalmente **direcionado por demanda**: o tráfego multicast só é estabelecido quando o receptor envia um **IGMPv3 Membership Report (S,G)** informando explicitamente de qual servidor deseja receber.

---

### 🔧 Configuração do PIM-SSM

O PIM precisa ser habilitado em todas as interfaces que transportarão tráfego multicast, tanto nas **LANs com fontes e receptores**, quanto nos **links entre roteadores**.

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

Após a configuração, o roteador passa a participar ativamente do domínio multicast, trocando mensagens PIM Hello e identificando vizinhos diretamente conectados.  
  
**OBS:** fazer isso para todos os ROTEADORES (de R01 a R05).  
  
✅ **Verificação do roteamento multicast**
  
Para confirmar que o roteamento multicast está operacional:  

```ios
R01#show ip multicast
  Multicast Routing: enabled
  Multicast Multipath: disabled
  Multicast Route limit: No limit
  Multicast Triggered RPF check: enabled
  Multicast Fallback group mode: Sparse
  Multicast DVMRP Interoperability: disabled
```

E a tabela de rotas multicast:  

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

💡 **Dica:**
Em um domínio **S**SM, as entradas (S,G)** só aparecerão quando um **host IGMPv3** manifestar interesse em uma fonte específica.  
Não existem mensagens **Bootstrap, nem anúncios de RP.** O controle é completamente descentralizado e guiado pelas solicitações **IGMPv3 dos receptores.**  
  
## 🧩 Eleição do Designated Router (DR)

O **Designated Router (DR)** é o roteador responsável por interagir com os hosts de uma **LAN multicast.**  
Ele recebe os relatórios IGMPv3, interpreta os pares (S,G) e envia mensagens PIM Join diretamente em direção à fonte indicada.  
A eleição do DR acontece automaticamente entre os roteadores PIM conectados à mesma rede local.  

**Critérios de eleição:**

- O roteador com o maior endereço IP ativo na LAN é eleito DR;
- Se ele falhar, outro roteador assume o papel após o timeout dos Hellos (30 segundos, por padrão).

💡 **Essa eleição ocorre de forma transparente, sem necessidade de configuração manual.**

## 💬 Mensagens PIM Hello

As mensagens **PIM Hello** são o primeiro passo para o estabelecimento de vizinhanças PIM.  
Elas são enviadas periodicamente no grupo **224.0.0.13 (PIM Routers) com TTL 1,** e permitem que os roteadores descubram vizinhos ativos, negociem parâmetros e mantenham a topologia multicast estável.  
  
Essas mensagens também informam o modo de operação **(SSM)**, a prioridade do DR e o holdtime de vizinhança.  

⚙️ **Funções principais das mensagens Hello**  

| **Função**                 | **Descrição**                                                                          |
|----------------------------|------------------------------------------------------------------------------------|
| **Descoberta de vizinhos** | Roteadores PIM trocam Hellos para identificar dispositivos ativos na mesma LAN.    |
| **Troca de parâmetros**    | Define tempo de expiração, prioridade de DR e modo de operação.                    |
| **Monitoramento**          | Se um vizinho deixa de enviar Hellos dentro do holdtime, é removido da tabela PIM. |

---

🧩 **Estrutura simplificada da mensagem Hello**  

| Campo          | Função                                                  | Valor típico |
|----------------|---------------------------------------------------------|--------------|
| Type           | Tipo da mensagem PIM (Hello = 0x00)                     | 0x00         |
| Holdtime       | Tempo máximo de inatividade antes da remoção do vizinho | 105 s        |
| DR Priority    | Prioridade do Designated Router (maior vence)           | 1 (padrão)   |
| Generation ID  | Valor aleatório que muda a cada boot                    | Aleatório    |
| Hello Interval | Tempo entre Hellos consecutivos                         | 30 s         |

💡 **Dica:**
Use o Wireshark com o filtro **pim.type == 0** para observar essas mensagens em tempo real.  
  
🔍 **Exemplo de log da eleição do DR**

Logo após ativar o PIM-SSM, o log do roteador mostrará a eleição automática do Designated Router:  

```ios
*Mar  1 02:00:36.563: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.18 on interface FastEthernet1/0
```
  
👉 Isso indica que o roteador 10.0.0.18 foi eleito DR na interface FastEthernet1/0, responsável por processar os relatórios IGMPv3 dos hosts.  
  
👏 **Mas ainda existe eleição do DR?**  

👉 Sim, o PIM-SSM (Source-Specific Multicast) ainda tem eleição de Designated Router (DR) — mas com uma diferença importante no papel funcional dele.  

Vamos detalhar didaticamente:  

- ⚙️ O DR existe no SSM, mas faz menos coisas que no PIM-SM
- Mesmo no SSM, quando há mais de um roteador conectado à mesma LAN multicast, o protocolo PIM precisa eleger um único roteador responsável por representar aquela LAN.
- Esse roteador eleito é o Designated Router (DR).
  
🔹 **Por que ele ainda é necessário?**

Porque o DR é quem recebe os relatórios **IGMPv3 (Membership Reports)** dos hosts na LAN e toma as decisões iniciais de multicast:

- Ele interpreta os pares (S,G) recebidos dos hosts;
- Gera as entradas correspondentes na tabela multicast;
- E envia mensagens PIM Join (S,G) diretamente em direção à fonte (S).

📊 **Diferença prática entre PIM-SM e PIM-SSM quanto ao DR**  

| Função                          | PIM Sparse Mode (com RP)                 | PIM-SSM (com IGMPv3)           |
|---------------------------------|------------------------------------------|--------------------------------|
| Receber IGMP                    | Sim                                      | Sim                            |
| Enviar PIM Join                 | Sim — mas em direção ao RP               | Sim — direto para a fonte (S)  |
| Enviar PIM Register             | Sim — envia registros encapsulados ao RP | ❌ Não existe registro no SSM  |
| Descobrir RP / BSR              | Sim                                      | ❌ Não aplicável               |
| Participa na árvore (*,G)       | Sim                                      | ❌ Só (S,G)                    |
| Eleição entre roteadores na LAN | Sim                                      | Sim                            |

💡 **Resumo prático**  
  
Mesmo no SSM, quando há dois ou mais roteadores em uma mesma LAN (por exemplo, R1 e R2 ligados ao mesmo segmento onde está o Host01), um deles precisa ser o DR.
Isso evita que múltiplos roteadores enviem PIM Joins duplicados para a mesma fonte.  

➡️ Portanto:

- O processo de eleição do DR permanece igual: **o roteador com maior IP ativo vence**;
- O tráfego de eleição usa as **mesmas mensagens PIM Hello com o campo DR Priority**;
- A diferença é que o DR não interage com RP, e sim diretamente com as fontes informadas nos **relatórios IGMPv3**.  
  
🧭 **Conclusão**  
  
- O DR existe e é eleito automaticamente no PIM-SSM.
- Mas ele não envia PIM Register nem usa RP/BSR.
- Sua única função é processar IGMPv3 dos hosts locais e iniciar os PIM Join (S,G) diretamente em direção à fonte.

### ⚙️ Configurando o PIM-SSM (Source-Specific Multicast)

Agora que o **PIM** está ativo em todas as interfaces, podemos configurar o domínio multicast para operar em **Source-Specific Multicast (SSM)** — modo no qual **não há Rendezvous Point (RP)** nem mensagens Bootstrap.  
O tráfego multicast flui diretamente da **fonte (S)** para os **receptores interessados (G)**, conforme indicado pelas mensagens **IGMPv3**.

Diferente do **PIM Sparse Mode tradicional (PIM-SM)**, que utiliza RPs para coordenar o fluxo, o **SSM** utiliza **pares (*S,G*)** formados dinamicamente, garantindo simplicidade, segurança e menor dependência de controle.

---

### 🧩 1️⃣ Definindo o intervalo de endereços SSM

Por padrão, as redes Cisco utilizam o intervalo **232.0.0.0/8** para o **Source-Specific Multicast (SSM)**, conforme definido pelo IANA (RFC 4607).  
Ainda assim, é boa prática **declarar explicitamente o range SSM** para evitar ambiguidade entre grupos tradicionais (*,G*) e específicos (*S,G*).

➡️ **Comando no modo global:**

- Primeiro devemos definir o range do intervalo multicast a ser utilizado:

```ios
R01(config)#access-list 10 permit 232.0.0.0 255.0.0.0
```

- Depois precisamos aplicar o range no comando:

```ios
R01(config)#ip pim ssm ?
  default  Use 232/8 group range for SSM
  range    ACL for group range to be used for SSM

R01(config)#ip pim ssm range 10
R01(config)#
```

⚠️ **Observação Importante — Limitação do IOS 12.4 com Wildcards Grandes**
  
No IOS clássico (como o 12.4) existe uma limitação conhecida no parser de **ACLs STANDARD:**  

- wildcards muito amplos, como **255.0.0.0**, fazem o roteador zerar o endereço base, exibindo:

```ios
permit 0.0.0.0 255.0.0.0
```

Isso não representa corretamente o bloco **232/8** e não deve ser usado em laboratórios que dependem de SSM.  
  
💡 **Solução recomendada para o IOS 12.4:**
Defina explicitamente apenas os grupos SSM usados no laboratório, evitando wildcards extensos.

Exemplo:

```ios
ip access-list standard SSM-RANGE
 permit 232.1.1.1
 permit 232.2.2.2
!
ip pim ssm range SSM-RANGE
```

Assim, o SSM funciona corretamente e evita que o roteador degrade a ACL para 0.0.0.0 255.0.0.0, comportamento normal do IOS mais antigo.  

---

💡 **Explicação:**  

- O **access-list** define o bloco de endereços que será tratado como SSM;
- Qualquer grupo dentro de **232.0.0.0/8** será gerenciado sem RP;
- Como é mostrado na saída, é possível se utilizar outro tipo de range dentro do multicast, porém se estiver fora do range **232/8** estaremos fora da **RFC 4607** que não é uma boa prática
- Isso permite que o roteador processe **joins específicos (S,G) vindos via IGMPv3**.

⚠️ **Observação importante sobre ip pim ssm-range no IOS**  
  
No **IOS clássico (12.x e 15.x)**, o comando ip pim ssm-range não aceita diretamente o prefixo, exigindo a definição do intervalo SSM por meio de uma ACL:

```ios
access-list 10 permit 232.0.0.0 255.0.0.0
ip pim ssm range 10
```

Já em sistemas mais recentes — como IOS XE, NX-OS e IOS XR — o intervalo SSM pode ser configurado diretamente:  

```ios
ip pim ssm-range 232.0.0.0 255.0.0.0
```

Neste laboratório utilizamos o IOS clássico, portanto adotamos o método baseado em ACL.

---

🔧 **Configuração do SSM em Todo o Domínio PIM**

Para que o Source-Specific Multicast (SSM) funcione corretamente, todos os roteadores do domínio PIM devem possuir o intervalo SSM configurado. Isso garante que cada roteador interprete corretamente os grupos do intervalo 232.0.0.0/8 como SSM, evitando a busca por RP, a criação de (*,G) e qualquer comportamento associado ao PIM Sparse Mode tradicional.  

💡 **Boa prática:**
Em laboratórios e ambientes reais, o SSM-range deve estar presente em todos os hops entre o Host e o Server, garantindo que os **joins (S,G)** sejam aceitos e propagados ao longo de toda a árvore **PIM-SSM**.  

### 🧭 2️⃣ Habilitando o IGMPv3 nos roteadores

O IGMPv3 é fundamental para o funcionamento do SSM, pois ele permite que os receptores especifiquem as fontes (S) das quais desejam receber tráfego.  
Sem IGMPv3, o roteador não reconhece solicitações do tipo (S,G).  

➡️ Comando por interface LAN conectada aos hosts receptores:  

```ios
R04(config)#int fa1/1
R04(config-if)#ip igmp version 3
```

Faça o mesmo nas interfaces onde há receptores multicast (ex.: R04 e R05).  

💡 **Dica:**
Mesmo que alguns roteadores suportem IGMPv3 por padrão, é recomendado forçar a versão explicitamente para evitar incompatibilidades.  

Para verificar o estado/versão do **IGMP**, execute o comando:  

```ios
show ip igmp interface
```

Exemplo em R01  

```ios
R01#show ip igmp interface
Loopback0 is up, line protocol is up
  Internet address is 1.1.1.1/32
  IGMP is enabled on interface
  Current IGMP host version is 3
  Current IGMP router version is 3
  IGMP query interval is 60 seconds
  IGMP querier timeout is 120 seconds
  IGMP max query response time is 10 seconds
  Last member query count is 2
  Last member query response interval is 1000 ms
  Inbound IGMP access group is not set
  IGMP activity: 1 joins, 0 leaves
  Multicast routing is enabled on interface
  Multicast TTL threshold is 0
  Multicast designated router (DR) is 1.1.1.1 (this system)
  IGMP querying router is 1.1.1.1 (this system)
  Multicast groups joined by this system (number of users):
      224.0.1.40(1)
FastEthernet0/0 is up, line protocol is up
  Internet address is 192.168.10.254/24
  IGMP is enabled on interface
  Current IGMP host version is 3
  Current IGMP router version is 3
  IGMP query interval is 60 seconds
  IGMP querier timeout is 120 seconds
  IGMP max query response time is 10 seconds
  Last member query count is 2
  Last member query response interval is 1000 ms
  Inbound IGMP access group is not set
  IGMP activity: 0 joins, 0 leaves
  Multicast routing is enabled on interface
  Multicast TTL threshold is 0
  Multicast designated router (DR) is 192.168.10.254 (this system)
  IGMP querying router is 192.168.10.254 (this system)
  No multicast groups joined by this system
FastEthernet0/1 is up, line protocol is up
  Internet address is 10.0.0.1/30
  IGMP is enabled on interface
  Current IGMP host version is 3
  Current IGMP router version is 3
  IGMP query interval is 60 seconds
  IGMP querier timeout is 120 seconds
  IGMP max query response time is 10 seconds
  Last member query count is 2
  Last member query response interval is 1000 ms
  Inbound IGMP access group is not set
  IGMP activity: 1 joins, 0 leaves
  Multicast routing is enabled on interface
  Multicast TTL threshold is 0
  Multicast designated router (DR) is 10.0.0.2
  IGMP querying router is 10.0.0.1 (this system)
  No multicast groups joined by this system
FastEthernet1/0 is up, line protocol is up
  Internet address is 10.0.0.18/30
  IGMP is enabled on interface
  Current IGMP host version is 3
  Current IGMP router version is 3
  IGMP query interval is 60 seconds
  IGMP querier timeout is 120 seconds
  IGMP max query response time is 10 seconds
  Last member query count is 2
  Last member query response interval is 1000 ms
  Inbound IGMP access group is not set
  IGMP activity: 0 joins, 0 leaves
  Multicast routing is enabled on interface
  Multicast TTL threshold is 0
  Multicast designated router (DR) is 10.0.0.18 (this system)
  IGMP querying router is 10.0.0.17
  No multicast groups joined by this system
R01#
```

---

### 🧰 3️⃣ Associando hosts e fontes multicast

Neste laboratório, temos duas fontes e um ou mais receptores:

| Dispositivo | Função             | IP           | Grupo (G)                            |
|-------------|--------------------|--------------|--------------------------------------|
| Server01    | Fonte multicast #1 | 192.168.10.1 | 232.1.1.1                            |
| Server02    | Fonte multicast #2 | 192.168.40.1 | 232.2.2.2                            |
| Host02      | Receptor multicast | 192.168.20.1 | (S,G) Join para Server01 e Server02  |
| Host03      | Receptor multicast | 192.168.30.1 | (S,G) Join para Server01 e Server02  |

📘 **Comando de Join nos receptores (simulados com roteadores Cisco):**  

Devemos executar os mesmos comandos em HOST02 e HOST03

**Host02**  

```ios
Host02(config)#int fa0/0
Host02(config-if)#ip igmp join-group 232.1.1.1 source 192.168.10.1
Host02(config-if)#ip igmp join-group 232.1.1.1 source 192.168.40.1
Host02(config-if)#ip igmp join-group 232.2.2.2 source 192.168.10.1
Host02(config-if)#ip igmp join-group 232.2.2.2 source 192.168.40.1
```

**Host03**  

```ios
Host03(config)#int fa0/0
Host03(config)#ip igmp join-group 232.1.1.1 source 192.168.40.1
Host03(config)#ip igmp join-group 232.2.2.2 source 192.168.10.1
Host03(config)#ip igmp join-group 232.1.1.1 source 192.168.10.1
Host03(config)#ip igmp join-group 232.2.2.2 source 192.168.40.1
```

**OBS:** agora no **SSM + IGMPv3** quando vamos realizar o join group precisamos informar a fonte. Por essa questão, não é mais necessário se fazer o join nos servidores. Isso era feito nos laboratórios anteriores para fecharmos o par (S, G) e, nesse caso, se fizermos o join nos servidores pode ser que quando executarmos o teste de ping a interface de gateway responda pode gerar um loop.  

Agora vamos verificar a tabela de **roteamento multicast** em **R04 e R05** com o comando:

```ios
show ip mroute
```

Exemplo de saída esperada:  

```ios
R04#show ip mroute
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

(*, 232.2.2.2), 00:02:25/00:02:58, RP 0.0.0.0, flags: SJC
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:02:25/00:02:58

(*, 232.1.1.1), 00:05:51/00:02:54, RP 0.0.0.0, flags: SJC
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    FastEthernet1/0, Forward/Sparse, 00:05:51/00:02:54

(*, 224.0.1.40), 00:29:06/00:02:50, RP 0.0.0.0, flags: DCL
  Incoming interface: Null, RPF nbr 0.0.0.0
  Outgoing interface list:
    Loopback0, Forward/Sparse, 00:29:06/00:02:50

R04#
```

💡 **Observe:**

- As entradas aparecem no **formato (S,G) — indicando a árvore por fonte**;
- Não há nenhuma **linha (,G), pois o SSM não utiliza RP**;
- O campo flags: **SJC confirma o modo Source-Specific ativo**.

📌 **Observação Importante**  

Em redes multicast, o querier define a versão do IGMP utilizada em cada segmento da LAN.  
Isso significa que:  

- Mesmo se um roteador ou host estiver configurado com ip igmp version 3,
- Se o querier enviar IGMPv2 Queries, todos os dispositivos do segmento passam automaticamente a operar em IGMPv2.

💡 **No IOS clássico, isso é um comportamento padrão do protocolo.**

📌 **Forçar o querier atual a usar IGMPv3**

Nos roteadores **R04 e R05** que estão atuando como querier, executar nas interfaces ligadas aos roteadores multicast:  

```ios
interface FaX/Y
 ip igmp version 3
```

### 🧪 5️⃣ Captura e análise via Wireshark

📌 **Local ideal para captura:**  

Interface entre R04 e o Host02, onde ocorrem os IGMPv3 Membership Reports.  
  
📌 **Filtro recomendado:**  

```whiresahrk
igmp.type == 0x22
```

![Whireshark](Imagens/02.png)

💡 **Explicação:**

- **0x22** identifica mensagens **IGMPv3 Membership Report**;
- Dentro dessas mensagens, é possível observar **os pares (S,G) solicitados**;  
- Verifique os endereços das **fontes (192.168.10.1 e 192.168.40.1)** listados como Source Addresses.
  
📸 **Captura real:**  
  
As mensagens IGMPv3 confirmam que o Host02 requisitou fluxos multicast apenas das fontes autorizadas, validando o funcionamento do SSM com múltiplas fontes simultâneas.  

🧠 **Resumo**

| Função                  | Protocolo / Comando                  | Observação técnica                              |
|-------------------------|--------------------------------------|-------------------------------------------------|
| Definir range SSM       | ip pim ssm range 232.0.0.0 255.0.0.0 | Ativa o modo Source-Specific para o bloco 232/8 |
| Ativar IGMPv3           | ip igmp version 3                    | Necessário para joins específicos (S,G)         |
| Associar receptor (S,G) | ip igmp join-group <G> source <S>    | Simula associação IGMPv3                        |
| Verificar rotas         | show ip mroute                       | Mostra entradas (S,G) no domínio multicast      |
| Capturar tráfego        | Filtro igmp.type == 0x22             | Exibe os Membership Reports IGMPv3              |

Com isso, o domínio multicast está completamente operacional em modo SSM, e o tráfego das fontes Server01 e Server02 será entregue somente aos hosts que enviarem joins IGMPv3 (S,G).  

### 🎥 Configurando os servidores simulados (senders)

Como os servidores deste laboratório são roteadores Cisco simulando PCs, não existe aplicação multicast real (como VLC ou ffmpeg) para abrir um socket e transmitir para um grupo multicast.  
  
Por isso, para simular corretamente o envio do fluxo multicast, é necessário que a interface do “servidor” execute um **IGMP join-group** apenas para o **grupo que ele irá transmitir**. Isso ativa o socket multicast interno do IOS, permitindo gerar tráfego para o endereço do grupo.  

#### 🟩 Server01 – Transmitindo para 232.1.1.1 e 232.2.2.2

Como explicado anteriormente, não devemos fazer um ip igmp join-group nos nossos servidores. Só iremos configurar a interface ligada aos roteadores de trânsito para que se utilize o **igmpv3** para garantirmos que toda nossa rede funcione na **versão 3 e não na 2**.

```ios
interface fa0/0
 ip igmp version 3
```

### 🟦 Server02 – Transmitindo para 231.1.1.1 e 232.2.2.2

```ios
interface fa0/0
 ip igmp version 3
```

Cada servidor anuncia apenas um único grupo, como ocorre em aplicações multicast reais. Os receptores **(Host02 e Host03)** fazem os joins **IGMPv3 (S,G)** para ambas as fontes, recebendo dois fluxos simultâneos.

### Realizando testes - Simulando fluxo nos servidores

Agora vamos entrar em **Server** e executar:

`ping 232.1.1.1 repeat 1000 size 1500 source Fa0/0`  
  
`ping 232.2.2.2 repeat 1000 size 1500 source F0/0`  


Demos entrar em **Server02** e executar também:  

`ping 232.1.1.1 repeat 1000 size 1500 source Fa0/0`  
  
`ping 232.2.2.2 repeat 1000 size 1500 source F0/0`


Devemos ter uma saída assim:  

```ios
SERVER#ping 232.1.1.1 repeat 10000 size 1500 source Fa0/0

Type escape sequence to abort.
Sending 10000, 1500-byte ICMP Echos to 232.1.1.1, timeout is 2 seconds:
Packet sent with a source address of 192.168.10.1
...
Reply to request 3 from 192.168.30.1, 48 ms
Reply to request 3 from 192.168.20.1, 76 ms
Reply to request 4 from 192.168.30.1, 84 ms
Reply to request 4 from 192.168.20.1, 120 ms
Reply to request 5 from 192.168.30.1, 128 ms
Reply to request 5 from 192.168.20.1, 168 ms
Reply to request 6 from 192.168.30.1, 136 ms
Reply to request 6 from 192.168.20.1, 172 ms
Reply to request 7 from 192.168.30.1, 124 ms
Reply to request 7 from 192.168.20.1, 160 ms
SERVER#ping 232.2.2.2 repeat 10000 size 1500 source Fa0/0

Type escape sequence to abort.
Sending 10000, 1500-byte ICMP Echos to 232.2.2.2, timeout is 2 seconds:
Packet sent with a source address of 192.168.10.1

Reply to request 0 from 192.168.30.1, 36 ms
Reply to request 0 from 192.168.20.1, 60 ms
Reply to request 1 from 192.168.30.1, 160 ms
Reply to request 1 from 192.168.20.1, 196 ms
Reply to request 2 from 192.168.30.1, 120 ms
Reply to request 2 from 192.168.20.1, 156 ms
Reply to request 3 from 192.168.30.1, 132 ms
Reply to request 3 from 192.168.20.1, 168 ms
Reply to request 4 from 192.168.30.1, 116 ms
Reply to request 4 from 192.168.20.1, 152 ms
Reply to request 5 from 192.168.30.1, 132 ms
Reply to request 5 from 192.168.20.1, 168 ms
Reply to request 6 from 192.168.30.1, 104 ms
Reply to request 6 from 192.168.20.1, 144 ms
SERVER#wr
Building configuration...
[OK]
SERVER#
```

Repetir o mesmo para o SERVER02.  

🔎 **Observação importante sobre joins simulados e testes com ping**  

Em ambientes de produção, os servidores e aplicações multicast não executam **ip igmp join-group manualmente**.  
Quem realiza essa função é a aplicação (como VLC, encoders de vídeo, sistemas de monitoramento, middleware de streaming etc.), que informa ao sistema operacional em quais grupos multicast deve transmitir ou receber.  
  
Como no laboratório estamos usando roteadores **Cisco simulando servidores**, não existe uma aplicação real para gerar fluxos multicast.  
Por isso, os comandos **ip igmp join-group e ping <grupo>** são apenas uma simulação da lógica que uma aplicação multicast executaria automaticamente.  

**Isso significa que:**

- **ip igmp join-group** nos “hosts” serve apenas para formar a **entrada (S,G)** e permitir que o laboratório funcione;
- O uso de **ping** para enviar pacotes ICMP ao grupo não representa tráfego multicast real, mas garante um fluxo contínuo para validar **a árvore SSM;**
- Em **um ambiente real, o servidor só transmite, e o host só recebe**, sem qualquer necessidade de comandos manuais.
- Essa distinção é essencial para não confundir o funcionamento prático do protocolo com a abordagem usada no laboratório.

## 🛠️ Troubleshooting

| **Sintoma**                                   | **Causa Provável**             | **Comandos de Verificação** | **Correção**                                                    |
|-----------------------------------------------|--------------------------------|-----------------------------|-----------------------------------------------------------------|
| **Não aparece (S,G) no `show ip mroute`**     | - IGMPv3 desabilitado          | `show ip igmp interface`    | Ativar IGMPv3                                                   |
|                                               | - ACL SSM errada               | `show run \| i pim ssm`     | Corrigir ACL                                                    |
|                                               | - RPF falhando                 | `show ip rpf <S>`           | Corrigir rota da fonte                                          |
| **Grupo aparece como ”stopped”**              | Não há tráfego multicast ativo | `show ip mroute count`      | Gerar tráfego (ping multicast)                                  |
|                                               |                                | `show ip igmp groups`       | Confirmar joins                                                 |
| **Roteador forma **\*,G** ao invés de (S,G)** | Grupo fora do range SSM        | `show access-lists`         | Ajustar ACL SSM                                                 |
|                                               |                                | `show ip igmp interface`    | Habilitar IGMPv3                                                |
| **`show ip mroute count` vazio**              | Fonte não transmite            | `debug ip packet detail`    | Validar tráfego real                                            |
|                                               | Ping respondido localmente     | `show ip rpf`               | Garantir saída pela interface certa                             |
|                                               | RPF falha                      | `show ip route`             | Corrigir RPF                                                    |
| **Sem vizinhos PIM**                          | Interface LAN em p2p           | `show ip pim neighbor`      | Habilitar PIM                                                   |
|                                               | PIM ausente                    | `show ip pim interface`     | Ajustar tipo da interface                                       |
|                                               | L2/L1 com problema             | `show ip ospf interface`    | Verificar camada 2                                              |
| **RPF Failure**                               | Rota errada para a fonte (S)   | `show ip rpf <S>`           | Ajustar OSPF                                                    |
|                                               |                                | `show ip route`             | revisar métricas e next-hops                                    |
| **Host recebe apenas 1 fluxo**                | Uma fonte não transmite        | `show ip igmp groups`       | Corrigir ACL                                                    |
|                                               | ACL SSM incompleta             | `show access-lists`         | Garantir tráfego das duas fontes                                |
| **Ping multicast responde só do gateway**     | **Normal** —ICMP multicast     | —                           | Entender que o ping é **somente gerador de tráfego**, não teste |
|                                               | não vira unicast pros hosts    | —                           | de reachability                                                 |

## 🧩 O que aprendemos com este laboratório (SSM + IGMPv3)

Neste laboratório exploramos o funcionamento do Source-Specific Multicast (SSM) com PIM-SSM e IGMPv3, o modelo mais moderno e simples de multicast — sem RP, sem árvores compartilhadas e sem Bootstrap.  
  
O foco foi entender como o host escolhe exatamente qual fonte (S) deseja receber para um determinado grupo (G) dentro do intervalo 232.0.0.0/8, e como o domínio PIM constrói a árvore (S,G) de forma direta e otimizada.  

## 🎯 Principais aprendizados

| Tópico                      | Conceito-chave                                                                                                      |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|
| SSM ativado com ACL         | A rede só entra em modo SSM quando configuramos ip pim ssm default ou uma ACL definindo o range (ex.: 232.0.0.0/8). |
| IGMPv3 obrigatório          | Apenas IGMPv3 permite o join específico da fonte, enviando relatórios contendo Include {S,G}.                       |
| Árvore direta (S,G)         | Diferente do PIM-SM clássico, o SSM cria imediatamente o caminho mais curto até a fonte — sem RP e sem Shared Tree. |
| DR recebendo joins          | O roteador DR recebe o IGMPv3 Report e envia um PIM Join diretamente para a fonte S, construindo a árvore.          |
| Sem Register / Sem RP       | Em SSM não existe processo de Register, RP Designation, Bootstrap ou failover de RP. É tudo direto e simples.       |
| Testes com tráfego simulado | Utilizamos ping multicast apenas como mecanismo de geração de tráfego, não como teste de reachability.              |
| Validação da árvore         | O comportamento correto é ver entradas (S,G) no show ip mroute e contadores subindo no show ip mroute count.        |

## 💡 Conclusões gerais

- O **SSM** simplifica radicalmente o multicast, **removendo RP, Register, BSR, Auto-RP e qualquer forma de árvore compartilhada.**
- Com **IGMPv3**, cada host escolhe exatamente qual fonte quer receber, aumentando segurança e previsibilidade.
- É o modelo ideal para aplicações modernas: IPTV, streaming unidirecional, monitoramento e telemetria.
- Em laboratórios, a geração de tráfego via ping multicast é suficiente para validar a operação da árvore (S,G).

## 🗺️ Fluxo conceitual do SSM (S,G)

```text
┌────────────────────────────┐
│ 1. Host envia IGMPv3 Join  │
│     Include {S,G}          │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 2. DR recebe o Join        │
│    e instala interesse     │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 3. DR envia PIM Join → S   │
│    (sem RP, sem Shared Tree)│
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 4. Roteadores no caminho   │
│    criam estado (S,G)      │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 5. Tráfego flui direto     │
│    da fonte para o host    │
└────────────────────────────┘
```

## 📘 Tabela de Comandos

### 🖥️ Função	—	R01 atua como Designated Router (DR) para a LAN dos servidores

| **Seção**           | **Comando / Configuração**                | **Descrição**                                |
|---------------------|-------------------------------------------|----------------------------------------------|
| **Global**          | `ip multicast-routing`                    | Habilita roteamento multicast                |
| **Global**          | `ip pim ssm range SSM-RANGE`              | Ativa SSM e vincula ao range definido na ACL |
| **ACL**             | `ip access-list standard SSM-RANGE`       | Define os grupos SSM aceitos                 |
|                     | `permit 232.1.1.1`                        | Server                                       |
|                     | `permit 232.2.2.2`                        | Server02                                     |
| **Loopback0**       | `ip address 1.1.1.1 255.255.255.255`      | Router-ID e origem das mensagens PIM         |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                     |
| **FastEthernet0/0** | `ip address 192.168.10.254 255.255.255.0` | DR da LAN do servidor (HOSTS/SOURCES)        |
|                     | `ip pim sparse-mode`                      | Modo do protocolo                            |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                     |
| **FastEthernet0/1** | `ip address 10.0.0.1 255.255.255.252`     | Link P2P com R02                             |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                        |
|                     | `ip igmp version 3`                       | Link P2P com R05                             |
| **FastEthernet1/0** | `ip address 10.0.0.18 255.255.255.252`    | Link P2P com R05 – participa do domínio PIM  |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                     |
| **OSPF**            | `router ospf 100`                         | Processo OSPF                                |
|                     | `router-id 1.1.1.1`                       | ID do processo OSPF                          |
|                     | `network 1.1.1.1 0.0.0.0 area 0`          | Ativando o OSPF na Interface LOOPBACK0       |
|                     | `network 10.0.0.0 0.0.0.3 area 0`         | Ativando o OSPF na Interface FastEthernet0/1 |
|                     | `network 10.0.0.16 0.0.0.3 area 0`        | Ativando o OSPF na Interface FastEthernet1/0 |
|                     | `network 192.168.10.0 0.0.0.255 area 0`   | Ativando o OSPF na Interface FastEthernet0/0 |

### 📗 R02 – Router de Núcleo / Intermediário do Domínio SSM

| **Seção**           | **Comando / Configuração**           | **Descrição**                                        |
| --------------------|--------------------------------------|------------------------------------------------------|
| **Global**          | `ip multicast-routing`               | Habilita roteamento multicast                        |
| **Global**          | `ip pim ssm range SSM-RANGE`         | Ativa SSM sob os grupos definidos na ACL             |
| **ACL**             | `ip access-list standard SSM-RANGE`  | Grupos definidos para operação SSM                   |
|                     | `permit 232.1.1.1`                   | Server                                               |
|                     | `permit 232.2.2.2`                   | Server02                                             |
| **Loopback0**       | `ip address 2.2.2.2 255.255.255.255` | Router-ID e origem das mensagens PIM                 |
|                     | `ip pim sparse-mode`                 | Modo do protocolo PIM                                |
|                     | `ip igmp version 3`                  | Versão do protocolo IGMP                             |
| **FastEthernet0/1** | `ip address 10.0.0.2 255.255.255.252`| Link P2P com R01 – participa do domínio PIM          |
|                     | `ip pim sparse-mode`                 | Modo do protocolo PIM                                |
|                     | `ip igmp version 3`                  | Versão do protocolo IGMP                             |
| **FastEthernet1/0** | `ip address 10.0.0.5 255.255.255.252`| Link P2P com R03 – trânsito para o domínio multicast |
|                     | `ip pim sparse-mode`                 | Modo do protocolo PIM                                |
|                     | `ip igmp version 3`                  | Versão do protocolo IGMP                             |
| **OSPF**            | `router ospf 100`                    | Processo OSPF                                        |
|                     | `router-id 2.2.2.2`                  | ID do processo OSPF                                  |
|                     | `network 2.2.2.2 0.0.0.0 area 0`     | Ativando o OSPF na Interface LOOPBACK0               |
|                     | `network 10.0.0.0 0.0.0.3 area 0`    | Ativando o OSPF na Interface FastEthernet0/1         |
|                     | `network 10.0.0.4 0.0.0.3 area 0`    | Ativando o OSPF na Interface FastEthernet1/0         |

### 📙 R03 – DR da LAN do Host + Roteador de Trânsito no SSM

| **Seção**           | **Comando / Configuração**                | **Descrição**                                                |
|---------------------|-------------------------------------------|--------------------------------------------------------------|
| **Global**          | `ip multicast-routing`                    | Ativa roteamento multicast                                   |
| **Global**          | `ip pim ssm range SSM-RANGE`              | Define os grupos utilizados em modo SSM                      |
| **ACL SSM**         | `ip access-list standard SSM-RANGE`       | Range SSM (S,G) permitido                                    |
|                     | `permit 232.1.1.1`                        | Server                                                       |
|                     | `permit 232.2.2.2`                        | Server02                                                     |
| **Loopback0**       | `ip address 3.3.3.3 255.255.255.255`      | Router-ID e origem das mensagens PIM                         |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **FastEthernet0/0** | `ip address 10.0.0.9 255.255.255.252`     | Link P2P com R04 – participa do domínio SSM                  |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     |  `ip igmp version 3`                      | Versão do protocolo IGMP                                     |
| **FastEthernet0/1** | `ip address 192.168.40.254 255.255.255.0` | LAN do Host – **R03 é o DR deste segmento**                  |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **FastEthernet1/0** | `ip address 10.0.0.6 255.255.255.252`     | Link P2P com R02 – domínio multicast                         |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **OSPF**            | `router ospf 100`                         | Garante conectividade IP e RPF correto                       |
|                     | `router-id 3.3.3.3`                       | ID do processo OSPF                                          |
|                     | `network 3.3.3.3 0.0.0.0 area 0`          | Ativando o OSPF na Interface LOOPBACK0                       |
|                     | `network 10.0.0.4 0.0.0.3 area 0`         | Ativando o OSPF na Interface FastEthernet1/0                 |
|                     | `network 10.0.0.8 0.0.0.3 area 0`         | Ativando o OSPF na Interface FastEthernet1/0                 |
|                     | `network 192.168.40.0 0.0.0.255 area 0`   | Ativando o OSPF na Interface FastEthernet0/1                 |
| **Função**          | —                                         | **DR da LAN dos hosts** + **router de trânsito do SSM**      |

### 📒 R04 – DR da LAN do Host02 + Roteador de Trânsito no SSM

| **Seção**           | **Comando / Configuração**                | **Descrição**                                                |
|---------------------|-------------------------------------------|--------------------------------------------------------------|
| **Global**          | `ip multicast-routing`                    | Habilita o roteamento multicast                              |
| **Global**          | `ip pim ssm range SSM-RANGE`              | Define os grupos operando em modo SSM                        |
| **ACL SSM**         | `ip access-list standard SSM-RANGE`       | Range SSM utilizado pelos receptores                         |
|                     | `permit 232.1.1.1`                        | Server                                                       |
|                     | `permit 232.2.2.2`                        | Server02                                                     |
| **Loopback0**       | `ip address 4.4.4.4 255.255.255.255`      | Router-ID, origem lógica para PIM                            |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **FastEthernet0/0** | `ip address 10.0.0.10 255.255.255.252`    | Link P2P com R03 – trânsito do SSM                           |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **FastEthernet0/1** | `ip address 10.0.0.13 255.255.255.252`    | Link P2P com R05 – trânsito do SSM                           |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **FastEthernet1/0** | `ip address 192.168.20.254 255.255.255.0` | LAN do Host02 — **R04 é o DR desta LAN**                     |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                        |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                     |
| **OSPF**            | `router ospf 100`                         | Garante conectividade IP e RPF correto                       |
|                     | `router-id 4.4.4.4`                       | ID do processo OSPF                                          |
|                     | `network 4.4.4.4 0.0.0.0 area 0`          | Ativando o OSPF na Interface LOOPBACK4                       |
|                     | `network 10.0.0.8 0.0.0.3 area 0`         | Ativando o OSPF na Interface FastEthernet0/0                 |
|                     | `network 10.0.0.12 0.0.0.3 area 0`        | Ativando o OSPF na Interface FastEthernet0/1                 |
|                     | `network 192.168.20.0 0.0.0.255 area 0`   | Ativando o OSPF na Interface FastEthernet1/0                 |
| **Função**          | —                                         | **DR da LAN do Host02** + **roteador intermediário do SSM**  |

### 📕 R05 – Roteador de Trânsito + DR da LAN do Host03

| **Seção**           | **Comando / Configuração**                | **Descrição**                                                     |
|---------------------|-------------------------------------------|-------------------------------------------------------------------|
| **Global**          | `ip multicast-routing`                    | Habilita o roteamento multicast                                   |
| **Global**          | `ip pim ssm range SSM-RANGE`              | Define os grupos operando em modo SSM                             |
| **ACL SSM**         | `ip access-list standard SSM-RANGE`       | Lista de grupos permitidos para SSM                               |
|                     | `permit 232.1.1.1`                        | Server                                                            |
|                     | `permit 232.2.2.2`                        | Server02                                                          |
| **Loopback0**       | `ip address 5.5.5.5 255.255.255.255`      | Router-ID do R05 e origem PIM                                     |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                             |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                          |
| **FastEthernet0/0** | `ip address 192.168.30.254 255.255.255.0` | LAN do Host03 — **R05 é o DR deste segmento**                     |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                             |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                          |
| **FastEthernet0/1** | `ip address 10.0.0.14 255.255.255.252`    | Link P2P com R04 — trânsito do SSM                                |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                             |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                          |
| **FastEthernet1/0** | `ip address 10.0.0.17 255.255.255.252`    | Link P2P com R01 — caminho em direção às fontes                   |
|                     | `ip pim sparse-mode`                      | Modo do protocolo PIM                                             |
|                     | `ip igmp version 3`                       | Versão do protocolo IGMP                                          |
| **OSPF**            | `router ospf 100`                         | Mantém conectividade IP e garante RPF correto                     |
|                     | `router-id 5.5.5.5`                       | ID do processo OSPF                                               |
|                     | `network 5.5.5.5 0.0.0.0 area 0`          | Ativando o OSPF na Interface LOOPBACK5                            |
|                     | `network 10.0.0.12 0.0.0.3 area 0`        | Ativando o OSPF na Interface FastEthernet0/1                      |
|                     | `network 10.0.0.16 0.0.0.3 area 0`        | Ativando o OSPF na Interface FastEthernet1/0                      |
|                     | `network 192.168.30.0 0.0.0.255 area 0`   | Ativando o OSPF na Interface FastEthernet0/0                      |
| **Função**          | —                                         | **Roteador de trânsito SSM** + **DR da LAN do Host03**            |

### 🖥️ SERVER – Fonte Multicast (Sender)

| **Seção**               | **Comando / Configuração**                | **Descrição**                                                                   |
|-------------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| **Global**              | `ip multicast-routing`                    | Habilita o roteamento multicast no equipamento                                  |
| **FastEthernet0/0**     | `ip address 192.168.10.1 255.255.255.0`   | Interface conectada ao R01 — origem do fluxo multicast (S)                      |
| **Rota Padrão**         | `ip route 0.0.0.0 0.0.0.0 192.168.10.254` | Define R01 como gateway padrão (DR da LAN do servidor)                          |
| **Função no cenário**   | —                                         | Atua como **fonte multicast** enviando tráfego para grupos SSM (ex.: 232.x.x.x) |

### 🖥️ SERVER02 – Fonte Multicast (Sender)

| **Seção**               | **Comando / Configuração**                | **Descrição**                                                               |
|-------------------------|-------------------------------------------|-----------------------------------------------------------------------------|
| **Global**              | `ip multicast-routing`                    | Habilita o processamento multicast (necessário para gerar tráfego SSM)      |
| **FastEthernet0/0**     | `ip address 192.168.40.1 255.255.255.0`   | Interface conectada ao R03 — origem do fluxo multicast (S = 192.168.40.1)   |
| **Rota padrão**         | `ip route 0.0.0.0 0.0.0.0 192.168.40.254` | Usa R03 como gateway padrão                                                 |
| **Função no cenário**   | —                                         | Atua como **fonte multicast** para grupos SSM (ex.: 232.2.2.2)              |

### 💻 HOST02 – Receptor Multicast (IGMPv3 + SSM)

| **Seção**                    | **Comando / Configuração**                         | **Descrição**                                                                                    |
|------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Fa0/0 (LAN com R04)**      | `ip address 192.168.20.1 255.255.255.0`            | Host inscrito em **dois grupos (G)** e **duas fontes (S)** por grupo — simulação completa de SSM |
|                              | `ip igmp join-group 232.1.1.1 source 192.168.10.1` | Escolhendo a fonte de fluxo multicast como SERVER                                                |
|                              | `ip igmp join-group 232.1.1.1 source 192.168.40.1` | Escolhendo a fonte de fluxo multicast como SERVER                                                |
|                              | `ip igmp join-group 232.2.2.2 source 192.168.10.1` | Escolhendo a fonte de fluxo multicast como SERVER02                                              |
|                              | `ip igmp join-group 232.2.2.2 source 192.168.40.1` | Escolhendo a fonte de fluxo multicast como SERVER                                                |
| **Rota padrão**              | `ip route 0.0.0.0 0.0.0.0 192.168.20.254`          | Usa R04 como gateway padrão (DR do segmento)                                                     |
| **Função no cenário**        | —                                                  | Atua como **Receptor SSM (IGMPv3)** — envia Joins (S,G) diretamente ao DR                        |

### 🖥️ HOST03 – Receptor Multicast Secundário (SSM com múltiplas fontes)

| **Seção**                         | **Comando / Configuração**                         | **Descrição**                                                                               |
|-----------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Interface Fa0/0 (LAN com R05)** | `ip address 192.168.30.1 255.255.255.0`            | Host inscrito **em duas fontes (S)** para **dois grupos (G)** — comportamento SSM completo  |
|                                   | `ip igmp join-group 232.1.1.1 source 192.168.40.1` | Escolhendo a fonte de fluxo multicast como SERVER                                           |
|                                   | `ip igmp join-group 232.2.2.2 source 192.168.10.1` | Escolhendo a fonte de fluxo multicast como SERVER02                                         |
|                                   | `ip igmp join-group 232.1.1.1 source 192.168.10.1` | Escolhendo a fonte de fluxo multicast como SERVER                                           |
|                                   | `ip igmp join-group 232.2.2.2 source 192.168.40.1` | Escolhendo a fonte de fluxo multicast como SERVER02                                         |
| **Rota padrão**                   | `ip route 0.0.0.0 0.0.0.0 192.168.30.254`          | Define R05 como gateway padrão (DR do segmento)                                             |
| **Função no cenário**             | —                                              | Atua como **Receptor SSM** equivalente ao Host02; valida replicação multicast por outro caminho |

