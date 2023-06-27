from App.app import DB, BCRPYT
from App.models import UserModel
from App.utils import isValidEmail
from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    set_access_cookies,
    set_refresh_cookies,
    create_access_token,
    create_refresh_token,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity
)


AUTH_API : Blueprint = Blueprint("AUTH_API", __name__)


@AUTH_API.route("/signin/", methods=["POST"])
def signInUser():
    try:
        collection = DB.db.auth

        email = request.form["email"]
        password = request.form["password"]

        data = collection.find_one({"email" : email})
        user : UserModel = UserModel.fromObject(data)


        if data:
            if BCRPYT.check_password_hash(user.password, password):
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                
                response = jsonify({
                    "auth" : True,
                    "access_token" : access_token,
                    "message" : "Authorized Access",
                    "status" : 200
                })

                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)

                return response, 200
            
            return jsonify({
                "auth":False, 
                "message":"Incorrect Password",
                "status":401
            }), 401
            
        return jsonify({
            "auth" : False,
            "message" : "User does not Exists",
            "status" : 404
        }), 404
    
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500


@AUTH_API.route("/signup/", methods=["POST"])
def signUpUser():
    try:
        collection = DB.db.auth

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if collection.find_one({"username" : username, "email" : email}):
            return jsonify({
                "auth" : False,
                "message" : "User already Exists",
                "status" : 400
            }), 400
        
        if len(username) < 4:
            return jsonify({
                "auth" : False,
                "message" : "Username must at least be 4 characters long",
                "status" : 400
            }), 400
        
        if not isValidEmail(email):
            return jsonify({
                "auth" : False,
                "message" : "Invalid Email Address",
                "status" : 400
            }), 400
        
        if len(password) < 6:
            return jsonify({
                "auth" : False,
                "message" : "Password must at least be 6 characters long",
                "status" : 400
            }), 400

        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        response = jsonify({
            "auth": True,
            "access_token": access_token,
            "message": "Access Authorized",
            "status": 200
        })

        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        user : UserModel = UserModel(
            username = username, 
            email = email,
            password = BCRPYT.generate_password_hash(password)
        )
        collection.insert_one(user.toObject())
        return response, 200
        
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    

@AUTH_API.route("/signout/", methods=["POST"])
def signOutUser():
    response = jsonify({
        "message" : "Successfully Logout",
        "status" : 200
    })  
    unset_jwt_cookies(response)
    return response, 200


@AUTH_API.route("/refresh/", methods=["POST"])
@jwt_required(refresh=True)
def refreshToken():
    try:
        collection = DB.db.auth
        access_token = get_jwt_identity()
        data = collection.find_one({"email" : access_token})

        if data:
            new_token = create_access_token(identity=access_token)
            response = jsonify({
                "auth": True,
                "access_token": new_token,
                "message": "Access Authorized",
                "status": 200
            })
            set_access_cookies(response, new_token)
            return response, 200

        return jsonify({
            "auth" : False,
            "message" : "User does not Exists",
            "status" : 404
        }), 404
    
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    