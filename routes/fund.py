from fastapi import APIRouter, HTTPException
from database import get_all_funds, get_fund, create_fund
from models import Fund

fundApp = APIRouter()

@fundApp.get("/funds", tags=['Funds'])
async def get_funds():
    funds = await get_all_funds()
    return funds

@fundApp.get("/funds/{id}", tags=['Funds'], response_model=Fund)
async def obtain_fund(id: int):
    fund = await get_fund(id)
    if fund:
        return fund
    raise HTTPException(404,f'Fondo con id {id} no encontrado')

@fundApp.post("/funds", tags=['Funds'], response_model=Fund)
async def add_fund(fund: Fund):

    fundFound = await get_fund(fund.id)

    if fundFound:
        raise HTTPException(409,'Fondo con dicho id ya existe')

    response = await create_fund(fund.model_dump())
    if response:
        return response
    raise HTTPException(400,'No pudo crearse el fondo')