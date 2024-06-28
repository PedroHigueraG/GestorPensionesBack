from fastapi import APIRouter, HTTPException
from database import get_all_notifications, get_notification, create_notification
from models import Notification

notiApp = APIRouter()

@notiApp.get("/notifications", tags=['Notifications'])
async def get_notifications():
    notifications = await get_all_notifications()
    return notifications

@notiApp.get("/notifications/{id}", tags=['Notifications'], response_model=Notification)
async def obtain_notifications(id: int):
    notification = await get_notification(id)
    if notification:
        return notification
    raise HTTPException(404,f'Notificacion con id {id} no encontrada')

@notiApp.post("/notifications", tags=['Notifications'], response_model=Notification)
async def add_notification(notification: Notification):

    notificationFound = await get_notification(notification.id)

    if notificationFound:
        raise HTTPException(409,'Notificacion con dicho id ya existe')

    response = await create_notification(notification.model_dump())
    if response:
        return response
    raise HTTPException(400,'No pudo crearse la notificacion')