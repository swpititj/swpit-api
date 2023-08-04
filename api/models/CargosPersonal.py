from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Date
from sqlalchemy.orm import relationship
from api.data.db import db

class CargosPersonal(db.Model):
    __tablename__ = 'cargospersonal'
    idCargoPersonal = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date)
    FechaTermino = Column(Date)

    idPersonal = Column(Integer, ForeignKey('personal.idPersonal'))
    idPuesto = Column(Integer, ForeignKey('puestos.idPuesto'))
    idDepartamento = Column(Integer, ForeignKey('departamentos.idDepartamento'))
    #personal = db.relationship("Personal", bnackref='usuariopersonal', order_by=idUsuarioPersonal)
    #usuarios = db.relationship("Usuarios", backref='usuariopersonal', order_by=idUsuarioPersonal)