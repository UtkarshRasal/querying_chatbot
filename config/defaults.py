class Constants:
    OPEN_AI_SECRET_KEY=''
    PINECONE_SECRET_KEY=''
    PINECONE_INDEX = "engineer-embeddings"


class AppConfig:
    version: str = '1.0.0'
    app_name: str = "Querying Chatbot"
    debug: bool = True
    database_url: str = ""
    # origins = [
    # "http://localhost:3000",
    # ]   
    mongo_pass=''
config = AppConfig()