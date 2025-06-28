from models.products import Productos as ProductosModel
from schemas.products import Product


class ProductService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_productos(self):
        result = self.db.query(ProductosModel).all()
        return result

    def get_producto(self, id):
        result = self.db.query(ProductosModel).filter(ProductosModel.id == id).first()
        return result

    def get_productos_by_category(self, idCategoria):
        result = self.db.query(ProductosModel).filter(ProductosModel.idCategoria == idCategoria).all()
        return result

    def create_producto(self, Product: Product):
        new_producto = ProductosModel(**Product.model_dump(exclude={'categoria'}) )
        self.db.add(new_producto)
        self.db.commit()
        return
    def update_producto(self, id: int, data: Product):
        producto = self.db.query(ProductosModel).filter(ProductosModel.id == id).first()
        producto.nombre = data.nombre
        producto.descripcion = data.descripcion
        producto.foto = data.foto
        producto.precio = data.precio
        producto.idCategoria = data.idCategoria
        self.db.commit()
      
        return
    def delete_producto(self, id: int):
       self.db.query(ProductosModel).filter(ProductosModel.id == id).delete()
       self.db.commit()
       return