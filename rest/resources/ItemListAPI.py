from flask import abort, jsonify

from reststub.database import db


class ItemListAPI(Resource):
    def __init__(self):
        super(ItemListAPI, self).__init__()

    def get(self, name):
        return db.find_one({"name": name})
