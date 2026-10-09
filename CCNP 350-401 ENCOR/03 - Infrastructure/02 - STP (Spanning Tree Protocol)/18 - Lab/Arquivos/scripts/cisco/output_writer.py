"""
output_writer.py

Funcoes responsaveis por organizar e salvar as saidas brutas coletadas de
cada dispositivo em arquivos individuais dentro de arquivos/outputs/raw/.

Estrutura gerada:
    arquivos/outputs/raw/<hostname>/<comando_sanitizado>.txt

Mantido separado de coleta.py para isolar "como e onde salvar" de
"o que fazer com cada dispositivo".
"""

import os
from datetime import datetime
import json
import re
from pathlib import Path

# Este arquivo mora em arquivos/scripts/cisco/ -> sobe 3 niveis para chegar
# na raiz "arquivos/" e localizar as pastas outputs/raw/ e outputs/parsed/.
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# RAW_OUTPUT_DIR = BASE_DIR / "outputs" / "raw"
# PARSED_OUTPUT_DIR = BASE_DIR / "outputs" / "parsed"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RUN_ID_FILE = BASE_DIR / "outputs" / ".run_id"

# Se já existe um RUN_ID gravado, usa ele (mesma rodada).
# Senão, cria um novo e grava o arquivo.
if RUN_ID_FILE.exists():
    RUN_ID = RUN_ID_FILE.read_text().strip()
else:
    RUN_ID = datetime.now().strftime("coleta_%Y-%m-%dT%H-%M-%S")
    RUN_ID_FILE.parent.mkdir(parents=True, exist_ok=True)
    RUN_ID_FILE.write_text(RUN_ID)

RUN_DIR = BASE_DIR / "outputs" / RUN_ID
RAW_OUTPUT_DIR = RUN_DIR / "raw"
PARSED_OUTPUT_DIR = RUN_DIR / "parsed"


def _sanitizar_nome_comando(comando: str) -> str:
    """
    Converte um comando IOS em um nome de arquivo seguro.
    Ex: "show spanning-tree summary" -> "show_spanning-tree_summary"
    """
    nome = comando.strip().replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_\-]", "", nome)


def mapear_comandos(comandos: list[str]) -> dict:
    """
    Constroi o dicionario {nome_sanitizado: comando_original}, usado no
    Script 03 para descobrir qual comando gerou cada arquivo .txt salvo
    em outputs/raw/ (o nome do arquivo, sozinho, nao basta).
    """
    return {_sanitizar_nome_comando(comando): comando for comando in comandos}


def nome_arquivo_parsed(comando: str) -> str:
    """
    Retorna o nome do arquivo .json (sem caminho) correspondente a um
    comando. Usado pelo consolidador (Script 04) para localizar o arquivo
    parseado de cada comando, sem duplicar a logica de sanitizacao.
    """
    return _sanitizar_nome_comando(comando) + ".json"


def salvar_saida(hostname: str, comando: str, conteudo: str) -> Path:
    """
    Salva a saida de um comando em arquivos/outputs/raw/<hostname>/<comando>.txt
    Cria a pasta do hostname automaticamente se ainda nao existir.

    Args:
        hostname (str): nome do dispositivo, usado como subpasta.
        comando (str): comando executado, usado para nomear o arquivo.
        conteudo (str): saida bruta retornada pelo equipamento.

    Returns:
        Path: caminho completo do arquivo gerado.
    """
    pasta_dispositivo = RAW_OUTPUT_DIR / hostname
    pasta_dispositivo.mkdir(parents=True, exist_ok=True)

    nome_arquivo = _sanitizar_nome_comando(comando) + ".txt"
    caminho_arquivo = pasta_dispositivo / nome_arquivo

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    return caminho_arquivo


def salvar_parsed(hostname: str, comando: str, registros: list[dict]) -> Path:
    """
    Salva os registros estruturados (resultado do parsing via TextFSM) em
    arquivos/outputs/parsed/<hostname>/<comando>.json
    Cria a pasta do hostname automaticamente se ainda nao existir.

    Args:
        hostname (str): nome do dispositivo, usado como subpasta.
        comando (str): comando de origem, usado para nomear o arquivo.
        registros (list[dict]): lista de registros retornada pelo parser.

    Returns:
        Path: caminho completo do arquivo gerado.
    """
    pasta_dispositivo = PARSED_OUTPUT_DIR / hostname
    pasta_dispositivo.mkdir(parents=True, exist_ok=True)

    nome_arquivo = _sanitizar_nome_comando(comando) + ".json"
    caminho_arquivo = pasta_dispositivo / nome_arquivo

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, indent=2, ensure_ascii=False)

    return caminho_arquivo
