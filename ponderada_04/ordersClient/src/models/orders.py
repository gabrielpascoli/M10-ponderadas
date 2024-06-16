# orders.py
from sqlalchemy import Column, Integer, String, Double, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class Ordem(Base):
    __tablename__ = 'ordens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer)
    id_produto = Column(Integer)
    preco_total = Column(Double)
    status = Column(String)
    data_criacao = Column(DateTime)
    data_modificacao = Column(DateTime)
    
    def __repr__(self):
        return f"<Ordem(id={self.id}, id_user={self.id_user}, id_produto={self.id_produto}, preco_total={self.preco_total}, status={self.status}, data_criacao={self.data_criacao}, data_modificacao={self.data_modificacao})>"
