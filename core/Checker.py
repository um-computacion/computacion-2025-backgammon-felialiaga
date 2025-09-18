
class Checker:
    #Jugador 1: X o Negro
    #Jugador 2: O o Blanco
    #player puede tomar valores como 1 o 2
    def __init__(self, player):
        self.__player = player

    def get_player(self):
        return self.__player
    

    def __repr__(self):
        player = self.get_player()

        if player == 1:
            return 'X'
        else:
            return 'O'