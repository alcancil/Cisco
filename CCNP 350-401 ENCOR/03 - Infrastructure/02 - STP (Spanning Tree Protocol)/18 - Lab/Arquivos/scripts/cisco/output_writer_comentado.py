"""
output_writer.py                                                                       # nome do módulo, indicando que ele cuida da escrita dos arquivos de saída

Funcoes responsaveis por organizar e salvar as saidas brutas coletadas de                # início da docstring do módulo, explicando sua responsabilidade principal
cada dispositivo em arquivos individuais dentro de arquivos/outputs/raw/.                # continua a descrição, indicando o destino dos arquivos brutos

Estrutura gerada:                                                                        # cabeçalho da seção que mostra a estrutura de diretórios produzida
    arquivos/outputs/raw/<hostname>/<comando_sanitizado>.txt                             # formato do caminho final dos arquivos brutos salvos por dispositivo

Mantido separado de coleta.py para isolar "como e onde salvar" de                        # justifica a modularização, separando escrita de arquivos da lógica de coleta
"o que fazer com cada dispositivo".                                                      # completa a justificativa, separando o "o quê" do "como/onde"
"""                                                                                      # fecha a docstring do módulo

import os                                                                                # importa o módulo os, usado para acessar variáveis de ambiente e manipular caminhos
from datetime import datetime                                                            # importa datetime, usado para gerar o timestamp do nome da pasta de coleta
import json                                                                              # importa json, usado para serializar os registros parseados em disco
import re                                                                                # importa re, usado para sanitizar nomes de comandos via expressões regulares
from pathlib import Path                                                                 # importa Path, usado para manipular caminhos de arquivos e pastas

# Este arquivo mora em arquivos/scripts/cisco/ -> sobe 3 niveis para chegar                # comentário explicando a lógica de subida de diretórios
# na raiz "arquivos/" e localizar as pastas outputs/raw/ e outputs/parsed/.                # continua a explicação, indicando o destino final das pastas
# BASE_DIR = Path(__file__).resolve().parent.parent.parent                                 # linha antiga de definição do BASE_DIR, agora comentada
# RAW_OUTPUT_DIR = BASE_DIR / "outputs" / "raw"                                            # linha antiga do caminho fixo de raw, agora comentada
# PARSED_OUTPUT_DIR = BASE_DIR / "outputs" / "parsed"                                      # linha antiga do caminho fixo de parsed, agora comentada

BASE_DIR = Path(__file__).resolve().parent.parent.parent                                  # define o diretório raiz do projeto subindo três níveis a partir deste arquivo
RUN_ID_FILE = BASE_DIR / "outputs" / ".run_id"                                            # define o caminho do arquivo de controle que guarda o identificador da rodada atual

# Se já existe um RUN_ID gravado, usa ele (mesma rodada).                                  # comentário explicando a primeira condição da lógica abaixo
# Senão, cria um novo e grava o arquivo.                                                   # comentário explicando a segunda condição da lógica abaixo
if RUN_ID_FILE.exists():                                                                  # verifica se o arquivo de controle já existe em disco
    RUN_ID = RUN_ID_FILE.read_text().strip()                                              # se existir, lê seu conteúdo e remove espaços/quebras de linha nas pontas
else:                                                                                     # caso o arquivo ainda não exista (primeira execução da rodada)
    RUN_ID = datetime.now().strftime("coleta_%Y-%m-%dT%H-%M-%S")                          # gera um novo identificador com timestamp no formato coleta_AAAA-MM-DDTHH-MM-SS
    RUN_ID_FILE.parent.mkdir(parents=True, exist_ok=True)                                 # garante que a pasta outputs/ exista antes de gravar o arquivo de controle
    RUN_ID_FILE.write_text(RUN_ID)                                                        # grava o identificador recém-gerado no arquivo de controle

RUN_DIR = BASE_DIR / "outputs" / RUN_ID                                                   # monta o caminho da pasta versionada da rodada atual
RAW_OUTPUT_DIR = RUN_DIR / "raw"                                                          # define a subpasta onde as saídas brutas (.txt) serão salvas
PARSED_OUTPUT_DIR = RUN_DIR / "parsed"                                                    # define a subpasta onde os registros parseados (.json) serão salvos


def _sanitizar_nome_comando(comando: str) -> str:                                         # define a função que converte um comando IOS em um nome de arquivo seguro
    """                                                                                   # inicia a docstring da função
    Converte um comando IOS em um nome de arquivo seguro.                                 # descreve o propósito da função
    Ex: "show spanning-tree summary" -> "show_spanning-tree_summary"                      # mostra um exemplo do resultado da sanitização
    """                                                                                   # fecha a docstring da função
    nome = comando.strip().replace(" ", "_")                                              # remove espaços nas pontas e troca espaços internos por underline
    return re.sub(r"[^a-zA-Z0-9_\-]", "", nome)                                           # remove qualquer caractere que não seja alfanumérico, underline ou hífen


