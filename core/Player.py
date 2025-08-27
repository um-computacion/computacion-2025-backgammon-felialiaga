
class Player:
    def __init__(self, token, name):
        self.__name = name
        self.__token = token

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def token(self):
        return self.__token
    
    @token.setter
    def token(self, token):
        self.__token = token