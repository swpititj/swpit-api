
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class Aplicaciones(db.Model):
    __tablename__ = "aplicaciones"
    idAplicacion = Column(Integer, primary_key=True)
    TituloAplicacion = Column(String(200), unique=False, nullable=False)
    FechaInicial = Column(Date, unique=False, nullable=False)
    FechaFinal = Column(Date, unique=False, nullable=False)
    Autorizo = Column(String(200), unique=False, nullable=False)
    Observaciones = Column(String(200), unique=False, nullable=False)
    EstadoAplicacion = Column(Integer, unique=False,nullable=False)