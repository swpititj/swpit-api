
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class DetalleAsertividad(db.Model):
    __tablename__ = 'detalleasertividad'
    idDetalleAsertividad = Column(Integer, primary_key=True)
    FactorDeAcertividad = Column(String(15), unique=False, nullable=False)
    ValorNumerico = Column(Integer, unique=False, nullable=False)
    ObservacionesTutor = Column(String(300), unique=False, nullable=False)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    #dictamen = db.relationship("Dictamenes", backref='detalleasertividad', order_by=idDetalleAsertividad)
    #encuesta = db.relationship("Encuestas", backref='detalleasertividad', order_by=idDetalleAsertividad)
