from fastapi import FastAPI
from mymodels.servant import Servant
from mymodels.user import User

import utils.connection as db
import logging

logging.basicConfig(level=logging.INFO)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def test_post(user: dict):
    print(user)
    print(User(**user))


@app.get("/get/{database}/{collection}")
async def get_data(database, collection):
    try:
        mongo_url = "mongodb://localhost:27017/"
        data_list = db.get_data(mongo_url, database, collection)
        response = []
        for data in list(data_list):
            data.pop("_id", None)
            response.append(data)
        return response
    except Exception as e:
        logging.error(f"Error getting the data {e}")


@app.post("/edit/{userId}")
async def edit_servants_user(userId, data: dict):
    mongo_url = "mongodb://localhost:27017/"
    user = db.make_query(mongo_url, "db", "user", {"userId": userId})
    servants = user[0]["servants"]
    servants.append(data)
    db.update_data(mongo_url, "db", "user",
                   {"servants": user[0]["servants"]}, {"$set": {"servants": servants}})


@app.post("/add/{database}/{collection}")
async def post_data(database, collection, data: dict):
    try:
        mongo_url = "mongodb://localhost:27017/"
        db.add_data(mongo_url, database, collection, [data])
        return {"response": "Done"}
    except Exception as e:
        logging.error(f"Error adding the data {e}")
