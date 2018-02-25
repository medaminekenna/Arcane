# Arcane

Le projet contient 6 fichiers .py ( 1 fichier de configuration et des classes models).

Langage : Python /
Framework : Flask /
ORM : sqlalchemy /
IDE : Pycharm /
Base de données : MySQL

J'ai défini 4 classes : Utilisateur, BienImmobilier, Piece, Ville.

Toutes les methodes sont commentées.

Pour tourner le projet en local :
- Installer une base de données MySQL .
- Créer une base nommée "arcane" .
- Pour se connecter au serveur Mysql, voir modifier 'engine' dans le fichier config.py :
  mysql://VotreUserName:VotrePassword@localhost/arcane
- Installer flask-sqlalchemy and flask-marshmallow .
- S'assurer que tous les imports sont faits sans erreur.
- Lancer la commande '$ python inserts.py' dans le terminal pour générer la base de données avec quelques exemples pour la remplir.
- Une fois la base créée et remplie, on run '$ python BienImmobilier.py' .
- Lancer Advanced REST Client de google par exemple pour tester les URL.


pour afficher les biens de la ville qui a Id = 1 par exemple : http://localhost:5000/bien/1






