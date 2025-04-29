#!/usr/bin/env python
"""
Crée un venv (si absent), installe les libs et affiche leurs versions.
"""
import subprocess, sys, json, os, importlib.metadata as md, pathlib

PKGS = ["numpy", "pandas", "torch", "transformers"]

def ensure_venv() -> None:
    if not os.environ.get("VIRTUAL_ENV"):
        venv = pathlib.Path(".venv")
        subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)
        activate = venv / "bin" / "activate"
        print(f"Activez d’abord le venv : source {activate}")
        sys.exit(0)

def install_pkgs() -> None:
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip", *PKGS], check=True)
    versions = {p.split("==")[0]: md.version(p.split("==")[0]) for p in ["numpy", "pandas", "torch", "transformers"]}
    print(json.dumps(versions, indent=2))

if __name__ == "__main__":
    ensure_venv()
    install_pkgs()
