from Player import Player

class Checker:
    def __init__(self, color, player: Player, position):
        self.__color = color
        self.__player = player
        self.__position = position
        self.__bar = False
        self.__out = False

    def get_color(self):
        return self.__color
    
    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def validate_position(self):
        pass

    def move(self, position):
        self.set_position(position)

    def move_to_bar(self):
        self.__position = None
        self.__bar = True

    def move_out(self):
        self.__position = None
        self.__out = True


    def reset(self):
        pass