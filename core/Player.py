
class Player:
    def __init__(self, name, number, direction):
        self.__name = name
        self.__number = number
        self.__token = ""
        self.__direction = direction

        if number == 1:
            self.__token = "X"
            self.__direction = 1
        elif number == 2:
            self.__token = "O"
            self.__direction = -1
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

        if number == 1:
            self.__token = "X"
        elif number == 2:
            self.__token = "O"
        else:
            print('Debe ingresar o un 1 o un 2')#Lanzar excepcion IncorrectNumberPlayer

    @property
    def token(self):
        return self.__token
    
    @property
    def direction(self):
        return self.__direction