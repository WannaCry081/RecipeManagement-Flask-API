from App.app import DB
from App.models import UserModel
from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    unset_jwt_cookies
)

USER_API : Blueprint = Blueprint("USER_API", __name__)


@USER_API.route("/", methods=["GET"])
@jwt_required()
def getProfile():
    try:
        collection = DB.db.auth
        access_token = get_jwt_identity()
        data = collection.find_one({"email" : access_token})

        if data:
            user : UserModel = UserModel.fromObject(data)
            return jsonify({
                "user" : user.toObject(),
                "status" : 200
            }), 200

    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server error",
            "status" : 500
        }), 500
    
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/", methods=["PUT"])
@jwt_required()
def updateProfile():
    try:
        collection = DB.db.auth
        access_token = get_jwt_identity()
        data = collection.find_one({"email" : access_token})

        if data:
            user : UserModel = UserModel.fromObject(data)
            username = request.get_json()["username"]
            bio = request.get_json()["bio"]

            if username:
                if len(username) < 4:
                    return jsonify({
                        "message" : "Username must at least be 4 characters long",
                        "status" : 400
                    }), 400
                
                user.username = username

            if bio:
                user.bio = bio

            updated_data = collection.update_one(
                {"email" : access_token },
                {"$set" : {
                    "username" : user.username,
                    "bio" : user.bio
                }}
            )
            if updated_data.modified_count == 1:
                return jsonify({
                    "message" : "Successfully Updated",
                    "status" : 200
                }), 200
    
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500

    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/", methods=["DELETE"])
@jwt_required()
def deleteProfile():
    try:   
        collection = DB.db.auth 
        access_token = get_jwt_identity()
        data = collection.find_one({"email" : access_token})

        if data:
            deleted_data = collection.delete_one({"email" : access_token})
            if deleted_data.deleted_count == 1:
                response = jsonify({
                    "message" : "Successfully Deleted User",
                    "status" : 200
                })
                unset_jwt_cookies(response)
                return response, 200
        
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500

    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404