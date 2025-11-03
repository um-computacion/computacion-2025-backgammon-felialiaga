import unittest
from core.Board import Board
from core.Checker import Checker
from core.Player import Player

class TestBoard(unittest.TestCase):


    def setUp(self):
        self.board = Board()
        self.jugador1 = Player(1, "X")
        self.jugador2 = Player(2, "O")

    def test_inicializacion_tablero(self):
        self.assertEqual(len(self.board.get_position(1)), 2)
        self.assertEqual(len(self.board.get_position(6)), 5)
        self.assertEqual(len(self.board.get_position(8)), 3)
        self.assertEqual(len(self.board.get_position(12)), 5)
        self.assertEqual(len(self.board.get_position(13)), 5)
        self.assertEqual(len(self.board.get_position(17)), 3)
        self.assertEqual(len(self.board.get_position(19)), 5)
        self.assertEqual(len(self.board.get_position(24)), 2)

    def test_añadir_y_sacar_ficha(self):
        ficha = Checker(1)
        self.board.añadir_ficha(5, ficha)
        self.assertEqual(len(self.board.get_position(5)), 1)

        sacada = self.board.sacar_ficha(5)
        self.assertEqual(sacada, ficha)
        self.assertEqual(len(self.board.get_position(5)), 0)

    def test_sacar_ficha_vacia(self):
        resultado = self.board.sacar_ficha(10)
        self.assertEqual(resultado, None)

    def test_set_posicion(self):
        self.board.set_posicion(4, self.jugador1, 3)
        self.assertEqual(len(self.board.get_position(4)), 3)
        self.assertEqual(self.board.get_position(4)[0].get_jugador(), 1)

    def test_mandar_y_sacar_de_barra(self):
        ficha = Checker(1)
        self.board.mandar_a_barra(1, ficha)
        self.assertEqual(len(self.board.get_bar(1)), 1)

        sacada = self.board.sacar_de_barra(1)
        self.assertEqual(sacada.get_jugador(), 1)
        self.assertEqual(len(self.board.get_bar(1)), 0)

    def test_mandar_a_meta(self):
        ficha = Checker(2)
        self.board.mandar_a_meta(2, ficha)
        self.assertEqual(len(self.board.get_home(2)), 1)
        self.assertTrue(ficha.esta_en_meta())

    def test_vaciar_fichas(self):
        self.board.vaciar_fichas(self.jugador1)
        self.assertEqual(len(self.board.get_home(1)), 15)
        for i in range(1, 25):
            for ficha in self.board.get_position(i):
                self.assertFalse(ficha.get_jugador() == 1)

    def test_sacar_ficha_posicion_vacia(self):
        # Limpiar posición 10
        self.board.__positions__[10] = []
        
        # Intentar sacar ficha de posición vacía
        ficha = self.board.sacar_ficha(10)
        self.assertIsNone(ficha)

    def test_sacar_ficha_posicion_invalida(self):
        # Posiciones inválidas
        ficha = self.board.sacar_ficha(0)
        self.assertIsNone(ficha)
        
        ficha = self.board.sacar_ficha(25)
        self.assertIsNone(ficha)
        
        ficha = self.board.sacar_ficha(-1)
        self.assertIsNone(ficha)

    def test_set_posicion_valida(self):
        self.board.set_posicion(15, self.jugador1, 3)
        
        fichas = self.board.get_position(15)
        self.assertEqual(len(fichas), 3)
        self.assertTrue(all(f.get_jugador() == 1 for f in fichas))

    def test_set_posicion_sobrescribe(self):
        self.assertGreater(len(self.board.get_position(6)), 0)
        
        self.board.set_posicion(6, self.jugador2, 2)
        
        fichas = self.board.get_position(6)
        self.assertEqual(len(fichas), 2)
        self.assertTrue(all(f.get_jugador() == 2 for f in fichas))

    def test_set_posicion_invalida(self):
        self.board.set_posicion(0, self.jugador1, 3)
        self.board.set_posicion(25, self.jugador1, 3)
        self.board.set_posicion(-5, self.jugador1, 3)

    def test_mandar_a_barra_jugador_1(self):
        ficha = Checker(1)
        
        self.assertEqual(len(self.board.get_bar(1)), 0)
        
        self.board.mandar_a_barra(1, ficha)
        
        self.assertEqual(len(self.board.get_bar(1)), 1)
        self.assertTrue(ficha.esta_en_barra())

    def test_mandar_a_barra_jugador_2(self):
        ficha = Checker(2)
        
        self.board.mandar_a_barra(2, ficha)
        
        self.assertEqual(len(self.board.get_bar(2)), 1)
        self.assertTrue(ficha.esta_en_barra())

    def test_sacar_de_barra_con_fichas(self):
        ficha = Checker(1)
        
        # Poner ficha en barra
        self.board.mandar_a_barra(1, ficha)
        self.assertEqual(len(self.board.get_bar(1)), 1)
        
        # Sacar de barra
        ficha_sacada = self.board.sacar_de_barra(1)
        
        self.assertIsNotNone(ficha_sacada)
        self.assertFalse(ficha_sacada.esta_en_barra())
        self.assertEqual(len(self.board.get_bar(1)), 0)

    def test_sacar_de_barra_vacia(self):
        # Barra vacía
        self.assertEqual(len(self.board.get_bar(1)), 0)
        
        # Intentar sacar
        ficha = self.board.sacar_de_barra(1)
        self.assertIsNone(ficha)

    def test_mandar_a_meta_jugador_1(self):
        ficha = Checker(1)
        
        self.assertEqual(len(self.board.get_home(1)), 0)
        
        self.board.mandar_a_meta(1, ficha)
        
        self.assertEqual(len(self.board.get_home(1)), 1)
        self.assertTrue(ficha.esta_en_meta())

    def test_mandar_a_meta_jugador_2(self):
        ficha = Checker(2)
        
        self.board.mandar_a_meta(2, ficha)
        
        self.assertEqual(len(self.board.get_home(2)), 1)
        self.assertTrue(ficha.esta_en_meta())

    def test_vaciar_fichas_jugador_1(self):
        fichas_iniciales = 0
        for pos in self.board.__positions__[1:25]:
            for ficha in pos:
                if ficha.get_jugador() == 1:
                    fichas_iniciales += 1
        
        self.assertGreater(fichas_iniciales, 0)
        
        # Vaciar fichas
        self.board.vaciar_fichas(self.jugador1)
        
        # Verificar que no quedan fichas del jugador 1 en tablero
        fichas_restantes = 0
        for pos in self.board.__positions__[1:25]:
            for ficha in pos:
                if ficha.get_jugador() == 1:
                    fichas_restantes += 1
        
        self.assertEqual(fichas_restantes, 0)
        
        # Verificar que hay 15 fichas en home
        self.assertEqual(len(self.board.get_home(1)), 15)

    def test_vaciar_fichas_jugador_2(self):
        fichas_iniciales = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        self.assertGreater(fichas_iniciales, 0)
        
        self.board.vaciar_fichas(self.jugador2)
        
        # No deben quedar fichas en tablero
        fichas_restantes = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        self.assertEqual(fichas_restantes, 0)
        
        # 15 fichas en home
        self.assertEqual(len(self.board.get_home(2)), 15)

    def test_vaciar_fichas_no_afecta_otro_jugador(self):
        # Contar fichas del jugador 2
        fichas_j2_antes = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        
        # Vaciar jugador 1
        self.board.vaciar_fichas(self.jugador1)
        
        # Fichas del jugador 2 deben permanecer igual
        fichas_j2_despues = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        self.assertEqual(fichas_j2_antes, fichas_j2_despues)

    def test_display_no_crash(self):
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display() causó una excepción: {e}")

    def test_display_con_fichas_personalizadas(self):
        # Limpiar tablero
        for i in range(1, 25):
            self.board.__positions__[i] = []
        
        # Colocar fichas específicas
        self.board.añadir_ficha(13, Checker(1))
        self.board.añadir_ficha(13, Checker(1))
        self.board.añadir_ficha(24, Checker(2))
        
        # Agregar fichas en barra y home
        self.board.mandar_a_barra(1, Checker(1))
        self.board.mandar_a_meta(2, Checker(2))
        
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display() causó una excepción: {e}")

    def test_display_tablero_vacio(self):
        # Vaciar completamente el tablero
        for i in range(1, 25):
            self.board.__positions__[i] = []
        
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display() causó una excepción: {e}")

    def test_get_position_posicion_valida(self):
        # Posición 1 tiene 2 fichas inicialmente
        fichas = self.board.get_position(1)
        self.assertEqual(len(fichas), 2)
        self.assertTrue(all(f.get_jugador() == 1 for f in fichas))

    def test_get_position_posicion_invalida(self):
        # Posiciones inválidas retornan lista vacía
        self.assertEqual(self.board.get_position(0), [])
        self.assertEqual(self.board.get_position(25), [])
        self.assertEqual(self.board.get_position(-1), [])

    def test_añadir_ficha_posicion_valida(self):
        # Limpiar posición
        self.board.__positions__[15] = []
        
        # Añadir ficha
        ficha = Checker(1)
        self.board.añadir_ficha(15, ficha)
        
        self.assertEqual(len(self.board.get_position(15)), 1)

    def test_añadir_ficha_posicion_invalida(self):
        ficha = Checker(1)
        
        # No debe causar error
        try:
            self.board.añadir_ficha(0, ficha)
            self.board.añadir_ficha(25, ficha)
        except Exception as e:
            self.fail(f"añadir_ficha() causó una excepción: {e}")

    def test_sacar_ficha_exitoso(self):
        # Posición 1 tiene fichas
        ficha = self.board.sacar_ficha(1)
        
        self.assertIsNotNone(ficha)
        self.assertIsInstance(ficha, Checker)

    def test_inicializacion_completa(self):
        # Verificar configuración inicial
        self.assertEqual(len(self.board.get_position(1)), 2)
        self.assertEqual(len(self.board.get_position(6)), 5)
        self.assertEqual(len(self.board.get_position(8)), 3)
        self.assertEqual(len(self.board.get_position(12)), 5)
        self.assertEqual(len(self.board.get_position(13)), 5)
        self.assertEqual(len(self.board.get_position(17)), 3)
        self.assertEqual(len(self.board.get_position(19)), 5)
        self.assertEqual(len(self.board.get_position(24)), 2)
        
        # Verificar barras y homes vacías
        self.assertEqual(len(self.board.get_bar(1)), 0)
        self.assertEqual(len(self.board.get_bar(2)), 0)
        self.assertEqual(len(self.board.get_home(1)), 0)
        self.assertEqual(len(self.board.get_home(2)), 0)


if __name__ == "__main__":
    unittest.main()