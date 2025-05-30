# Python - Básico 10

## Manipulação de Arquivos em Automação de Redes

### Por Que Isso Importa?
A escolha do formato de arquivo correto determina:
- **Eficiência** da automação
- **Legibilidade** das configurações
- **Compatibilidade** com dispositivos Cisco

### Fluxo de Automação

```mermaid
graph TB
    A[Inventário CSV] --> B(API DNA Center/JSON)
    B --> C[Playbook Ansible/YAML]
    C --> D{Dispositivo}
    D -->|Config| E[Jinja2 Template/J2]
    D -->|Logs| F[Arquivos TXT/JSON]
    A --> G[Variáveis .env]
    B -.-> H[XML se NETCONF]
```

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
