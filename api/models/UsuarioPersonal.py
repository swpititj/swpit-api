from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from api.data.db import db

class UsuarioPersonal(db.Model):
    __tablename__ = 'usuariopersonal'
    idUsuarioPersonal = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date, unique= False, nullable=False)
    FechaTermino = Column(Date, unique=False, nullable=False)
    Activo = Column(Integer, default=1)

    idPersonal = Column(Integer, ForeignKey('personal.idPersonal'))
    idUsuarios = Column(Integer, ForeignKey('usuarios.idUsuario'))
    personal = db.relationship("Personal", bnackref='usuariopersonal', order_by=idUsuarioPersonal)
    usuarios = db.relationship("Usuarios", backref='usuariopersonal', order_by=idUsuarioPersonal)