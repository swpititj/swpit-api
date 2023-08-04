
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class Puestos(db.Model):
    __tablename__ = "puestos"
    idPuesto = Column(Integer, primary_key=True)
    Codigo = Column(CHAR(10), nullable=True, unique=True)
    Nombre = Column(String(200), nullable=True)
    Descripcion = Column(String(200))