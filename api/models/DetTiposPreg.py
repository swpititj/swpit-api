from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Date
from api.data.db import db

class DetTiposPreg(db.Model):
    __tablename__ = 'dettipospreg'
    idDetTipoPreg = Column(Integer, primary_key=True)
    Opcion = Column(String(50), nullable=True)

    idTipoPregunta = Column(Integer, ForeignKey('tipos.idTipoPregunta'))