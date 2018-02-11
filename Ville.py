# coding=utf-8

from sqlalchemy import Column, String, Integer
from config import *
from flask import jsonify, request

class Ville(Base):
    __tablename__ = 'ville'

    id = Column(Integer, primary_key=True)
    nom = Column(String(20))
    departement = Column(String(20))
    region = Column(String(20))
    codePostal = Column(Integer)


    def __init__(self, nom, departement, region, codePostal):
        self.nom = nom
        self.departement = departement
        self.region = region
        self.codePostal = codePostal



class VilleSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nom', 'departement', 'region', 'codePostal')


ville_schema = VilleSchema()
villes_schema = VilleSchema(many=True)

# Afficher toute les villes
@app.route("/ville", methods=["GET"])
def get_ville():
    session = Session()
    biens = session.query(Ville).all()
    result = villes_schema.dump(biens)
    return jsonify(result.data)

# Ajouter une nouvelle ville
@app.route("/ville", methods=["POST"])
def add_ville():
    session = Session()
    nom = request.json['nom']
    departement = request.json['departement']
    region = request.json['region']
    codePostal = request.json['codePostal']
    new_ville = Ville(nom, departement, region, codePostal)
    session.add(new_ville)
    session.commit()
    return jsonify(new_ville)

