# Changelog

Todos os marcos notáveis deste projeto serão documentados neste arquivo. O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.10.0] - 2026-05-24

### Added

- Implementação da Revisão 15 com foco em STP Multi-VLAN: CST, PVST e PVST+
- Explicação conceitual do problema do CST em redes com múltiplas VLANs (uma única árvore para todas)
- Introdução do PVST (Per-VLAN Spanning Tree) como solução Cisco para balanceamento Layer 2
- Evolução para PVST+ com compatibilidade a trunks IEEE 802.1Q e interoperabilidade com STP padrão
- Demonstração do balanceamento de carga estático via manipulação de Root Bridge por VLAN
- Exemplos práticos de comandos: `root primary`, `root secondary`, `priority`, `show spanning-tree vlan`
- Análise das limitações de escalabilidade do PVST+ em redes com muitas VLANs (alto consumo de CPU/memória e tráfego de BPDUs)
- Introdução ao MSTP (802.1s) como solução para agrupamento de VLANs em poucas instâncias STP
- Cinco simulados temáticos de 10 questões cada, cobrindo:
  - Conceitos e diferenças fundamentais (CST, PVST, PVST+)
  - Root Bridge por VLAN e Load Balancing Layer 2
  - Trunks 802.1Q, BPDUs por VLAN e interoperabilidade
  - Limitações do PVST+, escalabilidade e transição para MSTP
  - Troubleshooting, comandos CLI e cenários de produção
- Simulado completo de 50 questões (75 minutos) integrando todos os temas do módulo
- Painel de estatísticas para acompanhamento de desempenho nos simulados

### Changed

- Expansão da progressão didática: do STP clássico (Arquivos 13 e 14) para o STP multi-VLAN (Arquivo 15)
- Refinamento da abordagem comparativa entre CST, PVST, PVST+ e MSTP (tabela de características)
- Integração de conceitos de produção: root planejado, secundário, interoperabilidade com switches IEEE
- Aprimoramento dos materiais de revisão com simulados progressivos e dashboard de resultados

### Impact

- Fecha o ciclo de estudos do STP em ambientes multi-VLAN antes de avançar para RSTP e MSTP prático
- Prepara o aluno para cenários reais de balanceamento de carga Layer 2 e troubleshooting de instâncias STP
- Consolida o repositório como referência completa para certificações CCNP ENCOR (tópico 3.2 – Spanning Tree Protocol)
- Oferece ferramenta de autoavaliação robusta para o engenheiro validar seu conhecimento teórico antes dos laboratórios
- Cria base sólida para os próximos laboratórios de PVST+ e MSTP em ambientes controlados

## [1.9.0] - 2026-05-23

### Added

- Implementação da Revisão 14 com foco em EtherChannel, UplinkFast e BackboneFast
- Demonstração do impacto do EtherChannel no custo lógico do STP (Port-Channel como interface única)
- Configuração e validação de EtherChannel com LACP (modo active/passive)
- Análise do comportamento do STP antes e após a criação do bundle
- Demonstração da resiliência interna do EtherChannel ante falha de link físico individual
- Configuração e validação do UplinkFast em switch de acesso com uplink redundante
- Demonstração de convergência local imediata em falha direta de uplink
- Análise dos efeitos colaterais do UplinkFast (elevação de prioridade e custo)
- Configuração e validação do BackboneFast em todos os switches da topologia
- Simulação de falha indireta no backbone e medição de convergência acelerada (~30s vs ~50s)
- Validação do BackboneFast via contador de transições (show spanning-tree backbonefast)
- Nota técnica sobre limitações de RLQ em ambientes virtuais (EVE-NG/IOL)

### Changed

- Evolução dos laboratórios para otimizações proprietárias Cisco do STP clássico
- Expansão da progressão didática: EtherChannel como base → UplinkFast → BackboneFast
- Integração de checklist de conclusão por laboratório para autoavaliação do aprendizado
- Refinamento da abordagem comparativa com tabela técnica unificada (tipo de falha × mecanismo × tempo)

