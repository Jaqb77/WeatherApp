from pymongo import MongoClient
from config import Config

def db():
    client = MongoClient(Config.DB_URI)
    db = client["miasta_db"]
    collection = db["weather"]
    return collection

def save_to_mongo(data):
    try:
        mongo = db() # wywołanie db
        mongo.insert_one(data)  # wpisanie danych
        print("Zapisano dane do bazy")
    except Exception as e:
        print(e)