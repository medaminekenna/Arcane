# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey, FLOAT

from BienImmobilier import BienImmobilier
from config import *
from sqlalchemy.orm import relationship
from flask import jsonify, request


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
        fields = ('id','surface', 'descriptionP', 'bienImmobilier_id')


piece_schema = PieceSchema()
pieces_schema = PieceSchema(many=True)

# Creer un nouveau utilisateur
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

# Afficher tous les utilisateurs
@app.route("/piece/<idBien>", methods=["GET"])
def get_piece(idBien):
    session = Session()
    pieces = session.query(Piece).filter(Piece.bienImmobilier_id == idBien).all()
    result = pieces_schema.dump(pieces)
    return jsonify(result.data)
