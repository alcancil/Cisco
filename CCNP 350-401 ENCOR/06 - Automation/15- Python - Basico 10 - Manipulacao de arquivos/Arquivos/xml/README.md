# Python - Básico 10

## 04 Manipulação de arquivos - .xml

### O que é XML?
XML (eXtensible Markup Language) é uma linguagem de marcação projetada para:
- Armazenar e transportar dados hierárquicos
- Ser legível por humanos e máquinas
- Integrar-se com sistemas legados Cisco (NETCONF, SOAP)

**Comparação com YAML/JSON:**
```mermaid
graph TD
    A[XML] -->|Mais verboso| B[Configurações complexas]
    A -->|Suporte legado| C[IOS-XE Antigo]
    D[JSON] -->|Mais leve| E[APIs Modernas]
    D -->|Mais rápido| F[DNA Center]