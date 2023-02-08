from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Date
from api.data.db import db

class PadresEstudiantes(db.Model):
    __tablename__ = 'padresestudiantes'
    idPadreEstudiante = Column(Integer, primary_key=True)
    idPadreFamilia = Column(Integer, ForeignKey('padresfamilia.idPadreFamilia'))
    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiante'))
    padresFamilia = db.relationship("PadresFamilia", backref='padresestudiantes', order_by=idPadreEstudiante)
    estudiantes = db.relationship ("Estudiantes", backref='padresestudiantes', order_by=idPadreEstudiante)