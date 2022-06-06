from pymongo import MongoClient
from dateutil import parser
from datetime import datetime
from pandas import DataFrame
from bson.objectid import ObjectId
import pymongo


def get_database():
    print('db connected')
    CONNECTION_STRING = "mongodb+srv://guest:guest@cluster0.2vrmo.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']


# TODO: add error processing
def postToDatabase(obj):
    dbname = get_database()
    collection_name = dbname["users_basket"]
    now = datetime.now()
    create_date = now.strftime("%m/%d/%Y, %H:%M:%S")
    create = parser.parse(create_date)
    collection_name.insert_one([obj])


def getFromDatabase():
    dbname = get_database()
    collection_name = dbname["users_basket"]
    arr_obj = []
    item_details = collection_name.find()
    for item in item_details:
        arr_obj.append(item)
    return arr_obj


def getObjectById(object_id):
    dbname = get_database()
    collection_name = dbname["users_basket"]
    arr_obj = []
    item = collection_name.find_one({'_id': ObjectId(object_id)})
    return item


def deleteByObjectId(object_id):
    dbname = get_database()
    collection_name = dbname["users_basket"]
    result = collection_name.delete_one({'_id': ObjectId(object_id)})
    return result.deleted_count


def updateById(object_id, new_part):
    dbname = get_database()
    collection_name = dbname["users_basket"]
    result = collection_name.update_one(
        {'_id': ObjectId(object_id)}, {'$set': new_part})
    return result.matched_count
