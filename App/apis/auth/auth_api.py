from App.app import DB
from flask import (
    Blueprint,
    jsonify,
    json
)


AUTH_API : Blueprint = Blueprint("AUTH_API", __name__)

@AUTH_API.route("/")
def sample():

    collection = DB.db.recipe
    data = collection.find()

    data_list = []
    for i in data:
        data_list.append({
            "id" : str(i["_id"]),
            "name" : str(i["name"]),
            "age" : str(i["age"]),
        })

    

    return jsonify({
        "data" : data_list
    }), 200