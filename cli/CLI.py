import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from core.Board import Board
# from core.Game import Game
from core.Player import Player
from core.Dice import Dice

while True:
    print('Bienvenido a Backgammon!!!!')
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

        board = Board()
       

        while True:

            board.get_board()
            
            print("1- Tirar dado")

            option = int(input("Ingrese la opcion: "))

            if option == 1:
                dice = Dice()
                moves = []
                
                dice.throw_dice()

                dice1 = dice.get_dice1()
                dice2 = dice.get_dice2()

                if dice1 == dice2:
                    moves.extend([dice1] * 4)
                else:
                    moves.append(dice1)
                    moves.append(dice2)


                print(f"Dado 1: {dice1} \n Dado 2: {dice2}")
                print(f"Movimineto validos: {len(moves)}")



    if(opc == 2):
        board = Board()
        board.get_board()


    if(opc == 10):
        print("Terminando ejecucion...")
        break