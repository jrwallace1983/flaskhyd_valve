
from flask_sqlalchemy import SQLAlchemy
from app import app
from geoalchemy2.types import Geometry
import geoalchemy2.functions as func
import json
from sqlalchemy.dialects.postgresql import JSONB
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()


db = SQLAlchemy(app)


class Fire(db.Model):

    """represents an x/y coordinate location."""

    __tablename__ = 'firehydrant'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(30))
    watertype = db.Column(db.String(30))
