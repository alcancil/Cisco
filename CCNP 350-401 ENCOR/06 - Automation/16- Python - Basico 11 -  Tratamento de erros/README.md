# Python - Básico 10

## Tratamento de Erros

### Por Que Isso Importa?
Erros acontecem — especialmente em automação de redes, onde arquivos podem estar mal formatados, ausentes ou conter dados inválidos.  
Saber tratar esses erros evita que seus scripts quebrem e garante uma automação segura e confiável.  

### O que vamos estudar

- Identificar e capturar erros comuns com try, except, else e finally
- Tratar exceções específicas como FileNotFoundError, KeyError, json.JSONDecodeError, PermissionError, entre outras
- Criar scripts mais robustos e prontos para produção
- Adaptar tratamentos de erro para arquivos .txt, .csv, .json, .yaml, .env, .xml e .j2

### Fluxo de Automação

```mermaid
graph TB
    A[Inventário CSV] --> B[API DNA Center / JSON]
    B --> C[Playbook Ansible / YAML]
    C --> D{Dispositivo}
    D -->|Config| E[Jinja2 Template / J2]
    D -->|Logs| F[Arquivos TXT / JSON]
    A --> G[Variáveis .env]
    B -.-> H[XML se NETCONF]

    style A fill:#fff3cd,stroke:#f0ad4e,color:#000
    style F fill:#f8d7da,stroke:#dc3545,color:#000
    style G fill:#d1ecf1,stroke:#17a2b8,color:#000
    style E fill:#d4edda,stroke:#28a745,color:#000
```
  
    As caixas coloridas representam pontos onde erros são comuns:

        🟨 Arquivo não encontrado

        🟥 Formato malformado (ex: JSON inválido)

        🟦 Variável de ambiente ausente

        🟩 Renderização de template com erro

📂 Tipos de arquivos abordados e erros comuns

📄 Arquivos TXT

    Para que serve: Armazenar logs brutos, saídas de comandos (como show running-config) e relatórios simples.

    Erros comuns tratados:

        Arquivo não encontrado

        Permissão negada

    Quando usar: Quando você precisa armazenar ou analisar saídas de CLI simples ou logs sequenciais.

📑 Arquivos CSV

    Para que serve: Gerenciar inventários de dispositivos, listas de portas, VLANs, IPs ou usuários de forma tabular.

    Erros comuns tratados:

        Colunas ausentes

        Delimitadores incorretos

    Quando usar: Quando a estrutura dos dados é tabular (linhas e colunas), e você precisa importar ou exportar para planilhas.

🧾 Arquivos JSON

    Para que serve: Representar dados estruturados, como inventários hierárquicos ou configurações vindas de APIs (ex: DNA Center, Meraki).

    Erros comuns tratados:

        JSON malformado

        Chaves ausentes

    Quando usar: Quando os dados têm estrutura de dicionário/lista e precisam de integração com APIs modernas ou manipulação no Python.

📘 Arquivos YAML

    Para que serve: Configurar playbooks no Ansible, inventários do Nornir e dados hierárquicos legíveis por humanos.

    Erros comuns tratados:

        Identação incorreta

        Estrutura malformada

    Quando usar: Quando legibilidade e compatibilidade com ferramentas como Ansible e Nornir são prioridades.

🧮 Arquivos XML

    Para que serve: Troca de dados com APIs legadas (NETCONF, ACI, SOAP).

    Erros comuns tratados:

        Tags malformadas

        Falhas de parsing

    Quando usar: Quando a plataforma exige XML, como Cisco ACI, IOS-XE com NETCONF ou equipamentos que seguem YANG.

🧩 Templates J2

    Para que serve: Gerar configurações dinâmicas em massa com base em dados variáveis (como VLANs, interfaces, ACLs).

    Erros comuns tratados:

        Variáveis indefinidas

        Sintaxe incorreta nos templates

    Quando usar: Quando você precisa aplicar o mesmo modelo para dezenas de equipamentos, mudando apenas os dados.

🔐 Arquivos ENV

    Para que serve: Armazenar credenciais, IPs, senhas, tokens de API e outras variáveis sensíveis fora do código-fonte.

    Erros comuns tratados:

        Variáveis ausentes

        Arquivo .env não encontrado

    Quando usar: Sempre que você quiser manter o código limpo, seguro e reutilizável entre diferentes ambientes (ex: LAB, produção, nuvem).
    
📌 Como navegar

Clique em qualquer formato acima para ver:

    Exemplos práticos com tratamento de erro

    Bibliotecas Python relacionadas

    Erros específicos que ocorrem em redes Cisco

    Estratégias para garantir resiliência na automação





---
ARRUMAR

Explore os formatos essenciais:

### [Arquivos TXT](Arquivos/txt/README.md)
- **Para que serve:** Logs brutos e saída de comandos CLI  
- **Caso Cisco:** `show running-config` → análise básica  
- `with open('log.txt') as f: print(f.read())`

### [Arquivos CSV](Arquivos/csv/README.md)
- **Para que serve:** Inventários de dispositivos em massa  
- **Caso Cisco:** Importar 100+ switches para Nornir/Ansible  
- `import csv; csv.DictReader('inventario.csv')`

### [Arquivos JSON](Arquivos/json/README.md)
- **Para que serve:** APIs Cisco (DNA Center/Meraki)  
- **Caso Cisco:** `POST /restconf/data/` com configurações  
- `json.loads(response.text)`

### [Arquivos YAML](Arquivos/yaml/README.md)
- **Para que serve:** Playbooks Ansible e Nornir  
- **Caso Cisco:** Templates de VLANs/ACLs legíveis  
- `yaml.safe_load('vlan.yml')`

### [Arquivos XML](Arquivos/xml/README.md)
- **Para que serve:** APIs legadas (NETCONF/SOAP) e ACI  
- **Caso Cisco:** Configuração de dispositivos via NETCONF em IOS-XE e consulta de políticas no Cisco ACI  
- `xmltodict.parse(config.xml)`

### [Templates J2](Arquivos/j2/README.md)
- **Para que serve:** Configurações dinâmicas multi-dispositivo  
- **Caso Cisco:** Gerar unique configs para 50 switches  
- `Template(open('template.j2').read())`

### [Arquivos ENV](Arquivos/env/README.md)
- **Para que serve:** Gerenciar credenciais e variáveis de ambiente  
- **Caso Cisco:** Armazenar chaves de API do DNA Center e credenciais de dispositivos de forma segura  
- `load_dotenv('.env')`

---

### Como Navegar 

Clique em qualquer formato acima para ver:
   -  Exemplos práticos Cisco
   -  Bibliotecas Python relacionadas
   -  Armadilhas comuns em redes
