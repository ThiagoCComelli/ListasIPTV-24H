import pymongo
from pymongo import MongoClient
import random
cluester = MongoClient("mongodb+srv://thiago:1234@cluster0-jhejj.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluester['discord']
collection = db['discord-botimage']

def update(author,id):
    if collection.find_one({'_author':author}):
        collection.update_one({'_author': author}, {'$inc': {'message': 1,'money':round(random.uniform(0.5,1.0),1)}})
    else:
        collection.insert_one({'_author':author,'_id':id,'level':0,'message':1,'money':0,'money':round(random.uniform(0.5,1.0),1)})

def levelcheck(id):
    res = collection.find({'_id': id})
    if collection.find({'_id': id}):
        for i in res: return i['level']

def moneycheck(id):
    res = collection.find({'_id': id})
    if collection.find({'_id': id}):
        for i in res: return float(i['money'])

def levelup(id):
    res = collection.find({'_id': id})
    if collection.find({'_id': id}):
        for i in res:
            if i['level'] == 0 and i['money'] >= 10:
                collection.update_one({'_id': id}, {'$inc': {'level': 1}})
                return True
            elif i['level'] != 0 and int(i['money']) >= int(i['level'])**2:
                collection.update_one({'_id': id}, {'$inc': {'level': 1,'money':-(int(i['level'])**2)}})
                return True
            else:
                return False

def set(alvo,acao,qtde):
    res = collection.find({'_id': alvo})
    if collection.find({'_id': alvo}):
        collection.update_one({'_id': alvo}, {'$inc': {acao: qtde}})
        return True
    else:
        return False



