"""
inventory_loader.py

Carrega o inventario de dispositivos a partir do arquivo YAML                      # Descreve o objetivo principal do módulo.
(arquivos/inventario/inventario.yaml) e combina cada dispositivo com as           # Informa de onde os dispositivos são carregados.
credenciais definidas no .env (NET_USERNAME, NET_PASSWORD, NET_SECRET).           # Explica que as credenciais são obtidas do arquivo .env.

Substitui o antigo inventory.py com dicionario hardcoded. Mantido separado         # Explica a evolução da arquitetura do projeto.
de connection.py para isolar "de onde vem o dado" de "como conectar".              # Separa a responsabilidade do inventário da conexão SSH.

Dependencias novas: pip install pyyaml python-dotenv                               # Lista as dependências necessárias para este módulo.
"""

import os                                                                          # Importa funções para acessar variáveis de ambiente.
from pathlib import Path                                                           # Importa a classe Path para manipulação de caminhos.

import yaml                                                                        # Importa a biblioteca responsável por ler arquivos YAML.
from dotenv import load_dotenv                                                     # Importa a função responsável por carregar o arquivo .env.

# Este arquivo mora em arquivos/scripts/cisco/ -> sobe 3 niveis para chegar        # Explica como o caminho absoluto será construído.
# na raiz "arquivos/" e localizar a pasta inventario/.                             # Continua a explicação do comentário anterior.
BASE_DIR = Path(__file__).resolve().parent.parent.parent                           # Obtém o diretório base do projeto.
INVENTORY_DIR = BASE_DIR / "inventario"                                            # Define o diretório onde está localizado o inventário.
INVENTORY_PATH = INVENTORY_DIR / "inventario.yaml"                                 # Define o caminho completo do arquivo inventario.yaml.
ENV_PATH = INVENTORY_DIR / ".env"   # .env vive junto do inventario.yaml            # Define o caminho completo do arquivo .env.

# Caminho explicito em vez de busca automatica por cwd -- assim o script            # Justifica o uso de caminho absoluto.
# funciona igual, seja executado de dentro de scripts/cisco/ ou de onde for.       # Explica a vantagem dessa abordagem.
load_dotenv(ENV_PATH)                                                              # Carrega as variáveis definidas no arquivo .env.

NET_USERNAME = os.getenv("NET_USERNAME")                                           # Lê o usuário armazenado no .env.
NET_PASSWORD = os.getenv("NET_PASSWORD")                                           # Lê a senha armazenada no .env.
NET_SECRET = os.getenv("NET_SECRET")                                               # Lê a senha de modo privilegiado (enable).

def _validar_credenciais():                                                        # Define uma função privada para validar as credenciais.
    faltando = [                                                                   # Cria uma lista contendo as variáveis ausentes.
        nome for nome, valor in (                                                  # Percorre todas as variáveis obrigatórias.
            ("NET_USERNAME", NET_USERNAME),                                        # Verifica a variável de usuário.
            ("NET_PASSWORD", NET_PASSWORD),                                        # Verifica a variável de senha.
            ("NET_SECRET", NET_SECRET),                                            # Verifica a variável de senha privilegiada.
        ) if not valor                                                             # Adiciona à lista apenas as variáveis não definidas.
    ]                                                                              # Finaliza a construção da lista.

    if faltando:                                                                   # Verifica se existe alguma variável ausente.
        raise RuntimeError(                                                        # Gera uma exceção interrompendo a execução do programa.
            f"Variaveis ausentes no .env: {', '.join(faltando)}. "                 # Informa quais variáveis estão faltando.
            "Confirme se o arquivo .env existe e nao foi enviado ao Git."          # Orienta o usuário sobre a possível causa do problema.
        )                                                                          # Finaliza a exceção.

def carregar_inventario() -> list[dict]:                                           # Define a função responsável por carregar o inventário.

    """
    Le o inventario.yaml e retorna uma lista de dispositivos prontos               # Descreve o comportamento da função.
    para o Netmiko, ja combinados com as credenciais do .env.                      # Informa que o retorno já está pronto para o Netmiko.
    """

    _validar_credenciais()                                                         # Valida se todas as credenciais obrigatórias existem.

    with open(INVENTORY_PATH, "r", encoding="utf-8") as arquivo:                   # Abre o arquivo inventario.yaml para leitura.
        dados = yaml.safe_load(arquivo)                                            # Converte o conteúdo YAML em um dicionário Python.

    dispositivos = []                                                              # Cria uma lista vazia para armazenar os dispositivos.

    for item in dados["devices"]:                                                  # Percorre todos os dispositivos definidos no inventário.

        dispositivos.append({                                                      # Adiciona um novo dispositivo à lista.

            "hostname": item["hostname"],      # Nome utilizado apenas para identificação e logs.

            "device_type": item["platform"],   # Converte o campo platform para o parâmetro esperado pelo Netmiko.

            "host": item["host"],              # Endereço IP utilizado para estabelecer a conexão SSH.

            "username": NET_USERNAME,          # Adiciona o usuário carregado do .env.

            "password": NET_PASSWORD,          # Adiciona a senha carregada do .env.

            "secret": NET_SECRET,              # Adiciona a senha do modo privilegiado.

        })                                                                         # Finaliza a inclusão do dispositivo.

    return dispositivos                                                            # Retorna a lista completa de dispositivos.

def obter_dispositivo(hostname: str) -> dict:                                      # Define a função responsável por localizar um equipamento.

    """
    Retorna um unico dispositivo do inventario pelo hostname.                      # Descreve a finalidade da função.
    Usado pelo Script 01 para testar a conexao com um unico equipamento.           # Explica onde essa função será utilizada.
    """

    for dispositivo in carregar_inventario():                                      # Percorre todos os dispositivos carregados do inventário.

        if dispositivo["hostname"] == hostname:                                    # Verifica se o hostname corresponde ao solicitado.

            return dispositivo                                                     # Retorna o dispositivo encontrado.

    raise ValueError(f"Dispositivo '{hostname}' nao encontrado no inventario.")    # Gera uma exceção caso o equipamento não exista.