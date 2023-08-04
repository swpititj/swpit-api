from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from api.data.db import db
from sqlalchemy.orm import relationship
class Tipos(db.Model):
    __tablename__ = 'tipos'
    idTipoPregunta = Column(Integer, primary_key=True)
    Nombre = Column(String(50), nullable=True)
    Opcion = Column(Integer, nullable= True)
    
    DetTipoPreg = relationship('DetTiposPreg')