from fastapi import APIRouter, HTTPException
from database import get_all_transactions, get_transaction, create_transaction
from models import Transaction

transApp = APIRouter()

@transApp.get("/transactions", tags=['Transactions'])
async def get_transactions():
    transactions = await get_all_transactions()
    return transactions

@transApp.get("/transactions/{id}", tags=['Transactions'], response_model=Transaction)
async def obtain_transaction(id: int):
    transaction = await get_transaction(id)
    if transaction:
        return transaction
    raise HTTPException(404,f'Transaccion con id {id} no encontrada')

@transApp.post("/transactions", tags=['Transactions'], response_model=Transaction)
async def add_transaction(transaction: Transaction):

    transactionFound = await get_transaction(transaction.id)

    if transactionFound:
        raise HTTPException(409,'Transaccion con dicho id ya existe')

    response = await create_transaction(transaction.model_dump())
    if response:
        return response
    raise HTTPException(400,'No pudo crearse la transaccion')