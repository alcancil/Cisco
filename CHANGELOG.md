# Changelog

Todos os marcos notáveis deste projeto serão documentados neste arquivo. O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.5.3] - 2026-04-24

### Added

- Implementação da Revisão 07 (Parte 09)
- Novo conjunto de simulados focados em análise de cenários e comportamento do STP
- Expansão do banco de questões com foco em interpretação e tomada de decisão (nível CCNP)

### Changed

- Refinamento da progressão didática entre teoria, análise e validação prática
- Melhoria na coerência entre README e simulados gerados

## [1.5.2] - 2026-04-23

### Added

- Implementação da Revisão 08 (Parte 08)
- Seção "Toolbox do Engenheiro" com comandos CLI e filtros Wireshark para STP
- Cheat Sheet operacional focado em diagnóstico e troubleshooting (nível CCNP)

### Changed

- Melhoria na abordagem prática do plano de controle do STP
- Integração entre teoria e análise de pacotes (CLI + Wireshark)

## [1.5.1] - 2026-04-22

### Added

- Implementação da Revisão 06 (Parte 07)
- Expansão incremental do banco de questões

### Changed

- Continuidade da progressão teórica após a seção de laboratórios (Parte 06)
- Refinamento da clareza técnica nas explicações

## [1.5.0] - 2026-04-10

### Added

- Implementação do Simulado 05 (Parte 05): Arquitetura de Decisão e Diferenças de Protocolo.
- Adição de 10 novas questões focadas em glossário técnico (Root Port, Designated Port, Alternate Port).
- Seção comparativa detalhada entre STP (802.1D) e PVST+ (Cisco).

## [1.4.2] - 2026-04-10

### Changed

- Ajuste das questões dos simulados

## [1.4.1] - 2026-03-31

### Added

- Criação de `index.html` na pasta de simulados (Parte 01) para navegação centralizada via GitHub Pages

### Changed

- Ajuste do README para apontar para a central de simulados
- Melhoria da experiência de navegação (UX) entre simulados e dashboard

## [1.4.0] - 2026-03-31

### Added

- Implementação de simulados interativos para os módulos de STP (Partes 01, 02, 03 e 04)
- Criação de estrutura dedicada para exercícios e avaliação prática:
  - Diretório `Arquivos/` em cada módulo
  - Separação entre conteúdo teórico e prática
- Sistema de simulado com:
  - Timer por tentativa
  - Barra de progresso
  - Feedback visual (acerto/erro)
  - Explicação detalhada por questão
- Persistência de resultados utilizando `localStorage`
- Identificação do usuário para rastreamento de desempenho
- Dashboard de estatísticas com:
  - Total de simulados realizados
  - Total de questões respondidas
  - Percentual geral de acerto
  - Tempo médio por tentativa
  - Gráficos de desempenho (Chart.js)
  - Histórico detalhado de tentativas

### Changed

- Evolução do projeto de conteúdo estático para plataforma interativa de estudo
- Melhoria da experiência de aprendizado com feedback imediato e métricas de performance

## [1.3.0] - 2026-03-28

### Added

- Seção de fundamentos de switching (Layer 2 vs Layer 3)
- Explicação comparativa entre tabela CAM e tabela de roteamento
- Introdução à topologia de rede em 3 camadas (Core, Distribution, Access)
- Fluxo de decisão e encaminhamento em switches
- Criação da Revisão Parte 04 com aprofundamento em STP:
  - Exemplo de eleição de Root Bridge
  - Importância da posição do Root no design de rede
  - Definição de Root Primary e Secondary
  - Balanceamento de VLANs utilizando STP
  - Processo de eleição de Root Ports e Designated Ports
  - Cálculo de custos de porta e Root Path Cost
  - Critérios de desempate detalhados
  - Exemplo completo de cálculo de topologia STP

### Changed

- Evolução da narrativa para preparação conceitual antes do aprofundamento em STP
- Melhoria da progressão didática com foco em raciocínio lógico e troubleshooting

