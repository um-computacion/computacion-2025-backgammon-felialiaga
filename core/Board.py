import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.Checker import Checker
from core.exceptions import InableToGetOut, InvalidPosition

class Board:
    #Jugador 1: X
    #Jugador 2: O
    def __init__(self):
        self.__points = [[] for i in range(24)]
        self.__bar = { 'X': [], 'O': [] }
        self.__out = { 'X': [], 'O': [] }

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

        #Mostrar barra
        print('\n Barra \n')
        j1b = len(self.__bar["X"])
        j2b = len(self.__bar["O"])

        print(f"Jugador 1: {j1b} \n {"  X  " * j1b}")
        print(f"Jugador 2: {j2b} \n {"  O  " * j2b}")


        #Mostrar Home
        print('\n Home')
        j1o = len(self.__out["X"])
        j2o = len(self.__out["O"])

        print(f"Jugador 1: {j1o} \n {"  X  " * j1o}")
        print(f"Jugador 2: {j2o} \n {"  O  " * j2o}")

    def get_points(self):
        return self.__points

    def get_point(self, point):
        
        if 0 <= point <= 23:
            return self.__points[point]
        else:
            raise InvalidPosition("La posicion no es valida")

    def get_bar(self, player):
        if player == 1:
            return self.__bar["X"]
        else:
            return self.__bar["O"]
    
    def get_out(self, player):
        if player == 1:
            return self.__out["X"]
        else:
            return self.__out["O"]

    def addChecker(self, pos, player):
        
        if 0 <= pos <= 23:
            self.__points[pos].append(Checker(player))
        else:
            raise InvalidPosition("La posicion no es valida")

    def deleteChecker(self, pos):

        if 0 <= pos <= 23:
            self.__points[pos].pop()



    def send_to_bar(self, pos):
        #Esta funcion debe enviar a la barra al elemento que fue comido y eliminar del punto actual al elemento

        #validar que la posicion sea valida, validar que el jugador tenga una ficha en esa posicion
        ... 

    def send_from_bar_to_board(self, player):
        ...

    def send_out(self, player: int, point):
        #player = 1 o 2

        able = self.able_to_get_out(player, point)

        if able:

            #pop lo que va a hacer es eliminar el elemento de la ultima posicion 
            self.__points[point].pop()

            list(self.__out.keys())[player - 1].append(Checker(player))
    
    def make_move(self, fromPos, toPos, player):

        if list(self.__bar.keys())[player - 1]:
            self.send_from_bar_to_board(player)

        validFrom = self.valid_position(fromPos, player)
        validTo = self.valid_position(toPos, player)

        if validFrom and validTo:
            self.__points[fromPos].pop()
            self.__points[toPos].pop(0)
            self.__points[toPos].append(Checker(player))



    #-------------------------Validaciones-------------------------

    def valid_position(self, point, player: str):
        #validar si la posicion destino es valida
        #Antes de validar la cantidad de fichas tengo que poder validar si son "X" o "O"

        cant = len(self.__points[point])
        validPlayer = ""

        if cant == 1:
            validPlayer = self.valid_player(point, player)

            if validPlayer == False:
                self.send_to_bar(point)
                return True

        if cant > 1:
            validPlayer = self.valid_player(point, player)

        if cant == 5:
            return False

        if cant == 0 or validPlayer:
            return True
        else:
            return False

    def valid_player(self, pos, player: str):
        #Funcion para validar si un punto pertenece a un jugador o no

        if str(self.__points[pos][0]) == player:
            return True
        else:
            return False

    def valid_move(self, fromPos, toPos, player):
        ...
        
    def make_move(self, fromPos, toPos, player):

        if list(self.__bar.keys())[player - 1]:
            self.send_from_bar_to_board(player)

        validFrom = self.valid_position(fromPos, player)
        validTo = self.valid_position(toPos, player)

        if validFrom and validTo:
            self.__points[fromPos].pop()
            self.__points[toPos].pop(0)
            self.__points[toPos].append(Checker(player))


    def able_to_get_out(self, player, point):
        cuadrante1 = self.__points[0:6]
        cuadrante4 = self.__points[18:24]

        totalX = 0
        totalO = 0

        if player == 1:

            # que el jugador tenga todas sus fichas en el ultimo cuadrante
            for p in cuadrante4:
                totalX += p.count("X")

            if totalX == 15:
                valid1 = True
            else:
                raise InableToGetOut("Debes tener todas tus fichas en el tablero interno.")

            # que la posicion en la que quiero sacar una ficha este limpio, no tenga fichas detras
            valid2 = all('X' not in p for p in cuadrante4[:point] )
            if valid2 == False:
                raise InableToGetOut("No puedes tener fichas en las posiciones anteriores. Debes sacar primero las fichas que estan por detras")
            
            if valid1 and valid2:
                return True
            else: 
                return False
            

        if player == 2:
            # que el jugador tenga todas sus fichas en el ultimo cuadrante

            for p in cuadrante1:
                totalO += p.count("O")

            if totalO == 15:
                valid1 = True
            else:
                raise InableToGetOut("Debes tener todas tus fichas en el tablero interno.")


            # que la posicion en la que quiero sacar una ficha este limpio, no tenga fichas detras
            # valid2 = all(len(p) == 0 for p in cuadrante4[:point])
            valid2 = all('O' not in p for p in cuadrante1[:point] )

            if valid2 == False:
                raise InableToGetOut("No puedes tener fichas en las posiciones anteriores. Debes sacar primero las fichas que estan por detras")

            if valid1 and valid2:
                return True
            else: 
                return False





if __name__ == "__main__":
    board = Board()
    print(board.valid_position(7, "O"))