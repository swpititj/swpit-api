from sqlalchemy import Column,Integer,Text,ForeignKey
from sqlalchemy.dialects.mysql import YEAR
from api.data.db import db

class Salones(db.Model):
    __tablename__ = 'salones'
    idSalon= Column(Integer,primary_key=True)
    generacion = Column(YEAR, nullable=True)
    activo = Column(Integer, nullable=True)

    idCarrera = Column(Integer, ForeignKey('carreras.idCarrera'))
    Carrera = db.relationship("Carreras", back_populates="Salon")


    idPersonal = Column(Integer, ForeignKey('personal.idPersonal'))

    Estudiantes = db.relationship("Estudiantes")
