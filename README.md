# Arcane

Le projets contient 6 fichiers .py ( 1 fichier de configurations et des classes models).

# Langage : Python
# Framework : Flask
# ORM : sqlalchemy
# IDE : Pycharm
# Base de données : MySQL

J'ai défini 4 classes : Utilisateur, BienImmobilier, Piece, Ville.

Toutes les methodes sont accompagnées par des commentaires.

Pour tourner le projet en local :
- Installer une base de données MySQL .
- Créer une base nommée "arcane" .
- Installer flask-sqlalchemy and flask-marshmallow .
- S'assurer que tous les imports sont faits sans erreur.
- Lancer la commande '$ python inserts.py' dans le terminal pour générer la base de données avec quelques exemples pour la remplir.
- Une fois la base créée et remplie, on run '$ python BienImmobilier.py' .
- Lancer Advanced REST Client de google par exemple pour tester les URL.

#pour afficher les biens de la ville qui Id = 1 par exemple : http://localhost:5000/bien/1





