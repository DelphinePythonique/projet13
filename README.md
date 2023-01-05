## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Docker

##### Faire tourner l'application en local grace à docker

Prérequis; 
Avoir installé docker 

Récupérer une image présente sur le dockerhub, en remplaçant [tag] par une version d'image
```bash
docker pull delphinepythonique/oc-lettings:[tag]
```  

Créer et activer un container à partir de l'image uploadée
```bash
docker  container run --env-file .env_variables_development -p [port de l\'hôte']:8000 -d delphinepythonique/oc-lettings:lastest
```  

ou utiliser la commande docker-compose: 
pre-requis: docker compose est installé

```bash
docker-compose up
```  

### Vue d'ensemble de l'architecture CI/CD

Ce projet nécessite un compte sur le [docker hub](https://hub.docker.com/),
[circleci](https://circleci.com/), [github](https://github.com/), [heroku](https://dashboard.heroku.com/apps)

1 - Github héberge les sources.

#### Configuration du dépot github
##### Webhook vers circleci
Via le dépot github **DelphinePyhonique / projet13**, **Settings > Webhooks**, un webhook a été ajouté pour que circleci soit notifié en cas de commit sur le dépot


2 - l'application en lien avec ce projet a été créée sur HEROKU sous le nom de [oc-lettings-1974]
#### Configuration de l'application pour HEROKU côté HEROKU
Via Settings ajout des variables d'environnement : SECRET_KEY nécessaire à Django, DSN_SENTRY nécessaire à Sentry

les fichiers Procfile et runtime.txt ont permis à HEROKU d'identifier la stack utile à l'application

#### Configuration de l'application pour HEROKU (instance de production) côté Django

Le fichier de settings.py des sources a été actualisé pour tenir compte de HEROKU notamment grâce aux instructions suivante

```python 
IS_HEROKU = "DYNO" in os.environ
```

Chaque instruction sous condition **if IS_HEROKU:** est utilisé pour HEROKU; notamment
```python 
if IS_HEROKU:
    django_heroku.settings(locals())
```
Cette instruction permet de gérer correctement les fichiers statiques. 

3. **Circleci** prend le relais de github, ses rôles sont de pousser le dockerfile du projet sur le dockerhub, et pousser
les sources de l'application vers Heroku.

Via circleci associer le compte circleci au compte github hébergeant le dépot à suivre. sélectionner le dépot à suivre. 

#### Configuration du projet côté CIRCLE CI

via Circleci > projets > projet13 > ... > Project Settings > Environment Variables, 
les variables d'environnements suivantes sont à ajouter: 
- Pour l'application sous Heroku: HEROKU_API_KEY, HEROKU_APP_NAME
- Pour le transfer sur Docker Hub: PASSWORD_DOCKER_HUB_OPENCLASSROOMS, PASSWORD_DOCKER_HUB_OPENCLASSROOMS
