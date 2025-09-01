from Board import Board

class Game:
    def __init__(self):
        self.turn = ""
        self.board = Board()


    def who_start(self):
        ...
        #Logica para saber quien empieza jugando

    def move_file(self):
        ...
        #Logica para hacer un movimiento

    def change_turn(self):
        ...
        #Logica para el cambio de turno

    def is_win(self):
        ... 
        #Logica para verificar si hay un ganador