
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class Dictamenes(db.Model):
    __tablename__ = "dictamenes"
    idDictamen = Column(Integer,primary_key=True)
    FechaAplicacion = Column(Date, unique=False, nullable=False)
    EvalNumerica = Column(Integer, unique=False, nullable=False)
    EvalDescriptiva = Column(String(200), unique=False, nullable=False)
    Observaciones = Column(String(300), unique=False, nullable=False)
    Recomendaciones = Column(String(300), unique=False, nullable=False)

    idAplicPorEst = Column(Integer, ForeignKey('aplicporest.idAplicPorEst'))

    AplicPorEst = db.relationship("AplicPorEst", backref="Dictamenes")
