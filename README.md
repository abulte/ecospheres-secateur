# Ecosphères Sécateur

Plugin QGIS d'intersection spatiale. Sélectionnez une commune, le plugin intersecte automatiquement toutes les couches WFS visibles du projet et extrait les entités concernées.

## Fonctionnalités

- **Recherche de commune** avec autocomplétion (API geo.api.gouv.fr)
- **Intersection automatique** de toutes les couches WFS visibles du projet avec le contour communal
- **Résultats en couches mémoire** regroupées dans un groupe "Résultats secateur"
- **Export CSV** — un fichier par couche dans un dossier au choix

## Installation

QGIS 3.28 minimum.

```bash
# macOS
ln -s /chemin/vers/ecospheres-secateur \
  ~/Library/Application\ Support/QGIS/QGIS3/profiles/default/python/plugins/ecospheres-secateur

# Linux
ln -s /chemin/vers/ecospheres-secateur \
  ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/ecospheres-secateur
```

Puis dans QGIS : **Extensions > Gérer/Installer > chercher "Ecosphères Sécateur" > activer**.

## Utilisation

1. Charger un projet QGIS avec des couches WFS (GPU, Géorisques, etc.)
2. Cliquer sur l'icône sécateur dans la toolbar
3. Taper un nom de commune, sélectionner dans la liste
4. Cliquer **Interroger**
5. Les résultats apparaissent dans le groupe "Résultats secateur"
6. Cliquer **Exporter CSV** pour sauvegarder les attributs

## Développement

```bash
# Cloner et symlinker
git clone <repo> && cd qgis-plugins
ln -s "$(pwd)/ecospheres-secateur" ~/Library/Application\ Support/QGIS/QGIS3/profiles/default/python/plugins/

# Recharger après modif : installer le plugin "Plugin Reloader" et cibler ecospheres-secateur
```

### Structure

```
ecospheres-secateur/
├── __init__.py          # classFactory
├── metadata.txt         # Métadonnées plugin
├── plugin.py            # Toolbar + cycle de vie du dialog
├── ui/
│   └── dialog.py        # Dialog : recherche commune + boutons
├── core/
│   ├── commune_api.py   # Appels geo.api.gouv.fr
│   ├── intersector.py   # Détection WFS, intersection, couches résultat
│   └── export.py        # Export CSV
└── resources/
    └── icon.png
```
