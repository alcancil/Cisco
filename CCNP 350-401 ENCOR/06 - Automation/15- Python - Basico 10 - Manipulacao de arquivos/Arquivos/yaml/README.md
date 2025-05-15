# Python - Básico 10

## 03 Manipulação de arquivos - .yaml ou .yml

### O que é YAML? 

YAML = "Yet Another Markup Language" (mais uma linguagem de marcação) ou "YAML Ain’t Markup Language" (YAML não é linguagem de marcação).   
YAML (*.yaml* ou *.yml*) é uma linguagem de serialização de dados projetada para:  
- Ser legível por humanos (mais que JSON/XML).  
- Trabalhar com estruturas hierárquicas (ex.: configurações de rede).  
- Integrar-se facilmente com Python (converte para dicionários/listas).    


Os arquivos **.yaml (ou .yml)** são amplamente utilizados em automação de redes para:

```Bash
1. **Definição de Playbooks no Ansible**: Automatizar configurações em dispositivos Cisco (VLANs, ACLs, interfaces) de forma legível.
2. **Inventários de Dispositivos**: Estruturar listas de equipamentos (hostname, IP, credenciais) para ferramentas como Ansible e Nornir.
3. **Modelagem de Dados para APIs**: Descrever configurações complexas em ferramentas Cisco (DNA Center, ACI) antes de converter para JSON.
4. **Documentação de Topologias**: Descrever topologias de rede (links, dispositivos, VLANs) para ferramentas como ContainerLab ou Nautobot.
5. **Integração com Kubernetes (K8s)**: Gerenciar configurações de redes em containers (CNI, políticas de rede).
```

### Quando Usar YAML vs Outros Formatos

| **Escolha YAML quando...**                            |   **Evite YAML quando...**                          |
|-------------------------------------------------------|-----------------------------------------------------|
| Automação com Ansible/Nornir	Playbooks, inventários  | APIs que exigem JSON	DNA Center, Meraki            |
| Configurações legíveis	Templates de VLANs/ACLs       | Dados tabulares simples	Use CSV                     |
| Dados hierárquicos	Políticas de QoS                  | Performance crítica	JSON é mais rápido no parsing |

### Por que YAML é essencial para o CCNP?

- **Sintaxe limpa:** Ideal para automação de redes em ferramentas como Ansible e Nornir.
- **Hierarquia intuitiva:** Representa configurações de rede (VLANs, ACLs, interfaces) com indentação simples.
- **Legibilidade humana:** Facilita colaboração em equipe e debugging de playbooks.
- **Integração com Python:** Conversão direta para dicionários/listas nativas.

**JSON (JavaScript Object Notation)**  

- Usado em APIs Cisco (DNA Center, Meraki).
- Requer aspas "" e chaves {}.
- Melhor para máquinas (parsing rápido).

```json
    {
        "switch": {
            "hostname": "SW1",
            "vlans": [
                {"id": 10, "name": "VLAN_GESTAO"},
                {"id": 20, "name": "VLAN_VOIP"}
            ],
            "interfaces": {
                "Gig0/1": {"vlan": 10, "status": "up"}
            }
        }
    }
```
    
### YAML (YAML Ain't Markup Language)

