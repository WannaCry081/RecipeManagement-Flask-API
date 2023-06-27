
class RecipeModel:
    
    title : str = None
    ingredients : list[str] = None
    instruction : str = None


    def __init__(self, title : str, ingredients : list[str], instruction : str):
        self.title = title
        self.ingredients = ingredients
        self.instruction = instruction


    def __repr__(self) -> str:
        return "<Recipe %r>"%self.title
    

    def toObject(self) -> dict:
        return {
            "title" : self.title,
            "ingredients" : self.ingredients,
            "instruction" : self.instruction
        }
    
    @staticmethod
    def fromObject(data : dict) -> "RecipeModel":  
        return RecipeModel(
            title = str(data["title"]),
            ingredients = list(data["ingredients"]),
            instruction = str(data["instruction"])
        )
    
