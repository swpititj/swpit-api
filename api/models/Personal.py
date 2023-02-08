from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from api.data.db import db

class Personal(db.Model):
    __tablename__ = 'personal'
    idPersonal = Column(Integer, primary_key=True)
    nt = Column(Integer, unique=True, nullable=False)
    Apellidos = Column(String(100), nullable=False)
    Nombre = Column(String(100), nullable=False)
    rfc = Column(CHAR(13), unique=True, nullable=False)
    Direccion = Column(String(200), nullable=False)
    CorreoPersonal = Column(String(200), unique=True, nullable=False)
    CorreoInstitucional = Column(String(200), unique=True, nullable=False)
    TelCelular = Column(CHAR(12), unique=True, nullable=False)
    TelCasa = Column(CHAR(12), unique=True, nullable=True)
    Plaza = Column(CHAR(12), unique=False, nullable=False)
    Tipo = Column(CHAR, unique=False, nullable=False)