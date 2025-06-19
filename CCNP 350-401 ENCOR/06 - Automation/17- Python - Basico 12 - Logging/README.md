# Python - Básico 12

## Logging

### Por Que Logging é Essencial?

Em automação de redes, 90% dos problemas ocorrem em produção — conexões SSH falhas, APIs indisponíveis ou configurações inválidas.
Logging estruturado é sua "caixa preta" para:  

    🕵️‍♂️ Diagnosticar falhas que só acontecem em ambientes reais

    📜 Auditar mudanças em dispositivos de rede

    🔒 Cumprir requisitos de segurança

    🔄 Rollback inteligente com base em logs históricos

---
ARRUMAR

### O que vamos estudar

- Identificar e capturar erros comuns com try, except, else e finally
- Tratar exceções específicas como FileNotFoundError, KeyError, json.JSONDecodeError, PermissionError, entre outras
- Criar scripts mais robustos e prontos para produção
- Adaptar tratamentos de erro para arquivos .txt, .csv, .json, .yaml, .env, .xml e .j2
---
ARRUMAR

### Fluxo de Automação

```mermaid
graph TB
    A[Script Python] --> B[Configuração Inicial do Logging]
    B --> C["Handlers (Arquivo/Syslog/Console)"]
    C --> D{"Eventos Durante Execução"}
    D -->|Conexão SSH| E[Log INFO: 'Conectado a 192.168.1.1']
    D -->|Erro de API| F[Log ERROR: 'Time0out na API DNA Center']
    D -->|Alteração Config| G[Log WARNING: 'VLAN 10 modificada']
    D -->|Falha Crítica| H[Log CRITICAL: 'Dispositivo inacessível']
    E --> I[Arquivo network.log]
    F --> I
    G --> I
    H --> J[Alertas por Email/Slack]
    I --> K[Ferramentas de Análise]
    K --> L["Grafana (Dashboards)"]
    K --> M["ELK (Busca Full-Text)"]

    style B fill:#d1ecf1,stroke:#17a2b8,color:#000000  # Configuracao
    style E fill:#005500,stroke:#00AA00,color:#FFFFFF  # INFO
    style F fill:#5c4a00,stroke:#f0ad4e,color:#FFFFFF  # ERROR
    style G fill:#5c1a1a,stroke:#dc3545,color:#FFFFFF  # WARNING
    style H fill:#000000,stroke:#ff0000,color:#ffffff  # CRITICAL
    style I fill:#e2e3e5,stroke:#6c757d,color:#000000  # Arquivo
```
  
**Legenda de Uso:**  

| Cor         | Nível de Log  | Quando Usar                                  |
|-------------|---------------|----------------------------------------------|
| 🟢 Verde    | INFO          | Conexões bem-sucedidas, eventos rotineiros   |
| 🟡 Amarelo  |	WARNING       | Configurações incomuns mas não críticas      |
| 🔴 Vermelho |	ERROR         | Falhas recuperáveis (ex: timeout SSH)        |
| ⚫ Preto    | CRITICAL      | Falhas que exigem ação imediata              |

---
Arrumar

### Como funciona ?

Para o tratamento de erros, existem as estruturas **try, except, else e finally**. 

O tratamento de erros (try/except/finally) é essencial em automação de redes porque:

    Evita que scripts falhem silenciosamente (ex.: um erro em um roteador não deve parar toda a automação).

    Facilita a depuração (logs claros sobre o que deu errado).

    Garante limpeza de recursos (fechar conexões SSH, liberar memória).

1. Estrutura Básica e Propósito

| Bloco	  | Quando é Executado?	              | Para que Serve?                                                    |
|---------|-----------------------------------|--------------------------------------------------------------------|
| try	  | Sempre primeiro.	              | Delimita o código que pode gerar erros.                            |
| except  | Apenas se ocorrer um erro no try. | Trata erros específicos (ex.: conexão falhou, arquivo não existe). |
| else	  | Apenas se NÃO houver erro no try. | Executa código que depende do sucesso do try (opcional).           |
| finally | Sempre, com ou sem erros.         | Garante ações finais (ex.: fechar arquivos, conexões).             |

2. Funcionamento Passo a Passo

```python
try:
    print("Passo 1: Tenta executar este código.")
    resultado = 10 / 0  # Isso causa um erro (ZeroDivisionError)
except ZeroDivisionError:
    print("Passo 2: Se der erro, pula para cá.")
else:
    print("Passo 3: Só roda se NÃO houver erro.")
finally:
    print("Passo 4: Roda SEMPRE, mesmo com erro.")
```

**Saída:**  

```bash
Passo 1: Tenta executar este código.
Passo 2: Se der erro, pula para cá.
Passo 4: Roda SEMPRE, mesmo com erro.
```

### Posso Usar Mais de Um try no Mesmo Código?

> Sim! Você pode aninhar try/except ou usá-los sequencialmente

**Exemplo 1:** *try* Aninhados (para erros em etapas diferentes)

```python

try:
    arquivo = open("dados.json", "r")  # Pode dar FileNotFoundError
    try:
        dados = json.load(arquivo)  # Pode dar JSONDecodeError
    except json.JSONDecodeError:
        print("Erro: JSON inválido!")
    finally:
        arquivo.close()  # Fecha o arquivo, mesmo com erro no JSON
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
```

**Exemplo 2:** *try* Sequenciais (para ações independentes)

