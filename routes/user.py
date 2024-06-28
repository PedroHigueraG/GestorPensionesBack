from fastapi import APIRouter, HTTPException
from database import get_all_users,get_user, create_user, delete_user, update_user
from models import User, UpdateUser

userApp = APIRouter()

# Endpoints de usuario
@userApp.get("/users", tags=['Users'])
async def get_users():
    users = await get_all_users()
    return users

@userApp.get("/users/{cedula}", tags=['Users'], response_model=User)
async def obtain_user(cedula: int):
    user = await get_user(cedula)
    if user:
        return user
    raise HTTPException(404,f'Usuario con cedula {cedula} no encontrado')

@userApp.post("/users", tags=['Users'], response_model=User)
async def add_user(user: User):

    userFound = await get_user(user.cedula)

    if userFound:
        raise HTTPException(409,'Usuario con dicha cedula ya existe')

    response = await create_user(user.model_dump())
    if response:
        return response
    raise HTTPException(400,'No pudo crearse el usuario')

@userApp.put("/users/{cedula}", tags=['Users'], response_model=User)
async def put_user(cedula: int, user: UpdateUser):
    response = await update_user(cedula, user)
    if response:
        return response
    raise HTTPException(404,f'Usuario con cedula {cedula} no encontrado')

@userApp.delete("/users/{cedula}", tags=['Users'])
async def remove_user(cedula: int):
    response = await delete_user(cedula)
    if response:
        return "Usuario eliminado exitosamente"
    raise HTTPException(404,f'Usuario con cedula {cedula} no encontrado')
