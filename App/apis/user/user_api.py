from flask import (
    Blueprint,
    jsonify
)


USER_API : Blueprint = Blueprint("USER_API", __name__)


@USER_API.route("/", methods=["GET"])
def getProfile():
    return jsonify({})


@USER_API.route("/<int:user_id>/", methods=["POST"])
def updateProfile(user_id : int):
    return jsonify({})


@USER_API.route("/<int:user_id>/", methods=["DELETE"])
def deleteProfile(user_id : int):
    return jsonify({})