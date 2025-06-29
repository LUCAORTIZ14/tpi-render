from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Text
from sqlalchemy.orm import relationship


class Vehiculos(Base):

    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key = True)
    marca = Column(String(20))
    modelo = Column(String(40))
    año = Column(Integer)
    marca = Column(String(20), unique=True)
    capacidad = Column(Integer)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    categoria = relationship('Categorias',lazy="joined")



