
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class DetalleDictHE(db.Model):
    __tablename__ = 'detalledicthe'
    idDetalleDictHE = Column(Integer, primary_key=True)
    HabitoEstudio = Column(String(30), unique=False, nullable=False)
    CalifNumerica = Column(Integer, unique=False, nullable=False)
    CalifDescriptiva = Column(String(25), unique=False, nullable=False)
    ObservacionesTutor = Column(String(300), unique=False, nullable=False)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    dictamen = db.relationship("Dictamenes", backref='detalledicthe', order_by=idDetalleDictHE)
    encuesta = db.relationship("Encuestas", backref='detalledicthe', order_by=idDetalleDictHE)
