# ai-learning

# Phase 0 – Pré-requis & outillage (macOS)

## Phase 0.1 — Inventaire & nettoyage

Objectif : connaître l’état de votre machine et supprimer un éventuel Python 3.13 Homebrew qui risque de gêner l’installation propre.

```
python3 --version          # affiche la version actuellement active
which python3              # montre son emplacement
brew --version             # vérifie Homebrew
git --version              # vérifie Git
brew uninstall python@3.13 # retire le Python Homebrew s’il est en 3.13
```

Outils concernés : Terminal macOS, Homebrew.
Pourquoi : éviter les conflits de version et partir d’un environnement propre.

## Phase 0.2 — Outils système
Objectif : disposer des outils de compilation nécessaires à Python et aux bibliothèques natives.

```
xcode-select --install     # installe gcc/clang et make
brew update && brew upgrade
```

Outils concernés : Xcode Command Line Tools, Homebrew.
Pourquoi : beaucoup de dépendances IA (numpy, torch) ont des parties C/C++ qui nécessitent un compilateur.

## Phase 0.3 — Installation de Python 3.12 avec pyenv
Objectif : gérer plusieurs versions de Python sans toucher au Python système d’Apple.

```
brew install pyenv
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
exec $SHELL                   # recharge le shell
pyenv install 3.12.3
pyenv global 3.12.3
python --version              # doit maintenant afficher 3.12.3
```

Outil : pyenv.
Pourquoi : pouvoir changer de version de Python à la demande et reconstruire facilement l’environnement.

## Phase 0.4 — Installation du compilateur Rust
Objectif : régler à la source l’erreur « can’t find Rust compiler » que pip affiche pour certaines libs (ex. tiktoken).

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
rustc --version               # v1.78.0 ou supérieur
```

Outil : rustup.
Pourquoi : plusieurs bibliothèques IA modernes possèdent des extensions Rust pour la vitesse.

## Phase 0.5 — Création du projet et de l’environnement virtuel
Objectif : isoler les dépendances du cursus dans un seul dossier.

```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
cat << 'EOF' > requirements.txt
numpy
pandas
torch
transformers==2.11
EOF
pip install -r requirements.txt
```

Outils : venv, pip.
Pourquoi : garantir la reproductibilité et éviter toute pollution du système.

## Phase 0.6 — Configuration VS Code
Objectif : profiter d’un IDE complet (auto-complétion, formatage, lint).

Installer les extensions : Python, Jupyter, GitLens, Black Formatter, Ruff.

Créer .vscode/settings.json :
```
{
  "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "ruff.enable": true
}
```
Outil : VS Code + extensions.
Pourquoi : gagner du temps grâce au formatage automatique et aux alertes lint.

## Phase 0.7 — Exercice final : script d’automatisation + test
setup_env.py
tests/test_versions.py

# Phase 1 – Python scientifique

But global : manipuler des tableaux numériques, des jeux de données tabulaires, puis représenter visuellement vos résultats.
Livrable final : un mini-projet d’analyse exploratoire (notebook + README) commité et testé dans le CI.

## Phase 1.1 — Préparer l’espace de travail Jupyter
Objectif : disposer d’un dossier clair pour les notebooks et d’un lanceur Jupyter prêt à l’emploi.

# Créer le dossier et installer JupyterLab
```
mkdir -p notebooks
pip install --upgrade jupyterlab ipywidgets
```
# Lancer l’interface
```
jupyter lab
```
Outils : JupyterLab (éditeur notebook moderne), ipywidgets (contrôles interactifs).
Pourquoi : un environnement interactif est indispensable pour l’exploration de données.