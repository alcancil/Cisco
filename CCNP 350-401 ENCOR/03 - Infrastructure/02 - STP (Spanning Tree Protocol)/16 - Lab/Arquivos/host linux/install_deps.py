#!/usr/bin/env python3
import yaml
import subprocess
import sys

with open("requirements.yaml", "r") as f:
    deps = yaml.safe_load(f)

# Instalar pacotes APT
apt_pkgs = deps.get("system_packages", {}).get("apt", [])
if apt_pkgs:
    print(f"Instalando pacotes APT: {apt_pkgs}")
    subprocess.run(["sudo", "apt", "install", "-y"] + apt_pkgs, check=True)
else:
    print("Nenhum pacote APT encontrado.")

# Instalar pacotes pip
pip_pkgs = deps.get("python_packages", {}).get("pip", [])
if pip_pkgs:
    print(f"Instalando pacotes pip: {pip_pkgs}")
    subprocess.run([sys.executable, "-m", "pip", "install"] + pip_pkgs, check=True)
else:
    print("Nenhum pacote pip encontrado.")