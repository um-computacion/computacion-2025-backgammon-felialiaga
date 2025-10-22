import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.Board import Board
# from core.Dice import Dice
# from core.Player import Player

class Game:
    def __init__(self):
        self.turn = ""
        self.__board = Board()
        # self.__dice = Dice()
        # self.__players = list[Player] = []

    def start_game(self):
        #Primero se hace el setup de los elementos
        ...


    def who_start(self):
        ...
        #Logica para saber quien empieza jugando

    def change_turn(self):
        ...
        #Logica para el cambio de turno

    def get_current_player(self):
        ...

    def is_win(self): 
        #Logica para verificar si hay un ganador
        player1 = len(self.__board.get_out()[1])
        player2 = len(self.__board.get_out()[2])

        #Cada una de las variables va a devolver la cantidad de fichas que tenemos afuera
        #Los prints van a ser reemplazados por atributos
        if player1 == 15:
            print("Jugador 1 ha ganado")
        if player2 == 15:
            print("Jugador 2 ha ganado")
        else:
            print("Ninguno ha ganado, la partida sigue")


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