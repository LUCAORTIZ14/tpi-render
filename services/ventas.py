from models.ventas import Ventas as VentasModel
from schemas.ventas import Ventas, VentasUpdate


class VentasService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_ventass(self):
        result = self.db.query(VentasModel).all()
        return result

    def get_ventas(self, id):
        result = self.db.query(VentasModel).filter(VentasModel.id == id).first()
        return result
    def get_ventas_by_estado(self, estado):
        result = self.db.query(VentasModel).filter(VentasModel.despachado == estado).all()
        return result
    
    
    def create_ventas(self, Product: Ventas):
        new_producto = VentasModel(**Product.model_dump(exclude={'emailUsuario', 'nombreProducto'})  )
        self.db.add(new_producto)
        self.db.commit()
        return
    def update_ventas(self, id: int, data: VentasUpdate):
        venta = self.db.query(VentasModel).filter(VentasModel.id == id).first()
        venta.despachado = data.despachado
        self.db.commit()
        return
    def delete_ventas(self, id: int):
       self.db.query(VentasModel).filter(VentasModel.id == id).delete()
       self.db.commit()
       return