# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey, FLOAT
from sqlalchemy.orm import relationship
from Utilisateur import UtilisateurSchema, Utilisateur
from Ville import VilleSchema, Ville
from marshmallow import fields
from flask import jsonify, request
from config import *


class Piece(Base):
    __tablename__ = 'piece'

    id = Column(Integer, primary_key=True)
    surface = Column(FLOAT)
    descriptionP = Column(String(20))
    bienImmobilier_id = Column(Integer, ForeignKey('biens.id'))
    bienImmobilier = relationship("BienImmobilier", backref="biens")


    def __init__(self, surface, descriptionP, bienImmobilier):
        self.surface = surface
        self.descriptionP = descriptionP
        self.bienImmobilier = bienImmobilier

class PieceSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','surface','descriptionP','bienImmobilier_id')


piece_schema = PieceSchema()
pieces_schema = PieceSchema(many=True)


class BienImmobilier(Base):
    __tablename__ = 'biens'

    id = Column(Integer, primary_key=True)
    nom = Column(String(20))
    description = Column(String(20))
    typeBien = Column(String(20))
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    utilisateur = relationship("Utilisateur", backref="biens", cascade="all,delete")
    ville_id = Column(Integer, ForeignKey('ville.id'))
    ville = relationship("Ville", backref="ville")
    pieces = relationship("Piece")

    def __init__(self, nom, description,typeBien, utilisateur, ville):
        self.nom = nom
        self.description = description
        self.typeBien = typeBien
        self.utilisateur = utilisateur
        self.ville = ville



class BienImmobilierSchema(ma.Schema):
    utilisateur = fields.Nested(UtilisateurSchema)
    ville = fields.Nested(VilleSchema)
    pieces = fields.Nested(PieceSchema)
    class Meta:
        fields = ('id','nom', 'description', 'typeBien','utilisateur','ville')


bien_schema = BienImmobilierSchema()
biens_schema = BienImmobilierSchema(many=True)

# Afficher tous les biens
@app.route("/bien", methods=["GET"])
def get_bien():
    session = Session()
    biens = session.query(BienImmobilier).all()
    result = biens_schema.dump(biens)
    return jsonify(result.data)

# Ajouter un bien
@app.route("/bien", methods=["POST"])
def add_bien():

    session = Session()
    data = request.get_json(force=True)
    print(data)
    nomBien = data['nom']
    description = data['description']
    typeBien = data['typeBien']
    userObj = data['utilisateur']
    nomUtilisateur = userObj['nom']
    prenomUtilisateur = userObj['prenom']
    dateNaissance = userObj['dateNaissance']
    villeObj = data['ville']
    nomVille = villeObj['nom']
    codePos = villeObj['codePostal']
    departement = villeObj['departement']
    region = villeObj['region']
    new_user = Utilisateur(nomUtilisateur, prenomUtilisateur, dateNaissance)
    new_ville = Ville(nomVille, departement, region, codePos)
    new_bien = BienImmobilier(nomBien, description, typeBien, new_user, new_ville)
    session.add(new_bien)
    session.commit()
    return jsonify(new_bien)

# supprimer un bien par Id
@app.route("/bien/<id>", methods=["DELETE"])
def delete_bien(id):
    session = Session()
    bien = session.query(BienImmobilier).filter(BienImmobilier.id == id).one()
    session.delete(bien)
    session.commit()
    return bien_schema.jsonify(bien)

# Rechercher les biens par ville
@app.route("/bien/<idVille>", methods=["GET"])
def get_bien_by_id(idVille):
    session = Session()
    biens = session.query(BienImmobilier).filter(BienImmobilier.ville_id == idVille).all()
    result = biens_schema.dump(biens)
    return jsonify(result.data)

# Modifier un bien
@app.route("/bien/<id>", methods=["PUT"])
def update_bien(id):
  session = Session()
  bien = session.query(BienImmobilier).filter(BienImmobilier.id == id).one()
  data = request.get_json(force=True)
  nomm = data['nom']
  descriptionn = data['description']
  typeBienn = data['typeBien']
  villeObj = data['ville']
  nomVille = villeObj['nom']
  codePos = villeObj['codePostal']
  departement = villeObj['departement']
  region = villeObj['region']
  bien.nom = nomm
  bien.description = descriptionn
  bien.typeBien = typeBienn
  ville = Ville(nomVille, departement, region, codePos)
  bien.ville = ville
  session.commit()
  return bien_schema.jsonify(bien)




# Creer une nouvelle piece
@app.route("/piece/<idBien>", methods=["POST"])
def add_piece(idBien):
    session = Session()
    bien = session.query(BienImmobilier).filter(BienImmobilier.id == idBien).one()
    surface = request.json['surface']
    descriptionP = request.json['descriptionP']
    new_piece = Piece(surface, descriptionP, bien)
    session.add(new_piece)
    session.commit()
    return jsonify(new_piece)

# Afficher toutes les pieces
@app.route("/piece/<idBien>", methods=["GET"])
def get_piece(idBien):
    session = Session()
    pieces = session.query(Piece).filter(Piece.bienImmobilier_id == idBien).all()
    result = pieces_schema.dump(pieces)
    return jsonify(result.data)

# Modifier une piece
@app.route("/piece/<id>", methods=["PUT"])
def update_piece(id):
  session = Session()
  piece = session.query(Piece).filter(Piece.id == id).one()
  surface = request.json['surface']
  description = request.json['descriptionP']
  piece.surface = surface
  piece.descriptionP = description
  session.commit()
  return piece_schema.jsonify(piece)


if __name__ == '__main__':
    app.run(debug=True)






