import pymongo
from pymongo import MongoClient

cluester = MongoClient("mongodb+srv://thiago:x@cluster0-jhejj.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluester['discord']
collection = db['discord-botimage']

def update(id):
    if collection.find_one({'_id':id}):
        collection.update_one({'_id': id}, {'$inc': {'value': 1}})
    else:
        collection.insert_one({'_id':id,'value':1})