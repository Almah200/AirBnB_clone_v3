#!/usr/bin/python3
""" imported modules """

from flask import Flask, Blueprint, abort
from flask import make_response
from flask import render_template, jsonify
from app.v1.views import app_views
from flask_cors import CORS
import os
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_session(exception):
    """calls storage.close() for storing in each session"""
    storage.close()


@app.errorhandler(404)
def invalid_route(error):
    """ invalide route module for handling errors  """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)

    