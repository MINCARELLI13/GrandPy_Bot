# GrandPy_Bot

##Quel est le but de cette application ?

Cette application vous permet de trouver l'adresse de n'importe quel lieu dans le monde (exemples : Tour Eiffel, pyramide de Mykérinos en Egypte, la "bonne mère" à Marseille...) avec en prime la localisation du site sur une carte Google ainsi qu'une explication wikipedia sur lieu recherché.

##Comment lancer l'application ?

- En ligne, allez sur l'adresse suivante : https://grandpybot-em.herokuapp.com/

- En local :
- Créez un environnement virtuel et activez-le
- Récupérez les fichiers du dépôt GitHub : https://github.com/MINCARELLI13/GrandPy_Bot.git
- Installez les dépendances du fichier requirements.txt
- Le programme run.py peut alors être lancé
- Une fois lancé, allez sur votre navigateur et entrez l'url suivante : http://127.0.0.1:5000/
- Lorsque vous avez terminé, n'oubliez pas de désactiver votre environnement virtuel !

##Comment utiliser cette application ?
Sur la page d'accueil, saisissez une question intégrant une demande d'adresse et appuyez sur la touche "Entrée" de votre clavier.
L'application vous proposera une réponse d'adresse ainsi que la localisation du lieu sur une carte Google.
En prime, votre Grand-Py vous racontera une anecdote issue de ses recherches sur Wikipedia, en rapport avec l'adresse récupérée.

##Quelles sont les API utilisées dans cette application ?
- l'API Google Places pour obtenir l'adresse du lieu ainsi que le la latitude et la longitude du site.
- l'API Google Maps pour afficher une carte Google dans laquelle apparaît le lieu demandé avec un marqueur indiquant l'adresse précise.
- l'API Wiki Media pour obtenir l'histoire du lieu recherché.

##Quels sont les principaux programmes utilisés ?
- Python-3.8
- HTML et CSS
- Bootstrap
- Javascript
- Flask






