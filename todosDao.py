from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

class todosDao():

    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client.todoDB
        self.collection = db.todos

    def getAll(self):
        results = []
        cursor = self.collection.find({})
        for c in cursor:
            result = {'_id': str(c['_id']),
                      'title': c['title'],
                      'description': c['description'],
                      'is_completed': c['is_completed'],
                      'created_at': str(c['created_at'])}
            if(str(c['updated_at'])!=''):
                result['updated_at'] = str(c['updated_at'])
            results.append(result)
        return results


    def save(self,todoInsert):
        self.collection.insert_one({
            'title':todoInsert['title'],
            "description":todoInsert['description'],
            "is_completed":False,
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now()
        })
        return True


    def update(self,todo):
        self.collection.update_one(
            {"_id": ObjectId(todo["_id"])},
            {"$set":{"is_completed": True,
            "updated_at": datetime.datetime.now()
        }})
        return True

    def delete(self,todo):
        self.collection.delete_one({"_id": ObjectId(todo)})
        return True
