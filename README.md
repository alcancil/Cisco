# Jornada Cisco Networking 🌐

Bem-vindo ao meu repositório de estudos e desenvolvimento em **Networking Cisco**! Este espaço é um reflexo da minha jornada contínua no universo da Tecnologia da Informação, com foco na aquisição e aprofundamento de certificações que validam e expandem minhas habilidades em infraestrutura de redes.

---

## 📋 Índice

- [Jornada Cisco Networking 🌐](#jornada-cisco-networking-)
  - [📋 Índice](#-índice)
  - [🎯 Propósito do Repositório](#-propósito-do-repositório)
  - [🎓 Certificações](#-certificações)
  - [🎓 Certificados](#-certificados)
  - [⚙️ Padrões de Engenharia](#️-padrões-de-engenharia)
    - [Dicionário Semântico](#dicionário-semântico)
    - [Workflow de Commits Semânticos](#workflow-de-commits-semânticos)
  - [🏛️ Arquitetura do Repositório](#️-arquitetura-do-repositório)
  - [🛠️ Ecossistema de Ferramentas](#️-ecossistema-de-ferramentas)
  - [🗺️ Roadmap de Estudos](#️-roadmap-de-estudos)
  - [💡 Guia de Navegação](#-guia-de-navegação)
  - [📚 Base de Conhecimento e Padrões](#-base-de-conhecimento-e-padrões)
  - [✉️ Contato](#️-contato)

---

## 🎯 Propósito do Repositório

Este repositório serve como um **portfólio técnico dinâmico** e um **hub de conhecimento** para minha jornada de certificações Cisco. Ele demonstra minha abordagem estruturada e profissional para o aprendizado contínuo, aplicando princípios de engenharia de software à documentação e prática de redes. Aqui, você encontrará:

- **Documentação Detalhada:** Notas de estudo, resumos e insights sobre tecnologias de rede.
- **Laboratórios Práticos:** Implementações de cenários reais com configurações e topologias.
- **Projetos de Automação:** Scripts e ferramentas desenvolvidas para otimizar a gestão e operação de redes.
- **Aplicação de Boas Práticas:** Demonstração de um workflow de desenvolvimento profissional, incluindo commits semânticos e versionamento.

---

## 🎓 Certificações

Minha dedicação à excelência em redes é evidenciada pelas minhas certificações e objetivos futuros:

| Status        | Certificação                                         | Validade | Badges |
| :---          | :---                                                 | :---     | :---   |
| ✅ Ativa     | **Cisco Certified Network Associate (CCNA)**          | 2028     | [![CCNA](https://img.shields.io/badge/Cisco-CCNA_Certified-blue?logo=cisco&logoColor=white)](https://www.credly.com/badges/7ea5831f-be04-41f6-80bd-38e20d0f60a1/public_url) | 
| 📖 Em Estudo | **CCNP Enterprise Core (ENCOR 350-401)**              | -        | |
| 🚀 Futuro    | **CCNP Enterprise Advanced Routing (ENARSI 300-410)** | -        | |

---

## 🎓 Certificados

Minha dedicação à excelência em redes é evidenciada também pelas meus certificados.

| Status         | Certificação                                         | Obtido em | Badges |
| :---           | :---                                                 | :---     | :---   |
| ✅ Completado  | **Python Essentials 01 - PCAP 01**                   | 2023     | [![Python Essentials 1 - PCAP1](https://img.shields.io/badge/Python-Essentials-yellow?logo=python&logoColor=white)](https://www.credly.com/badges/90325923-fdaa-4f86-ba62-ffdb7077906e/public_url) |
| ✅ Completado  | **Python Essentials 02 - PCAP 02**                   | 2023     | [![Python Essentials 2 - PCAP2](https://img.shields.io/badge/Python-Essentials-yellow?logo=python&logoColor=white)](https://www.credly.com/badges/e4f2b4af-a5cc-4a10-a31a-71fb00286c40/public_url) |  

---

## ⚙️ Padrões de Engenharia

Para garantir um histórico de projeto limpo, rastreável e profissional, adoto as seguintes práticas:

### Dicionário Semântico

Organizo arquivos e pastas de forma lógica e consistente, utilizando uma nomenclatura clara que reflete o conteúdo e a hierarquia dos estudos. Isso facilita a localização de informações e a compreensão da estrutura do projeto.

### Workflow de Commits Semânticos

Utilizo um padrão de **Commits Semânticos** para descrever as alterações de forma padronizada, o que melhora a legibilidade do histórico do Git e permite a automação de changelogs. Para detalhes sobre nossa convenção de mensagens, consulte o [Guia de Commits Profissionais](./docs/git_commit_guide.md).

Os tipos de commit incluem:

- `feat:` Adição de um novo recurso ou laboratório.
- `docs:` Alterações na documentação (READMEs, notas de estudo).
- `fix:` Correção de bugs ou configurações incorretas.
- `refactor:` Reestruturação de código ou organização de arquivos sem mudança de funcionalidade.
- `style:` Melhorias de formatação que não afetam o significado do código.
- `test:` Adição ou correção de testes.
- `chore:` Manutenção geral do projeto (ex: atualização de dependências).

---

## 🏛️ Arquitetura do Repositório

A organização deste repositório foi pensada para ser modular e escalável, permitindo a adição de novas certificações e áreas de estudo de forma organizada. A estrutura principal é a seguinte:

```bash
./
├── cisco/                                # Hub para todas as certificações Cisco
│   ├── CCNP ENCOR 350-401/               # Estudos e Labs para o exame ENCOR
│   │   ├── 01 - Architecture/            # Domínio 1 do ENCOR
│   │   ├── 02 - Virtualization/          # Domínio 2 do ENCOR
│   │   ├── 03 - Infrastructure/          # Domínio 3 do ENCOR
│   │   ├── 04 - Network Assurance/       # Domínio 4 do ENCOR
│   │   ├── 05 - Security/                # Domínio 5 do ENCOR
│   │   ├── 06 - Automation/              # Domínio 6 do ENCOR
│   │   ├── Blueprint/                    # Blueprint do exame CCNP ENCOR
│   │   └── README.md                     # README específico do ENCOR
│   ├── CCNP ENARSI/                      # Futuros estudos para o exame ENARSI
│   │   └── README.md                     # README específico do ENARSI
│   └── README.md                         # README geral das certificações Cisco
├── dashboards/                           # Projetos de dashboards e análise de dados
│   └── README.md                         # README específico dos dashboards
├── docs/                                 # Documentação geral do repositório
├── .gitignore                            # Arquivos e pastas ignorados pelo Git
└── README.md                             # Este arquivo: Visão geral do repositório
```

---

## 🛠️ Ecossistema de Ferramentas

Para o desenvolvimento e a prática dos estudos, utilizo um conjunto de ferramentas robustas que suportam minha jornada em redes e automação:

- **Git & GitHub:** Para controle de versão, colaboração e hospedagem deste portfólio.
- **Python:** Linguagem de programação essencial para automação de redes, análise de dados e desenvolvimento de dashboards.
- **GNS3 / EVE-NG / CML / Packet Tracer:** Ferramentas de simulação e emulação para construção e teste de topologias de rede complexas.
- **Visual Studio Code:** Meu ambiente de desenvolvimento integrado (IDE) preferido.

---

## 🗺️ Roadmap de Estudos

Meu planejamento de estudos e objetivos futuros inclui:

- [x] Renovação CCNA (Válido até 2028)
- [ ] Conclusão dos Labs de Architecture (ENCOR)
- [ ] Conclusão dos Labs de Infrastructure (ENCOR)
- [ ] Certificação CCNP ENCOR 350-401
- [ ] Início dos estudos ENARSI

---

## 💡 Guia de Navegação

Para explorar o conteúdo deste repositório:

1. **Visão Geral:** Este `README.md` fornece uma introdução ao projeto e seus padrões.
1. **Certificações Cisco:** Navegue até a pasta `cisco/` para encontrar os estudos organizados por certificação (ex: `CCNP ENCOR 350-401/`).
1. **Projetos de Dashboards:** A pasta `dashboards/` contém meus projetos de visualização de dados e automação.

---

## 📚 Base de Conhecimento e Padrões

A pasta `docs/` centraliza guias e documentações detalhadas que regem a organização e as boas práticas deste repositório:

- [Guia de Commits Profissionais](./Docs/git_commit_guide.md): Detalhes sobre a convenção de mensagens de commit adotada.

- [Guia de Versionamento Semântico](./Docs/guia_versionamento.md): Explicação de como o versionamento é aplicado.

- [Dicionário Semântico](./Docs/dicionario_semantico.md) (Em Breve): Definição de termos e padrões de nomenclatura para arquivos e pastas.

---

## ✉️ Contato

Conecte-se comigo para discutir networking, automação ou certificações:

- **Nome:** Alexandre Lavorenti Cancilieri
- **LinkedIn:** [alexandre-analista-de-ti](https://www.linkedin.com/in/alexandre-analista-de-ti/)
- **GitHub:** [@alcancil](https://github.com/alcancil)

---

*Última atualização: Março de 2026*  