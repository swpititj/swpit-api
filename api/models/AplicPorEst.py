
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class AplicPorEst(db.Model):
    __tablename__ = "aplicporest"
    idAplicPorEst = Column(Integer, primary_key=True)
    FechaAplicacion = Column(Date)
    HoraInicio = Column(Time)
    HoraFinal = Column(Time)

    idEstudiante = Column(Integer,  ForeignKey('estudiantes.idEstudiante'))
    idAplicacion = Column(Integer, ForeignKey('aplicaciones.idAplicacion'))
    #Estudiantes = db.relationship("Estudiantes")
    #Aplicaciones = db.relationship("Aplicaciones")
    Dictamen = db.relationship("Dictamenes")