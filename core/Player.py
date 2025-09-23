
class Player:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        self.__token = ""

        if number == 1:
            self.__token = "X"
        elif number == 2:
            self.__token = "O"
        else:
            print('Debe ingresar o un 1 o un 2')#Lanzar excepcion IncorrectNumberPlayer



    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def token(self):
        return self.__token