# schemas/orders.py

from pydantic import BaseModel
from datetime import datetime

class Ordem(BaseModel):
    id: int
    id_user: int
    id_produto: int
    preco_total: float
    status: str
    data_criacao: datetime
    data_modificacao: datetime

    class Config:
        orm_mode = True