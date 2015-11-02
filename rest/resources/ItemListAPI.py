from flask import abort, jsonify

from rest_stub.database import db


class ItemListAPI(Resource):
    def __init__(self):
        super(ItemListAPI, self).__init__()

    def get(self, name):
        return
