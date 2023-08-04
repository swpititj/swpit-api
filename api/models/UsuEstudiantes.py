from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from api.data.db import db

class UsuEstudiantes(db.Model):
    __tablename__ = 'usuestudiantes'
    idUsuEstudiante = Column(Integer, primary_key=True)
    FechaIngreso= Column(Date)
    FechaTermino= Column(Date)
    Activo = Column(Integer)

    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiante'))
    idUsuario = Column(Integer, ForeignKey('usuarios.idusuario'))
    #estudiantes = db.relationship ("Estudiantes", backref='usuestudiantes', order_by=idUsuEstudiante)
    #usuarios = db.relationship("Usuarios", backref='usuestudiantes', order_by=idUsuEstudiante)