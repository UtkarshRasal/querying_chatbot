from fastapi import APIRouter
from src.controllers.AuthenticationController import Authentication
from src.Utils.validators import RegisterPayload, LoginPayload

router = APIRouter()
auth = Authentication()

@router.post("/register")
def register_user(body: RegisterPayload):
    return auth.register_user(body.username, body.password, body.confirm_password)

@router.post("/login")
def login_user(body: LoginPayload):
    return auth.login_user(body.username, body.password)

    