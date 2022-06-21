import pymongo

from util.logger import Logger

CONNECTION_URL = "mongodb+srv://admin:admin@mongo-aufgabe-dev.671lr.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "aufgabe-cli-dev"

client = pymongo.MongoClient(CONNECTION_URL, serverSelectionTimeoutMS=5000)

aufgabe_database = client.get_database(DATABASE_NAME)