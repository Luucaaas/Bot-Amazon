# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules
import PyInstaller.__main__

# Nom de l'exécutable final
exe_name = "AmazonBot"

# Fichiers à inclure
datas = [
    ("config.json", "."),   # Inclut config.json à la racine de l'exécutable
    ("product_url.txt", "."),  # Inclut product_url.txt
    ("chromedriver", "."),  # Inclut le fichier chromedriver si nécessaire
]

# Modules cachés si PyInstaller en oublie certains
hidden_imports = collect_submodules("selenium")  # Inclut tous les sous-modules de Selenium

# Configuration de PyInstaller
a = Analysis(
    ["main.py"],  # Script principal
    pathex=["."],  # Chemin du projet
    binaries=[],  # Fichiers binaires supplémentaires si nécessaire
    datas=datas,
    hiddenimports=hidden_imports, 
    hookspath=[], 
    runtime_hooks=[], 
    excludes=[], 
    noarchive=False,
)

pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name=exe_name,
    debug=False,  # Mettre à True pour voir les logs
    strip=False,
    upx=True,
    console=True,  # Mettre à False pour cacher la console
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name=exe_name,
)