## [1.3.0] - 2026-03-28

### Added

- Seção de fundamentos de switching (Layer 2 vs Layer 3)
- Explicação comparativa entre tabela CAM e tabela de roteamento
- Introdução à topologia de rede em 3 camadas (Core, Distribution, Access)
- Fluxo de decisão e encaminhamento em switches

### Changed

- Evolução da narrativa para preparação conceitual antes do aprofundamento em STP

## [1.2.0] - 2026-03-27

### Added

- Seção de fundamentos de switching (L2 vs L3, CAM vs Routing)
- Explicação de loops em camada 2 e camada 3
- Topologia de rede em 3 camadas
- Fluxo de decisão de switches

### Changed

- Melhoria da narrativa didática do conteúdo STP

## [1.1.1] - 2026-03-25

### Added

- Adição de imagem ilustrativa do formato de BPDU para suporte visual ao conteúdo de STP

### Fixed

- Correção da renderização de diagrama Mermaid no GitHub (ajuste de sintaxe do bloco de código)

## [1.1.0] - 2026-03-25

### Added

- Criação do arquivo `README.md` na subpasta de estudos de STP:
  `03 - Infrastructure/02 - STP (Spanning Tree Protocol)/01 - Revisao/`
- Adição do diretório `Imagens/` para suporte visual ao conteúdo de STP

### Changed

- Reestruturação da revisão de STP dentro do módulo de Infrastructure (CCNP ENCOR 350-401)
- Melhoria da narrativa com:
  - Transições entre seções
  - Checkpoints de aprendizado
  - Estrutura progressiva mais clara e didática

### Removed

- Remoção do arquivo legado `01.md`, substituído por `README.md` estruturado

## [1.0.0] - 2024-05-21

### 🚀 Grand Release: Portfolio Ready

- **Refatoração Geral:** Transformação do repositório de arquivos brutos em um portfólio estruturado.
- **Governança:** Implementação da metodologia de cálculo ponderado por domínio do exame.
- **Interface:** Novo README.md com indicadores visuais de progresso (Geps.dev).
- **Compliance:** Alinhamento total com o Blueprint Cisco v1.2 e suporte legado v1.1.

## [0.3.2] - 2026-03-22

### Modificado

- Refatoração do [Guia de Versionamento Semântico](./docs/guia_versionamento.md) para refletir a jornada de certificações Cisco (ENCOR/ENARSI).
- Atualização da lógica de incrementos baseada em aprovações de exames e conclusão de domínios.

## [0.3.1] - 2026-03-22

### Modificado

- fix: correção de case-sensitivity da pasta docs para compatibilidade web.

## [0.3.0] - 2026-03-22

### Adicionado

- Criado o [Dicionário Semântico](./docs/dicionario_semantico.md) com padronização baseada em POSIX, RFC 3986 e Clean Code.
- Integração de badges dinâmicas do Shields.io vinculadas ao Credly no README.
- Nova seção de "Padrões de Engenharia" detalhando SemVer e Commits Semânticos.

### Modificado

- Refatoração do README.md para melhor navegabilidade e inclusão de links de governança.
- Atualização da seção "Base de Conhecimento" com links ativos para todos os guias.

## [0.2.0] - 2026-03-20

### Adicionado

- Integração de badges dinâmicas do Shields.io com links para certificados Credly no README.
- Seção de "Padrões de Engenharia" detalhando o uso de SemVer (Versionamento Semântico).
- Linkagem direta para o Guia de Versionamento Semântico em `docs/`.

### Modificado

- Estrutura do README principal para refletir a nova governança do repositório.
- Atualização do status de documentos na "Base de Conhecimento" de (Em Breve) para ativos.

## [0.1.0] - 2026-03-20

### Adicionado

- Estrutura inicial do repositório de estudos Cisco.
- Implementação do README.md com Propósito, Roadmap e Arquitetura.
- Guia de Commits Profissionais na pasta `docs/`.
- Guia de Versionamento Semântico na pasta `docs/`.