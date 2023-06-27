from App.app import DB
from App.models import RecipeModel
from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


RECIPE_API : Blueprint = Blueprint("RECIPE_API", __name__)


@RECIPE_API.route("/", methods=["GET"])
@jwt_required()
def getRecipes():
    collection_user = DB.db.auth 
    collection_recipe = DB.db.recipe

    access_token = get_jwt_identity()
    data = collection_user.find_one({"email" : access_token})
    if data:
        recipe_list = []

        for recipes in collection_recipe.find():
            recipe : RecipeModel = RecipeModel.fromObject(recipes)
            recipe_list.append(recipe.toObject())
        
        return jsonify({
            "recipes" : recipe_list,
            "status" : 200
        }), 200
    
    else:
        return jsonify({
            "message" : "User does not Exists",
            "status" : 404
        }), 404


@RECIPE_API.route("/<recipe_title>/", methods=["GET"])
@jwt_required()
def getRecipeDetail(recipe_title : str):
    try:
        collection_auth = DB.db.auth
        collection_recipe = DB.db.recipe

        access_token = get_jwt_identity()
        data_auth = collection_auth.find_one({"email" : access_token })

        if data_auth:
            data_recipe = collection_recipe.find_one({"title" : recipe_title})
            if data_recipe:
                recipe : RecipeModel = RecipeModel.fromObject(data_recipe)
                return jsonify({
                    "recipe" : recipe.toObject(),
                    "status" : 200
                }), 200

            else:
                return jsonify({
                    "message" : "Recipe does not Exists",
                    "status" : 404
                }), 404
            
        else:
            return jsonify({
                "message" : "User does not Exists", 
                "status" : 404
            }), 404

    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500 
    

@RECIPE_API.route("/", methods=["POST"])
@jwt_required()
def addRecipe():    
    try:
        collection_auth = DB.db.auth
        collection_recipe = DB.db.recipe

        access_token = get_jwt_identity()
        data_auth = collection_auth.find_one({"email" : access_token})
        if data_auth:
            title = request.get_json()["title"]
            ingredients = request.get_json()["ingredients"]
            instruction = request.get_json()["instruction"]

            data_recipe = collection_recipe.find_one({"title" : title})
            if data_recipe:
                return jsonify({
                    "message" : "Recipe already Exists",
                    "status" : 404
                }), 404

            if not (ingredients or instruction):
                return jsonify({
                    "message" : "Invalid Recipe",
                    "status" : 400
                }), 400
            
            recipe : RecipeModel = RecipeModel(title, list(ingredients), instruction)
            collection_recipe.insert_one(recipe.toObject())
            return jsonify({
                "message" : "Successfully Added Recipe",
                "status" : 200
            }), 200
        
        else:
            return jsonify({
                "message" : "User does not Exists",
                "status" : 404,
            }), 404
            
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500


@RECIPE_API.route("/<recipe_title>/", methods=["PUT"])
# @jwt_required()
def updateRecipe(recipe_title : str):
    try:
        collection_auth = DB.db.auth
        collection_recipe = DB.db.recipe

        # access_token = get_jwt_identity()
        access_token = "liraedata59@gmail.com"
        data_auth = collection_auth.find_one({"email" : access_token})
        if data_auth:
            data_recipe = collection_recipe.find_one({"title" : recipe_title})
            if not data_recipe:
                return jsonify({
                    "message" : "Recipe does not Exists",
                    "status" : 404
                }), 404
            
            ingredients = request.get_json()["ingredients"]
            instruction = request.get_json()["instruction"]
            recipe : RecipeModel = RecipeModel.fromObject(data_recipe)
            
            if ingredients:
                recipe.ingredients = list(ingredients)

            if instruction:
                recipe.instruction = instruction

            updated_data = collection_recipe.update_one(
                {"title" : recipe_title},
                {"$set" : {
                    "ingredients" : recipe.ingredients,
                    "instruction" : recipe.instruction
                }}
            )
            if updated_data.modified_count == 1:
                return jsonify({
                    "message" : "Successfully Updated Recipe",
                    "status" : 200
                }), 200
            else:
                return jsonify({
                    "message" : "Document does not Exists",
                    "status" : 404
                }), 404
                
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500


@RECIPE_API.route("/<recipe_title>/", methods=["DELETE"])
@jwt_required()
def deleteRecipe(recipe_title : str):
    try:
        collection_auth = DB.db.auth 
        collection_recipe = DB.db.recipe

        access_token = get_jwt_identity()
        data_auth = collection_auth.find_one({"email" : access_token})
        if data_auth:
            data_recipe = collection_recipe.find_one({"title" : recipe_title}) 
            if not data_recipe:
                return jsonify({
                    "message" : "Recipe does not Exists",
                    "status" : 404
                }), 404
            
            deleted_data = collection_recipe.delete_one({"title" :  recipe_title})
            if deleted_data.deleted_count == 1:
                return jsonify({
                    "message" : "Successfully Deleted Recipe",
                    "status" : 200
                }), 200
            else:
                return jsonify({
                    "message" : "Document does not Exists",
                    "status" : 404 
                }), 404

        return jsonify({
            "message" : "User does not Exists",
            "status" : 404,
        }), 404
        
    except Exception as e:
        return jsonify({
            "error" : e,
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
