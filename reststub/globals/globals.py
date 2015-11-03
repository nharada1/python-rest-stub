import pymongo
import os
from flask.ext.httpauth import HTTPBasicAuth


def encode_mongo_obj(obj):
    """Convert a Mongo object into a dict for Flask-RESTful"""
    obj['_id'] = str(obj['_id'])
    return obj

# Database stuff is here because we don't wanna connect multiple times
uri = os.environ.get('MONGOLAB_URI')
print("connecting to URI: {}".format(uri))
client = pymongo.MongoClient(uri)
db = client.get_default_database()

# Auth stuff is global
auth = HTTPBasicAuth()
