import os
import json
from App.app import DB
from App.models import RecipeModel 


def loadRecipes() -> None:    

    file : str = "App/static/json/recipe.json"
    collection = DB.db.recipe
    
    if os.path.exists(file):
        with open(file, "r") as data:
            json_datas = json.load(data)

            for json_data in json_datas:
                recipe : RecipeModel = RecipeModel(
                    json_data["id"],
                    json_data["title"],
                    json_data["ingredients"],
                    json_data["instructions"]
                )

                isValid : bool = collection.find_one(recipe.toObject()) 
                if isValid: break

                collection.insert_one(recipe.toObject())          
            
            data.close()

    return None