from motor.motor_asyncio import AsyncIOMotorClient
from models import User, Fund, Transaction, Notification

#Instancia de la BD
client = AsyncIOMotorClient('mongodb://localhost')
database = client.GestorFondosDB
userCollection = database.user
fundCollection = database.fund
transactionCollection = database.transaction
notificationCollection = database.notification

#Funciones para usuarios
async def get_user(cedula):
    user = await userCollection.find_one({'cedula': cedula})
    return user

async def get_all_users():
    users = []
    cursor = userCollection.find({})
    async for document in  cursor:
        users.append(User(**document))
    return users

async def create_user(user):
    new_user = await userCollection.insert_one(user)
    created_user = await userCollection.find_one({'_id': new_user.inserted_id})
    return created_user

async def update_user(cedula: int,data):
    user = {k:v for k, v in data.model_dump().items() if v is not None}
    await userCollection.update_one({'cedula': cedula}, {'$set': user})
    updated_user = await userCollection.find_one({'cedula': cedula})
    return updated_user

async def delete_user(cedula: int):
    await userCollection.delete_one({'cedula': cedula})
    return True


#Funciones para fondos
async def get_fund(id):
    fund = await fundCollection.find_one({'id': id})
    return fund

async def get_all_funds():
    funds = []
    cursor = fundCollection.find({})
    async for document in  cursor:
        funds.append(Fund(**document))
    return funds

async def create_fund(fund):
    new_fund = await fundCollection.insert_one(fund)
    created_fund = await fundCollection.find_one({'_id': new_fund.inserted_id})
    return created_fund

#Funciones para transacciones
async def get_transaction(id):
    transaction = await transactionCollection.find_one({'id': id})
    return transaction

async def get_all_transactions():
    transactions = []
    cursor = transactionCollection.find({})
    async for document in  cursor:
        transactions.append(Transaction(**document))
    return transactions

async def create_transaction(transaction):
    new_transaction = await transactionCollection.insert_one(transaction)
    created_transaction = await transactionCollection.find_one({'_id': new_transaction.inserted_id})
    return created_transaction

#Funciones para notificaciones
async def get_notification(id):
    notification = await notificationCollection.find_one({'id': id})
    return notification

async def get_all_notifications():
    notifications = []
    cursor = notificationCollection.find({})
    async for document in  cursor:
        notifications.append(Notification(**document))
    return notifications

async def create_notification(notification):
    new_notification = await notificationCollection.insert_one(notification)
    created_notification = await notificationCollection.find_one({'_id': new_notification.inserted_id})
    return created_notification