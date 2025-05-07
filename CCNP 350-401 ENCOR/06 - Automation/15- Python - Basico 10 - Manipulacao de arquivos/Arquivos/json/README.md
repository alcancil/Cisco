# Python - Básico 10

## 03 Manipulação de arquivos - .json

Arquivos **.json** são amplamente utilizados em automação de redes para:

1. **Inventário de dispositivos**: armazenar atributos complexos como VLANs, interfaces e políticas de QoS.  
2. **Backup de configurações**: salvar configurações com metadados (timestamp, usuário que fez o backup).  
3. **Processamento de logs estruturados**: registrar eventos com múltiplos níveis de detalhe (ex.: interface, severidade, timestamp).  
4. **Comparação de configurações**: identificar diferenças entre versões de configs (antes/depois de mudanças).  
5. **Integração com APIs**: 99% das APIs modernas (Cisco DNA Center, Meraki, ACI) usam JSON.  
6. **Troca de dados entre sistemas**: comunicação entre Ansible/Nornir e dispositivos de rede.  

### Quando Usar JSON vs Outros Formatos

| **Escolha JSON quando...**                  |   **Evite JSON quando...**                 |
|---------------------------------------------|--------------------------------------------|
| Dados têm estrutura hierárquica/aninhada    | Dados são tabulares simples (ex.: CSV)     |
| Necessidade de interoperabilidade com APIs  | Arquivos muito grandes (>100MB)            |
| Legibilidade humana é importante            | Configurações ultra-simples (ex.: .env)    |
| Metadados complexos (ex.: timestamp, tags)  | Performance crítica (use binário/protobuf) |

Antes de começarmos com os exemplos precisamos entender como é a estrutura de um arquivo .json e porquê ele é bastante utilizado hoje em dia. Com o aumento da automação no mercado, as empresas passaram a ter que liberar uma maneira dos usuários / técnicos poderem interagir com seus produtos. Como exemplo temos os sites, redes sociais e ai também temos os equipamentos de rede. Mas por questões de segurança, os fabricantes começaram a disponibilizar parte do seu conteúdo para os usuários poderem interagir. <br></br>
 
Com o crescimento da automação de redes, os fabricantes precisaram criar formas padronizadas para sistemas e dispositivos se comunicarem. Surgiram então dois formatos principais:

1. **XML** (Extensible Markup Language):  
- Primeiro formato amplamente adotado para APIs.  
- Problema: Verbosidade excessiva e difícil leitura humana.  

   ```xml
   <device>
       <hostname>R1</hostname>
       <ip>10.0.0.1</ip>
   </device>
   ```

**JSON (JavaScript Object Notation):**

Desenvolvido como parte do JavaScript, mas tornou-se independente.

**Vantagens:**
- Estrutura leve e fácil de ler/escrever.  
- Mapeamento direto para estruturas de dados em linguagens modernas.  

```json

        {
            "hostname": "R1",
            "ip": "10.0.0.1"
        }
```

Por que JSON domina na automação de redes?

- **Legibilidade:** Facilita debugging e manutenção.
- **Interoperabilidade:** Suporte nativo em Python, JavaScript, APIs Cisco/Meraki/etc.
- **Eficiência:** Menos overhead que XML (em tamanho e processamento).
- **Hierarquia:** Representa naturalmente configurações complexas de redes:
    
```json
    {
        "device": {
            "hostname": "switch01",
            "vlans": [
                {"id": 10, "name": "VLAN_GESTAO"},
                {"id": 20, "name": "VLAN_VOIP"}
            ]
        }
    }
```

Certo, mas vamos analisar de perto a estrutura do arquivos json. Ele  não lembra algo que já vimos ?  
Sim. Se pararmos para verificar bem de perto, podemos notar que ele é praticamente um dicionário aninhado de python. Ele também aceita uma lista dentro dentro dele.  

**Exemplo .json**  

```json
    {
        "hostname": "R1",
        "ip": "10.0.0.1",
        "interfaces": ["Gig0/1", "Gig0/2"], # [ ] é uma lista
        "ativo": true # Note o 'T' minusculo em json
    }
```

- **Chaves ({}):** Delimitam objetos (equivalente a dicionários em Python).  
- **Colchetes ([]):** Delimitam arrays (listas).  
- **Tipos de dados suportados:** Strings (" "), números, booleanos (true/false), null, objetos e arrays.  

**Exemplo dicionário python**

```Python
    # Equivalente em Python:
    dispositivo = {
        "hostname": "R1",
        "ip": "10.0.0.1",
        "interfaces": ["Gig0/1", "Gig0/2"], # [ ] é uma lista
        "ativo": True  # Note o 'T' maiúsculo em Python
    }
```

- **Diferença:** JSON é um formato de texto padronizado, enquanto dicionários são estruturas de dados nativas do Python.  

Como podemos notar, os dois arquivos tem a estrutura de **chave: valor** . Isso em python é um dicionário.
