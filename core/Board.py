import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.Checker import Checker
from core.exceptions import InableToGetOut, InvalidPosition, InvalidMove
from core.Player import Player

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

    def get_bar(self, player: Player):
        number = player.number
        if number == 1:
            return self.__bar["X"]
        else:
            return self.__bar["O"]
    
    def get_out(self, player):
        if player == 1:
            return self.__out["X"]
        else:
            return self.__out["O"]

    def addChecker(self, pos, player:Player):
        
        playerNb = player.number

        if 0 <= pos <= 23:
            self.__points[pos].append(Checker(playerNb))
        else:
            raise InvalidPosition("La posicion no es valida")

    def deleteChecker(self, pos):

        if 0 <= pos <= 23:
            self.__points[pos].pop()

    #------------------------ Validaciones ------------------------------------------

    def is_valid_move(self, player: Player, fromPos, toPos, dice):
        direction = player.direction()
        token = player.token()
        
        #Esto validara que la posicion sea valida
        if fromPos < 0 or fromPos > 23 or toPos < 0 or toPos > 23:
            raise InvalidMove("Origen o destino no valido.")
        
        #Esto validara que en el punto de origen hayan elementos y que aparte esos elementos (en este caso se verifica con el primero) pertenezcan al jugador 
        if not self.__points[fromPos] or self.__points[fromPos][0] != token:
            raise InvalidMove("No tienes fichas en el punto de origen.")
        
        #Esto validara si la posicion de destino pertenece  a otro jugador y si tiene mas de una ficha
        if self.__points[toPos]:
            destinationToken = self.__points[toPos][0]

            if destinationToken != token and len(self.__points[toPos]) > 1:
                raise InvalidMove("El punto de destino pertenece a otro jugador.")
        
        #Esto validara que el origen mas el numero de dado, llegue al destino correcto. Se lo multiplica por la direccion ya que si esta es -1 ira para un lado y si es 1 ira para el otro
        if toPos != fromPos + direction * dice:
            raise InvalidMove("Destino invalido.")
        
    def possibles_positions(self, player: Player, fromPos, dices):
        direction = player.direction
        options = []

        for d in dices:
            destination = fromPos + direction * d

            if 0 <= destination <= 23:
                try:
                    self.is_valid_move(player, fromPos, destination, d)

                    if destination not in options:
                        options.append(destination)

                except InvalidMove:
                    continue
        
        return options

    #
    def are_possibles_moves(self, player: Player, dices):
        token = player.token

        for i in range(24):
            if self.__points[i] and self.__points[i][0] == token:
                if self.possibles_positions(player, i, dices):
                    return True
        return False

    def destination_from_bar(self, player: Player, dice):
        #Me indica el indice donde tendria que salir mi ficha. Si me toca un dado 5, entro a la posicion 4 que equivale al quinto punto, si la direccion es 1, en caso contrario entro desde el otro lado
        direction = player.direction

        if direction == 1:
            return dice - 1
        else:
            return 24 - dice

    def can_reenter(self, player: Player, dice):
        #Comprueba si se puede ingresar una ficha desde la barra. Si no puede devuelve None, si puede devuelve el indice
        destination = self.destination_from_bar()
        token = player.token

        if destination < 0 or destination > 23:
            return None

        if not self.__points[destination]:
            return destination

        if self.__points[destination][0] == token and len(self.__points[destination]) < 5:
            return destination
        
        if len(self.__points[destination]) == 1:
            return destination
        
        return None
            
    def all_on_internal_board(self, player: Player):
        #Verifica que todas las fichas del jugador esten en su tablero interno
        token = player.direction
        direction = player.direction

        if self.get_bar(player):
            return False
        
        #Jugador 1: tablero interno 18 - 23
        if direction == 1:
            for i in range(0, 18):

                if self.__points[i] and self.__points[i][0] == token:

                    return False
        else:
            for i in range(6, 24):
                
                if self.__points[i] and self.__points[i][0] == token:

                    return False
                
        return True

    def can_go_out(self, player: Player, fromPos, dice):
        token = player.token
        direction = player.direction
        
        #verifica que tenga todas las fichas en el tablero interno
        if not self.all_on_internal_board(player):
            return False
        
        #verifica que tenga fichas en el origen, y que aparte correspondan a un jugador
        if not self.__points[fromPos] or self.__points[fromPos][0] != token:
            return False
        
        #Aca verifico cual es la distancia necesaria para sacar un dado dependiendo de la direccion, despues esa distancia debe ser igual al dado sacado
        distance = 0

        if direction == 1:
            distance = 24 - fromPos
        else:
            distance = fromPos + 1

        if dice == distance:
            return True
        
        if dice > distance:
            
            if direction == 1:
                for i in range(0, fromPos):
                    if self.__points[i] and self.__points[i][0] == token:
                        return False
                    
            else:
                for i in range(fromPos + 1, 24):
                    if self.__points[i] and self.__points[i][0] == token:
                        return False
                    
            return True

        return False


#--------------- Metodos --------------------------

    def move(self, player: Player, fromPos, toPos, dice):
        self.is_valid_move(player, fromPos, toPos, dice)

        token = player.token
        
        if self.__points[toPos] and self.__points[toPos][0] != token and len(self.__points[toPos]) == 1:
            oponent = self.__points[toPos].pop()
            self.__bar[oponent].append(oponent)

        self.deleteChecker(fromPos)
        self.addChecker(toPos, player)

    def reenter_from_bar(self, player: Player, dice):

        destination = self.can_reenter
        token = player.token

        if destination == None:
            raise InvalidMove("No se puede reingresar con ese dado.")
        
        self.__bar[token].pop()

        #condiciones para saber si se puede capturar la ficha del oponente
        if self.__points[destination] and self.__points[destination][0] != token and len(self.__points[destination]) == 1:
            oponent = self.__points[destination].pop()

            self.__bar[oponent].append(oponent)

        self.__points[destination].append(token)

    def go_out(self, player: Player, fromPos, dice):
        if not self.can_go_out(player, fromPos, dice):
            raise InvalidMove("La ficha no puede ser sacada")
        
        token = self.__points[fromPos].pop()

        self.__out[token].append(token)


if __name__ == "__main__":
    board = Board()
    board.get_board()