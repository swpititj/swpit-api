from sqlalchemy import Column, Integer,CHAR,Date,String,ForeignKey
from api.data.db import db

class Estudiantes(db.Model):
    __tablename__ = 'estudiantes'
    idEstudiante= Column(Integer,primary_key=True)
    NumeroControl = Column(CHAR(10), nullable=True)
    ApellidoPaterno = Column(String(100), nullable=True)
    ApellidoMaterno = Column(CHAR(100))
    Nombre = Column(String(100), nullable=True)
    Sexo= Column(CHAR(1), nullable=True)
    Nacimiento= Column(Date)
    RFC= Column(String(13))
    ESC= Column(Integer)
    
    idSalon = Column(Integer, ForeignKey('salones.idSalon'))
    Salon = db.relationship("Salones", back_populates="Estudiantes")
