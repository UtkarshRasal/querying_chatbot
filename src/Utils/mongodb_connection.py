# import motor.motor_asyncio
from pymongo import MongoClient
from config.defaults import AppConfig

# def get_mongo_instance():
#     connection_uri = AppConfig.database_url
#     client = motor.motor_asyncio.AsyncIOMotorClient(connection_uri)
#     return client.get_database('mercor')

def get_mongo_instance():
    connenction_uri = AppConfig.database_url
    client = MongoClient(connenction_uri)
    return client.get_database('mercor')