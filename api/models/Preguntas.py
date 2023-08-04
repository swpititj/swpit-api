from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from sqlalchemy.orm import relationship
from api.data.db import db

class Preguntas(db.Model):
    __tablename__ = 'preguntas'
    idPregunta = Column(Integer, primary_key=True)
    NumeroPregunta = Column(Integer, nullable=True)
    TituloPregunta = Column(String(200), nullable=True)

    idSeccion = Column(Integer, ForeignKey('seccion.idSeccion'))

    idTipoPregunta = Column(Integer, ForeignKey('tipos.idTipoPregunta'))
    TipoPregunta = relationship('Tipos')