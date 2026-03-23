# 🚀 Trilha de Especialista: Cisco CCNP ENCOR (350-401)

Este diretório centraliza os artefatos de estudo, laboratórios práticos e documentação técnica para o exame **Implementing and Operating Cisco Enterprise Network Core Technologies (350-401)**. 

Este repositório é um **diário de engenharia** que documenta minha preparação para o nível Professional da Cisco, aplicando rigor técnico tanto na configuração quanto na organização.

---

## 📊 Status da Jornada (Progress Tracking)

**Progresso Total para a Certificação:**
![Progresso Total](https://geps.dev/progress/20)  

| Tópico | Domínio do Exame      | Peso  | Progresso                              | Status                 |
| :---   | :---                  | :---: | :---                                   | :---                   |
| 01     | **Architecture**      | 15%   | ![15%](https://geps.dev/progress/2.25) | 🏗️ Em andamento        |
| 02     | **Virtualization**    | 10%   | ![0%](https://geps.dev/progress/4.55)  | 🏗️ Em andamento        |
| 03     | **Infrastructure**    | 30%   | ![0%](https://geps.dev/progress/8.5)   | 🏗️ Em andamento        |
| 04     | **Network Assurance** | 10%   | ![0%](https://geps.dev/progress/0)     | ⏳ Planejado           |
| 05     | **Security**          | 20%   | ![0%](https://geps.dev/progress/0)     | ⏳ Planejado           |
| 06     | **Automation**        | 15%   | ![0%](https://geps.dev/progress/0)     | ⏳ Planejado           |

### 🧮 Metodologia de Cálculo

Para garantir a precisão do portfólio, o progresso é calculado de forma ponderada baseada no peso oficial de cada domínio da Cisco.  

**A conta funciona assim:**

1. Cada Domínio tem um **Peso** (ex: Arquitetura = 15%).
2. Dividimos esse peso pelo **Total de Checkboxes** do domínio no Blueprint (ex: 20 itens).
3. **Valor por Checkbox:** 15 \div 20 = 0,75\% de progresso real na certificação por item concluído.

**Exemplo Atual:**
No Domínio 01, foram concluídos os 3 itens de QoS (18, 19, 20).  
> $3 \text{ itens} \times 0,75 = \mathbf{2,25\%}$ de progresso global.

### Tabela com os pesos calculados

| Domínio              | Peso Cisco | Qtd de Checkboxes | Valor de cada [x] |
|:---                  | :---       | :---              |:---               |
| 1. Architecture      | 15%        | 20                | 0,75%             |
| 2. Virtualization    | 10%        | 15                | 0,66%             |
| 3. Infrastructure    | 30%        | 60                | 0,50%             |
| 4. Network Assurance | 10%        | 20                | 0,50%             |
| 5. Security          | 20%        | 25                | 0,80%             |
| 6. Automation        | 15%        | 18                | 0,83%             |

> [!IMPORTANT]
> **Observação de Versões (v1.1 vs v1.2):** > Este projeto é focado no Blueprint **v1.2**. No entanto, tópicos da versão **v1.1** (como conceitos específicos de Wireless ou Hardware Switching) serão mantidos e indicados sempre que agregarem valor técnico indispensável para a atuação profissional, indo além do que é exigido estritamente na prova.

---

## 🏛️ Estrutura de Estudos (Blueprint v1.1/1.2)

A organização segue rigorosamente os domínios oficiais. Todos os tópicos seguem o blueprint oficial disponível em: [Cisco Exam Topics](https://learningnetwork.cisco.com/s/encor-exam-topics).

- [**01-architecture**](./01-architecture/): Design de rede, WLAN, SD-WAN, SD-Access e QoS.
- [**02-virtualization**](./02-virtualization/): Tecnologias de virtualização de dispositivos e caminhos (VRF, GRE, IPsec).
- [**03-infrastructure**](./03-infrastructure/): Layer 2 (STP, EtherChannel), Layer 3 (OSPF, EIGRP, BGP) e serviços IP.
- [**04-network-assurance**](./04-network-assurance/): Diagnóstico, SNMP, Syslog, NetFlow e SPAN/RSPAN.
- [**05-security**](./05-security/): Segurança de infraestrutura, controle de acesso e VPNs.
- [**06-automation**](./06-automation/): Python, JSON, APIs (DNA Center, vManage) e ferramentas de automação.

---

## 🛠️ Ecossistema de Simulação

Todo o conteúdo é desenvolvido e validado através de laboratórios práticos utilizando:

- **Cisco CML (Modeling Labs)** e **EVE-NG** para simulações de alta fidelidade com IOS-XE.
- **Cisco Packet Tracer** para provas de conceito rápidas e fundamentos.
- Simulações multi-fabricante quando aplicável.

---

## 📚 Fontes e Materiais de Referência

A fundamentação técnica deste repositório é baseada nos seguintes recursos oficiais e acadêmicos, garantindo conformidade com os padrões da indústria:

### Portais e Documentação Oficial

- [Cisco - Documentação Oficial](https://www.cisco.com)
- [Cisco Brasil](https://www.cisco.com.br)
- [Cisco Networking Academy](https://www.netacad.com/pt-br)
- [Cisco Learning Network](https://learningnetwork.cisco.com/)
- [Cisco CML - Guia de Início Rápido](https://www.cisco.com/c/en/us/td/docs/cloud_services/cisco_modeling_labs/v200/quick/start/b_cml_quick_start_2-0/m_whats_new.html)

### Cursos e Prática

- [Curso Cisco Packet Tracer](https://www.netacad.com/pt-br/courses/packet-tracer)
- [EVE-NG - Emulador de Redes](https://www.eve-ng.net/)
- [Python Institute](https://pythoninstitute.org/)
- [RFC Editor](https://www.rfc-editor.org/) (Consulta direta aos padrões IETF)

### Bibliografia Especializada

- [*CCNP and CCIE Enterprise Core ENCOR 350-401 Official Cert Guide* – David Hucaby](https://www.ciscopress.com/store/ccnp-and-ccie-enterprise-core-encor-350-401-official-9780138216764)
- [*Cisco Press* Materiais Complementares](https://www.ciscopress.com/)
- [*Programação de Redes com Python* – Rhodes Goerzen](https://www.novatec.com.br/livros/programacao-redes-com-python/) (Indispensável para o domínio de Automação)

---
*Este repositório segue os padrões de [Dicionário Semântico](../docs/dicionario_semantico.md) e [Versionamento](../docs/guia_versionamento.md) definidos na raiz do projeto.*