def mapear_comandos(comandos: list[str]) -> dict:                                         # define a função que gera um dicionário comando_sanitizado -> comando_original
    """                                                                                   # inicia a docstring da função
    Constroi o dicionario {nome_sanitizado: comando_original}, usado no                   # descreve o formato do dicionário retornado
    Script 03 para descobrir qual comando gerou cada arquivo .txt salvo                   # explica em qual contexto o dicionário é usado
    em outputs/raw/ (o nome do arquivo, sozinho, nao basta).                              # justifica por que o nome do arquivo, sozinho, não é suficiente
    """                                                                                   # fecha a docstring da função
    return {_sanitizar_nome_comando(comando): comando for comando in comandos}            # percorre a lista de comandos e monta o dicionário sanitizado -> original


def nome_arquivo_parsed(comando: str) -> str:                                             # define a função que retorna o nome do arquivo .json de um comando
    """                                                                                   # inicia a docstring da função
    Retorna o nome do arquivo .json (sem caminho) correspondente a um                     # descreve o que a função retorna
    comando. Usado pelo consolidador (Script 04) para localizar o arquivo                 # explica quem consome o resultado
    parseado de cada comando, sem duplicar a logica de sanitizacao.                       # justifica a existência da função, evitando duplicação
    """                                                                                   # fecha a docstring da função
    return _sanitizar_nome_comando(comando) + ".json"                                     # aplica a sanitização no comando e adiciona a extensão .json


def salvar_saida(hostname: str, comando: str, conteudo: str) -> Path:                     # define a função que salva a saída bruta de um comando em disco
    """                                                                                   # inicia a docstring da função
    Salva a saida de um comando em arquivos/outputs/raw/<hostname>/<comando>.txt          # descreve o destino do arquivo salvo
    Cria a pasta do hostname automaticamente se ainda nao existir.                        # informa o comportamento automático de criação de pasta

    Args:                                                                                 # inicia a seção de parâmetros da docstring
        hostname (str): nome do dispositivo, usado como subpasta.                         # descreve o parâmetro hostname
        comando (str): comando executado, usado para nomear o arquivo.                    # descreve o parâmetro comando
        conteudo (str): saida bruta retornada pelo equipamento.                           # descreve o parâmetro conteudo

    Returns:                                                                              # inicia a seção de retorno da docstring
        Path: caminho completo do arquivo gerado.                                         # descreve o que a função devolve
    """                                                                                   # fecha a docstring da função
    pasta_dispositivo = RAW_OUTPUT_DIR / hostname                                         # monta o caminho da pasta específica deste dispositivo
    pasta_dispositivo.mkdir(parents=True, exist_ok=True)                                  # cria a pasta do dispositivo (e pais) se ainda não existir

    nome_arquivo = _sanitizar_nome_comando(comando) + ".txt"                              # monta o nome do arquivo .txt a partir do comando sanitizado
    caminho_arquivo = pasta_dispositivo / nome_arquivo                                    # combina pasta e nome para obter o caminho completo do arquivo

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:                         # abre o arquivo em modo escrita com codificação UTF-8
        arquivo.write(conteudo)                                                           # escreve o conteúdo bruto retornado pelo equipamento

    return caminho_arquivo                                                                # devolve o caminho completo do arquivo salvo


def salvar_parsed(hostname: str, comando: str, registros: list[dict]) -> Path:            # define a função que salva os registros parseados em disco
    """                                                                                   # inicia a docstring da função
    Salva os registros estruturados (resultado do parsing via TextFSM) em                 # descreve o que é salvo e sua origem
    arquivos/outputs/parsed/<hostname>/<comando>.json                                     # mostra o caminho final do arquivo gerado
    Cria a pasta do hostname automaticamente se ainda nao existir.                        # informa o comportamento automático de criação de pasta

    Args:                                                                                 # inicia a seção de parâmetros da docstring
        hostname (str): nome do dispositivo, usado como subpasta.                         # descreve o parâmetro hostname
        comando (str): comando de origem, usado para nomear o arquivo.                    # descreve o parâmetro comando
        registros (list[dict]): lista de registros retornada pelo parser.                 # descreve o parâmetro registros

    Returns:                                                                              # inicia a seção de retorno da docstring
        Path: caminho completo do arquivo gerado.                                         # descreve o que a função devolve
    """                                                                                   # fecha a docstring da função
    pasta_dispositivo = PARSED_OUTPUT_DIR / hostname                                      # monta o caminho da pasta parsed específica deste dispositivo
    pasta_dispositivo.mkdir(parents=True, exist_ok=True)                                  # cria a pasta do dispositivo (e pais) se ainda não existir

    nome_arquivo = _sanitizar_nome_comando(comando) + ".json"                             # monta o nome do arquivo .json a partir do comando sanitizado
    caminho_arquivo = pasta_dispositivo / nome_arquivo                                    # combina pasta e nome para obter o caminho completo do arquivo

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:                         # abre o arquivo em modo escrita com codificação UTF-8
        json.dump(registros, arquivo, indent=2, ensure_ascii=False)                       # serializa os registros em JSON formatado, preservando acentos

    return caminho_arquivo                                                                # devolve o caminho completo do arquivo salvo