- Usado em Ansible/Nornir (playbooks, inventários).
- Sintaxe limpa (sem {}, "" ou vírgulas).
- Suporta comentários (#) e multi-linhas (para comandos Cisco).

```yaml
    switch:
      hostname: SW1
      vlans:
        - id: 10
          name: VLAN_GESTAO
        - id: 20
          name: VLAN_VOIP
      interfaces:
        Gig0/1:
          vlan: 10
          status: up
```

## Sintaxe do YAML  

Essa é uma linguagem que utiliza espaços e não tabulações, porém ela é bem rígida com esse requisito.

- **Inicio e fim de um arquivo**  

```yaml
   YAML é uma linguagem baseada em indentação (espaços, **nunca tabs**).  
    - `---` (opcional): Indica o início de um documento.  
    - `...` (opcional): Indica o fim (usado apenas em arquivos com múltiplos documentos).
    Obs: dentro de um arquivo yaml ou yml pode existir 1 ou mais arquivos
```
**Exemplo:**  
    
```yaml
    ---  # Documento 1
    switch:
      hostname: SW1
    ---  # Documento 2
    router:
      hostname: R1
```

**Por que isso existe?**

- **Separação lógica:** Permite armazenar configurações diferentes (ex.: switches e roteadores) no mesmo arquivo.  
- **Processamento individual:** Ferramentas como Ansible podem ler cada documento separadamente.  
- **Reuso em pipelines:** Útil para ferramentas que processam fluxos de dados (ex.: Kubernetes).  

**Uso Prático no CCNP**  

- **Ansible:** Você pode definir múltiplos playbooks em um único arquivo YAML (cada um iniciado com ---).  
- **Inventários de dispositivos:** Agrupar switches, roteadores e firewalls em um só arquivo.  


**Exemplo com Ansible:**

```yaml
---  # Playbook 1: Configurar VLANs
- name: Configurar VLANs
  hosts: switches
  tasks:
   - name: Adicionar VLAN 10
     cisco.ios.ios_vlan:
       vlan_id: 10
       name: VLAN_GESTAO

---  # Playbook 2: Configurar Interfaces
- name: Configurar Interfaces
  hosts: routers
  tasks:
    - name: Ativar Gig0/0
      cisco.ios.ios_interface:
        name: GigabitEthernet0/0
        state: up
```

- **Comentários**

```yaml
    # Inicia um comentário
    OBS: o yaml não aceita comentários de múltiplas linhas. Portanto, se quiser que várias linhas tenham comentários, iniciar cada linha com #
    Exemplo:  
    
    vlans:
    - 10  # VLAN_GESTAO (apenas uma linha por comentário)
    - 20  # VLAN_VOIP
    # Não existe /* ... */ como em outras linguagens!
```

- **Chave: Valor**

```yaml
    Os arquivos yaml praticamente funcionam com chave: valor
    - chave: valor                   # pode estar entre " " ou não. O uso de aspas não é obrigatório
    - Interface: Serial0/0 Serial0/2 # pode conter vários elementos
    - Número: 3                      # Valores numéricos
    - Status: true                   # Valores booleanos
    - Date: 2025-05-01               # Data em formato americano
```

- **Objetos**

    Como já citado, o yaml trabalha com espaços nunca tabs. Ele também é hierárquico. Então vamos criar um objeto.

```yaml
    equipamentos:
        nome: sw01
        portas: 24
        local: adm

    Nesse exemplo temos um objeto chamado equipamentos: com suas características definidas em chave: valor
```

- **Listas**

    Vamos atualizar o exemplo anterior  
    - o caractere - indica uma lista
  
```yaml
  equipamentos:
        - nome: sw01
          portas: 24
          local: adm
        - nome: sw02
          portas: 16
          local: rh
        - nome: sw03
          portas: 8
          local: mkt
```

Agora, nesse exemplo temos um objeto chamado **equipamentos** com 3 listas  

- **Multilinhas**

    **Pipe (|)**: Utilizado para blocos com mais de uma linha.  
    **Uso ideal:** Comandos Cisco que exigem formatação exata (ex.: configurações de interface, ACLs).

```yaml
cisco_switch:
  hostname: "SW1"
  config: |
    interface GigabitEthernet0/1
     description Link para Roteador
     ip address 192.168.1.1 255.255.255.0
     no shutdown
    !
    vlan 10
     name VLAN_GESTAO
```

Resultado (Python):

```python
    {
      'cisco_switch': {
        'hostname': 'SW1',
        'config': 'interface GigabitEthernet0/1\n description Link para Roteador\n ip address 192.168.1.1 255.255.255.0\n no shutdown\n!\nvlan 10\n name VLAN_GESTAO\n'
      }
    }
```

    **Maior que (>)** - Dobra Linhas em Espaços  
    **Uso ideal:** Textos longos sem formatação crítica (ex.: descrições, documentação).

```yaml
backup_report: >
  Este é um relatório de backup automático
  do switch SW1 em 2024-05-20.
  VLANs configuradas: 10, 20, 30.
  Interfaces ativas: Gig0/1, Gig0/2.
```

Resultado (Python):

```python

{
  'backup_report': 'Este é um relatório de backup automático do switch SW1 em 2024-05-20. VLANs configuradas: 10, 20, 30. Interfaces ativas: Gig0/1, Gig0/2.\n'
}
```

**OBS:** o caractere **>** deixa escrever em múltiplas linhas porém ele não interpreta o **Enter** e o resultado é que o texto sai todo em uma única linha.  
**OBS2:** em python, para pularmos uma linha podemos utilizar **\n** e nesse nosso caso, no bloco **>** se quisermos puar linhas devemos usar **\n**

| Característica     | Pipe (\|)                | Greater Than (>)           |
|--------------------|--------------------------|----------------------------|
| Quebras de linha   | Preservadas              | Convertidas em espaços     |
| Uso típico no CCNP | Configurações Cisco      | Relatórios/documentação    |
| Exemplo            | Comandos interface, vlan | Descrições de dispositivos |

### Exemplos

**Exemplo 01:** Automação com Ansible/Nornir	Playbooks, inventários

**Ansible**

```yaml
  ---
  # Inventário de dispositivos Cisco para Ansible
  all:
    children:
      switches:
        hosts:
          sw01:
            ansible_host: 192.168.1.1
            ansible_user: admin
            ansible_network_os: ios
            vlans:
             - id: 10
                name: VLAN_GESTAO
              - id: 20
                name: VLAN_VOIP
          sw02:
            ansible_host: 192.168.1.2
            ansible_user: admin
            ansible_network_os: ios

      routers:
        hosts:
          rtr01:
            ansible_host: 10.0.0.1
            ansible_user: cisco
            ansible_network_os: iosxe
            interfaces:
              - GigabitEthernet0/0
              - GigabitEthernet0/1
  ...
```

**Exemplo 02:** Modelagem de Dados para APIs  

- Criar o arquivo **aci_config.yml**

```yaml
---
# Modelo de configuração para Cisco ACI API
# Foco: Tenant e EPGs (Endpoint Groups)

tenant: "TENANT_WEB"
description: "Ambiente para aplicações web"

vrfs:
  - name: "VRF_WEB"
    enforce_routing: true

application_profiles:
  - name: "AP_WEB_APP"
    epgs:
      - name: "EPG_FRONTEND"
        bridge_domain: "BD_WEB"
        contracts:
          - provider: "HTTP-CONTRACT"
          - consumer: "DB-CONTRACT"
      - name: "EPG_DATABASE"
        bridge_domain: "BD_DB"
        physical_domain: "PHYS_DB_SERVERS"

policies:
  bd:
    - name: "BD_WEB"
      gateway: "10.10.10.1/24"
      vrf: "VRF_WEB"
    - name: "BD_DB"
      gateway: "10.20.20.1/24"
...
```

**Explicação**  

Como visto, yaml é mais próximo da linguagem humana. Então esse modelo de configuração funciona como se fosse um rascunho. Ele é dividido por blocos.

    - Seção tenant:

        Define o container lógico no ACI
        Atribui descrição para documentação

    - Seção vrfs:

        Configura Virtual Routing & Forwarding
        enforce_routing ativa políticas de roteamento

    - Seção application_profiles:

        Modela EPGs (grupos de endpoints)
        Associa contracts (políticas de comunicação)
        Exemplo típico de frontend/database

    - Seção policies:

        Bridge Domains com sub-redes IP

**Script converter_json.py**  

```Python
  [01] import yaml, json
  [02]
  [03] with open('aci_config.yml') as f:
  [04]    aci_data = yaml.safe_load(f)
  [05]    print(json.dumps(aci_data, indent=2)) 
```

**Saída**

```Bash
alcancil@linux:~/automacoes/arquivos/yaml/02$ ls
aci_config.yml  converter_json.py
alcancil@linux:~/automacoes/arquivos/yaml/02$ python3 converter_json.py 
{
  "tenant": "TENANT_WEB",
  "description": "Ambiente para aplica\u00e7\u00f5es web",
  "vrfs": [
    {
      "name": "VRF_WEB",
      "enforce_routing": true
    }
  ],
  "application_profiles": [
    {
      "name": "AP_WEB_APP",
      "epgs": [
        {
          "name": "EPG_FRONTEND",
          "bridge_domain": "BD_WEB",
          "contracts": [
            {
              "provider": "HTTP-CONTRACT"
            },
            {
              "consumer": "DB-CONTRACT"
            }
          ]
        },
        {
          "name": "EPG_DATABASE",
          "bridge_domain": "BD_DB",
          "physical_domain": "PHYS_DB_SERVERS"
        }
      ]
    }
  ],
  "policies": {
    "bd": [
      {
        "name": "BD_WEB",
        "gateway": "10.10.10.1/24",
        "vrf": "VRF_WEB"
      },
      {
        "name": "BD_DB",
```

**Explicação**

```Bash
Linha[01]: importa as bibliotecas yaml (ler/escrever arquivos yml) e json (nativa do python)
           OBS: para instalar a biblioteca yaml >>> pip install pyyaml  
Linha[03]: - with: Garante que o arquivo será fechado automaticamente após o uso
           - aci_config.yml: Nome do arquivo YAML de entrada (seu arquivo de configuração)
           - Modo padrão: 'r' (leitura) é assumido quando não especificado
Linha[04]: Carregamento do YAML ( aci_data = yaml.safe_load(f) )
           - yaml.safe_load(): Método seguro para converter YAML → Dicionário Python
             Evita execução de código malicioso (ao contrário de yaml.load())
             f: Objeto do arquivo aberto na linha 3
             Saída: aci_data vira um dicionário Python com a estrutura do YAML
Linha[05]: Conversão e Impressão do JSON ( Conversão e Impressão do JSON )
           - json.dumps(): Converte o dicionário Python → String JSON formatada
           Parâmetros:
            aci_data: Dicionário convertido do YAML
            indent=2: Formatação com 2 espaços (para legibilidade)
```

**Fluxo de trabalho**  

![Fluxo](Imagens/fluxo.png)

  1. Escolher um bom editor para códigos .yml. Exemplo: VSCODE
  2. Escrever primeiro em YAML que serve como uma espécie de resumos e evita erros
         - Erros comuns: Esquecer , ou {} em JSON grandes
         - Sem comentários: Não pode explicar o que cada campo faz
         - Hierarquia confusa: Difícil enxergar aninhamentos complexos
  3. Converter o arquivo YAML para JASON (`json.dumps`)
  4. Enviar ou Receber dados para os equipamentos como o Cisco Dna Center através de APIs (`curl`/`requests`) 
  

Por Que Usar safe_load?

    - Segurança: APIs Cisco manipulam configurações críticas

    - Boas Práticas: Nunca use yaml.load() com fontes não confiáveis

Exemplo de Uso no CCNP

    Crie aci_config.yml com configurações de tenant/VRF

    Execute o script:
    
```bash
python3 converter.py > config.json
```

Envie para a API Cisco

Este script é a ponte essencial entre sua automação legível (YAML) e as APIs Cisco que exigem JSON!

## Exercício Prático

Converta este JSON para YAML e envie para a API DNA Center:  

```json
{
  "interface": {
    "name": "Gig0/1",
    "ip": "10.0.0.1/24",
    "status": "up"
  }
}
```
Utilize ferramentas de validação de arquivos YAML  
- https://www.yamllint.com/
- https://www.site24x7.com/pt/tools/yaml-validator.html

### Recursos Adicionais
- [Documentação YAML](https://yaml.org/spec/)
- [API Cisco DNA Center](https://developer.cisco.com/docs/dna-center/)