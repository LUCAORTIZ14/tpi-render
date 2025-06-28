from config.database import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

class Ventas(Base):

    __tablename__ = "ventas"
    
    id= Column(Integer, primary_key=True)
    idUsuario=Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    emailUsuario=relationship('Usuarios',lazy="joined")
    idProducto= Column(Integer, ForeignKey('productos.id'), nullable=False)
    nombreProducto=relationship('Productos',lazy="joined") 
    cantidad= Column(Integer)
    fecha= Column(Date) 
    despachado= Column(Boolean)