```python

try:
    conectar_ao_switch("192.168.1.1")
except NetmikoTimeoutException:
    print("Falha na conexão ao switch.")

try:
    enviar_comando("show run")
except NetmikoCommandError:
    print("Falha no comando.")
```

### Posso Usar Mais de Um finally?

> Não diretamente. Cada try pode ter apenas um finally, mas você pode aninhar blocos try/finally:

```python

try:
    arquivo = open("config.txt", "r")
    try:
        conteudo = arquivo.read()
    finally:
        arquivo.close()  # Fecha o arquivo, mesmo se houver erro na leitura
except IOError:
    print("Erro ao abrir o arquivo.")
```

### Posso Ter Vários except para o Mesmo try?

> Sim! Capture erros diferentes com ações específicas

```python

try:
    resposta = requests.get("https://api.cisco.com/data", timeout=5)
    resposta.raise_for_status()  # Gera HTTPError para status 4xx/5xx
except requests.Timeout:
    print("API não respondeu a tempo.")
except requests.HTTPError as e:
    print(f"Erro HTTP: {e.response.status_code}")
except Exception as e:  # Genérico (só use se necessário)
    print(f"Erro inesperado: {e}")
```

### Quando Usar else?

> Use para código que só deve rodar se o try for bem-sucedido:

```python

try:
    conexao = Netmiko(**device)
except NetmikoTimeoutException:
    print("Falha na conexão.")
else:  # Só executa se não houver erro no try
    print("Conexão OK! Enviando comandos...")
    conexao.send_command("show run")
finally:
    if 'conexao' in locals():
        conexao.disconnect()
```

### Regras de Ouro

Seja específico nos **except**

   - **Evite except:** sem especificar o erro (captura até KeyboardInterrupt!).
   - **Prefira** except ZeroDivisionError em vez de except Exception.

Use **finally** para limpeza:

   - Conexões de rede (SSH), arquivos abertos (open()), etc.

**else** é opcional, mas útil:

   - Separa o código de "tentativa" do código de "sucesso".

**Não abuse de try/except:**

   - Erros esperados (ex.: usuário digitar letra em campo numérico) devem ser validados antes com if/else.


📂 Tipos de arquivos abordados e erros comuns

### [Arquivos TXT](Arquivos/txt/README.md)

- **Para que serve:** Armazenar logs brutos, saídas de comandos (como show running-config) e relatórios simples.
- **Erros comuns tratados:** Arquivo não encontrado, Permissão negada, etc.
- **Quando usar:** Quando você precisa armazenar ou analisar saídas de CLI simples ou logs sequenciais.

### [Arquivos CSV](Arquivos/csv/README.md) 

- **Para que serve:** Gerenciar inventários de dispositivos, listas de portas, VLANs, IPs ou usuários de forma tabular.
- **Erros comuns tratados:** Colunas ausentes, Delimitadores incorretos, etc.
- **Quando usar:** Quando a estrutura dos dados é tabular (linhas e colunas), e você precisa importar ou exportar para planilhas.

### [Arquivos JSON](Arquivos/json/README.md)

- **Para que serve:** Representar dados estruturados, como inventários hierárquicos ou configurações vindas de APIs (ex: DNA Center, Meraki).
- **Erros comuns tratados:** JSON malformado, Chaves ausentes, etc.
- **Quando usar:** Quando os dados têm estrutura de dicionário/lista e precisam de integração com APIs modernas ou manipulação no Python.
 
### [Arquivos YAML](Arquivos/yaml/README.md) Arrumar

- **Para que serve:** Configurar playbooks no Ansible, inventários do Nornir e dados hierárquicos legíveis por humanos.
- **Erros comuns tratados:** Identação incorreta, Estrutura malformada, etc.
- **Quando usar:** Quando legibilidade e compatibilidade com ferramentas como Ansible e Nornir são prioridades.

### [Arquivos XML](Arquivos/xml/README.md) Arrumar

- **Para que serve:** Troca de dados com APIs legadas (NETCONF, ACI, SOAP).
- **Erros comuns tratados:** Tags malformadas, Falhas de parsing, etc.
- **Quando usar:** Quando a plataforma exige XML, como Cisco ACI, IOS-XE com NETCONF ou equipamentos que seguem YANG.

### [Templates J2](Arquivos/j2/README.md) Arrumar

- **Para que serve:** Gerar configurações dinâmicas em massa com base em dados variáveis (como VLANs, interfaces, ACLs).
- **Erros comuns tratados:** Variáveis indefinidas, Sintaxe incorreta nos templates, etc.
- **Quando usar:** Quando você precisa aplicar o mesmo modelo para dezenas de equipamentos, mudando apenas os dados.

### [Arquivos ENV](Arquivos/env/README.md) Arrumar

- **Para que serve:** Armazenar credenciais, IPs, senhas, tokens de API e outras variáveis sensíveis fora do código-fonte.
- **Erros comuns tratados:** Variáveis ausentes, Arquivo .env não encontrado, etc.
- **Quando usar:** Sempre que você quiser manter o código limpo, seguro e reutilizável entre diferentes ambientes (ex: LAB, produção, nuvem).

📌 Como navegar

Clique em qualquer formato acima para ver:

    Exemplos práticos com tratamento de erro

    Bibliotecas Python relacionadas

    Erros específicos que ocorrem em redes Cisco

    Estratégias para garantir resiliência na automação
