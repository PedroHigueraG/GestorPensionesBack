from fastapi import FastAPI
from routes.user import userApp
from routes.fund import fundApp
from routes.transaction import transApp
from routes.notification import notiApp
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

# Creación de app
app = FastAPI()
app.version = "1.0.0"
app.title = "Backend de gestor de fondos BTG"

# Lectura de variables de entorno
origins = [
    config('FRONTEND_URL')
]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ['*'],
    allow_credentials = True,
    allow_headers = ['*']
)

# Endpoint default
@app.get("/", tags=['Home'])
def read_root():
    return "Backend de gestor de fondos BTG"

app.include_router(userApp)
app.include_router(fundApp)
app.include_router(transApp)
app.include_router(notiApp)