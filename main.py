from fastapi import FastAPI
from src.routers import MessageRouter
from src.routers import AuthenticationRouter
from fastapi.staticfiles import StaticFiles

from config.defaults import AppConfig

app = FastAPI(debug=True, title=AppConfig.app_name )

# app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(AuthenticationRouter.router, prefix="/query_chatbot/v1/api/auth")
app.include_router(MessageRouter.router, prefix="/query_chatbot/v1/api/chat")


@app.get('/query_chatbot')
def root():
    return {'message': f'Application is up and running with version {AppConfig.version}'}