class InvalidMOve(Exception):
    pass

class InvalidPosition(Exception):
    pass


class Board:
    def __init__(self):
        self.__container = [
            [ ["o","o","o","o","o"],[],[],[],["x","x","x"],[] ] , [ ["x","x","x","x","x"],[],[],[],[],["o","o"] ],
            [ ["x","x","x","x","x"],[],[],[],["o","o","o"],[] ] , [ ["o","o","o","o","o"],[],[],[],[],["x","x"] ]
        ]
        self.__out = []

        def get_board(self):
            #trae el tablero
            ...

        def play(self):
            #hacer un movimiento
            ...