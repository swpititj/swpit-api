from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Date,CHAR
from api.data.db import db

class PadresFamilia(db.Model):
    __tablename__ = 'padresfamilia'
    idPadreFamilia =Column(Integer, primary_key=True)
    Apellidos =  Column(String(200), nullable=True)
    Nombre = Column(String(100), nullable=True)
    Sexo = Column(Integer)
    EstadoTrabaja = Column(Integer)
    TelefonoTrabajo = Column(CHAR(12))
    EstadoVive = Column(Integer)