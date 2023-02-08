from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from sqlalchemy.orm import relationship
from api.data.db import db

class Preguntas(db.Model):
    __tablename__ = 'preguntas'
    idPregunta = Column(Integer, primary_key=True)
    NumeroPregunta = Column(Integer, unique=False, nullable=False)
    TituloPregunta = Column(String(200), unique=False, nullable=False)

    idSeccion = Column(Integer, ForeignKey('seccion.idSeccion'))

    idTipoPregunta = Column(Integer, ForeignKey('tipos.idTipoPregunta'))
    TipoPregunta = relationship('Tipos')