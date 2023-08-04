
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db


class DetalleAutoEstima(db.Model):
    __tablename__ = 'detalleautoestima'
    idDetalleAutoEstima = Column(Integer, primary_key=True)
    FactorDeAutoEstima = Column(String(15), nullable=True)
    ValorNumerico = Column(Integer, nullable=True)
    ObservacionesTutor = Column(String(300), nullable=True)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    #dictamen = db.relationship("Dictamenes", backref='detalleautoestima', order_by=idDetalleAutoEstima)
    #encuesta = db.relationship("Encuestas", backref='detalleautoestima', order_by=idDetalleAutoEstima)