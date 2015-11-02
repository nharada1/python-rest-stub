from flask import abort, jsonify
from flask.ext.restful import Resource, reqparse

from rest_stub.database import db


class ItemAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json', required=True)
        self.reqparse.add_argument('text', type=str, location='json', required=True)
        super(ItemAPI, self).__init__()

    def get(self):
        return

    def post(self):
        args = self.reqparse.parse_args()
        try:
            user = args['username']
            hashed_pass = args['password']
            offer = db.new_user(user, hashed_pass)
            return offer
        except Exception as e:
            print(e)
            return {'error': e}
