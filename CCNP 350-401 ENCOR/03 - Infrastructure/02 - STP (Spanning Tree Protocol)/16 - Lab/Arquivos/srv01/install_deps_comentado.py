#!/usr/bin/env python3                                                      # 1. Define o interpretador Python (usa o do sistema ou do venv, dependendo de onde for executado)
import yaml                                                                 # 2. Importa a biblioteca 'yaml' para ler o arquivo requirements.yaml
import subprocess                                                           # 3. Importa o módulo que permite executar comandos no sistema (como 'apt' e 'pip')
import sys                                                                  # 4. Importa o módulo 'sys' para acessar o interpretador Python atual

with open("requirements.yaml", "r") as f:                                   # 5. Abre o arquivo requirements.yaml no modo leitura ('r')
    deps = yaml.safe_load(f)                                                # 6. Carrega o conteúdo do YAML e converte para um dicionário Python chamado 'deps'

# Instalar pacotes APT (isso ainda precisa de sudo, pois é sistema)
apt_pkgs = deps.get("system_packages", {}).get("apt", [])                    # 7. Pega a lista de pacotes APT (em 'system_packages.apt'). Se não existir, retorna lista vazia.
if apt_pkgs:                                                                 # 8. Se a lista não estiver vazia, executa o bloco de instalação
    subprocess.run(["sudo", "apt", "install", "-y"] + apt_pkgs, check=True)  # 9. Executa 'sudo apt install -y' seguido pela lista de pacotes. 'check=True' interrompe o script se ocorrer erro.

# Instalar pacotes pip (dentro do venv, sem sudo)
pip_pkgs = deps.get("python_packages", {}).get("pip", [])                    # 10. Pega a lista de pacotes pip (em 'python_packages.pip'). Se não existir, retorna lista vazia.
if pip_pkgs:                                                                 # 11. Se a lista não estiver vazia, executa o bloco de instalação
    subprocess.run([sys.executable, "-m", "pip", "install"] + pip_pkgs, check=True) # 12. Executa 'python -m pip install' seguido pela lista de pacotes. Usa 'sys.executable' para garantir o Python correto (do venv).