from core.Board import Board
from core.Player import Player
from core.Dice import Dice

class Game:

    def __init__(self):
        self.__board__ = Board()
        self.__players__ = [Player(1, "X"), Player(2, "O")]
        self.__dice__ = Dice()
        self.__turno__ = 0
        self.__dados_actuales__ = []
        self.__dados_usados__ = []

    def get_jugador_actual(self):
        return self.__players__[self.__turno__]

    def cambiar_turno(self):
        self.__turno__ = 1 - self.__turno__
        self.__dados_actuales__ = []
        self.__dados_usados__ = []

    def tirar_dados(self):
        valores = self.__dice__.roll()
        self.__dados_actuales__ = self.__dice__.get_values()  # usar get_values() para dobles
        self.__dados_usados__ = []
        return valores

    def direccion_movimiento(self, jugador: Player) -> int:
        return 1 if jugador.get_numero() == 1 else -1

    def posicion_casa(self, jugador: Player) -> range:
        return range(19, 25) if jugador.get_numero() == 1 else range(1, 7)

    def puede_bear_off(self, jugador: Player) -> bool:
        for pos in range(1, 25):
            fichas = self.__board__.get_position(pos)
            if fichas and fichas[-1].get_jugador() == jugador.get_numero():
                if pos not in self.posicion_casa(jugador):
                    return False
        return True

    def mover_ficha(self, origen: int, destino: int, dado: int) -> bool:
        jugador = self.get_jugador_actual()
        num_jugador = jugador.get_numero()

        # Si hay fichas en la barra, debe reingresar primero
        if len(self.__board__.get_bar(num_jugador)) > 0 and origen != 0:
            return False

        # Verificar dado disponible
        if dado not in self.__dados_actuales__:
            return False

        # Movimiento desde barra
        if origen == 0:
            entrada = 25 - dado if num_jugador == 1 else dado
            destino = entrada
            ficha = self.__board__.sacar_de_barra(num_jugador)
            if not ficha:
                return False
        else:
            # Movimiento normal
            fichas = self.__board__.get_position(origen)
            if not fichas or fichas[-1].get_jugador() != num_jugador:
                return False
            ficha = self.__board__.sacar_ficha(origen)

        # Bearing off (sacar ficha del tablero)
        if destino == 25 or destino == 0:
            if not self.puede_bear_off(jugador):
                self.__board__.añadir_ficha(origen, ficha)  # devolver ficha
                return False
            self.__board__.mandar_a_meta(num_jugador, ficha)
        else:
            destino_fichas = self.__board__.get_position(destino)
            if destino_fichas and destino_fichas[-1].get_jugador() != num_jugador:
                if len(destino_fichas) == 1:
                    # Captura
                    capturada = self.__board__.sacar_ficha(destino)
                    self.__board__.mandar_a_barra(3 - num_jugador, capturada)
                else:
                    self.__board__.añadir_ficha(origen, ficha)
                    return False
            self.__board__.añadir_ficha(destino, ficha)

        # Marcar dado como usado
        self.__dados_actuales__.remove(dado)
        self.__dados_usados__.append(dado)
        return True

    def juego_terminado(self) -> bool:
        for player in self.__players__:
            if len(self.__board__.get_home(player.get_numero())) == 15:
                return True
        return False

    def get_board(self) -> Board:
        return self.__board__

    def get_dados_actuales(self) -> list:
        return self.__dados_actuales__

    def get_dados_usados(self) -> list:
        return self.__dados_usados__

    def get_ganador(self):
        for player in self.__players__:
            if len(self.__board__.get_home(player.get_numero())) == 15:
                return player
        return None