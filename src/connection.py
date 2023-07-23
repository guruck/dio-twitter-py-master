from pymongo import MongoClient

# client = MongoClient("mongodb://dio:dio@localhost:27017/")
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

db = client.dio_live

trends_collection = db.trends
