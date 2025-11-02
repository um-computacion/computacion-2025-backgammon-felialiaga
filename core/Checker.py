
class Checker:


    def __init__(self, jugador: int):


        if jugador not in (1, 2):
            raise ValueError("El jugador debe ser 1 o 2")
        
        self.__jugador__ = jugador    
        self.__en_barra__ = False    
        self.__en_meta__ = False      


    def get_jugador(self) -> int:
        return self.__jugador__

    def esta_en_barra(self) -> bool:
        return self.__en_barra__

    def esta_en_meta(self) -> bool:
        return self.__en_meta__

    def esta_en_tablero(self) -> bool:
        return not self.__en_barra__ and not self.__en_meta__


    def mandar_a_barra(self) -> None:
        self.__en_barra__ = True
        self.__en_meta__ = False

    def sacar_de_barra(self) -> None:
        self.__en_barra__ = False

    def mandar_a_meta(self) -> None:
        self.__en_meta__ = True
        self.__en_barra__ = False



    def __repr__(self):
        if self.__en_barra__:
            estado = "barra"
        elif self.__en_meta__:
            estado = "meta"
        else:
            estado = "tablero"
        return f"<Checker jugador={self.__jugador__}, estado={estado}>"