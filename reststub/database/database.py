import pymongo
import os


def encode_mongo_obj(obj):
    """Convert a Mongo object into a dict for Flask-RESTful"""
    obj['_id'] = str(obj['_id'])
    return obj


uri = os.environ.get('MONGOLAB_URI')
print("connecting to URI: {}".format(uri))
client = pymongo.MongoClient(uri)
db = client.get_default_database()
