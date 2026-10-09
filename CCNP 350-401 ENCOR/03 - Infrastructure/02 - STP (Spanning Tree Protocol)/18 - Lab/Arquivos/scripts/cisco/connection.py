"""
connection.py

Funcoes responsaveis por abrir e fechar conexoes SSH com dispositivos Cisco
utilizando Netmiko. Mantido separado do script principal (script_01) para
permitir reuso em outros scripts do laboratorio, como o Script 02, que
percorrera toda a topologia.
"""

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException


def conectar(dispositivo: dict):
    """
    Abre uma conexao SSH com o dispositivo informado.

    Args:
        dispositivo (dict): dicionario vindo do inventory_loader, contendo
                             'hostname' (apenas identificacao) + os campos
                             esperados pelo Netmiko (device_type, host,
                             username, password, secret, ...).

    Returns:
        BaseConnection: objeto de conexao ativo com o equipamento.
    """
    # 'hostname' e usado so para logs/identificacao -- o Netmiko nao
    # reconhece essa chave, entao ela e removida antes do ConnectHandler.
    parametros_netmiko = {
        chave: valor for chave, valor in dispositivo.items() if chave != "hostname"
    }

    try:
        conexao = ConnectHandler(**parametros_netmiko)
        return conexao
    except NetmikoAuthenticationException:
        print(f"[ERRO] Falha de autenticacao em {dispositivo['host']}")
        raise
    except NetmikoTimeoutException:
        print(f"[ERRO] Timeout ao conectar em {dispositivo['host']}")
        raise


def executar_comando(conexao, comando: str) -> str:
    """
    Executa um comando na sessao ja estabelecida e retorna a saida bruta.
    """
    return conexao.send_command(comando)


def desconectar(conexao):
    """
    Encerra a sessao SSH corretamente.
    """
    conexao.disconnect()
