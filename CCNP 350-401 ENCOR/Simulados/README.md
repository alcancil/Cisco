# 📚 Guia de Uso — Simulados e Dashboard (CCNP ENCOR 350-401)

- [📚 Guia de Uso — Simulados e Dashboard (CCNP ENCOR 350-401)](#-guia-de-uso--simulados-e-dashboard-ccnp-encor-350-401)
  - [🎯 Objetivo deste Material](#-objetivo-deste-material)
  - [🧠 Como o Conteúdo Está Organizado](#-como-o-conteúdo-está-organizado)
  - [🧪 Simulados: Como Funcionam](#-simulados-como-funcionam)
    - [Características:](#características)
  - [📊 Dashboard: Acompanhamento de Desempenho](#-dashboard-acompanhamento-de-desempenho)
    - [O que o dashboard mostra:](#o-que-o-dashboard-mostra)
  - [⚠️ Importante — Armazenamento Local](#️-importante--armazenamento-local)
    - [🚨 Atenção:](#-atenção)
  - [🔄 Evolução Contínua dos Simulados](#-evolução-contínua-dos-simulados)
  - [🧪 Simulados Disponíveis (Exemplo Atual — STP)](#-simulados-disponíveis-exemplo-atual--stp)
    - [📍 Infrastructure → STP (Spanning Tree Protocol)](#-infrastructure--stp-spanning-tree-protocol)
      - [Parte 01 — Revisão](#parte-01--revisão)
      - [Parte 02 — Revisão](#parte-02--revisão)
      - [Parte 03 — Revisão](#parte-03--revisão)
      - [Parte 04 — Revisão](#parte-04--revisão)
  - [🚀 Como Utilizar (Fluxo Recomendado)](#-como-utilizar-fluxo-recomendado)
  - [👥 Público-Alvo](#-público-alvo)
  - [🧩 Filosofia do Projeto](#-filosofia-do-projeto)
  - [📌 Observação Final](#-observação-final)
  - [💬 Resumo](#-resumo)

## 🎯 Objetivo deste Material

Este repositório foi estruturado com base no blueprint oficial do CCNP ENCOR (350-401), organizando o conteúdo em tópicos e subtópicos progressivos.

A proposta é simples:

- 📖 Você estuda a teoria por tópico  
- 🧪 Valida o conhecimento com simulados práticos  
- 📊 Acompanha sua evolução através de um dashboard  

Esse fluxo cria um ciclo contínuo de aprendizado:

> **Estudar → Praticar → Medir → Evoluir**

---

## 🧠 Como o Conteúdo Está Organizado

A estrutura segue exatamente a lógica do blueprint da Cisco:

- Cada **pasta principal** representa um domínio (ex: Architecture, Infrastructure, Automation)
- Cada **subpasta** representa um tópico ou subtópico
- Dentro de cada tópico você encontrará:
  - Conteúdo teórico (Markdown)
  - Pasta `Imagens/`
  - Pasta `Arquivos/`
    - Onde ficam os **simulados**

---

## 🧪 Simulados: Como Funcionam

Ao final de cada tópico teórico, você encontrará um ou mais simulados.

### Características:

- ⏱️ Tempo controlado por simulado  
- 📊 Barra de progresso  
- ✅ Feedback imediato (acerto/erro)  
- 📖 Explicação detalhada de cada questão  
- 👤 Identificação do usuário (nome)  

Cada simulado foi projetado para:

- Reforçar conceitos importantes  
- Simular cenários de prova  
- Desenvolver raciocínio técnico  

---

## 📊 Dashboard: Acompanhamento de Desempenho

Todos os resultados dos simulados são armazenados localmente no navegador.

### O que o dashboard mostra:

- Total de simulados realizados  
- Total de questões respondidas  
- Percentual geral de acerto  
- Tempo médio por tentativa  
- Histórico completo de execuções  
- Gráficos de evolução (Chart.js)  

---

## ⚠️ Importante — Armazenamento Local

Os dados do dashboard utilizam:

> `localStorage` do navegador

Isso significa que:

- ✔️ Os dados ficam salvos no seu navegador  
- ❌ NÃO existe banco de dados externo  
- ❌ NÃO há sincronização entre dispositivos  

### 🚨 Atenção:

Se você:

- Limpar o cache do navegador  
- Usar aba anônima  
- Trocar de navegador ou computador  

➡️ **Você perderá todo o histórico de desempenho**

---

## 🔄 Evolução Contínua dos Simulados

Este projeto está em constante evolução.

- Novos simulados serão adicionados gradualmente  
- A lista abaixo será atualizada conforme novos conteúdos forem desenvolvidos  
- Nem todos os tópicos possuem simulados ainda (em construção)  

---

## 🧪 Simulados Disponíveis (Exemplo Atual — STP)

### 📍 Infrastructure → STP (Spanning Tree Protocol)

#### Parte 01 — Revisão

- Simulados temáticos:
  - Frame & Loop  
  - BPDU & Eleição  
  - Port Roles  
  - Timers  
  - TCN & Falhas  

- Simulado completo:
  - 50 questões  

- Dashboard:
  - Painel de desempenho consolidado  

📘 Parte 01 – Revisão - [Simulado Parte 01](https://alcancil.github.io/Cisco/CCNP%20350-401%20ENCOR/03%20-%20Infrastructure/02%20-%20STP%20(Spanning%20Tree%20Protocol)/01%20-%20Revisao/Arquivos/Simulado/)

#### Parte 02 — Revisão

- Simulados temáticos:
  - Port States: Os 5 Estados
  - Timers: Hello Time, Max Age e Forward Delay
  - Switch L2 vs L3 e Tabela CAM  
  - Reconvergência e Fluxo de Boot-Up
  - Topologia 3-Tier, Decisão de Encaminhamento e Visão Geral  

- Simulado completo:
  - 50 questões  

- Dashboard:
  - Painel de desempenho consolidado

📘 Parte 02 – Revisão - [Simulado Parte 02](https://alcancil.github.io/Cisco/CCNP%20350-401%20ENCOR/03%20-%20Infrastructure/02%20-%20STP%20(Spanning%20Tree%20Protocol)/02%20-%20Revisao%20-%20Parte%2002/Arquivos/Simulado/)

#### Parte 03 — Revisão

- Simulados temáticos:
  - Evolução do STP e BPDU  
  - Bridge ID: Estrutura e Cálculo  
  - Eleição do Root Bridge e Papéis de Porta  
  - Critérios de Desempate (Tie-Breakers)  
  - Consolidação: Estados, Convergência e Evolução  

- Simulado completo:
  - 50 questões  

- Dashboard:
  - Painel de desempenho consolidado

📘 Parte 03 – Revisão - [Simulado Parte 03](https://alcancil.github.io/Cisco/CCNP%20350-401%20ENCOR/03%20-%20Infrastructure/02%20-%20STP%20(Spanning%20Tree%20Protocol)/03%20-%20Revisao%20Parte%2003/Arquivos/Simulado/)

#### Parte 04 — Revisão

- Simulados temáticos:
  - Posicionamento do Root Bridge e Design de Rede  
  - Bridge ID: Estrutura e Cálculo  
  - Eleição do Root Bridge e Papéis de Porta
  - Critérios de Desempate (Tie-Breakers)
  - Consolidação: Estados, Convergência e Evolução

- Simulado completo:
  - 50 questões  

- Dashboard:
  - Painel de desempenho consolidado

📘 Parte 04 – Revisão - [Simulado Parte 04](https://alcancil.github.io/Cisco/CCNP%20350-401%20ENCOR/03%20-%20Infrastructure/02%20-%20STP%20(Spanning%20Tree%20Protocol)/04%20-%20Revisao%20Parte%2004/Arquivos/Simulado/)

---

## 🚀 Como Utilizar (Fluxo Recomendado)

1. Estude o conteúdo teórico do tópico  
2. Execute os simulados daquele tópico  
3. Analise seu desempenho no dashboard  
4. Revise os pontos de erro  
5. Avance para o próximo tópico  

---

## 👥 Público-Alvo

Este material foi desenvolvido para atender diferentes perfis:

- 👨‍🎓 Estudantes iniciantes em redes  
- 🧑‍🏫 Instrutores Cisco  
- 💼 Recrutadores técnicos  
- 📊 Recrutadores de RH  
- 🧑‍💻 Analistas e Engenheiros de Redes  
- 🧠 Profissionais experientes buscando revisão estruturada  

---

## 🧩 Filosofia do Projeto

O objetivo não é apenas ensinar teoria.

É desenvolver:

- Raciocínio lógico  
- Capacidade de troubleshooting  
- Interpretação de cenários  
- Preparação real para certificação  

---

## 📌 Observação Final

Este material é vivo.

Ele cresce conforme novos tópicos são estudados, estruturados e transformados em prática.

> Aprender redes não é decorar comandos.  
> É entender comportamento.

---

## 💬 Resumo

📘 Estude  
🧪 Teste  
📊 Meça  
🚀 Evolua  