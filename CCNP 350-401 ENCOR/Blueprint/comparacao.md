# Comparação CCNP ENCOR 350-401: v1.1 vs v1.2

## Resumo Geral das Mudanças

| Aspecto | v1.1 (Atual) | v1.2 (Futura) | Status |
|---------|--------------|---------------|---------|
| **Duração** | 120 minutos | 120 minutos | ✅ Mantido |
| **Percentual Arquitetura** | 15% | 15% | ✅ Mantido |
| **Percentual Virtualização** | 10% | 10% | ✅ Mantido |
| **Percentual Infraestrutura** | 30% | 30% | ✅ Mantido |
| **Percentual Network Assurance** | 10% | 10% | ✅ Mantido |
| **Percentual Segurança** | 20% | 20% | ✅ Mantido |
| **Percentual Automação** | 15% | 15% | ✅ Mantido |

---

## 1.0 ARQUITETURA (15%)

### Tópicos que PERMANECEM
| Tópico | Detalhes |
|--------|----------|
| 1.1 Design principles | High-level enterprise network design, High availability techniques |
| 1.3/1.2 SD-WAN | Control and data planes elements, Benefits and limitations |
| 1.4/1.3 SD-Access | Control and data planes elements, Traditional campus interoperating |

### Tópicos que SAEM (v1.1 → v1.2)
| Tópico Removido | Detalhes |
|-----------------|----------|
| **1.2 Wireless network design** | • Wireless deployment models<br>• Location services in WLAN design<br>• Client density |
| **1.5 QoS configurations** | • QoS components<br>• QoS policy<br>• **Wired and wireless** QoS |
| **1.6 Hardware/software switching** | • CEF, CAM, TCAM, FIB, RIB<br>• Adjacency tables |

### Tópicos que ENTRAM (v1.2)
| Novo Tópico | Detalhes |
|-------------|----------|
| **1.4 QoS configurations** | • Apenas **interpretação** de configurações<br>• **Sem menção específica a wireless** |

### Mudanças de Nomenclatura
| v1.1 | v1.2 |
|------|------|
| Cisco SD-WAN solution | **Cisco Catalyst SD-WAN** solution |

---

## 2.0 VIRTUALIZAÇÃO (10%) - SEM ALTERAÇÕES

Todos os tópicos permanecem idênticos entre as versões.

---

## 3.0 INFRAESTRUTURA (30%)

### Reorganização da Seção
| v1.1 | v1.2 |
|------|------|
| 3.1 Layer 2<br>3.2 Layer 3<br>**3.3 Wireless**<br>3.4 IP Services | 3.1 Layer 2<br>3.2 Layer 3<br>**3.3 IP Services**<br>*(Wireless removido)* |

### Tópicos que SAEM COMPLETAMENTE
| Seção Removida | Tópicos Perdidos |
|----------------|------------------|
| **3.3 Wireless** | • Layer 1 concepts (RF power, RSSI, SNR, etc.)<br>• AP modes and antenna types<br>• Access point discovery and join process<br>• Layer 2 and Layer 3 roaming<br>• WLAN troubleshooting using GUI<br>• Wireless segmentation (groups, profiles, tags) |

### Mudanças em IP Services (3.4 → 3.3)
| Tópico | v1.1 | v1.2 | Status |
|--------|------|------|--------|
| **Multicast protocols** | PIM and IGMP v2/v3 | PIM **SM**, IGMP v2/v3, **SSM, bidir, and MSDP** | 🔄 **Expandido** |
| Outros tópicos | NTP/PTP, NAT/PAT, HSRP/VRRP | Idênticos | ✅ Mantidos |

---

## 4.0 NETWORK ASSURANCE (10%)

### Mudanças Principais
| Tópico | v1.1 | v1.2 | Status |
|--------|------|------|--------|
| **4.5 DNA Center** | Cisco DNA Center workflows | **Cisco Catalyst Center** (formerly Cisco DNA Center)<br>**+ AI-powered workflows** | 🔄 **Atualizado** |
| Outros tópicos | Diagnósticos, NetFlow, SPAN, IPSLA, NETCONF/RESTCONF | Idênticos | ✅ Mantidos |

---

## 5.0 SEGURANÇA (20%)

### Tópicos que SAEM COMPLETAMENTE
| Seção Removida | Tópicos Perdidos |
|----------------|------------------|
| **5.4 Wireless security** | • 802.1X<br>• WebAuth<br>• PSK<br>• EAPOL (4-way handshake) |

### Reorganização
| v1.1 | v1.2 |
|------|------|
| 5.1 Device access control<br>5.2 Infrastructure security<br>5.3 REST API security<br>**5.4 Wireless security**<br>5.5 Network security design | 5.1 Device access control<br>5.2 Infrastructure security<br>5.3 REST API security<br>**5.4 Network security design**<br>*(Wireless security removido)* |

### Mudanças em Network Security Design
| Componente | v1.1 | v1.2 | Status |
|------------|------|------|--------|
| Network access control | 802.1X, MAB, and WebAuth | *(Removido)* | ❌ **Removido** |
| Outros | Threat defense, Endpoint security, NGFW, TrustSec/MACsec | Idênticos | ✅ Mantidos |

---

## 6.0 AUTOMAÇÃO (15%)

### Mudança no Título da Seção
| v1.1 | v1.2 |
|------|------|
| **Automation** | **Automation and Artificial Intelligence** |

### Mudanças em APIs
| Tópico | v1.1 | v1.2 |
|--------|------|------|
| **6.4 APIs** | Cisco DNA Center and **vManage** | **Cisco Catalyst Center** and **SD-WAN Manager** |
| **6.5 REST API** | Cisco DNA Center and RESTCONF | **Cisco Catalyst Center** and RESTCONF |

### Simplificação
| v1.1 | v1.2 |
|------|------|
| 6.7 Compare **agent vs. agentless** orchestration tools, such as **Chef, Puppet, Ansible, and SaltStack** | 6.7 Compare **agent vs. agentless** orchestration tools |

---

## Resumo das Principais Perdas

| Área Removida | Impacto |
|---------------|---------|
| **Wireless Design** | Deployment models, location services, client density |
| **Wireless Infrastructure** | RF concepts, AP modes, roaming, troubleshooting |
| **Wireless Security** | 802.1X, WebAuth, PSK, EAPOL |
| **Hardware Switching** | CEF, CAM, TCAM, FIB, RIB, adjacency tables |
| **QoS Granular** | Componentes e políticas detalhadas |

## Resumo das Principais Adições

| Área Adicionada | Detalhes |
|-----------------|----------|
| **Multicast Expandido** | PIM SM, SSM, bidir, MSDP |
| **AI Integration** | AI-powered workflows no Catalyst Center |
| **Nomenclatura Catalyst** | SD-WAN → Catalyst SD-WAN<br>DNA Center → Catalyst Center |

---

**Conclusão:** A v1.2 remove significativamente o conteúdo wireless e simplifica alguns tópicos, enquanto adiciona elementos de IA e expande protocolos multicast. O exame mantém a mesma estrutura percentual, mas com foco reduzido em wireless e hardware de switching.