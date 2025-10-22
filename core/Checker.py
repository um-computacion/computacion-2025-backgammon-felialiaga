import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.exceptions import InvalidPlayerNumber

class Checker:

    def __init__(self, player):

        if player not in (1,2):
            raise InvalidPlayerNumber("El nunmero del jugador debe ser 1 o 2.")

        self.__player = player


    def get_player(self):
        return self.__player

        self.__in_out = True


    def __repr__(self):
        player = self.get_player()

        if player == 1:
            return 'X'
        else:
            return 'O'