from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Text
from sqlalchemy.orm import relationship


class Productos(Base):

    __tablename__ = "productos"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(20))
    descripcion = Column(String(100))
    foto = Column(Text)
    precio =  Column(Numeric(13,2))
    idCategoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    categoria = relationship('Categorias',lazy="joined")



