# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)

engine = create_engine('mysql://root:@localhost/arcane',echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()


