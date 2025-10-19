import random

class Dice:
    def __init__(self):
        self.__dice1 = 0
        self.__dice2 = 0
        self.__total = 0

    def throw_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        if(dice1 == dice2):
            total = dice1 * 4
        
        total = dice1 + dice2

        self.__dice1 = dice1
        self.__dice2 = dice2
        self.__total = total

    def get_dice1(self):
       
        return self.__dice1
    
    def get_dice2(self):
        
        return self.__dice2
    
    def get_total(self):

        return self.__total

    def set_dice1(self, number):
        self.__dice1 = int(number)

    def set_dice2(self, number):
        self.__dice2 = int(number)

    def set_total(self, dice1, dice2):

        if(dice1 == dice2):
            total = dice1 * 4
        else:
            total = dice1 + dice2

        self.__total = total


    def __str__(self):
        return f"Valor dado 1: {self.__dice1}, Valor dado 2: {self.__dice2}, Valor Total: {self.__total}"