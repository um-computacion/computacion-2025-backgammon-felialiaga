import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from core.Board import Board
# from core.Game import Game
from core.Player import Player

while True:
    print('Bienvenido a Backgammon')
    print("1. Iniciar Partida")
    print("2. Mostrar Tablero(provisorio)")
    print("10. Salir")

    opc = int(input('Ingrese una opcion: '))

    if(opc == 1):
        nombre1 = input("Ingrese el nombre del primer jugador: ")
        nombre2 = input("Ingrese el nombre del segundo jugador: ")

        jugador1 = Player(nombre1, 1)
        jugador2 = Player(nombre2, 2)

        print(f" {jugador1.name} : X ")
        print(f" {jugador2.name} : O ")

    if(opc == 2):
        board = Board()
        board.get_board()


    if(opc == 10):
        print("Terminando ejecucion...")
        break