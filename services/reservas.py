from models.reservas import Reserva as ReservaModel
from schemas.reservas import Reserva


class ReservaService():
    
    def __init__(self, db) -> None:
        self.db = db
    def get_reservas(self):
        result = self.db.query(ReservaModel).all()
        return result
    def get_reservas(self, id):
        result = self.db.query(ReservaModel).filter(ReservaModel.id == id).first()
        return result
    def create_reserva(self, Reserva: Reserva):
        new_reserva = ReservaModel(**Reserva.model_dump(exclude={'emailUsuario', 'matriculaVehicula'})  )
        self.db.add(new_reserva)
        self.db.commit()
        return
    def delete_reserva(self, id: int):
       self.db.query(ReservaModel).filter(ReservaModel.id == id).delete()
       self.db.commit()
       return