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

        for i in ["12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
            print(i, end="  ")
        print(" ")

        for row in range(max_len):
            #mostrar tablero por filas
            for i in top:
                print(i[row], end="   ")
            print(" ")

        print("- " * 23)

        for i in bottom:
            #Aca lo primero que hago es calcular la cantidad de "|" que necesito agregar
            n = max_len - len(i)

            if n > 0:
                i[:0] = ['|'] * n

        for row in range(max_len):
            for i in bottom:
                print(i[row], end="   ")
            print(" ")

        for i in ["11", "10", "09", "08", "07", "06", "05", "04", "03", "02", "01", "00"]:
            print(i, end="  ")

    def get_bar(self):
        return self.__bar
    
    def get_out(self):
        return self.__out


if __name__ == "__main__":
    board = Board()
    board.get_board()