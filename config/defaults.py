class Constants:
    OPEN_AI_SECRET_KEY='sk-proj-kLEaBsJZ1IAezSyu1EyDT3BlbkFJHFtV4t2aV2lCKAM7vE0j'
    PINECONE_SECRET_KEY='092c1fad-c7b6-4fd4-a3a0-f6287d775f55'
    PINECONE_INDEX = "engineer-embeddings"


class AppConfig:
    version: str = '1.0.0'
    app_name: str = "Querying Chatbot"
    debug: bool = True
    database_url: str = "mongodb+srv://utkarshrasal:K3cYVC7kvw2ojjdv@mercor.rhkhw9v.mongodb.net/mercor?retryWrites=true&w=majority&appName=mercor"
    # origins = [
    # "http://localhost:3000",
    # ]   
    mongo_pass='K3cYVC7kvw2ojjdv'
config = AppConfig()