from fastapi import FastAPI
from mymodels.servant import Servant

import utils.connection as db


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     print(item_dict)
#     return item_dict["price"] + item_dict["tax"]


@app.get("/{database}/{collection}")
async def get_data(database, collection):
    mongo_url = "mongodb://localhost:27017/"
    data = db.get_data(mongo_url, database, collection)[0]
    data.pop("_id", None)
    return data

@app.post("/{database}/{collection}")
async def post_data(database, collection, servant: Servant):
    mongo_url = "mongodb://localhost:27017/"
    db.add_data(mongo_url, database, collection, [servant.dict()])
    return {"response":"Done"}