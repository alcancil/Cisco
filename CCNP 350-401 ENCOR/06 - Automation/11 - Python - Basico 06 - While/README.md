# Python - Básico 06

Agora vamos ver um pouco sobre **while**. 

## While

Essa é uma outra estrutura de repetição. Semelhante ao **for**, ele repete uma ou mais instruções que estiverem dentro de uma certa condição especificada. Então vamos transformar os exemplos anteriores de **for** para **while**.

```Python

   [01] >>> lista = ["Ethernet0/0", "Ethernet0/1", "Ethernet0/2", "Ethernet0/0"]
   [02] >>> indice = 0
   [03] >>> while indice < len(lista):
   [04] ...     print(lista[indice])
   [05] ...     indice += 1
   [06] ... 
   [07] Ethernet0/0
   [08] Ethernet0/1
   [09] Ethernet0/2
   [10] Ethernet0/0
   [11] >>>
```
Nesse exemplo, tivemos que utilizar uma estrutura tradicional em programação, **o contador**. Na linha [01] iniciamos a variável indice em 0 para servir de contador. Ja na linha seguinte [03] temos a nossa condição. Então aqui lê-se : **"enquanto o contador indice for menor que o tamanho da lista faça:"** .  
Logo após, nas linhas [04] e [05], vemos que essas são nossas ações. Antes delas começarem tem um espaço que precisa ser igual ao de todas as nossas ações. Isso se chama indentação.  
Então vamos analisar a linha **[05] indice += 1**. Essa estrutura de **+=** é uma estrutura presente no python para representar soma. Podemos utilizar de outra forma: **indice = indece + 1**, que é a forma clássica. Porém isso foi introduzido no python para simplificar.


Exemplo 2: Configuração de VLANs (original com for)
python

vlans = [10, 20, 30, 40]
for vlan in vlans:
    print(f"Configurando Vlan {vlan}")

Versão com while:
python

vlans = [10, 20, 30, 40]
contador = 0
while contador < len(vlans):
    print(f"Configurando Vlan {vlans[contador]}")
    contador += 1

Exemplo 3: Dispositivos e IPs (original com for)
python

dispositivos = {"R1": "192.168.1.1", "SW1": "10.0.0.1", "FW1": "172.16.0.1"}
for nome, ip in dispositivos.items():
    print(f"{nome} -> IP: {ip}")

Versão com while (mais complexo):
python

dispositivos = {"R1": "192.168.1.1", "SW1": "10.0.0.1", "FW1": "172.16.0.1"}
chaves = list(dispositivos.keys())
indice = 0
while indice < len(chaves):
    chave = chaves[indice]
    print(f"{chave} -> IP: {dispositivos[chave]}")
    indice += 1

Boas Práticas para Loops while:
O que fazer:

    Inicialize o contador antes do loop: Sempre declare e inicialize a variável de controle antes do while

    Atualize a condição dentro do loop: Garanta que o loop terá um fim atualizando a variável de controle

    Use break para condições complexas: Quando a condição de parada não é simples

    Prefira for para iteráveis conhecidos: Use while principalmente quando o número de iterações é desconhecido

    Adicione timeout em loops infinitos: Para evitar loops eternos em monitoramentos contínuos

O que evitar:

    Loops infinitos acidentais: Sempre garanta que a condição do while eventualmente será falsa

    Atualizações esquecidas do contador: Esquecer de incrementar o contador é causa comum de loops infinitos

    Condições complexas demais: Se precisar de muitas condições, considere usar for ou refatorar o código

    Uso desnecessário: Não use while quando um for seria mais claro e seguro

Exemplo Completo com Boas Práticas:
python

# Monitoramento de interfaces com while (exemplo mais realista)
interfaces = {
    "GigabitEthernet0/0": "up",
    "GigabitEthernet0/1": "down",
    "GigabitEthernet0/2": "up"
}

print("Iniciando monitoramento...")
contador = 0
max_tentativas = 3
problema_detectado = False

while contador < max_tentativas and not problema_detectado:
    chaves = list(interfaces.keys())
    indice = 0
    
    while indice < len(chaves):
        interface = chaves[indice]
        status = interfaces[interface]
        
        print(f"Verificando {interface}... Status: {status}")
        
        if status == "down":
            print(f"ALERTA: {interface} está DOWN!")
            problema_detectado = True
            break
            
        indice += 1
    
    if not problema_detectado:
        contador += 1
        print(f"Tentativa {contador}/{max_tentativas} concluída")
        if contador < max_tentativas:
            print("Aguardando 5 segundos para próxima verificação...")
            # time.sleep(5)  # Descomente em código real

print("Monitoramento encerrado.")

Quando usar while ao invés de for:

    Monitoramento contínuo: Quando você quer executar até que uma condição externa mude

    Processamento com condição complexa: Quando a condição de parada não é baseada em um contador simples

    Leitura de streams: Quando lendo dados de uma fonte até que ela se esgote

    Tentativas repetidas: Quando tentando uma operação que pode falhar várias vezes

Lembre-se: em Python, o for é geralmente mais pythonico para iterar sobre elementos conhecidos, enquanto o while é melhor para condições dinâmicas ou desconhecidas.