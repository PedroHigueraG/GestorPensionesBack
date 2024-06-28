from pydantic import BaseModel
from typing import Optional

#Modelos para usuario
class User(BaseModel):
    
    cedula: int
    nombre: str
    email: str
    telefono: int
    metodo_preferido: str
    saldo: float
    fondos_actuales: Optional[list] = None

class UpdateUser(BaseModel):
    
    cedula: Optional[int] = None
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[int] = None
    metodo_preferido: Optional[str] = None
    saldo: Optional[float] = None
    fondos_actuales: Optional[list] = None

#Modelos para fondos
class Fund(BaseModel):
    
    id: int
    nombre: str
    descripcion: Optional[str] = None
    monto_minimo: float
    categoria: str

#Modelo para transacciones
class Transaction(BaseModel):
    
    id: int
    tipo: str
    monto: float
    fecha_transaccion: str
    idFondo: int
    idUsuario: int

#Modelo para notificaciones
class Notification(BaseModel):
    
    id: int
    idUsuario: int
    tipo: str
    mensaje: str
    fecha: str