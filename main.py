import pymongo

client = pymongo.MongoClient("mongodb://192.168.29.103:27017")
db = client['backend']
collection = db["fetch"]
onn={
    "Email":"hemlo@gmail.com",
    "password":"pass",
}
collection.insert_one(onn)
    