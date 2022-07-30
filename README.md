# Créez une paltforme pour amateur de Nutella
***

## Cahier des charges
Le cahier des charges est disponible <a href="https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/DAPython_P8/Cahier_des_charges.zip"> en cliquant sur ce lien.</a>

***
## Fonctionnalités
* Affichage du champ de recherche dès la page d'accueil
* La recherche ne doit pas s'effectuer en AJAX
* Interface responsive
* Authentification de l'utilisateur: création de compte en entrant un mail et un mot de passe, sans possibilité de changer son mot de passe pour le moment.

***
## Livrables
* Lien vers le <a href="https://leshtroumpfpurbeurre.herokuapp.com/">site</a> en production, entièrement fonctionnel.
* Document écrit expliquant notre __démarche de création__:
  * difficultés rencontrées / solution trouvées
  * lien GitHub
  * lien du site déployé pour utiliser notre projet en production
  * format pdf n'excédent pas 2 pages
  * rédigé en anglais ou français
* Code source du dépôt GitHub
* Tableau agile sur <a href="https://trello.com/b/T00arpyO/pur-beurre">Trello</a>

## Contraintes
* Tests: testez le projet en adoptant la démarche qui nous semble la plus appropriée (TDD ou tests écrits à la fin d'une fonctionnalitée).
* Utilisez une base de données PostgresSQL et non MySQL sous peine de ne pas pouvoir déployer l'applicaiton sur Heroku.
* Inclure une page "Mentions Légales" qui contiendra toutes les coordonnées de l'hébergeur ainsi que les auteurs des différentes ressources libres utilisées (templates, photos, icônes, ...).
* Suivre les bonnes pratiques de la PEP 8.
* Pusher le code régulièrement sur GitHub et créer des PR pour avoir le retour du mentor.
* Code intégralement rédigé en anglais: fonctions, commentaires, ...
* Utiliser une méthodologie de projet agile pour travailler en mode projet.

## How to get this app:
1. Clone this repo;
2. Create a database whit PostgreSQL;
3. Create and open a virtualenv;
4. Install requirement ```pip install -r requirements.txt```;
5. Change password of the database in ```settings.py```;
6. update the database with ```python manage.py makemigrations``` & ```python manage.py migrate```;
7. Download the product with ```python manage.py category``` & ```python manage.py product```;
8. Run the app with ```python manage.py runserver```;