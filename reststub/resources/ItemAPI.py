from flask import abort, jsonify
from flask.ext.restful import Resource

from reststub.globals import db, encode_mongo_obj


class ItemAPI(Resource):
    def __init__(self):
        super(ItemAPI, self).__init__()

    def get(self, name):
        found = [encode_mongo_obj(v) for v in db['item'].find({"name": name})]
        return found
