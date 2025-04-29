# ai-learning

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