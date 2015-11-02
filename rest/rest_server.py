from flask import Flask, make_response, jsonify
from flask.ext.restful import Api
from flask.ext.cors import CORS

from rest_stub.resources import ItemAPI
from rest_stub.resources import ItemListAPI


def init_app():
    rest_stub = Flask(__name__)
    # Enable CORS for development
    CORS(rest_stub)

    # Wrap the app in the restful interface
    api = Api(rest_stub)
    api.add_resource(ItemListAPI, '/api/tests', endpoint='items')
    api.add_resource(ItemAPI, '/api/test/<string:id>', endpoint='item')

    return rest_stub


def run_server():
    rest_stub_app = init_app()
    rest_stub_app.run(debug=True)

    @rest_stub_app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    run_server()
