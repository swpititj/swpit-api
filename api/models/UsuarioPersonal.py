from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Date
from api.data.db import db

class UsuarioPersonal(db.Model):
    __tablename__ = 'usuariopersonal'
    idUsuarioPersonal = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date)
    FechaTermino = Column(Date)
    Activo = Column(Integer, default=1)

    idPersonal = Column(Integer, ForeignKey('personal.idPersonal'))
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    #personal = db.relationship("Personal", bnackref='usuariopersonal', order_by=idUsuarioPersonal)
    #usuarios = db.relationship("Usuarios", backref='usuariopersonal', order_by=idUsuarioPersonal)