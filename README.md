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
    - [Versionamento Semântico (SemVer)](#versionamento-semântico-semver)
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
| 📖 Em Estudo | **CCNP Enterprise Core (ENCOR 350-401)**              | -        |        |
| 🚀 Futuro    | **CCNP Enterprise Advanced Routing (ENARSI 300-410)** | -        |        |

---

## 🎓 Certificados

Além das certificações de carreira, possuo certificados que complementam minha base técnica em automação e fundamentos:

| Status         | Certificação                                         | Obtido em | Badges |
| :---           | :---                                                 | :---      | :---   |
| ✅ Completado  | **Python Essentials 01 - PCAP 01**                   | 2023      | [![Python Essentials 1 - PCAP1](https://img.shields.io/badge/Python-Essentials-yellow?logo=python&logoColor=white)](https://www.credly.com/badges/90325923-fdaa-4f86-ba62-ffdb7077906e/public_url) |
| ✅ Completado  | **Python Essentials 02 - PCAP 02**                   | 2023      | [![Python Essentials 2 - PCAP2](https://img.shields.io/badge/Python-Essentials-yellow?logo=python&logoColor=white)](https://www.credly.com/badges/e4f2b4af-a5cc-4a10-a31a-71fb00286c40/public_url) |  

---

## ⚙️ Padrões de Engenharia

Para garantir um histórico de projeto limpo, rastreável e profissional, adoto as seguintes práticas fundamentadas em padrões de mercado:

### Dicionário Semântico

Utilizo o padrão **kebab-case** e prefixos funcionais para organizar arquivos e pastas, garantindo compatibilidade com ambientes Linux e scripts de automação. Para detalhes das normas (POSIX, RFC 3986), consulte o [Dicionário Semântico](./docs/dicionario_semantico.md).

### Workflow de Commits Semânticos

Adoto a convenção de **Commits Semânticos** para padronizar o histórico de alterações. Isso permite uma leitura clara da evolução do projeto e facilita a geração automática de logs. Veja o [Guia de Commits Profissionais](./docs/git_commit_guide.md).

### Versionamento Semântico (SemVer)

Este repositório segue o modelo `MAJOR.MINOR.PATCH` para controle de progresso e releases. Cada marco nos estudos ou grandes adições de labs refletem uma nova versão, conforme detalhado no [Guia de Versionamento Semântico](./docs/guia_versionamento.md).

---

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
├── docs/                                 # Documentação geral do repositório
├── .gitignore                            # Arquivos e pastas ignorados pelo Git
└── README.md                             # Este arquivo: Visão geral do repositório
```

---

## 🛠️ Ecossistema de Ferramentas

Para o desenvolvimento e a prática dos estudos, utilizo um conjunto de ferramentas robustas que suportam minha jornada em redes e automação:

- **Git & GitHub:** Para controle de versão, colaboração e hospedagem deste portfólio.
- **Python:** Linguagem de programação essencial para automação de redes, análise de dados e desenvolvimento de dashboards.
- **GNS3 / EVE-NG / PNETLab / CML / Packet Tracer:** Ferramentas de simulação e emulação para construção e teste de topologias de rede complexas.
- **Visual Studio Code:** Meu ambiente de desenvolvimento integrado (IDE) preferido.

---

## 🗺️ Roadmap de Estudos

Meu planejamento de estudos e objetivos futuros inclui:

- [x] Renovação CCNA (Válido até 2028)
- [ ] Conclusão dos Labs de Architecture (ENCOR)
- [ ] Conclusão dos Labs de Infrastructure (ENCOR)
- [ ] Certificação CCNP ENCOR 350-401
- [ ] Início dos estudos ENARSI (Ou outra trilha)

---

## 💡 Guia de Navegação

Para explorar o conteúdo deste repositório:

1. **Visão Geral:** Este `README.md` fornece uma introdução ao projeto e seus padrões.
2. **Certificações Cisco:** Navegue até a pasta `cisco/` para encontrar os estudos organizados por certificação (ex: `CCNP ENCOR 350-401/`).
3. **Histórico:** Verifique o progresso detalhado no `CHANGELOG.md`.

---

## 📚 Base de Conhecimento e Padrões

A pasta `docs/` centraliza guias e documentações detalhadas que regem a organização e as boas práticas deste repositório:

- [Guia de Commits Profissionais](./docs/git_commit_guide.md): Detalhes sobre a convenção de mensagens de commit adotada.

- [Guia de Versionamento Semântico](./docs/guia_versionamento.md): Explicação de como o versionamento é aplicado.

- [Dicionário Semântico](./docs/dicionario_semantico.md): Definição de termos e padrões de nomenclatura para arquivos e pastas.

---

## ✉️ Contato

Conecte-se comigo para discutir networking, automação ou certificações:

- **Nome:** Alexandre Lavorenti Cancilieri
- **LinkedIn:** [alexandre-analista-de-ti](https://www.linkedin.com/in/alexandre-analista-de-ti/)
- **GitHub:** [@alcancil](https://github.com/alcancil)

---

*Última atualização: Março de 2026*  