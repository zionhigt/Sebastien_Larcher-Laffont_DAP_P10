
# Softdesk

Application de critiques littéraire. 


## Prérequis

 - [Python > 3.7.2](https://www.python.org/downloads/)
 - [python-venv](https://docs.python.org/fr/3/library/venv.html)
  
## Installation

- Clonez/téléchargez ce projet
- Placez vous dans le répertoire P10
- Reportez-vous à la documentation [python-venv](https://docs.python.org/fr/3/library/venv.html)
  pour exécuter un environement virtuel.
- Lancez la commande `[PYTHON] -m pip install -r requirements.txt`
- Placez vous dans le répertoire softdesk
- Démarrer le server web avec la commande `[python] manage.py runserver`
- La sortie de commande indique l'url de l'application (default: [http://127.0.0.1:8000/](http://127.0.0.1:8000/))
- Le backoffice d'admistration sera accessible à (admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/))
## POSTMAN

- Rendez-vous sur ma [collection postman](https://www.postman.com/technical-administrator-88271381/workspace/softdesk-dap-p10/collection/14215789-42623f57-ae2f-441f-93bb-95a55a0b95b7)
- Charger l'environement softdeskEnvironment
- Parcourez les différentes routes pour essayer l'API
## PEP8

- [Documentation flake8 configuration](https://flake8.pycqa.org/en/latest/user/configuration.html)
- Reportez-vous à la documentation pour configurer flake8 pour les systèmes UNIX
### TEXTE
- Lancez la commande `[PYTHON] -m flake8 ./ > rapport_flake8.txt`
- Vous obtiendrez un rapport flake8 dans le fichier rapport_flake8.txt
- Ce fichier restera vide si aucune violation n'a été rencontrée
### HTML
- Lancez la commande `[PYTHON] -m flake8 --format=html --htmldir=flake-report`
- Ouvrez le fichier `flake-report/index.html` dans un navigateur web.
- Les erreurs seront explicitement indiquées
  
## Auteur

- [@SébastienLarcherLaffont](https://www.github.com/zionhigt)

  