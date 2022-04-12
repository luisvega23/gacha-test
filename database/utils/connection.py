from http import client
from sqlite3 import connect
from pymongo import * 
import logging

logging.basicConfig(level=logging.INFO)

def connect_db(mongo_url):
    return MongoClient(mongo_url)

def create_db(mongo_url, database):
    client = connect_db(mongo_url)
    return client[database]

def add_data(mongo_url, database, collection, data):
    client = connect_db(mongo_url)
    try:
        if len(data) > 1:
            logging.info("Inserting multiple data")
            client[database][collection].insert_many(data)
        elif len(data) == 0:
            logging.warning("Data is empty !")
        else:
            logging.info("Inserting data")
            client[database][collection].insert_one(data[0])
    except Exception as e:
        logging.error(f"Problems adding data ! Error: {e}")

def get_data(mongo_url, database, collection):
    client = connect_db(mongo_url)
    if database in client.list_database_names():
        if collection in client[database].list_collection_names():
            return client[database][collection].find()

def make_query(mongo_url, database, collection, query):
    client = connect_db(mongo_url)
    return client[database][collection].find(query)

