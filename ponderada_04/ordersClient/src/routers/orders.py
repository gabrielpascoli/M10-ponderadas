# src/routers/orders.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.orders import Ordem as OrdemSchema
from services.orders import OrdemService
from databases import database
import logging

LOGGER = logging.getLogger(__name__)

router = APIRouter(
    prefix="ordersClient",
    tags=["ordersClient"],
)

@router.get("/orders/{ordem_id}")
async def get_ordem(ordem_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders/{ordem_id}", "ordem_id": ordem_id, "method": "GET"})
    ordemService = OrdemService(db)
    return ordemService.get(ordem_id)

@router.get("/orders")
async def get_ordens(db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders", "method": "GET"})
    ordemService = OrdemService(db)
    return ordemService.get_all()

@router.post("/orders")
async def create_ordem(ordem: OrdemSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders", "method": "POST", "ordem": ordem.dict()})
    ordemService = OrdemService(db)
    return ordemService.add(ordem=ordem)

@router.put("/orders/{ordem_id}")
async def update_ordem(ordem_id: int, ordem: OrdemSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders/{ordem_id}", "method": "PUT", "ordem_id": ordem_id, "ordem": ordem.dict()})
    ordemService = OrdemService(db)
    return ordemService.update(ordem_id, ordem=ordem)

@router.delete("/orders/{ordem_id}")
async def delete_ordem(ordem_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders/{ordem_id}", "method": "DELETE", "ordem_id": ordem_id})
    ordemService = OrdemService(db)
    return ordemService.delete(ordem_id)