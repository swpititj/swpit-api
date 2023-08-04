
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class DetalleDicHE(db.Model):
    __tablename__ = 'detallediche'
    idDetalleDicHE = Column(Integer, primary_key=True)
    HabitoEstudio = Column(String(30), nullable=True)
    CalifNumerica = Column(Integer, nullable=True)
    CalifDescriptiva = Column(String(25), nullable=True)
    ObservacionesTutor = Column(String(300), nullable=True)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    # dictamen = db.relationship("Dictamenes", backref='DetalleDicHE', order_by=idDetalleDicHE)
    # encuesta = db.relationship("Encuestas", backref='DetalleDicHE', order_by=idDetalleDicHE)
