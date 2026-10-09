"""
inventory_loader.py

Carrega o inventario de dispositivos a partir do arquivo YAML
(arquivos/inventario/inventario.yaml) e combina cada dispositivo com as
credenciais definidas no .env (NET_USERNAME, NET_PASSWORD, NET_SECRET).

Substitui o antigo inventory.py com dicionario hardcoded. Mantido separado
de connection.py para isolar "de onde vem o dado" de "como conectar".

Dependencias novas: pip install pyyaml python-dotenv
"""

import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

# Este arquivo mora em arquivos/scripts/cisco/ -> sobe 3 niveis para chegar
# na raiz "arquivos/" e localizar a pasta inventario/.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
INVENTORY_DIR = BASE_DIR / "inventario"
INVENTORY_PATH = INVENTORY_DIR / "inventario.yaml"
ENV_PATH = INVENTORY_DIR / ".env"   # .env vive junto do inventario.yaml

# Caminho explicito em vez de busca automatica por cwd -- assim o script
# funciona igual, seja executado de dentro de scripts/cisco/ ou de onde for.
load_dotenv(ENV_PATH)

NET_USERNAME = os.getenv("NET_USERNAME")
NET_PASSWORD = os.getenv("NET_PASSWORD")
NET_SECRET = os.getenv("NET_SECRET")


def _validar_credenciais():
    faltando = [
        nome for nome, valor in (
            ("NET_USERNAME", NET_USERNAME),
            ("NET_PASSWORD", NET_PASSWORD),
            ("NET_SECRET", NET_SECRET),
        ) if not valor
    ]
    if faltando:
        raise RuntimeError(
            f"Variaveis ausentes no .env: {', '.join(faltando)}. "
            "Confirme se o arquivo .env existe e nao foi enviado ao Git."
        )


def carregar_inventario() -> list[dict]:
    """
    Le o inventario.yaml e retorna uma lista de dispositivos prontos
    para o Netmiko, ja combinados com as credenciais do .env.
    """
    _validar_credenciais()

    with open(INVENTORY_PATH, "r", encoding="utf-8") as arquivo:
        dados = yaml.safe_load(arquivo)

    dispositivos = []
    for item in dados["devices"]:
        dispositivos.append({
            "hostname": item["hostname"],      # so para identificacao/logs, removido antes do Netmiko
            "device_type": item["platform"],    # "cisco_ios" ja e o valor esperado pelo Netmiko
            "host": item["host"],
            "username": NET_USERNAME,
            "password": NET_PASSWORD,
            "secret": NET_SECRET,
        })
    return dispositivos


def obter_dispositivo(hostname: str) -> dict:
    """
    Retorna um unico dispositivo do inventario pelo hostname.
    Usado pelo Script 01 para testar a conexao com um unico equipamento.
    """
    for dispositivo in carregar_inventario():
        if dispositivo["hostname"] == hostname:
            return dispositivo
    raise ValueError(f"Dispositivo '{hostname}' nao encontrado no inventario.")
