

class Player:


    def __init__(self, numero: int, ficha: str):

        self.__numero__ = numero  # Número del jugador (1 o 2)
        self.__ficha__ = ficha    # Símbolo de la ficha del jugador

    def get_numero(self) -> int:
        return self.__numero__

    def get_ficha(self) -> str:
        return self.__ficha__