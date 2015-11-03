from flask import abort, jsonify
from flask.ext.restful import Resource, reqparse

from reststub.database import db


class ItemAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('text', type=str, location='json', required=True)
        super(ItemAPI, self).__init__()

    def get(self):
        found = [v for v in db.find()]
        return found

    def post(self):
        args = self.reqparse.parse_args()
        try:
            new_item = {"name": args['name'], "text": args['text']}
            inserted_id = db.insert_one(new_item).inserted_id
            return {'inserted': inserted_id}, 201
        except Exception as e:
            return {'error': e}, 500
