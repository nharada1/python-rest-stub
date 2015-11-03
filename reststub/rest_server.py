from flask import Flask, make_response, jsonify
from flask.ext.restful import Api
from flask.ext.cors import CORS

from reststub.resources import ItemListAPI
from reststub.resources import ItemAPI
from reststub.globals import auth


# Main app
rest_stub_app = Flask(__name__)
rest_stub_app.debug = True
# Restful extension
api = Api(rest_stub_app)
api.add_resource(ItemListAPI, '/api/items', endpoint='items')
api.add_resource(ItemAPI, '/api/item/<string:name>', endpoint='item')
# Enable CORS for development
CORS(rest_stub_app)


@rest_stub_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.get_password
def get_password(username):
    if username == "tester":
        return "auth"
    return None


@auth.error_handler
def unauthorized():
    # Return a 403 instead of the dialog
    return make_response(jsonify({'message': 'Access unauthorized'}), 403)


def run_server():
    rest_stub_app.run()


if __name__ == "__main__":
    run_server()
