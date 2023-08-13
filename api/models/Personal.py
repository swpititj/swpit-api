from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from api.data.db import db

class Personal(db.Model):
    __tablename__ = 'personal'
    idPersonal = Column(Integer, primary_key=True)
    NT = Column(String(45))
    Apellidos = Column(String(100))
    Nombre = Column(String(100))
    RFC = Column(CHAR(13))
    Direccion = Column(String(200))
    CorreoPersonal = Column(String(200))
    CorreoInstitucional = Column(String(200))
    TelefonoCelular = Column(CHAR(12))
    TelefonoCasa = Column(CHAR(12))
    Plaza = Column(CHAR(12))
    Tipo = Column(CHAR)

    CargosPersonal = db.relationship("CargosPersonal")