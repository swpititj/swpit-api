
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date,Time
from api.data.db import db

class DetalleDicHA(db.Model):
    __tablename__ = 'detalledicha'
    idDetalleDicHA = Column(Integer, primary_key=True)
    Estilo = Column(CHAR(11), nullable=True)
    Resultado = Column(Integer, nullable=True)
    ObservacionesTutor = Column(String(300), nullable=True)

    idDictamen = Column(Integer, ForeignKey('dictamenes.idDictamen'))
    idEncuesta =  Column(Integer, ForeignKey('encuestas.idEncuesta'))
    # dictamen = db.relationship("Dictamenes", backref='DetalleDicHA', order_by=idDetalleDicHA)
    # encuesta = db.relationship("Encuestas", backref='DetalleDicHA', order_by=idDetalleDicHA)