### Impact

- Completa a cobertura do STP 802.1D clássico com todos os seus mecanismos de otimização
- Cria a ponte conceitual direta para o próximo módulo: PVST+, RSTP e MSTP
- Fortalece o repositório como referência técnica completa de Camada 2 para CCNP Enterprise
- Consolida o portfólio com laboratório de nível sênior cobrindo falhas diretas, indiretas e agregação de links

---

## [1.8.0] - 2026-05-20

### Added

- Implementação da Revisão 13 com foco em UDLD e links unidirecionais
- Demonstração prática dos modos UDLD normal e UDLD aggressive
- Simulação de falhas unidirecionais utilizando ACLs em EtherChannel
- Análise operacional de err-disable causado por UDLD aggressive
- Validação do comportamento do UDLD em links agregados
- Captura e análise de quadros UDLD utilizando Wireshark
- Simulação de recuperação manual e automática de interfaces UDLD
- Inclusão de troubleshooting avançado para links redundantes e unidirecionais

### Changed

- Evolução dos laboratórios para cenários avançados de proteção em camada 2
- Expansão da abordagem operacional com foco em falhas físicas e comportamento de produção
- Refinamento da progressão didática entre STP, EtherChannel e proteção de enlaces
- Maior integração entre troubleshooting, redundância e análise de protocolos

### Impact

- Aproxima os laboratórios de cenários reais encontrados em ambientes corporativos
- Fortalece o repositório como material avançado para preparação CCNP Enterprise
- Expande o projeto como portfólio técnico voltado para troubleshooting operacional
- Cria base para futuras integrações com monitoramento e automação de redes

---

## [1.7.0] - 2026-05-14

### Added

- Implementação da Revisão 12 com foco em BPDU Filter e err-disable recovery
- Simulação prática de loops de camada 2 em ambiente STP
- Demonstração do comportamento do BPDU Filter em modo global e por interface
- Análise operacional do ciclo automático de recovery (`errdisable recovery`)
- Simulação de falhas e instabilidade operacional em cenários redundantes
- Captura e análise de BPDUs utilizando Wireshark
- Geração de BPDUs maliciosos utilizando Scapy em Python

### Changed

- Evolução da abordagem prática para cenários avançados de troubleshooting STP
- Ampliação da análise operacional com foco em comportamento de produção
- Refinamento da progressão didática entre proteção, falha e recuperação automática
- Expansão da integração entre segurança, troubleshooting e análise de protocolos

### Impact

- Aproxima o laboratório de cenários reais encontrados em redes corporativas
- Fortalece o repositório como material técnico avançado para CCNP Enterprise
- Expande o projeto como portfólio voltado para troubleshooting e operação de redes
- Cria base para futuras integrações com automação e monitoramento

## [1.6.0] - 2026-05-01

### Added

- Implementação da Revisão 11 com laboratório prático de proteção STP
- Simulação de ataque STP utilizando Kali Linux e Yersinia
- Análise de BPDUs com Wireshark
- Aplicação prática de PortFast e BPDU Guard
- Inclusão de automação inicial com scripts Python para backup e restore de configurações
- Disponibilização de arquivos `.cfg` para replicação dos laboratórios

### Changed

- Refinamento da abordagem didática com foco em comportamento e troubleshooting
- Separação progressiva entre laboratórios fundamentais e avançados
- Melhoria na estrutura de documentação e reprodutibilidade dos cenários
- Ajuste do escopo do Lab 01 para manter alinhamento entre objetivo e implementação

### Impact

- Aproxima o projeto de cenários reais encontrados em ambientes corporativos
- Fortalece o repositório como material de estudo e portfólio técnico
- Cria base para evolução futura em automação e troubleshooting avançado

## [1.5.4] - 2026-04-27

### Added

- Implementação da Revisão 10 (Parte 10)
- Expansão do banco de simulados com foco em análise de cenários STP

### Changed

- Padronização da nomenclatura das revisões para manter consistência sequencial
- Continuidade da progressão didática voltada ao nível CCNP

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