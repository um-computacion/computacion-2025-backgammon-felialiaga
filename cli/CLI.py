import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from core.Board import Board

while True:
    print('Juego Backgammon')
    print("1. Iniciar Partida")
    print("2. Mostrar Tablero(provisorio)")
    print("10. Salir")

    opc = int(input('Ingrese una opcion: '))

    if(opc == 2):
        board = Board()
        board.get_board()


    if(opc == 10):
        print("Terminando ejecucion...")
        break