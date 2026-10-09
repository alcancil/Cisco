"""
parser.py

Aplica os templates do TextFSM (via NTC-Templates) sobre as saidas brutas
coletadas em outputs/raw/, convertendo texto puro em registros estruturados
(lista de dicionarios).

Dois comandos (show spanning-tree summary e show interfaces trunk) nao tem
template dedicado no NTC-Templates -- o parser generico e selecionado por
aproximacao e nao bate com o formato real da saida, resultando em lista
vazia. Para esses dois casos, usamos templates TextFSM proprios, salvos em
arquivos/templates/. Para todos os outros comandos, o NTC-Templates
continua sendo usado normalmente.

Mantido separado de script_03 para isolar "como parsear" de "quais
arquivos percorrer".

Dependencias novas: pip install ntc-templates textfsm
"""

from pathlib import Path

import textfsm
from ntc_templates.parse import parse_output

# Este arquivo mora em arquivos/scripts/cisco/ -> sobe 3 niveis para chegar
# na raiz "arquivos/" e localizar a pasta templates/.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# Comandos sem template dedicado no NTC-Templates -> usam template proprio.
TEMPLATES_CUSTOMIZADOS = {
    "show spanning-tree summary": TEMPLATES_DIR / "cisco_ios_show_spanning-tree_summary.textfsm",
    "show interfaces trunk": TEMPLATES_DIR / "cisco_ios_show_interfaces_trunk.textfsm",
}


def _parsear_com_template_customizado(caminho_template: Path, conteudo: str) -> list[dict]:
    """
    Aplica um template TextFSM local (fora do NTC-Templates) sobre o
    conteudo informado, devolvendo os registros no mesmo formato que o
    NTC-Templates devolveria: uma lista de dicionarios.
    """
    with open(caminho_template, encoding="utf-8") as arquivo_template:
        fsm = textfsm.TextFSM(arquivo_template)
        linhas = fsm.ParseText(conteudo)

    return [dict(zip(fsm.header, linha)) for linha in linhas]


def parsear_saida(comando: str, conteudo: str) -> list[dict]:
    """
    Aplica o template TextFSM correspondente ao comando informado sobre o
    conteudo bruto, retornando uma lista de dicionarios com os campos
    estruturados.

    Se o comando estiver em TEMPLATES_CUSTOMIZADOS, usa o template local
    em arquivos/templates/. Caso contrario, usa o NTC-Templates.

    Args:
        comando (str): comando IOS original (ex: "show vlan brief").
        conteudo (str): saida bruta da CLI, lida de um arquivo em outputs/raw/.

    Returns:
        list[dict]: registros estruturados. Lista vazia se nao houver
                     correspondencia nenhuma.
    """
    template_customizado = TEMPLATES_CUSTOMIZADOS.get(comando)
    if template_customizado is not None:
        return _parsear_com_template_customizado(template_customizado, conteudo)

    return parse_output(platform="cisco_ios", command=comando, data=conteudo)
