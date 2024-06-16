# src/repository/produtos.py

from models.orders import Ordem
from sqlalchemy.orm import Session
from datetime import datetime

class OrdemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, ordem_id):
        return self.db.query(Ordem).get(ordem_id)

    def get_all(self):
        return self.db.query(Ordem).all()

    def add(self, ordem: Ordem):
        ordem.id = None
        ordem.data_criacao = datetime.now()
        self.db.add(ordem)
        self.db.flush()
        self.db.commit()
        return {"message": "Ordem cadastrada com sucesso"}

    def update(self, ordem_id, ordem):
        ordemdb = self.db.query(Ordem).filter(Ordem.id == ordem_id).first()
        if ordemdb is None:
            return {"message": "Ordem não encontrada"}
        ordem.data_modificacao = datetime.now()
        ordem = ordem.__dict__
        ordem.pop("_sa_instance_state")
        ordem.pop("data_criacao")
        ordem.pop("id")
        self.db.query(Ordem).filter(Ordem.id == ordem_id).update(ordem)
        self.db.flush()
        self.db.commit()
        return {"message": "Ordem finalizada com sucesso"}

    def delete(self, ordem_id):
        ordemdb = self.db.query(Ordem).filter(Ordem.id == ordem_id).first()
        if ordemdb is None:
            return {"message": "Ordem não encontrada"}
        self.db.query(Ordem).filter(Ordem.id == ordem_id).delete()
        self.db.flush()
        self.db.commit()
        return {"message": "Ordem deletada com sucesso"}