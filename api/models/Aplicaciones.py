
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class Aplicaciones(db.Model):
    __tablename__ = "aplicaciones"
    idAplicacion = Column(Integer, primary_key=True)
    TituloAplicacion = Column(String(200), nullable=True)
    FechaInicial = Column(Date)
    FechaFinal = Column(Date)
    Autorizo = Column(String(200), nullable=True)
    Observaciones = Column(String(200), nullable=True)
    EstadoAplicacion = Column(Integer, nullable=True)