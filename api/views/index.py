#!/usr/bin/python3
"""
Create a folder views inside v1
create a variable app_views which is an instance of Blueprint 
(url prefix must be
"""
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views
from models import storage



@app_views.route('/status', strict_slashes=False)
def _status():
    """returns a JSON file with Status: OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    my_amenity = storage.count("Amenity")
    my_cities = storage.count("City")
    my_places = storage.count("Place")
    my_reviews = storage.count("Review")
    my_states = storage.count("State")
    my_users = storage.count("User")
    return jsonify(amenities=my_amenity,
                   cities=my_cities,
                   places=my_places,
                   reviews=my_reviews,
                   states=my_states,
                   users=my_users)

if __name__ == "__main__":
    pass