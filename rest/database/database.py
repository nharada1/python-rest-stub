import pymongo
import os

uri = os.environ.get('MONGOLAB_URI')
client = pymongo.MongoClient(uri)
db = client.get_default_database()
