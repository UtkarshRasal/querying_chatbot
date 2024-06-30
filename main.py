from fastapi import FastAPI
from src.routers import MessageRouter
from src.routers import AuthenticationRouter
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

from config.defaults import AppConfig

app = FastAPI(debug=True, title=AppConfig.app_name)

# defined middlewares to handle cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# API routers for auth
app.include_router(AuthenticationRouter.router, prefix="/query_chatbot/v1/api/auth")
# API routers for chat messages
app.include_router(MessageRouter.router, prefix="/query_chatbot/v1/api/chat")

@app.get('/query_chatbot')
def root():
    return {'message': f'Application is up and running with version {AppConfig.version}'}