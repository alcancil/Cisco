"""
connection.py

Funcoes responsaveis por abrir e fechar conexoes SSH com dispositivos Cisco
utilizando Netmiko. Mantido separado do script principal (script_01) para
permitir reuso em outros scripts do laboratorio, como o Script 02, que
percorrera toda a topologia.
"""                                                                                     # fecha a docstring do modulo, que documenta o proposito deste arquivo

from netmiko import ConnectHandler                                                      # importa a classe que abre e gerencia a sessao SSH com o equipamento
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException  # importa as excecoes especificas que o Netmiko lanca em falha de timeout e de autenticacao


def conectar(dispositivo: dict):                                                        # define a funcao que recebe um dicionario de conexao e devolve uma sessao ativa
    """
    Abre uma conexao SSH com o dispositivo informado.

    Args:
        dispositivo (dict): dicionario vindo do inventory_loader, contendo
                             'hostname' (apenas identificacao) + os campos
                             esperados pelo Netmiko (device_type, host,
                             username, password, secret, ...).

    Returns:
        BaseConnection: objeto de conexao ativo com o equipamento.
    """                                                                                 # fecha a docstring da funcao, explicando parametro de entrada e retorno
    # 'hostname' e usado so para logs/identificacao -- o Netmiko nao
    # reconhece essa chave, entao ela e removida antes do ConnectHandler.
    parametros_netmiko = {                                                              # cria um novo dicionario que sera efetivamente passado ao Netmiko
        chave: valor for chave, valor in dispositivo.items() if chave != "hostname"     # percorre cada par chave/valor do dispositivo e descarta apenas a chave 'hostname'
    }                                                                                   # fecha a compreensao de dicionario que monta parametros_netmiko

    try:                                                                                # inicia o bloco protegido, pois a conexao pode falhar por rede, IP errado ou credencial invalida
        conexao = ConnectHandler(**parametros_netmiko)                                  # abre de fato a sessao SSH usando os parametros filtrados (device_type, host, username, password, secret...)
        return conexao                                                                  # devolve o objeto de conexao ja autenticado para quem chamou a funcao
    except NetmikoAuthenticationException:                                              # captura especificamente o erro de usuario/senha incorretos
        print(f"[ERRO] Falha de autenticacao em {dispositivo['host']}")                 # informa no console qual host falhou na autenticacao
        raise                                                                           # relanca a excecao para que o chamador saiba que a conexao nao foi estabelecida
    except NetmikoTimeoutException:                                                     # captura especificamente o erro de tempo esgotado ao tentar conectar
        print(f"[ERRO] Timeout ao conectar em {dispositivo['host']}")                   # informa no console qual host nao respondeu a tempo
        raise                                                                           # relanca a excecao para que o chamador saiba que a conexao nao foi estabelecida


def executar_comando(conexao, comando: str) -> str:                                     # define a funcao que roda um comando numa sessao ja aberta e retorna a saida como texto
    """
    Executa um comando na sessao ja estabelecida e retorna a saida bruta.
    """                                                                                 # fecha a docstring da funcao, explicando o que ela faz
    return conexao.send_command(comando)                                                # envia o comando ao equipamento via Netmiko e retorna a resposta da CLI como string


def desconectar(conexao):                                                               # define a funcao responsavel por encerrar a sessao SSH corretamente
    """
    Encerra a sessao SSH corretamente.
    """                                                                                 # fecha a docstring da funcao, explicando seu proposito
    conexao.disconnect()                                                                # fecha a conexao SSH, liberando o recurso no equipamento e na estacao de automacao
