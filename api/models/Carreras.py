from sqlalchemy import Column, Integer,String,Text
from api.data.db import db

class Carreras(db.Model):
    __tablename__ = 'carreras'
    idCarrera= Column(Integer,primary_key=True)
    nombre = Column(String(50), nullable=True)
    descripcion = Column(Text, nullable=True)

    Salon = db.relationship("Salones", back_populates="Carrera")
