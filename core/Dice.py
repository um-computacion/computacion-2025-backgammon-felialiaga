import random

class Dice:

    def __init__(self):
        self.__valores__ = []
        self.__usados__ = []

    def roll(self):

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == d2:
            self.__valores__ = [d1, d1, d1, d1]
        else:
            self.__valores__ = [d1, d2]

        self.__usados__ = []
        return self.__valores__

    def get_values(self):
        return list(self.__valores__)

    def tirada_doble(self):
        return len(self.__valores__) == 4

    def individual_values(self):
        if self.tirada_doble():
            return [self.__valores__[0], self.__valores__[2]]
        return list(self.__valores__)

    def usar_valor(self, value: int):
        if value in self.__valores__:
            self.__valores__.remove(value)
            self.__usados__.append(value)
            return True
        return False

    def valores_usados(self):
        return list(self.__usados__)