from fastapi import FastAPI
from src.routers import MessageRouter
from src.routers import AuthenticationRouter
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

from config.defaults import AppConfig

app = FastAPI(debug=True, title=AppConfig.app_name )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or specify specific origins like "http://localhost"
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.mount("/client", StaticFiles(directory="client_frontend", html=True), name="client_frontend")

app.include_router(AuthenticationRouter.router, prefix="/query_chatbot/v1/api/auth")
app.include_router(MessageRouter.router, prefix="/query_chatbot/v1/api/chat")


@app.get('/query_chatbot')
def root():
    return {'message': f'Application is up and running with version {AppConfig.version}'}