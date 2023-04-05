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
    """calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def invalid_route(error):
    """ invalide route module """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    """ getenv run """
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')),
            threaded=True, debug=True)


    