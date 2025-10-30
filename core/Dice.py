import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Dice:
    def __init__(self):
        self.__values = [0,0]

    def throw_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        self.__values = [dice1, dice2]
        return self.__values

    def get_dice1(self):
       
        return self.__dice1
    
    def get_dice2(self):
        
        return self.__dice2
    
    def doubles(self):
        #Esta funcion devolvera True si los 2 dados son iguales
        return self.__values[0] == self.__values[1]

    def set_dice1(self, number):
        self.__dice1 = int(number)

    def set_dice2(self, number):
        self.__dice2 = int(number)

    def duplicate(self):
        #Este metodo se usara para saber los movimientos que tenemos, si son iguales los duplica, sino devuelve los valores de los 2 dados
        if self.doubles():
            return[self.__values[0] * 4]
        else:
            return self.__values

    def __str__(self):
        return f"Valor dado 1: {self.__dice1}, Valor dado 2: {self.__dice2}, Valor Total: {self.__total}"