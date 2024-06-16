# src/services/orders.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from repository.orders import OrdemRepository
from models.orders import Ordem
from schemas.orders import Ordem as OrdemSchema

class OrdemService:
    def __init__(self, db: Session):
        self.repository = OrdemRepository(db)

    def get(self, ordem_id):
        ordem = self.repository.get(ordem_id)
        if ordem is None:
            raise HTTPException(status_code=404, detail="Ordem não encontrada")
        return ordem

    def get_all(self):
        return self.repository.get_all()

    def add(self, ordem : OrdemSchema):
        ordem = Ordem(**ordem.dict())
        return self.repository.add(ordem)

    def update(self, ordem_id, ordem : OrdemSchema):
        ordem = Ordem(**ordem.dict())
        return self.repository.update(ordem_id, ordem)

    def delete(self, ordem_id):
        return self.repository.delete(ordem_id)