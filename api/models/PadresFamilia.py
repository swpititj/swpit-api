from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Date,CHAR
from api.data.db import db

class PadresFamilia(db.Model):
    __tablename__ = 'padresfamilia'
    idPadreFamilia =Column(Integer, primary_key=True)
    Apellidos =  Column(String(200), unique=False, nullable=False)
    Nombre = Column(String(100), unique=False, nullable=False)
    Sexo = Column(Integer, unique=False, nullable=False)
    EstadoTrabaja = Column(Integer, unique=False, nullable=False)
    TelefonoTrabajo = Column(CHAR(12), unique=True, nullable=False)
    EstadoVive = Column(Integer, nullable=True)