from flask import abort, jsonify
from flask.ext.restful import Resource, reqparse

from reststub.globals import db, encode_mongo_obj, auth


class ItemListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('text', type=str, location='json', required=True)
        super(ItemListAPI, self).__init__()

    def get(self):
        found = [encode_mongo_obj(v) for v in db['item'].find()]
        return found

    def post(self):
        args = self.reqparse.parse_args()
        try:
            new_item = {"name": args['name'], "text": args['text']}
            inserted_id = db['item'].insert_one(new_item).inserted_id
            return {'inserted': str(inserted_id)}, 201
        except Exception as e:
            return {'error': e}, 500
