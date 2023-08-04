
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class Dictamenes(db.Model):
    __tablename__ = "dictamenes"
    idDictamen = Column(Integer,primary_key=True)
    FechaAplicacion = Column(Date)
    EvalNumerica = Column(Integer, nullable=True)
    EvalDescripctiva = Column(String(200), nullable=True)
    Observaciones = Column(String(300), nullable=True)
    Recomendaciones = Column(String(300), nullable=False)

    idAplicPorEst = Column(Integer, ForeignKey('aplicporest.idAplicPorEst'))
    #aplicporest = db.relationship("AplicPorEst", backref='dictamenes', order_by=idDictamen)

    DetalleAutoEstima = db.relationship("DetalleAutoEstima")
    DetalleDictInvApre = db.relationship("DetalleDictInvApre")
    DetalleDicHA = db.relationship("DetalleDicHA")
    DetalleDicHE = db.relationship("DetalleDicHE")
    DetalleAsertividad = db.relationship("DetalleAsertividad")
