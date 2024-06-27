from fastapi import APIRouter
from src.Utils.validators import CreateThreadPayload
from src.controllers.MessageController import Message



router = APIRouter()

@router.post('/messages')
def send_message(payload: CreateThreadPayload):
    return Message().send_message(payload.message, payload.thread_id)