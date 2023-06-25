
class RecipeModel:
    
    id : int = None
    title : str = None
    ingredients : list[str] = None
    instruction : str = None


    def __init__(self, id : int, title : str, ingredients : list[str], instruction : str):
        self.id = id
        self.title = title
        self.ingredients = ingredients
        self.instruction = instruction


    def __repr__(self) -> str:
        return "<Recipe %r>"%self.title
    

    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "title" : self.title,
            "ingredients" : self.ingredients,
            "instruction" : self.instruction
        }