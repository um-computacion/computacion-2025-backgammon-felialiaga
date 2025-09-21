class InvalidMOve(Exception):
    pass

class InvalidPosition(Exception):
    pass

from Checker import Checker

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

        top = self.__points[12:24] #24 ya que el ultimo no se incluye 

        print(" " + " ".join(f"{i + 13:>2}" for i in range(12)))

        top = self.__points[12:24] #24 ya que el ultimo no se incluye 

        for i in range(5):
            line = []
            for p in top:
                if len(p) > i:
                    line.append(str(p[i]))
                else:
                    line.append(".")
            print("   " + " ".join(line))

        print("----------------------------------------------------")

        bottom = self.__points[0:12]

        for i in range(0, 5):
            line = []
            for p in bottom:
                if len(p) > i:
                    line.append(str(p[i]))
                else:
                    line.append(".")
            print("   " + " ".join(line))

        print(" " + " ".join(f"{i + 1:>2}" for i in range(12)))



if __name__ == "__main__":
    board = Board()
    board.get_board()