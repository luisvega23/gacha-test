from fastapi import FastAPI
import utils.connection as db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{database}/{collection}")
async def get_data(database, collection):
    mongo_url = "mongodb://localhost:27017/"
    data = db.get_data(mongo_url, database, collection)[0]
    data.pop("_id", None)
    return data
    