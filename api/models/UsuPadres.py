from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from api.data.db import db

class UsuPadres(db.Model):
    __tablename__ = 'usupadres'
    idUsuPadres = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date)
    FechaTermino = Column(Date)
    Activo = Column(Integer)

    idUsuario = Column(Integer, ForeignKey('usuarios.idusuario'))
    idPadreFamilia = Column(Integer, ForeignKey('padresFamilia.idPadreFamilia'))
    #padresFamilia = db.relationship("PadresFamilia", backref='usupadres', order_by=idUsuPadres)
    #usuarios = db.relationship("Usuarios", backref='usupadres', order_by=idUsuPadres)