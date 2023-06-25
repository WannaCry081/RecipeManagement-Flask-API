from flask import (
    Blueprint,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


RECIPE_API : Blueprint = Blueprint("RECIPE_API", __name__)


@RECIPE_API.route("/", methods=["GET"])
@jwt_required
def getRecipes():
    return jsonify({

    })


@RECIPE_API.route("/<int:recipe_id>/", methods=["GET"])
@jwt_required()
def getRecipeDetail(recipe_id : int):
    return jsonify({})


@RECIPE_API.route("/", methods=["POST"])
@jwt_required()
def addRecipe():
    return jsonify({})


@RECIPE_API.route("/<int:recipe_id>/", methods=["PUT"])
@jwt_required()
def updateRecipe(recipe_id : int):
    return jsonify({})


@RECIPE_API.route("/<int:recipe_id>/", methods=["DELETE"])
@jwt_required()
def deleteRecipe(recipe_id : int):
    return jsonify({})
