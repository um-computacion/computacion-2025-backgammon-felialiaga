from core.Checker import Checker

class Board:
    def __init__(self):

        self.__positions__ = [[] for _ in range(25)]  
        self.__bar__ = {1: [], 2: []}   
        self.__home__ = {1: [], 2: []}   

        self.__inicializar_posiciones__()


    def __inicializar_posiciones__(self):
        self.__positions__[1]  = [Checker(1) for _ in range(2)]
        self.__positions__[6]  = [Checker(2) for _ in range(5)]
        self.__positions__[8]  = [Checker(2) for _ in range(3)]
        self.__positions__[12] = [Checker(1) for _ in range(5)]
        self.__positions__[13] = [Checker(2) for _ in range(5)]
        self.__positions__[17] = [Checker(1) for _ in range(3)]
        self.__positions__[19] = [Checker(1) for _ in range(5)]
        self.__positions__[24] = [Checker(2) for _ in range(2)]


    def get_position(self, pos: int):
        return self.__positions__[pos] if 1 <= pos <= 24 else []

    def añadir_ficha(self, pos: int, ficha: Checker):
        if 1 <= pos <= 24:
            self.__positions__[pos].append(ficha)

    def sacar_ficha(self, pos: int):
        if 1 <= pos <= 24 and self.__positions__[pos]:
            return self.__positions__[pos].pop()
        return None

    def set_posicion(self, pos: int, jugador, cantidad: int):
        if 1 <= pos <= 24:
            self.__positions__[pos] = [
                Checker(jugador.get_numero()) for _ in range(cantidad)
            ]


    def mandar_a_barra(self, jugador: int, ficha: Checker):
        ficha.mandar_a_barra()
        self.__bar__[jugador].append(ficha)

    def sacar_de_barra(self, jugador: int):
        if self.__bar__[jugador]:
            ficha = self.__bar__[jugador].pop()
            ficha.sacar_de_barra()
            return ficha
        return None

    def mandar_a_meta(self, jugador: int, ficha: Checker):
        ficha.mandar_a_meta()
        self.__home__[jugador].append(ficha)

    def get_bar(self, jugador: int):
        return self.__bar__[jugador]

    def get_home(self, jugador: int):
        return self.__home__[jugador]

    def vaciar_fichas(self, jugador):
        for i in range(1, 25):
            self.__positions__[i] = [
                c for c in self.__positions__[i]
                if c.get_jugador() != jugador.get_numero()
            ]
        self.__home__[jugador.get_numero()] = [
            Checker(jugador.get_numero()) for _ in range(15)
        ]


    def display(self):
        col_width = 6
        max_depth = 5  # profundidad visible máxima

        print("\n=== TABLERO DE BACKGAMMON ===\n")

        # --- Parte superior (13–24) ---
        top_range = range(13, 25)
        print( "       ","".join([f"{i:2}".center(col_width) for i in top_range]))

        # En la parte superior, las fichas “cuelgan” desde los números hacia abajo
        for level in range(max_depth):
            fila = []
            for i in top_range:
                pos = self.__positions__[i]
                if level < len(pos):
                    ficha = "X" if pos[level].get_jugador() == 1 else "O"
                    fila.append(ficha.center(col_width))
                else:
                    fila.append("|".center(col_width))
            print("        " + "".join(fila))

        print("-" * (col_width * 12 + 8))

        # --- Parte inferior (12–1) ---
        bottom_range = range(12, 0, -1)
        print( "       ","".join([f"{i:2}".center(col_width) for i in bottom_range]))

        # En la parte inferior, las fichas “suben” desde los números hacia arriba
        for level in range(max_depth - 1, -1, -1):
            fila = []
            for i in bottom_range:
                pos = self.__positions__[i]
                # Calcular el índice de ficha desde abajo hacia arriba
                if len(pos) > (max_depth - 1 - level):
                    ficha = "X" if pos[len(pos) - (max_depth - level)].get_jugador() == 1 else "O"
                    fila.append(ficha.center(col_width))
                else:
                    fila.append("|".center(col_width))
            print("        " + "".join(fila))

        # --- Barra ---
        print("\nBarra:")
        print(
            f"       J1: {len(self.__bar__[1])}".ljust(12)
            + f"J2: {len(self.__bar__[2])}".ljust(12)
        )

        # --- Home ---
        print("\nHome:")
        print(
            f"       J1: {len(self.__home__[1])}".ljust(12)
            + f"J2: {len(self.__home__[2])}".ljust(12)
        )


if __name__ == "__main__":
    board = Board()
    board.display()