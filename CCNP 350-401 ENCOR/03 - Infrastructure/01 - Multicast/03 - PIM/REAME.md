# Índice

- [Índice](#índice)
  - [03 - PIM - Protocol Independent Multicast](#03---pim---protocol-independent-multicast)
  - [Contexto Histórico](#contexto-histórico)
    - [Tipos de Árvores de Distribuição](#tipos-de-árvores-de-distribuição)

## 03 - PIM - Protocol Independent Multicast  

## Contexto Histórico

O desenvolvimento do multicast IP e seus protocolos de roteamento passou por várias fases importantes:
Primeiros Protocolos (1980s-1990s):

- DVMRP (Distance Vector Multicast Routing Protocol) foi um dos primeiros protocolos de roteamento multicast
- MOSPF (Multicast Extensions to OSPF) tentou integrar multicast ao OSPF
- Esses protocolos tinham limitações significativas em termos de escalabilidade

**Evolução para PIM (1990s):**

- O PIM foi desenvolvido para superar as limitações dos protocolos anteriores
- Primeira especificação do PIM-DM (Dense Mode) e PIM-SM (Sparse Mode)
- O conceito "Protocol Independent" foi revolucionário - permitia que o PIM funcionasse sobre qualquer protocolo de roteamento unicast

**Padronização:**

- RFC 2362 (1998): PIM-SM versão 2 - https://tools.ietf.org/rfc/rfc2362.txt
- RFC 4601 (2006): PIM-SM versão 2 (revisão e atualização) - https://tools.ietf.org/rfc/rfc4601.txt
- RFC 3973 (2005): PIM-DM - https://tools.ietf.org/rfc/rfc3973.txt

**O que é o PIM?**

O IGMP é o protocolo que permite aos hosts participarem de grupos multicast e sinalizarem seu interesse em receber fluxos multicast específicos. Porém, o IGMP opera apenas no escopo da rede local e não tem a capacidade de rotear pacotes multicast da origem até os destinos através de múltiplas redes. É nesse momento que o PIM (Protocol Independent Multicast) entra em ação.  

O PIM é um protocolo de roteamento multicast que:

- **Constrói árvores de distribuição** para entregar tráfego multicast de forma eficiente
- **É independente de protocolo** - pode utilizar informações de qualquer protocolo de roteamento unicast (OSPF, BGP, RIP, etc.)
- **Otimiza o uso da largura de banda** evitando duplicação desnecessária de pacotes
- **Escalável** para redes de grande porte

O protocolo é descrito principalmente na RFC **4601 (PIM-SM)** e possui diferentes modos de operação para atender diferentes cenários de rede.  

**Como o PIM Funciona**  

Como o PIM por si só não transporta o tráfego dos pacotes entre os roteadores multicast, ele precisa consultar a tabela de roteamento unicast para determinar os caminhos de rede. Por isso ele é chamado de Protocol Independent - porque se baseia na tabela de roteamento unicast formada por protocolos como EIGRP, OSPF, RIP, BGP, etc., ou até mesmo rotas estáticas.  

Resumindo, ele consulta a tabela RIB (Routing Information Base).  

Com essas informações de roteamento, o PIM constrói árvores de distribuição multicast para definir os caminhos otimizados entre origem e destinos do tráfego multicast.

### Tipos de Árvores de Distribuição

O PIM utiliza dois tipos principais de árvores para distribuir o tráfego multicast:

**1. Source Tree (Árvore de Origem) - (S,G)**  

Também conhecida como: **Shortest Path Tree (SPT)**  
Notação: **(S,G) onde S = Source (origem) e G = Group (grupo)**  

**Características:**  

- Cada origem (source) tem sua própria árvore
- Utiliza o caminho mais curto da origem para cada receptor
- Oferece a menor latência possível
- Consome mais memória nos roteadores (uma entrada por origem)
- Exemplo: (192.168.1.10, 224.1.1.1)

**2. Shared Tree (Árvore Compartilhada) - (*,G)**  

- Também conhecida como: **Rendezvous Point Tree (RP Tree)**  
- Notação: **(*,G) onde * = qualquer origem e G = Group (grupo)**  

**Características:**

- Todas as origens do mesmo grupo compartilham a mesma árvore
- Utiliza um ponto central chamado Rendezvous Point (RP)
- Consome menos memória (uma entrada por grupo)
- Pode não oferecer o caminho mais curto
- Exemplo: (*, 224.1.1.1)

**3. Source-Specific Multicast (SSM) - (S,G) no modo SSM**  

- Notação: **(S,G) em grupos SSM (232.0.0.0/8)**

**Características:**

- Os receptores especificam tanto a origem quanto o grupo
- Não requer Rendezvous Point (RP)
- Elimina problemas de segurança do multicast tradicional
- Utilizado principalmente em IPTV e streaming

**Principais Características**  

- **Protocol Independent:** Utiliza a tabela de roteamento unicast existente
- **Suporte a diferentes topologias:** Funciona em redes densas e esparsas
- **Eficiência:** Constrói árvores otimizadas para distribuição
- **Flexibilidade:** Múltiplos modos de operação (Sparse Mode, Dense Mode, etc.)