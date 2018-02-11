# coding=utf-8

from sqlalchemy import Column, String, Integer, Date
from flask import jsonify, request
from config import *


class Utilisateur(Base):
    __tablename__ = 'utilisateurs'

    id = Column(Integer, primary_key=True)
    nom = Column(String(20))
    prenom = Column(String(20))
    dateNaissance = Column(Date)

    def __init__(self, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance



class UtilisateurSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','nom', 'prenom', 'dateNaissance')


user_schema = UtilisateurSchema()
users_schema = UtilisateurSchema(many=True)


# Afficher tous les utilisateurs
@app.route("/user", methods=["GET"])
def get_user():
    session = Session()
    users = session.query(Utilisateur).all()
    result = users_schema.dump(users)
    return jsonify(result.data)


# Creer un nouveau utilisateur
@app.route("/user", methods=["POST"])
def add_user():
    session = Session()
    nom = request.json['nom']
    prenom = request.json['prenom']
    dateNaissance = request.json['dateNaissance']
    new_user = Utilisateur(nom, prenom, dateNaissance)
    session.add(new_user)
    session.commit()
    return jsonify(new_user)


# Supprimer un utilisateur
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    session = Session()
    user = session.query(Utilisateur).filter(Utilisateur.id == id).one()
    session.delete(user)
    session.commit()
    return user_schema.jsonify(user)


# Modifier infos utilisateur
@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
  session = Session()
  user = session.query(Utilisateur).filter(Utilisateur.id == id).one()
  nomm = request.json['nom']
  prenomm = request.json['prenom']
  dateNaissancee = request.json['dateNaissance']
  user.nom = nomm
  user.prenom = prenomm
  user.dateNaissance = dateNaissancee
  session.commit()
  return user_schema.jsonify(user)



