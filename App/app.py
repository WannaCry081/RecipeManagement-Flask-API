from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from App.config import Config


DB : PyMongo = PyMongo()
JWT : JWTManager = JWTManager() 
BCRPYT : Bcrypt = Bcrypt()


def createRecipeManagementApp(configClass : Config = Config) -> Flask:

    app : Flask = Flask(__name__) 
    app.config.from_object(configClass)
    DB.init_app(app)
    JWT.init_app(app)
    BCRPYT.init_app(app)
    CORS(app)

    
    from App.apis.auth import AUTH_API
    from App.apis.user import USER_API
    from App.apis.recipe import RECIPE_API


    app.register_blueprint(AUTH_API, url_prefix="/api/auth")
    app.register_blueprint(USER_API, url_prefix="/api/user")
    app.register_blueprint(RECIPE_API, url_prefix="/api/recipes")


    return app


