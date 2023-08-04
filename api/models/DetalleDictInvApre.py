
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class DetalleDictInvApre(db.Model):
    __tablename__ = 'detalledictinvapre'
    idDetalleDictInvApre = Column(Integer, primary_key=True)
    Canal = Column(CHAR(11), nullable=True)
    ValorNumerico = Column(Integer, nullable=True)
    ObservacionesTutor = Column(String(300), nullable=True)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    #dictamen = db.relationship("Dictamenes", backref='detalledictinvapre', order_by=idDetalleDictInvApre)
    #encuesta = db.relationship("Encuestas", backref='detalledictinvapre', order_by=idDetalleDictInvApre)
