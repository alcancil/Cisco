# Python - Básico 07

Agora vamos ver um pouco sobre funções. **def**. 

## Funções

Vamos imaginar que em nosso código precisamos repetir uma parte do código várias vezes.  

```Python
    >>> interfaces = {
    ...     "GigabitEthernet0/0": "up",
    ...     "GigabitEthernet0/1": "down",
    ...     "GigabitEthernet0/2": "up"
    ... }
    >>> 
    >>> # Código repetido para cada interface
    >>> print(f"Verificando GigabitEthernet0/0...")
    Verificando GigabitEthernet0/0...
    >>> if interfaces["GigabitEthernet0/0"] == "up":
    ...     print("Status: UP - Operacional")
    ... else:
    ...     print("Status: DOWN - Problema detectado!")
    ...     print("Enviando alerta para a equipe de redes...")
    ... 
    Status: UP - Operacional
    >>> print(f"\nVerificando GigabitEthernet0/1...")

    Verificando GigabitEthernet0/1...
    >>> if interfaces["GigabitEthernet0/1"] == "up":
    ...     print("Status: UP - Operacional")
    ... else:
    ...     print("Status: DOWN - Problema detectado!")
    ...     print("Enviando alerta para a equipe de redes...")
    ... 
    Status: DOWN - Problema detectado!
    Enviando alerta para a equipe de redes...
    >>> print(f"\nVerificando GigabitEthernet0/2...")

    Verificando GigabitEthernet0/2...
    >>> if interfaces["GigabitEthernet0/2"] == "up":
    ...     print("Status: UP - Operacional")
    ... else:
    ...     print("Status: DOWN - Problema detectado!")
    ...     print("Enviando alerta para a equipe de redes...")
    ... 
    Status: UP - Operacional
    >>> 
```

Será que não existe uma forma mais simples de simplesmente a gente ficar repetindo os mesmos códigos ? Sim existe. Para resolver esse tipo de problema fora desenvolvidas as funções. Mas como elas funcionam ? Vamos analisar a sintaxe básica.

### Sintaxe

```Python
    def nome_da_funcao(parametros):
        """
        Docstring (opcional): 
        Explica o que a função faz e seus parâmetros.
        """
        instrução 1
        instrução 2
        ...
        return valor (opcional)
```
* **def**: Palavra-chave para definir uma função.
* **nome_da_funcao**

    Regras:
        
        Usar em minúsculas (não é obrigatório, mas é uma boa prática)
        Use nomes descritivos.  
        Relacione com a ação (ex: backup_config, testar_ping).
        Não utilizar caracteres especiais.
            
* **(parametros)**: Variáveis de entrada.  
* **Docstring (Opcional, mas recomendado)** Finalidade: Documenta a função para outros desenvolvedores.
* **Corpo da Função**: Bloco de código indentado (4 espaços).
* **return (Opcional)**: Existem casos que vamos ter que retornar algum valor em tela, então utiliza-se o **return**


No exemplo anterior podemos notar alguns problemas.

Problemas:

    O mesmo bloco de código é repetido para cada interface.

    Se precisar mudar a lógica (ex: adicionar um teste de ping), terá que alterar manualmente em todos os lugares.

    Dificuldade de manutenção.

Exemplo COM Funções (Código ORGANIZADO)
python

# Verificação de status de interfaces COM funções (código reutilizável)

# Dados das interfaces (simulando saída de comando 'show interface')
interfaces = {
    "GigabitEthernet0/0": "up",
    "GigabitEthernet0/1": "down",
    "GigabitEthernet0/2": "up"
}

# Função para verificar status e gerar alertas
def verificar_status(interface, status):
    """Verifica o status de uma interface e gera alertas se necessário"""
    print(f"\nVerificando {interface}...")
    if status == "up":
        print("Status: UP - Operacional")
    else:
        print("Status: DOWN - Problema detectado!")
        print("Enviando alerta para a equipe de redes...")

# Loop principal (código limpo e reutilizável)
for interface, status in interfaces.items():
    verificar_status(interface, status)

Vantagens:

    Reutilização: A função verificar_status() é chamada para cada interface.

    Manutenção: Se precisar adicionar um teste de ping, basta modificar a função uma vez.

    Legibilidade: O código principal fica mais claro e objetivo.