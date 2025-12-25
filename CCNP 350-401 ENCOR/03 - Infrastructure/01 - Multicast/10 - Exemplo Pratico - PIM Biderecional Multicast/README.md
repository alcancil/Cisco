# Índice

- [Índice](#índice)
  - [10 - Exemplo Pratico - PIM Bidirecional Multicast](#10---exemplo-pratico---pim-bidirecional-multicast)
  - [🧾 Introdução](#-introdução)
  - [🎯 Objetivo do Laboratório](#-objetivo-do-laboratório)
  - [📚 O que você vai aprender](#-o-que-você-vai-aprender)
    - [💼 Relevância prática](#-relevância-prática)
  - [🧠 Explicação do Cenário](#-explicação-do-cenário)
    - [🌐 Do PIM-SM Tradicional ao PIM Bidirectional (BIDIR)](#-do-pim-sm-tradicional-ao-pim-bidirectional-bidir)
    - [🔁 O que é SPT Switching?](#-o-que-é-spt-switching)
    - [🔁 Sobre o SPT Switching no Contexto do PIM BIDIR](#-sobre-o-spt-switching-no-contexto-do-pim-bidir)
    - [🧩 1️⃣ Fontes e Receptores no Cenário](#-1️⃣-fontes-e-receptores-no-cenário)
    - [🧭 Estrutura do Roteamento](#-estrutura-do-roteamento)
    - [📡 Grupos Multicast no PIM Bidirectional](#-grupos-multicast-no-pim-bidirectional)
    - [🧩 Conclusão](#-conclusão)
    - [🛰️ O que muda no PIM Bidirectional (BIDIR)](#️-o-que-muda-no-pim-bidirectional-bidir)
      - [🌳 1️⃣ O comportamento do PIM BIDIR](#-1️⃣-o-comportamento-do-pim-bidir)
      - [🔹 2️⃣ O papel do IGMP no PIM BIDIR](#-2️⃣-o-papel-do-igmp-no-pim-bidir)
      - [🔀 3️⃣ Designated Forwarder (DF) e prevenção de loops](#-3️⃣-designated-forwarder-df-e-prevenção-de-loops)
      - [🛰️ 4️⃣ Quando as fontes começam a transmitir](#️-4️⃣-quando-as-fontes-começam-a-transmitir)
      - [📡 5️⃣ Vantagens do PIM BIDIR sobre o PIM-SM tradicional](#-5️⃣-vantagens-do-pim-bidir-sobre-o-pim-sm-tradicional)
  - [🌐 Topologia do Laboratório](#-topologia-do-laboratório)
    - [🔧 Endereçamento e Funções](#-endereçamento-e-funções)
    - [📡 Grupos Multicast no PIM Bidirectional - resumo](#-grupos-multicast-no-pim-bidirectional---resumo)
    - [🔍 Testes Preliminares](#-testes-preliminares)
  - [🚀 Ativação do Roteamento Multicast](#-ativação-do-roteamento-multicast)
    - [🧩 Principais Diferenças do PIM BIDIR em Relação ao PIM-SM](#-principais-diferenças-do-pim-bidir-em-relação-ao-pim-sm)
    - [🌍 Onde o PIM Deve Ser Ativado](#-onde-o-pim-deve-ser-ativado)
    - [💡 Observação Sobre as Fontes Multicast](#-observação-sobre-as-fontes-multicast)
    - [🧩 E se o Host01 quiser apenas uma das fontes?](#-e-se-o-host01-quiser-apenas-uma-das-fontes)
    - [🚫 E se o Host01 quiser bloquear uma das fontes?](#-e-se-o-host01-quiser-bloquear-uma-das-fontes)
    - [🧠 Resumo Final](#-resumo-final)
  - [⚙️ Ativando o protocolo PIM Bidirectional (PIM-BIDIR)](#️-ativando-o-protocolo-pim-bidirectional-pim-bidir)
    - [🔧 Configuração do PIM-BIDIR](#-configuração-do-pim-bidir)
      - [Exemplo – Ativando o PIM nas interfaces do R01](#exemplo--ativando-o-pim-nas-interfaces-do-r01)
  - [🧩 Eleição do Designated Router (DR) no PIM-BIDIR](#-eleição-do-designated-router-dr-no-pim-bidir)
    - [⚙️ Critérios de eleição do DR](#️-critérios-de-eleição-do-dr)
  - [💬 Mensagens PIM Hello no PIM-BIDIR](#-mensagens-pim-hello-no-pim-bidir)
    - [⚙️ Funções principais das mensagens Hello](#️-funções-principais-das-mensagens-hello)
    - [🧩 Estrutura simplificada da mensagem PIM Hello](#-estrutura-simplificada-da-mensagem-pim-hello)
  - [🔍 Exemplo de log da eleição do DR](#-exemplo-de-log-da-eleição-do-dr)
  - [🧭 Surgimento do Designated Forwarder (DF) no PIM-BIDIR](#-surgimento-do-designated-forwarder-df-no-pim-bidir)
  - [📊 Comparação clara: DR × DF no PIM-BIDIR](#-comparação-clara-dr--df-no-pim-bidir)
  - [🧪 Identificação do Designated Router (DR) no Domínio PIM](#-identificação-do-designated-router-dr-no-domínio-pim)
  - [⚙️ Como o DR é eleito neste estágio](#️-como-o-dr-é-eleito-neste-estágio)
  - [🔍 Comandos para identificar o DR](#-comandos-para-identificar-o-dr)
    - [0️⃣ Verificar em que interfaces o PIM está ativado](#0️⃣-verificar-em-que-interfaces-o-pim-está-ativado)
    - [1️⃣ Verificar vizinhança PIM](#1️⃣-verificar-vizinhança-pim)
    - [2️⃣ Verificar logs de eleição do DR em tempo real](#2️⃣-verificar-logs-de-eleição-do-dr-em-tempo-real)
    - [3️⃣ Confirmar a interface LAN envolvida](#3️⃣-confirmar-a-interface-lan-envolvida)
    - [🧠 Evidência via captura de pacotes (Wireshark)](#-evidência-via-captura-de-pacotes-wireshark)
    - [✅ Conclusão deste estágio do laboratório](#-conclusão-deste-estágio-do-laboratório)
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

## 10 - Exemplo Pratico - PIM Bidirecional Multicast

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

Neste laboratório, utilizamos cinco roteadores Cisco (R01 a R05) interconectados, responsáveis pelo encaminhamento do tráfego unicast e multicast no domínio de rede. O ambiente também conta com **três hosts simulados — SERVER, SERVER02 e HOSTS**— que representam **fontes e receptores multicast** em um cenário **many-to-many**, característico do **PIM Bidirectional (BIDIR)**.

Os hosts são configurados **exclusivamente com endereçamento IP e IGMP (tipicamente IGMPv2)**, sem participação em protocolos de roteamento dinâmico, refletindo o comportamento esperado de dispositivos finais em ambientes multicast BIDIR.

Os roteadores intermediários executam **OSPF**, garantindo a **convergência do roteamento unicast e a conectividade IP completa** entre todas as sub-redes antes da habilitação do **PIM Sparse Mode operando em modo Bidirectional (BIDIR)**. Essa conectividade unicast é um pré-requisito fundamental para o correto funcionamento do RP estático e para a eleição adequada do **Designated Forwarder (DF)** em cada enlace.

---

### 🌐 Do PIM-SM Tradicional ao PIM Bidirectional (BIDIR)

Diferente do **PIM Sparse Mode tradicional (PIM-SM)**, no qual o tráfego multicast inicialmente é encaminhado da fonte para o **Rendezvous Point (RP)** e, posteriormente, comuta para árvores de menor custo **(SPT), o PIM Bidirectional (BIDIR)** adota um modelo **many-to-many**, no qual **fontes e receptores compartilham a mesma árvore multicast bidirecional**.  
  
No **PIM BIDIR, o Rendezvous Point (RP)** continua sendo um elemento central do domínio multicast, **porém não atua como ponto de rendezvous de dados**, e sim como **raiz lógica da árvore compartilhada (Shared Tree)**.  
O tráfego multicast nunca é encapsulado ou redirecionado para o RP, sendo encaminhado de forma nativa em ambas as direções ao longo da árvore.  

Esse modelo oferece benefícios importantes em cenários com múltiplas fontes simultâneas, tais como:

- **Redução significativa de estado (state) nas tabelas mroute**, pois não há criação de entradas (S,G);
- **Eliminação do processo de SPT switch**, reduzindo overhead e instabilidade;
- **Escalabilidade elevada** em ambientes many-to-many, como aplicações financeiras, colaboração em tempo real e protocolos de controle;
- **Caminhos de encaminhamento previsíveis**, baseados exclusivamente na árvore compartilhada (*,G).

No PIM BIDIR, os receptores utilizam IGMP (normalmente IGMPv2) para expressar interesse em grupos multicast ((*,G)), sem necessidade de especificação de fontes.  
A seleção do encaminhamento correto é garantida pelo mecanismo de Designated Forwarder (DF), que define qual roteador será responsável pelo tráfego multicast em cada enlace, evitando loops e duplicações.  

### 🔁 O que é SPT Switching?

**SPT Switching (Shortest Path Tree Switching)** é o processo pelo qual um roteador abandona a árvore compartilhada (*,G) e passa a receber o tráfego multicast diretamente da fonte (S) pela árvore de menor custo (S,G).  

👉 **Em outras palavras:**  

- o tráfego multicast deixa de passar pelo RP e passa a seguir o caminho mais curto entre a fonte e o receptor, conforme a tabela de roteamento unicast.

### 🔁 Sobre o SPT Switching no Contexto do PIM BIDIR

No **PIM Sparse Mode tradicional (PIM-SM)**, o tráfego multicast é inicialmente encaminhado por meio da árvore compartilhada (*,G), com raiz no Rendezvous Point (RP). À medida que o fluxo multicast se estabelece, os roteadores próximos aos receptores podem realizar o SPT Switching (Shortest Path Tree Switching), migrando o tráfego para uma árvore de menor custo (S,G), eliminando o RP do caminho de dados e otimizando o encaminhamento.  

Entretanto, no **PIM Bidirectional (BIDIR)**, o conceito de **SPT Switching** não se aplica. Nesse modo, não são criadas árvores (S,G), e todo o tráfego multicast é encaminhado exclusivamente por meio de **uma única árvore compartilhada (*,G), com raiz lógica no RP**.

Essa decisão arquitetural é intencional e traz benefícios claros:

- Elimina completamente o processo de SPT switch, reduzindo overhead e complexidade operacional;
- Evita a criação de múltiplos estados (S,G) nas tabelas mroute;
- Garante previsibilidade de caminhos e estabilidade do tráfego multicast;
- Torna o PIM BIDIR altamente escalável, especialmente em cenários many-to-many com múltiplas fontes simultâneas.

Assim, diferentemente do PIM-SM, o PIM BIDIR prioriza simplicidade e escalabilidade, mantendo todo o encaminhamento multicast baseado exclusivamente na árvore compartilhada (*,G).

---

### 🧩 1️⃣ Fontes e Receptores no Cenário

Neste cenário, temos múltiplas fontes e múltiplos receptores multicast, caracterizando um ambiente **many-to-many**, típico do **PIM Bidirectional (BIDIR)**.

As fontes e receptores compartilham os mesmos grupos multicast, utilizando exclusivamente o modelo **(*,G)**, sem associação explícita a uma fonte específica.

| Função         | Dispositivo | Rede/Sub-rede   | Interface | Endereço IP     | Descrição                                      |
|----------------|-------------|-----------------|-----------|-----------------|------------------------------------------------|
| **Fonte 1**    | SERVER      | 192.168.10.0/24 | fa0/0     | 192.168.10.1    | Envia tráfego multicast para o grupo 239.1.1.1 |
| **Fonte 2**    | SERVER02    | 192.168.40.0/24 | fa0/0     | 192.168.40.1    | Envia tráfego multicast para o grupo 239.1.1.1 |
| **Receptor 1** | HOST02      | 192.168.20.0/24 | fa0/0     | 192.168.20.1    | Inscreve-se no grupo multicast via IGMP (*,G)  |
| **Receptor 2** | HOST03      | 192.168.30.0/24 | fa0/0     | 192.168.30.1    | Inscreve-se no grupo multicast via IGMP (*,G)  |
| **Receptor 3** | (opcional)  | —               | —         | —               | Pode ser adicionado em qualquer outra sub-rede |

---

### 🧭 Estrutura do Roteamento

Todos os roteadores (**R01 a R05**) participam de uma **única área OSPF (Área 0)**, garantindo conectividade unicast completa antes da ativação do multicast.  
  
Essa conectividade é essencial para:

- Construção da árvore compartilhada **(*,G)**;
- Funcionamento do **Rendezvous Point (RP)** como raiz lógica;
- Eleição correta do **Designated Forwarder (DF)** em cada enlace.  
  
| Link Ponto-a-Ponto | Rede / Máscara | Interface Local | Interface Remota |
|--------------------|----------------|-----------------|------------------|
| R01 – R02          | 10.0.0.0/30    | Fa0/1 (R01)     | Fa1/0 (R02)      |
| R02 – R03          | 10.0.0.4/30    | Fa1/0 (R02)     | Fa1/0 (R03)      |
| R03 – R04          | 10.0.0.8/30    | Fa0/0 (R03)     | Fa0/0 (R04)      |
| R04 – R05          | 10.0.0.12/30   | Fa0/1 (R04)     | Fa0/1 (R05)      |
| R05 – R01          | 10.0.0.16/30   | Fa1/0 (R05)     | Fa1/0 (R01)      |

---

### 📡 Grupos Multicast no PIM Bidirectional

No **PIM Bidirectional (BIDIR)**, os grupos multicast operam exclusivamente no modelo **(*,G)**.

| Grupo Multicast | Modelo PIM | Descrição                                          |
|-----------------|------------|----------------------------------------------------|
| 239.1.1.1       | (*,G)      | Grupo multicast compartilhado por múltiplas fontes |

Nesse modelo:  

- Não há criação de estados **(S,G)**;
- Não ocorre **SPT Switching**;
- O tráfego multicast flui bidirecionalmente pela árvore compartilhada;
- O **RP atua apenas como raiz lógica**, não como ponto de comutação de dados.

O **PIM BIDIR** prioriza simplicidade, previsibilidade e escalabilidade em cenários **many-to-many**.

### 🧩 Conclusão

Com esse modelo, o laboratório demonstra como o **PIM Bidirectional (BIDIR)** oferece um roteamento multicast **estável, previsível e altamente escalável** para cenários **many-to-many**, nos quais múltiplas fontes e múltiplos receptores participam simultaneamente do mesmo grupo multicast.  
  
Ao utilizar **apenas uma árvore compartilhada (*,G)** e eliminar completamente o **SPT Switching**, o PIM BIDIR reduz drasticamente o estado multicast nos roteadores, simplifica a operação e mantém caminhos de encaminhamento consistentes — tornando o ambiente ideal para **aplicações financeiras, colaboração em tempo real, controle distribuído e sistemas multicast de larga escala**.  
  
---

### 🛰️ O que muda no PIM Bidirectional (BIDIR)
  
Diferente do **PIM Sparse Mode tradicional (PIM-SM)**, no qual o tráfego multicast pode migrar da árvore compartilhada (*,G) para árvores de menor custo (S,G) por meio do **SPT Switching**, o **PIM Bidirectional (BIDIR)** opera **exclusivamente com uma única árvore compartilhada (*,G)**.  
  
No BIDIR:

- O **Rendezvous Point (RP)** continua existindo, mas atua apenas como **raiz lógica da árvore**, não como ponto de encontro de dados;
- O tráfego multicast **nunca é encapsulado nem redirecionado ao RP**;
- Não são criadas árvores (S,G) em nenhum momento.
  
O resultado é um domínio multicast **mais simples e previsível**, com menor consumo de recursos e maior estabilidade.  

---

#### 🌳 1️⃣ O comportamento do PIM BIDIR

No **PIM Bidirectional**, todas as fontes e receptores compartilham a **mesma árvore multicast (*,G)**.  
Não há distinção entre tráfego inicial e otimizado, pois **não existe transição de árvore**.  
  
As principais características desse comportamento são:
  
- Ausência total de **SPT Switching**;
- Uso exclusivo de estado **(*,G)** nas tabelas **mroute**;
- Caminhos de encaminhamento definidos com base na árvore compartilhada;
- Alta escalabilidade em ambientes com múltiplas fontes simultâneas.

Esse modelo é especialmente eficiente quando **não é desejável ou necessário otimizar caminhos por fonte**, priorizando simplicidade e estabilidade.

---

#### 🔹 2️⃣ O papel do IGMP no PIM BIDIR

No **PIM BIDIR**, os hosts utilizam **IGMP (tipicamente IGMPv2)** apenas para **informar interesse em um grupo multicast (G)**.  
  
Diferente do SSM:  
  
- Os hosts **não especificam fontes**;
- Não existe o conceito de inscrição (S,G);
- A decisão de encaminhamento é feita exclusivamente no domínio PIM.
  
O roteador diretamente conectado ao host (**Designated Router – DR**) registra o interesse no grupo e passa a participar da árvore compartilhada (*,G).  

---

#### 🔀 3️⃣ Designated Forwarder (DF) e prevenção de loops

Como o tráfego multicast no BIDIR pode fluir **em ambas as direções** ao longo da árvore compartilhada, o protocolo utiliza o conceito de **Designated Forwarder (DF)**.  
  
O **DF** é eleito em cada enlace multicast e é responsável por:  

- Decidir qual roteador pode encaminhar tráfego multicast naquele segmento;
- Evitar loops e duplicação de pacotes;
- Garantir encaminhamento consistente em ambientes com múltiplas fontes.
  
A eleição do DF é baseada em métricas unicast em direção ao RP.  
  
---
  
#### 🛰️ 4️⃣ Quando as fontes começam a transmitir
  
Quando uma ou mais fontes passam a enviar tráfego para um determinado grupo multicast:  
  
- O tráfego é imediatamente encaminhado pela **árvore compartilhada (*,G)**;
- Não há registro, encapsulamento ou redirecionamento para o RP;
- Todos os receptores inscritos no grupo recebem os fluxos multicast.
  
O comportamento é **simétrico e contínuo**, independentemente do número de fontes ativas.  
  
---
  
#### 📡 5️⃣ Vantagens do PIM BIDIR sobre o PIM-SM tradicional

| Aspecto                    | PIM Sparse Mode (tradicional) | PIM Bidirectional (BIDIR) |
|----------------------------|-------------------------------|---------------------------|
| Tipo de árvore             | (*,G) + (S,G)                 | Apenas (*,G)              |
| SPT Switching              | Sim                           | ❌ Não                    |
| Estado multicast           | Elevado em muitos fluxos      | Reduzido                  |
| Dependência do RP          | Funcional                     | Apenas lógica             |
| Encapsulamento (Register)  | Sim                           | ❌ Não                    |
| Escalabilidade             | Moderada                      | Alta                      |
| Modelo de comunicação      | One-to-many                   | Many-to-many              |

---

👉 **Resumo:**  
O **PIM Bidirectional (BIDIR)** é projetado para cenários multicast **de larga escala e múltiplas fontes**, onde previsibilidade, simplicidade e estabilidade são mais importantes do que a otimização individual de caminhos.  
Ao eliminar o **SPT Switching** e manter todo o domínio baseado em **uma única árvore compartilhada (*,G)**, o BIDIR se torna uma solução robusta e eficiente para ambientes corporativos e críticos.

## 🌐 Topologia do Laboratório

Este laboratório simula um cenário enterprise de multicast **many-to-many**, comum em ambientes financeiros, sistemas de colaboração em tempo real e plataformas de replicação distribuída.  
  
O objetivo é demonstrar, de forma prática e didática, o funcionamento do **PIM Bidirectional (PIM BIDIR)**, destacando sua arquitetura baseada em **árvore compartilhada (*,G)**, a ausência de **SPT Switching** e o papel do **Rendezvous Point como raiz lógica** da topologia multicast.  

A topologia deste laboratório é composta por **cinco roteadores principais (R01 a R05)** e **quatro hosts simulados (Server, Server02, Host02 e Host03)**.  
Os hosts são roteadores Cisco configurados de forma simplificada, apenas com **endereçamento IP** e **participação em grupos multicast via IGMP (tipicamente IGMPv2)**, simulando o comportamento de dispositivos finais.

O protocolo **OSPF** garante a conectividade unicast entre todos os roteadores, enquanto o **PIM Bidirectional (BIDIR)** é utilizado para o roteamento multicast.  
Diferente do **PIM Sparse Mode tradicional**, o **PIM BIDIR** utiliza **uma única árvore compartilhada (*,G)** para todos os fluxos multicast, **sem criação de estados (S,G)** e **sem SPT Switching**.

Neste modelo, múltiplas **fontes e receptores** compartilham o mesmo grupo multicast, caracterizando um ambiente **many-to-many**, no qual o tráfego flui **bidirecionalmente** ao longo da árvore, com o **Rendezvous Point (RP)** atuando apenas como **raiz lógica** do domínio multicast.

---

### 🔧 Endereçamento e Funções

| **Dispositivo** | **Interface** | **Endereço IP / Máscara** | **Conexão / Função**                                 |
|-----------------|---------------|---------------------------|------------------------------------------------------|
| **R01**         | Loopback0     | 1.1.1.1 /32               | Identificação / Router-ID OSPF                       |
|                 | Fa0/0         | 192.168.10.254 /24        | LAN do Server — Gateway multicast                    |
|                 | Fa0/1         | 10.0.0.1 /30              | Link com R02 — PIM BIDIR + OSPF                      |
|                 | Fa1/0         | 10.0.0.18 /30             | Link com R05 — PIM BIDIR + OSPF                      |
| **R02**         | Loopback0     | 2.2.2.2 /32               | Identificação / Router-ID OSPF                       |
|                 | Fa0/0         | 10.0.0.2 /30              | Link com R01 — PIM BIDIR + OSPF                      |
|                 | Fa1/0         | 10.0.0.5 /30              | Link com R03 — PIM BIDIR + OSPF                      |
| **R03**         | Loopback0     | 3.3.3.3 /32               | Identificação / Router-ID OSPF                       |
|                 | Fa0/0         | 10.0.0.6 /30              | Link com R02 — PIM BIDIR + OSPF                      |
|                 | Fa1/0         | 10.0.0.9 /30              | Link com R04 — PIM BIDIR + OSPF                      |
| **R04**         | Loopback0     | 4.4.4.4 /32               | Identificação / Router-ID OSPF                       |
|                 | Fa0/0         | 10.0.0.10 /30             | Link com R03 — PIM BIDIR + OSPF                      |
|                 | Fa1/0         | 10.0.0.13 /30             | Link com R05 — PIM BIDIR + OSPF                      |
|                 | Fa1/1         | 192.168.20.254 /24        | LAN do Host02 — Gateway multicast                    |
| **R05**         | Loopback0     | 5.5.5.5 /32               | Identificação / Router-ID OSPF                       |
|                 | Fa0/0         | 10.0.0.14 /30             | Link com R04 — PIM BIDIR + OSPF                      |
|                 | Fa1/0         | 10.0.0.17 /30             | Link com R01 — PIM BIDIR + OSPF                      |
|                 | Fa0/1         | 192.168.30.254 /24        | LAN do Host03 — Gateway multicast                    |
| **Server**      | Fa0/0         | 192.168.10.1 /24          | Fonte multicast                                      |
| **Server02**    | Fa0/0         | 192.168.40.1 /24          | Fonte multicast                                      |
| **Host02**      | Fa0/0         | 192.168.20.1 /24          | Receptor multicast (IGMP (*,G))                      |
| **Host03**      | Fa0/0         | 192.168.30.1 /24          | Receptor multicast (IGMP (*,G))                      |

---

### 📡 Grupos Multicast no PIM Bidirectional - resumo

No **PIM BIDIR**, os grupos multicast utilizam exclusivamente o modelo **(*,G)**.  
Os hosts **não escolhem fontes específicas** e todos os emissores podem enviar tráfego para o mesmo grupo multicast.

Neste laboratório, será utilizado o seguinte grupo:

| Grupo Multicast | Modelo | Descrição                                          |
|-----------------|--------|----------------------------------------------------|
| 239.1.1.1       | (*,G)  | Grupo multicast compartilhado por múltiplas fontes |

📌 **Observações importantes:**

- Não há uso de endereços SSM (232/8);
- Não existem inscrições (S,G);
- Não ocorre SPT Switching;
- O encaminhamento é controlado pelo **Designated Forwarder (DF)** em cada enlace;
- O **RP atua apenas como raiz lógica** da árvore compartilhada.

Esse comportamento reflete fielmente o funcionamento do **PIM Bidirectional (BIDIR)** em ambientes **many-to-many**, priorizando **simplicidade, previsibilidade e escalabilidade**.

---

**🧭 Resumo da Lógica**  

- O **Server (192.168.10.1)** atua como **fonte multicast**, enviando tráfego para o **grupo multicast 239.1.1.1 (G)**.  
- O **Server02 (192.168.40.1)** também atua como **fonte multicast**, enviando tráfego para o **mesmo grupo multicast 239.1.1.1 (G)**.  
- O **Host02 (192.168.20.1)** participa do domínio multicast utilizando **IGMP (tipicamente IGMPv2)**, inscrevendo-se no **grupo multicast (*,G)**.  
- O **Host03 (192.168.30.1)** participa do domínio multicast utilizando **IGMP (tipicamente IGMPv2)**, inscrevendo-se no **grupo multicast (*,G)**.  
- O protocolo **PIM Bidirectional (BIDIR)** é ativado em todas as interfaces participantes do domínio multicast (LANs e links de roteamento).  
- Os **roteadores utilizam um Rendezvous Point (RP)**, que atua **apenas como raiz lógica da árvore compartilhada**, sem receber ou encapsular tráfego multicast.  
- O encaminhamento do tráfego multicast é controlado pelo **Designated Forwarder (DF)** em cada enlace, evitando loops e duplicações.  
- O **RPF (Reverse Path Forwarding)** é utilizado para validar o encaminhamento multicast com base na **melhor rota unicast em direção ao RP**, aprendida via OSPF.  

Assim, o laboratório demonstra a operação do **PIM Bidirectional (BIDIR)**, no qual múltiplas fontes e múltiplos receptores compartilham uma **única árvore multicast (*,G)**, sem criação de estados **(S,G)** e **sem SPT Switching**, priorizando simplicidade, previsibilidade e escalabilidade.

---

### 🔍 Testes Preliminares

Antes de ativar o multicast, é essencial confirmar a **conectividade unicast** entre todos os dispositivos.

Cada roteador possui uma **interface Loopback** utilizada como **Router-ID** no OSPF:

- R01 → 1.1.1.1/32  
- R02 → 2.2.2.2/32  
- R03 → 3.3.3.3/32  
- R04 → 4.4.4.4/32  
- R05 → 5.5.5.5/32  

Após o OSPF estar operacional, valide a conectividade com **ping entre todas as loopbacks**.

![01](Imagens/01.png)

Se todos os roteadores se alcançam, a infraestrutura unicast está pronta para o multicast.  
Lembre-se: o **PIM BIDIR** depende de uma **base unicast funcional** para a correta construção da árvore compartilhada e para o processo de **eleição do Designated Forwarder (DF)**.

---

## 🚀 Ativação do Roteamento Multicast  
  
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
  
Com o roteamento multicast ativo, o próximo passo é habilitar o **PIM Bidirectional (BIDIR)** nas interfaces participantes (LANs e links entre roteadores).  
Esse procedimento deve ser repetido em R01 a R05, garantindo que todas as interfaces de roteamento façam parte do domínio **PIM BIDIR**.  

---

### 🧩 Principais Diferenças do PIM BIDIR em Relação ao PIM-SM  

| Característica            | PIM Sparse Mode (tradicional) | PIM Bidirectional (BIDIR)  |
|---------------------------|-------------------------------|----------------------------|
| Tipo de árvore            | (*,G) e (S,G)                 | Apenas (*,G)               |
| SPT Switching             | Sim                           | ❌ Não                     |
| Encapsulamento (Register) | Sim                           | ❌ Não                     |
| Uso do RP                 | Dados passam pelo RP          | RP é apenas raiz lógica    |
| Estado multicast          | Elevado                       | Reduzido                   |
| Modelo de comunicação     | One-to-many                   | Many-to-many               |
| Escalabilidade            | Moderada                      | Alta                       |

---

### 🌍 Onde o PIM Deve Ser Ativado

No PIM Bidirectional **(BIDIR)**, o tráfego multicast é encaminhado por meio de uma única **árvore compartilhada (*,G)**, utilizada simultaneamente por **múltiplas fontes e múltiplos receptores**.  
  
Diferente do PIM-SM tradicional e do SSM, o **BIDIR**:

- Não cria estados **(S,G)**;
- Não realiza **SPT Switching**;
- Não encapsula tráfego multicast;
- Utiliza o **Rendezvous Point (RP) apenas como raiz lógica da árvore**.  
  
Apesar disso, o PIM deve ser ativado em todas as interfaces que participam do domínio multicast, garantindo a troca correta de mensagens PIM Join/Prune (*,G) e a eleição adequada do Designated Forwarder (DF).  

✅ **Interfaces onde o PIM deve ser ativado**

| Situação                           | PIM deve ser ativado? | Motivo                                                 |
|------------------------------------|-----------------------|--------------------------------------------------------|
| Interface entre roteadores         | ✅ Sim                | Construção da árvore (*,G) e troca de mensagens PIM    |
| Interface com host receptor (IGMP) | ✅ Sim                | Registro de interesse no grupo multicast               |
| Interface com fonte multicast      | ✅ Sim                | Inserção correta do tráfego multicast na árvore (*,G)  |
| Loopback apenas como Router-ID     | ⚙️ Opcional           | Usada apenas para identificação OSPF                   |

---

### 💡 Observação Sobre as Fontes Multicast

No PIM Bidirectional (BIDIR):

- As fontes multicast **não se registram em RP**;
- Não existem mensagens **PIM Register**;
- O tráfego multicast é inserido diretamente na **árvore compartilhada (*,G)** pelo roteador conectado à fonte;
- O encaminhamento é controlado pelo **Designated Forwarder (DF)** em cada enlace.
- Todas as fontes que enviam tráfego para o mesmo grupo multicast **compartilham a mesma árvore**, sem criação de caminhos independentes por fonte.

No contexto deste laboratório, **SERVER e SERVER02** transmitem simultaneamente para o mesmo grupo multicast (ex.: 239.1.1.1).  
Todos os receptores inscritos nesse grupo passam a receber os fluxos multicast, independentemente de qual fonte os originou.  
  
Diferente do SSM:  
  
- O receptor **não escolhe fontes específicas**;
- Não há filtragem por origem;
- O controle ocorre exclusivamente no domínio PIM.

---

💡 **Em resumo:**  
  
O **PIM Bidirectional (BIDIR)** elimina a complexidade associada ao **SPT Switching** e à criação de múltiplas árvores multicast, mantendo todo o domínio baseado em **uma única árvore compartilhada (*,G)**.  
  
Esse modelo oferece simplicidade operacional, previsibilidade de caminhos e alta escalabilidade, sendo ideal para ambientes **many-to-many com múltiplas fontes ativas**.  

🎯 **Situação**

Você tem:  
  
- **Server01 (192.168.10.10)** transmitindo tráfego multicast  
- **Server02 (192.168.40.10)** transmitindo tráfego multicast  
- Ambos transmitem para **o mesmo grupo multicast (G)**, por exemplo **239.1.1.1**
- **Host01** quer receber **todo o tráfego multicast desse grupo**, independentemente de qual servidor seja a fonte
  
Esse cenário representa um modelo clássico **many-to-many**, ideal para **PIM Bidirectional (BIDIR)**.

---

🧠 **Como o PIM BIDIR trata isso?**

No **PIM Bidirectional**, o encaminhamento multicast **não é baseado em (S,G)**.  
Ele utiliza **exclusivamente a árvore compartilhada (*,G)**.

Isso significa que:

- O **host não escolhe fontes**
- Não existe controle por origem
- Todas as fontes que transmitem para o grupo **compartilham a mesma árvore multicast**

O **IGMP (v2 ou v3)** é usado **apenas para sinalizar interesse no grupo (G)**.

---

📩 **Sinalização do Host (IGMP)**

O **Host01** envia **um único IGMP Report**, informando que deseja participar do grupo multicast:

```text
IGMP Report (*, 239.1.1.1)
```  

📩 **Sinalização do Host (IGMP)**

No **PIM BIDIR**, **não há INCLUDE (S,G)** nem qualquer tipo de **seleção de fonte**.  
O host simplesmente sinaliza interesse **no grupo multicast (G)**.

> “Quero receber o grupo **239.1.1.1**.”

---

🔁 **O que acontece no roteador (Designated Router – DR)**

- O roteador conectado ao **Host01** recebe o **IGMP Join para o grupo (G)**  
- Ele cria **uma única entrada multicast (*,G)** na sua tabela  
- O roteador envia **PIM Join (*,G)** na direção do **Rendezvous Point (RP)**  

⚠️ **Importante**  
No **PIM BIDIR**, o **RP é apenas a raiz lógica da árvore multicast**.  
Ele:

- ❌ Não recebe tráfego  
- ❌ Não realiza encapsulamento  
- ❌ Não participa do caminho de dados  

---

🌳 **Construção da Árvore Multicast**

- Uma **única árvore (*,G)** é construída para o grupo **239.1.1.1**
- Essa árvore é usada **simultaneamente por todas as fontes e todos os receptores**
- **Não ocorre**:
  - ❌ SPT Switching  
  - ❌ Criação de árvores (S,G)  
  - ❌ PIM Register  

O tráfego multicast entra na árvore pelo **roteador conectado à fonte**, respeitando o papel do **Designated Forwarder (DF)** em cada enlace.

---

🔎 **Visualmente**

```text
      Server01 (192.168.10.10)
                │
                │
      Server02 (192.168.40.10)
                │
                ▼
          Árvore Compartilhada (*,G)
                │
          [RP – raiz lógica]
                │
          [Roteador DR]
                │
                ▼
             [Host01]
```  

O **Host01** recebe todo o tráfego multicast do grupo **239.1.1.1**, vindo de:

- **Server01**
- **Server02**

Sem qualquer distinção por origem.

---

### 🧩 E se o Host01 quiser apenas uma das fontes?

➡️ **Não é possível no PIM BIDIR.**

O modelo não permite filtragem por fonte, pois:

- Não existem estados **(S,G)**
- O **IGMP não controla origem**
- O **PIM encaminha todo o tráfego do grupo**

Se esse tipo de controle for necessário, o modelo correto é **SSM com IGMPv3**.

---

### 🚫 E se o Host01 quiser bloquear uma das fontes?

➡️ **Também não é possível no PIM BIDIR.**

O BIDIR assume que:

- Todas as fontes do grupo são válidas
- O controle de conteúdo ocorre **na aplicação**, não na rede
- O foco é **simplicidade, escalabilidade e previsibilidade**

---

### 🧠 Resumo Final

- **PIM BIDIR trabalha apenas com (*,G)**
- Uma **única árvore multicast** é usada por todas as fontes
- **Não há SPT Switching** nem seleção de fonte
- Ideal para cenários **many-to-many**
- Controle por origem **não faz parte do modelo**

Esse comportamento torna o **PIM Bidirectional** extremamente eficiente em ambientes com **múltiplas fontes ativas**, como aplicações financeiras, sistemas de replicação e serviços de colaboração em tempo real.
  
💬 **Resumo final**  
  
| Caso                        | IGMP Join enviado pelo host | Resultado no PIM BIDIR             |
|-----------------------------|-----------------------------|------------------------------------|
| Host quer Server01          | Join (*,G)                  | Recebe tráfego do Server01         |
| Host quer Server02          | Join (*,G)                  | Recebe tráfego do Server02         |
| Host quer os dois           | Join (*,G)                  | Recebe tráfego de ambas as fontes  |
| Host quer excluir uma fonte | Não suportado               | Recebe todo o tráfego do grupo     |

👉 **Em resumo:**  

- No PIM Bidirectional, o controle é feito apenas por grupo (*,G).
- Não existe seleção, exclusão ou combinação de fontes no nível da rede.
- Todos os fluxos pertencentes ao grupo multicast são encaminhados pela mesma árvore.
  
---

⚙️ **Nosso cenário PIM BIDIR**  

Nosso laboratório considera múltiplas fontes multicast ativas simultaneamente, todas transmitindo para o mesmo grupo multicast, caracterizando um cenário many-to-many.  
  
| Fonte     | Roteador conectado | Sub-rede        | Grupo multicast utilizado   |
|-----------|--------------------|-----------------|-----------------------------|
| SERVER    | R01                | 192.168.10.0/24 | 239.1.1.1                   |
| SERVER02  | R03                | 192.168.40.0/24 | 239.1.1.1                   |

Os receptores multicast (hosts simulados) não especificam fontes.  
Eles apenas ingressam no grupo multicast desejado, por exemplo 239.1.1.1, e passam a receber todo o tráfego associado a esse grupo, independentemente da origem.  
  
📡 **Papel do IGMP no PIM BIDIR**  
  
No PIM BIDIR, o IGMP é utilizado somente para sinalizar interesse no grupo multicast (G).

- Não existe INCLUDE (S,G)
- Não existe EXCLUDE (S,G)
- Não há Source Filtering

| Tipo de Mensagem IGMP | Descrição                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| Membership Report     | Informa ao roteador local que o host deseja receber o grupo multicast (G) |
| Leave Group           | Indica que o host não quer mais receber o tráfego do grupo                |

O IGMP não controla origem no modelo Bidirectional.  
  
🔁 **Funcionamento geral do PIM BIDIR**  
  
1. O receptor envia um IGMP Join solicitando apenas o grupo multicast (G).
2. O roteador de borda (Designated Router) cria uma entrada (*,G) na tabela multicast.
3. O roteador envia PIM Join (*,G) em direção ao Rendezvous Point (RP).
4. Uma única árvore multicast compartilhada (*,G) é construída.
5. Todas as fontes injetam tráfego nessa árvore, e todos os receptores recebem.
  
Não ocorre:  

- SPT Switching
- Criação de árvores (S,G)
- PIM Register
- Encapsulamento de tráfego no RP
  
🧱 **No nosso laboratório**
  
O PIM Bidirectional será ativado em todos os roteadores e interfaces relevantes:  

- Entre os roteadores R01 a R05, formando o domínio PIM BIDIR
- Nas interfaces LAN conectadas às fontes multicast (SERVER e SERVER02)
- Nas interfaces LAN conectadas aos receptores (Host02 e Host03)
- Nas Loopbacks, apenas como Router-ID para OSPF
- O Rendezvous Point (RP) é configurado manualmente e atua como raiz lógica da árvore, sem receber ou encaminhar tráfego multicast.

🧩 **Resumo prático**  
  
| Elemento                 | Função no cenário                                 |
|--------------------------|---------------------------------------------------|
| SERVER (192.168.10.10)   | Fonte multicast (grupo 239.1.1.1)                 |
| SERVER02 (192.168.40.10) | Segunda fonte multicast (mesmo grupo)             |
| Host02 / Host03          | Receptores multicast (Join apenas por grupo)      |
| Roteadores R01–R05       | Encaminham tráfego via PIM BIDIR                  |
| OSPF                     | Mantém conectividade unicast (base para RPF)      |
| RP                       | Raiz lógica da árvore (*,G), sem tráfego de dados |

💬 **Conclusão**  

O **PIM Bidirectional (BIDIR)** oferece uma arquitetura multicast simples, previsível e altamente escalável, ideal para **cenários many-to-many**.  
Ao utilizar **uma única árvore compartilhada (*,G)**, o modelo elimina a complexidade de múltiplas árvores por fonte, dispensa SPT Switching e reduz drasticamente o estado multicast nos roteadores.  

O controle por origem não faz parte do modelo — todo o tráfego pertencente ao grupo é encaminhado igualmente.  
Esse comportamento torna o PIM BIDIR especialmente adequado para ambientes como sistemas financeiros, replicação distribuída, colaboração em tempo real e aplicações com múltiplos produtores simultâneos.  

## ⚙️ Ativando o protocolo PIM Bidirectional (PIM-BIDIR)

Com o ambiente **unicast totalmente operacional** e os conceitos de **multicast many-to-many** já estabelecidos, é hora de ativar o **PIM Bidirectional (PIM-BIDIR)** nos roteadores do domínio multicast.

Este modelo é indicado para cenários em que **múltiplas fontes e múltiplos receptores** participam simultaneamente de um mesmo grupo multicast, como em ambientes financeiros, colaboração em tempo real e aplicações distribuídas.

Diferente do **PIM-SSM**, onde os receptores solicitam explicitamente pares **(S,G)** via **IGMPv3**, o **PIM-BIDIR** trabalha exclusivamente com **(*,G)** e utiliza um **Rendezvous Point (RP)** estável como ponto lógico central para o encaminhamento do tráfego.

No BIDIR:

- Não há construção de **Shortest Path Tree (SPT)**  
- Não existem mensagens **PIM Register**
- O tráfego flui **bidirecionalmente** em direção ao RP ao longo de uma **árvore compartilhada**

---

### 🔧 Configuração do PIM-BIDIR

O PIM deve ser habilitado em **todas as interfaces que transportarão tráfego multicast**, incluindo:

- LANs com **fontes e receptores**
- Links **entre roteadores**
- Interfaces envolvidas no caminho até o **RP**

> ⚠️ **Importante:** Para que o PIM-BIDIR funcione corretamente, o **RP deve estar previamente configurado como BIDIR** em todos os roteadores do domínio multicast.

#### Exemplo – Ativando o PIM nas interfaces do R01

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

Após essa configuração, o roteador passa a participar do domínio multicast BIDIR, trocando mensagens **PIM Hello**, elegendo **Designated Routers (DR)** nas LANs e encaminhando tráfego multicast ao longo da **árvore compartilhada (*,G).**  
  
📌 **OBS**: Este procedimento deve ser repetido em todos os roteadores do domínio multicast (R01 a R05).
  
✅ **Verificação do roteamento multicast**  
  
Para confirmar que o roteamento multicast está ativo:

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
R01#show ip mroute
IP Multicast Routing Table
Flags: D - Dense, S - Sparse, B - Bidir Group, s - SSM Group, C - Connected,
       L - Local, P - Pruned, R - RP-bit set, F - Register flag,
       T - SPT-bit set, J - Join SPT
...
(*, 224.0.1.40), 00:12:34/00:02:25, RP 1.1.1.1, flags: BSR
  Incoming interface: FastEthernet0/1, RPF nbr 10.0.0.2
  Outgoing interface list:
    FastEthernet0/0, Forward/Bidir, 00:12:34/00:02:25
```

💡 **Dica Importante:**
Em um domínio PIM-BIDIR, somente **entradas (*,G) são criadas**.  
Não existem **estados (S,G)**, nem comutação para **SPT**.  
O **RP** atua como **referência lógica**, e o tráfego multicast flui de forma **bidirecional** ao longo da árvore compartilhada, garantindo **escalabilidade e simplicidade em ambientes many-to-many.**  

A entrada **(*,224.0.1.40)** representa tráfego de controle do PIM e aparece independentemente de fontes ou receptores. Entradas **(,239.x.x.x)** só são criadas quando há interesse explícito via IGMP ou tráfego multicast ativo, especialmente em cenários PIM-BIDIR.  

## 🧩 Eleição do Designated Router (DR) no PIM-BIDIR

Mesmo no **PIM Bidirectional (PIM-BIDIR)**, o **Designated Router (DR)** continua existindo e sendo eleito em cada **LAN multicast com hosts**.

O DR é o roteador responsável por representar aquela LAN dentro do domínio multicast, atuando como ponto de interconexão entre os **hosts IGMP** e a **árvore multicast (*,G)**.

No PIM-BIDIR, o DR:

- Recebe relatórios **IGMP (*,G)** dos hosts
- Cria estado multicast **(*,G)** local
- Encaminha o interesse do grupo em direção ao **Rendezvous Point (RP BIDIR)**
- **Não interpreta pares (S,G)**
- **Não envia mensagens PIM Register**
- **Não constrói Shortest Path Tree (SPT)**

A eleição do DR ocorre automaticamente entre os roteadores PIM conectados à mesma LAN.

### ⚙️ Critérios de eleição do DR

- O roteador com o **maior endereço IP ativo na LAN** é eleito DR;
- Em caso de falha, um novo DR é eleito após o **timeout das mensagens PIM Hello** (30 segundos por padrão).

💡 **Essa eleição ocorre de forma transparente e não requer configuração manual.**

---

## 💬 Mensagens PIM Hello no PIM-BIDIR

As mensagens **PIM Hello** são utilizadas para o estabelecimento e manutenção de vizinhanças PIM.  
Elas são enviadas periodicamente ao grupo **224.0.0.13 (PIM Routers)** com **TTL 1**, garantindo que apenas roteadores na mesma LAN participem da vizinhança.

Essas mensagens são responsáveis por:

- Descobrir roteadores PIM vizinhos
- Negociar parâmetros operacionais
- Eleger o **Designated Router (DR)** por segmento LAN

No **PIM-BIDIR**, as mensagens Hello **não sinalizam fontes**, **não criam estados (S,G)** e **não iniciam SPTs**.  
Elas mantêm exclusivamente o **plano de controle multicast**.

### ⚙️ Funções principais das mensagens Hello

| Função                     | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| Descoberta de vizinhos     | Identifica roteadores PIM ativos na mesma LAN                              |
| Troca de parâmetros        | Define holdtime, prioridade de DR e capacidades PIM                        |
| Eleição do DR              | Permite a escolha automática do DR por segmento LAN                        |
| Monitoramento              | Remove vizinhos inativos após o tempo de holdtime                          |

---

### 🧩 Estrutura simplificada da mensagem PIM Hello

| Campo           | Função                                                  | Valor típico |
|-----------------|---------------------------------------------------------|--------------|
| Type            | Tipo da mensagem PIM (Hello = 0x00)                     | 0x00         |
| Holdtime        | Tempo máximo sem Hellos antes de remover o vizinho      | 105 s        |
| DR Priority     | Prioridade do DR (maior vence)                          | 1 (padrão)   |
| Generation ID   | Identificador que muda a cada reboot                    | Aleatório    |
| Hello Interval  | Intervalo entre mensagens Hello                         | 30 s         |

💡 **Dica:**  
Use o Wireshark com o filtro **`pim.type == 0`** para observar as mensagens PIM Hello em tempo real.

---

## 🔍 Exemplo de log da eleição do DR

```ios
*Mar  1 02:00:36.563: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.18 on interface FastEthernet1/0
```
  
👉 O roteador **10.0.0.18** foi eleito Designated Router na interface FastEthernet1/0, passando **a representar aquela LAN no domínio multicast BIDIR.**  
  
## 🧭 Surgimento do Designated Forwarder (DF) no PIM-BIDIR

Além do **DR, o PIM-BIDIR** introduz um novo papel exclusivo: **o Designated Forwarder (DF)**.  
  
**O DF não substitui o DR.**  
Eles coexistem e atuam em pontos diferentes da topologia, resolvendo problemas distintos.  

O **Designated Forwarder (DF)** é responsável por controlar **o encaminhamento efetivo do tráfego multicast em cada enlace entre roteadores, evitando loops em uma árvore bidirecional (*,G)**.  

A eleição do DF:  

- Ocorre por enlace, e não por LAN de hosts
- É baseada no RPF em direção ao RP
- Define qual roteador pode encaminhar tráfego multicast naquele link

## 📊 Comparação clara: DR × DF no PIM-BIDIR

| Característica              | Designated Router (DR)    | Designated Forwarder (DF)  |
|-----------------------------|---------------------------|----------------------------|
| Existe no PIM-BIDIR         | ✅ Sim                    | ✅ Sim                    |
| Onde atua                   | LAN com hosts             | Enlaces entre roteadores   |
| Interage com hosts          | ✅ Sim                    | ❌ Não                    |
| Recebe IGMP                 | ✅ Sim                    | ❌ Não                    |
| Tipo de estado multicast    | (*,G)                     | (*,G)                      |
| Base da eleição             | Maior IP / prioridade     | RPF em direção ao RP       |
| Encaminha tráfego multicast | ❌ Não (controle apenas)  | ✅ Sim                    |
| Evita loops                 | ❌ Não                    | ✅ Sim                    |

💡 **Resumo conceitual importante:**  
No **PIM-BIDIR, o Designated Router (DR)** continua sendo o ponto de entrada da LAN multicast, enquanto o **Designated Forwarder (DF) é o mecanismo que garante encaminhamento bidirecional sem loops na árvore compartilhada (*,G)**.

## 🧪 Identificação do Designated Router (DR) no Domínio PIM

Até este ponto do laboratório, **nenhuma configuração explícita de DR ou DF foi realizada**.  
Foram aplicados apenas os comandos:

- `ip multicast-routing`
- `ip pim sparse-mode` nas interfaces

Mesmo assim, o **Designated Router (DR)** já é automaticamente eleito em cada segmento LAN multicast.

Isso ocorre porque:

- A **eleição do DR é implícita**
- Baseia-se exclusivamente nas **mensagens PIM Hello**
- Não depende de RP, SSM ou BIDIR configurado

---

## ⚙️ Como o DR é eleito neste estágio

Em qualquer LAN com dois ou mais roteadores PIM:

1. Todos enviam **PIM Hello** para o grupo `224.0.0.13`
2. Os Hellos carregam:
   - Endereço IP da interface
   - DR Priority (default = 1)
3. O roteador com o **maior IP ativo na LAN** é eleito **DR**

📌 **Nenhum comando adicional é necessário.**

---

## 🔍 Comandos para identificar o DR

### 0️⃣ Verificar em que interfaces o PIM está ativado

```ios
R01#show ip pim interface

Address          Interface                Ver/   Nbr    Query  DR     DR
                                          Mode   Count  Intvl  Prior
192.168.10.254   FastEthernet0/0          v2/S   0      30     1      192.168.10.254
10.0.0.1         FastEthernet0/1          v2/S   1      30     1      10.0.0.2
10.0.0.18        FastEthernet1/0          v2/S   1      30     1      10.0.0.18
R01#
```

### 1️⃣ Verificar vizinhança PIM

```ios
R01#show ip pim neighbor
PIM Neighbor Table
Mode: B - Bidir Capable, DR - Designated Router, N - Default DR Priority,
      S - State Refresh Capable
Neighbor          Interface                Uptime/Expires    Ver   DR
Address                                                            Prio/Mode
10.0.0.2          FastEthernet0/1          00:05:29/00:01:40 v2    1 / DR S
10.0.0.17         FastEthernet1/0          00:05:29/00:01:40 v2    1 / S
R01#
```

### 2️⃣ Verificar logs de eleição do DR em tempo real

```ios
R01#terminal monitor

%PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 10.0.0.2 on interface FastEthernet0/1
```

### 3️⃣ Confirmar a interface LAN envolvida

```ios
R01#show ip pim neighbor
PIM Neighbor Table
Mode: B - Bidir Capable, DR - Designated Router, N - Default DR Priority,
      S - State Refresh Capable
Neighbor          Interface                Uptime/Expires    Ver   DR
Address                                                            Prio/Mode
10.0.0.17         FastEthernet1/0          00:04:13/00:01:27 v2    1 / S
10.0.0.2          FastEthernet0/1          00:03:54/00:01:15 v2    1 / DR S
  
R01#show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            192.168.10.254  YES NVRAM  up                    up
FastEthernet0/1            10.0.0.1        YES NVRAM  up                    up
FastEthernet1/0            10.0.0.18       YES NVRAM  up                    up
Loopback0                  1.1.1.1         YES NVRAM  up                    up
R01#
```

### 🧠 Evidência via captura de pacotes (Wireshark)

Vamos entrar em R01 e ativar a captura de pacotes na Interface **FastEthernet0/1** com o seguinte filtro:  

```Whireshark
pim.type == 0
```

![Whireshark](Imagens/Whireshark01.png)

### ✅ Conclusão deste estágio do laboratório

- O DR já existe, mesmo sem configuração manual
- A eleição ocorre automaticamente via PIM Hello

O DR é válido para:

- Receber mensagens IGMP
- Representar a LAN no domínio multicast
- Servir como base para os próximos passos (RP e DF)

🚧 **Importante:**
Neste momento não existe DF, pois:

- O RP BIDIR ainda não foi configurado
- O DF só surge em cenários PIM-BIDIR, após a definição do RP

---

alterar daqui

---


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

