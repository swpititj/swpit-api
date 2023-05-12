
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db
   

class RespuestaEva(db.Model):
    __tablename__ = 'respuestaseva'
    idRespuestEva = Column(Integer, primary_key=True)
    Respuesta = Column(Integer, unique=False, nullable=False)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idPregunta =  Column(Integer, ForeignKey('preguntas.idPregunta'))
    #dictamen = db.relationship("Dictamenes", backref='respuestaeva', order_by=idRespuestEva)
    #pregunta = db.relationship("Preguntas", backref='respuestaeva', order_by=idRespuestEva)

