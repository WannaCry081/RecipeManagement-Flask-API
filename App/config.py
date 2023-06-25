from App.utils import secretKeyGenerator
from datetime import timedelta



class Config:
    
    SECRET_KEY : str = secretKeyGenerator(15)
    JWT_SECRET_KEY : str = secretKeyGenerator(15)

    JWT_EXPIRATION_DELTA : timedelta = timedelta(days=1)

    MONGO_URI : str = "mongodb://localhost:27017/recipe-management"
    
    