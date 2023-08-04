from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from sqlalchemy.orm import relationship
from api.data.db import db

class Encuestas(db.Model):
    __tablename__ = 'encuestas'
    idEncuesta = Column(Integer,primary_key=True)
    Nombre = Column(String(100), nullable=True)
    Descripcion = Column(String(500), nullable=True)
    Instrucciones = Column(String(1000), nullable=True)
    Observaciones = Column(String(500), nullable=True)
    EstadoEncuesta = Column(Integer)

    Secciones = relationship("Seccion", backref="Encuesta")