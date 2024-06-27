from fastapi import APIRouter, Depends
from src.Utils.validators import CreateThreadPayload
from src.controllers.MessageController import Message
from src.Utils.validators import AuthTokenValidator
from src.services.AuthenticationService import get_current_user



router = APIRouter()
messageInstance = Message()

@router.post('/messages')
def send_message(payload: CreateThreadPayload, loggedInUser: AuthTokenValidator = Depends(get_current_user)):
    return messageInstance.send_message(payload.message, payload.thread_id, loggedInUser)