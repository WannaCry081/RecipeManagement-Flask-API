
class UserModel:

    username : str = None
    email : str = None
    password : str = None
    bio : str = None


    def __init__(self, username : str, email : str, password : str, bio : str = ""):
        self.username = username
        self.email = email
        self.password = password 
        self.bio = bio


    def __repr__(self) -> str:
        return "<User %r>"%self.username
    

    def toObject(self) -> dict:
        return {
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "bio" : self.bio
        }
    
    
    @staticmethod
    def fromObject(data : dict) -> "UserModel":
        return UserModel(
            str(data["username"]),
            str(data["email"]),
            str(data["password"].decode("utf-8")),
            str(data["bio"])
        )
   