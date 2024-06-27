
from pydantic import BaseModel
from typing import Optional

class RegisterPayload(BaseModel):
    username: str
    password: str
    confirm_password: str

class LoginPayload(BaseModel):
    username: str
    password: str

class AuthTokenValidator(BaseModel):
    username: str = None
    id: str = None

class CreateThreadPayload(BaseModel):
    message: str
    thread_id: Optional[str] = None
    queryMode: Optional[str] = None