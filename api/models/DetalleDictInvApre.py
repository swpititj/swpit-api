
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class DetalleDictInvApre(db.Model):
    __tablename__ = 'detalledictinvapre'
    idDetalleDictInvApre = Column(Integer, primary_key=True)
    Canal = Column(CHAR(11), unique=False, nullable=False)
    ValorNumerico = Column(Integer, unique=False, nullable=False)
    ObservacionesTutor = Column(String(300), unique=False, nullable=False)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    dictamen = db.relationship("Dictamenes", backref='detalledictinvapre', order_by=idDetalleDictInvApre)
    encuesta = db.relationship("Encuestas", backref='detalledictinvapre', order_by=idDetalleDictInvApre)
