# coding=utf-8


from config import *
from datetime import date
from config import Session
from BienImmobilier import  BienImmobilier, Piece

from Utilisateur import Utilisateur
from Ville import Ville

# 2 - generer la base de données
Base.metadata.create_all(engine)

# 3 - creer une nouvelle session
session = Session()

user1 = Utilisateur("kenna", "amine", date(1994, 6, 1))
user2 = Utilisateur("baali", "kaoutar", date(1997, 1, 11))

ville1 = Ville("Paris", "Paris", "ile de france", 75000)
ville2 = Ville("Chatenay Malabry", "Haut seine", "ile de france", 92290)

bien1 = BienImmobilier("appartement", "tres jolie", "appt", user1, ville1)
bien2 = BienImmobilier("villa", "tres belle", "vl", user2, ville2)

piece1 = Piece(20, "vaste", bien1)



session.add(user1)
session.add(user2)
session.add(ville1)
session.add(ville2)
session.add(bien1)
session.add(bien2)
session.add(piece1)

session.commit()
session.close()
