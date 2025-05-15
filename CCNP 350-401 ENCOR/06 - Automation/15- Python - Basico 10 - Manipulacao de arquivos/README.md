# Python - Básico 10

## Manipulação de arquivos

Este é um assunto muito importante quando tratamos de automação de redes. A primeira coisa que devemos notar é que o Python é uma das linguagens de programação que mais se aproximam da linguagem humana. Isso nos traz alguns benefícios, mas também alguns desafios.  

Vamos pensar: "Se para nós, humanos, fica mais fácil entender um código, então é mais fácil programar e obter resultados?"  

De imediato, a resposta é sim, pois como a interpretação dessa linguagem é feita primeiramente por um humano, o raciocínio se aproxima mais da nossa forma de pensar. Mas e se estivermos interagindo com uma máquina, por exemplo, um switch ou um roteador? Será que esse pensamento continua o mesmo?  

A resposta é não. Para que a máquina interprete corretamente os dados, ela precisa recebê-los de forma sequencial e estruturada. Isso também facilita a leitura por humanos, mas principalmente permite que os dispositivos compreendam e processem as informações de forma eficiente.  

Então, o Python consegue trabalhar com vários tipos de arquivos. Vamos dar uma olhada em alguns tipos de arquivos.  

* [txt](Arquivos/txt/README.md) - Comece com .txt para entender o básico de I/O (Input/Output) em Python.
* [csv](Arquivos/csv/README.md)  - para dados tabulares (inventários).
* [json](Arquivos/json/README.md) - para APIs e automação.
* [yaml](Arquivos/yaml/README.md) - para playbooks do Ansible.
* **.j2**   - Combine tudo com .j2 para templates dinâmicos.

# Python - Básico 10

## 📁 Manipulação de Arquivos em Automação de Redes

### Por Que Isso Importa?
A escolha do formato de arquivo correto determina:
- **Eficiência** da automação
- **Legibilidade** das configurações
- **Compatibilidade** com dispositivos Cisco

Explore os formatos essenciais:

### 🔤 [Arquivos TXT](Arquivos/txt/README.md)
- **Para que serve:** Logs brutos e saída de comandos CLI  
- **Caso Cisco:** `show running-config` → análise básica  
- `with open('log.txt') as f: print(f.read())`

### 📊 [Arquivos CSV](Arquivos/csv/README.md)
- **Para que serve:** Inventários de dispositivos em massa  
- **Caso Cisco:** Importar 100+ switches para Nornir/Ansible  
- `import csv; csv.DictReader('inventario.csv')`

### 🗃️ [Arquivos JSON](Arquivos/json/README.md)
- **Para que serve:** APIs Cisco (DNA Center/Meraki)  
- **Caso Cisco:** `POST /restconf/data/` com configurações  
- `json.loads(response.text)`

### 📝 [Arquivos YAML](Arquivos/yaml/README.md)
- **Para que serve:** Playbooks Ansible e Nornir  
- **Caso Cisco:** Templates de VLANs/ACLs legíveis  
- `yaml.safe_load('vlan.yml')`

### 🧩 [Templates J2](Arquivos/j2/README.md)
- **Para que serve:** Configurações dinâmicas multi-dispositivo  
- **Caso Cisco:** Gerar unique configs para 50 switches  
- `Template(open('template.j2').read())`

---

### Como Navegar
1. Clique em qualquer formato acima para ver:
   - 📌 Exemplos práticos Cisco
   - 🛠️ Bibliotecas Python relacionadas
   - ⚠️ Armadilhas comuns em redes

2. Fluxo de Aprendizado Recomendado:
   ```mermaid
   graph LR
     A[TXT-Básico] --> B[CSV-Inventários]
     B --> C[JSON-APIs]
     C --> D[YAML-Ansible]
     D --> E[J2-Templates]