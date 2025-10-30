import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import random

from core.Board import Board
from core.Dice import Dice
from core.Player import Player
from exceptions import InvalidMove, InvalidDice, InvalidPosition

class Game:
    def __init__(self):
        self.__turn = 1
        self.__board = Board()
        self.__dice = Dice()
        self.__players: list[Player] = []
        self.__remaining_moves = []

    #------------- Validaciones ----------------------

    def are_possibles_moves(self):
        """
        Verifica si el jugador tiene al menos un movimiento válido con los dados disponibles.

        Retorna:
            True  -> si existe al menos un movimiento posible
            False -> si no hay ningún movimiento válido
        """
        if self.tiene_fichas_en_barra():
            for d in self.__remaining_moves:
                if self.__board.can_reenter(self.get_current_player(), d) is not None:
                    return True
            return False
        return self.__board.are_possibles_moves(self.get_current_player(), self.__remaining_moves)

    def has_on_bar(self):
        token = self.get_current_player().token
        
        return self.__board.get_bar[token]

    def entrance_from_bar(self):
        # devuelve las posibles entradas desde la barra
        entrances = []

        for d in self.__remaining_moves:
            point = self.__board.can_reenter(self.get_current_player(), d)

            if point is not None:
                entrances.append((d, point))

        return entrances

    def all_in_home(self):
        return self.__board.all_on_internal_board(self.get_current_player())

    def validate_origin(self, fromPos):
        
        points = self.__board.possibles_positions(self.get_current_player(), fromPos, self.__remaining_moves)

        if not points:
            raise InvalidPosition("El punto de origen actual no tiene moviminetos posibles.")
        
        return points

    def is_win(self): 
        #Logica para verificar si hay un ganador
        player1 = self.__players[0]
        player2 = self.__players[1]

        #Cada una de las variables va a devolver la cantidad de fichas que tenemos afuera
        if len(self.__board.get_out(player1)) == 15:
            return player1
        if len(self.__board.get_out(player2)) == 15 :
            return player2
        else:
            print("Ninguno ha ganado, la partida sigue")

#---------------- Metodos --------------------------

    def start_game(self):
        #Primero se hace el setup de los elementos
        ...

    def who_start(self):
        while True:
            player1 = random.randint(1, 6)
            player2 = random.randint(1, 6)

            if player1 > player2:
                self.__turn = 1
                return self.__players[0]
            elif player2 > player1:
                self.__turn = 2
                return self.__players[1]

    def throw_dices(self):
        self.__dice.throw_dice()

        self.__remaining_moves = self.__dice.duplicate()
        
        return self.__remaining_moves

    def change_turn(self):
        if self.__turn == 1:
            self.__turn = 2
        elif self.__turn == 2:
            self.__turn = 1

    def get_current_player(self):
        if self.__turn == 1:
            return self.__players[0]
        elif self.__turn == 2:
            return self.__players[1]

    def reenter_from_bar(self, dice):
        if dice not in self.__remaining_moves:
            raise InvalidDice("El dado no esta disponible.")
        
        self.__board.reenter_from_bar(self.get_current_player(), dice)

        self.__remaining_moves.remove(dice)

    def go_out(self, fromPos, dice):
        if dice not in self.__remaining_moves:
            raise InvalidDice("El dado no esta disponible.")
        
        self.__board.go_out(self.get_current_player(), fromPos, dice)
        
        self.__remaining_moves.remove(dice)



if __name__ == "__main__":
    game = Game()
    game.is_win()









#Reglas del Juego
#- Objetivo: Extraer todas las fichas del tablero lo mas rapido posible
#- Cada jugador tiene 15 fichas, y uno se mueve en sentido horario y el otro en sentido antihorario
#- Primero se deben llevar todas las fichas al tablero interno (Ultimo cuadrante) y una vez ahi, sacar todas las fichas
#- Tablero: Se divide en 4 cuadrantes, con 6 triangulos (puntos) en cada uno. Posee una barra, que es donde van las fichas cuando son golpeadas  
#- Inicialmente tira un dado cada participante, el de mayor numero empezara, usando el dado que tiro y el del oponente
#   - Si los 2 dados son iguales, el lanzamiento no es valido
#   - Los dados, al momento de hacer el movimiento, deben usarse por separado
#   - Cuando en un punto tenemos 2 o mas fichas, el punto queda bloqueado, por lo que el oponente no puede mover una ficha a ese punto
#   - Cuando tenemos una sola ficha en un punto, el oponente puede poner su ficha en ese punto y golpear a la nuestra 
#   - Si los 2 dados son iguales, se multiplican la cantidad de veces 
#- Golpes y Reentrada:
#   - Cuando se vuelve a entrar, se debe entrar en las posiciones iniciales. Si tengo un 5, debo entrar en el punto numero 5. 
#   - Al entrar, debo hacerla en un punto vacio
#   - No nos podemos mover hasta que no entren todas las fichas
#   - Si el oponente tiene todo su tablero interno ocupado y nosotros tenemos una ficha en la barra, perdemos el turno hasta que podamos hacer un movimiento valido
#- Extraccion:
#   - Una vez tengamos todas las fichas en el tablero interno, tiramos los dados y vamos sacando las fichas haciendo los movimientos adecuados
#   - Si me toca un '6' y yo tengo una ficha en la posicion 5, lo puedo sacar. Pero si tengo una ficha en la posicion 5 y 3, y me toca un '4', la ficha de la posicion 3 no la puedo sacar ya que atras no esta limpio, sigo teniendo fichas en la posicion 5

#Las X van a mover hacia puntos mayores, y los O hacia puntos menores 