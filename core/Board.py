import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.Checker import Checker

class Board:
    #Jugador 1: X
    #Jugador 2: O
    def __init__(self):
        self.__points = [[] for i in range(24)]
        self.__bar = { 1: [], 2: [] }
        self.__out = { 1: [], 2: [] }

        self.setup()

    def setup(self):

        self.__points[0] = [Checker(1) for i in range(2)]
        self.__points[11] = [Checker(1) for i in range(5)]
        self.__points[16] = [Checker(1) for i in range(3)]
        self.__points[18] = [Checker(1) for i in range(5)]

        self.__points[23] = [Checker(2) for i in range(2)]
        self.__points[12] = [Checker(2) for i in range(5)]
        self.__points[7] = [Checker(2) for i in range(3)]
        self.__points[5] = [Checker(2) for i in range(5)]

        

    def get_board(self):
        #trae el tablero
        print("----- Tablero de juego -----")

        top = self.__points[12:24]
        bottom = self.__points[0:12][::-1]
        max_len = 5

        for i in top:
            # Agregar barras en los espacios faltantes

            n = len(i)
            
            if n < max_len:
                i.extend(["|"] * (max_len - n))


        for row in range(max_len):
            #mostrar tablero por filas
            for i in top:
                print(i[row], end=" ")
            print(" ")


        print("-------------------------------")
        
        for i in bottom:
            n = len(i)

            if n < max_len:
                i.extend(["|"] * (max_len - n))

        for row in range(max_len):
            for i in bottom:
                print(i[row], end=" ")
            print(" ")


if __name__ == "__main__":
    board = Board()
    board.get_board()