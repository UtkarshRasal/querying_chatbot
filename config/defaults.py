class Constants:
    OPEN_AI_SECRET_KEY=''

class AppConfig:
    version: str = '1.0.0'
    app_name: str = "Querying Chatbot"
    debug: bool = True
    database_url: str = "mongodb+srv://utkarshrasal:K3cYVC7kvw2ojjdv@mercor.rhkhw9v.mongodb.net/mercor?retryWrites=true&w=majority&appName=mercor"
    # origins = [
    # "http://localhost:3000",
    # ]   
    mongo_pass=''

config = AppConfig()