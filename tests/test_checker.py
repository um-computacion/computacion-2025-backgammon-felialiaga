import unittest
from core.Checker import Checker

class TestChecker(unittest.TestCase):

    def setUp(self):
        self.ficha = Checker(1)  

    def test_jugador_asignado_correctamente(self):
        self.assertEqual(self.ficha.get_jugador(), 1)

    def test_estado_inicial(self):
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())
        self.assertTrue(self.ficha.esta_en_tablero())

    def test_init_jugador_invalido(self):
        for jugador in [0, 3, -1]:
            with self.assertRaises(ValueError):
                Checker(jugador)

    def test_init_jugador_valido(self):
        for jugador in [1, 2]:
            ficha = Checker(jugador)
            self.assertEqual(ficha.get_jugador(), jugador)
            self.assertFalse(ficha.esta_en_barra())
            self.assertFalse(ficha.esta_en_meta())

    def test_mandar_a_barra(self):
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_tablero())

    def test_sacar_de_barra(self):
        self.ficha.mandar_a_barra()
        self.ficha.sacar_de_barra()
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertTrue(self.ficha.esta_en_tablero())

    def test_mandar_a_meta(self):
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_tablero())

    def test_cambio_barra_a_meta(self):
        self.ficha.mandar_a_barra()
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())

    def test_cambio_meta_a_barra(self):
        self.ficha.mandar_a_meta()
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_ciclo_completo_estados(self):
        self.ficha.mandar_a_barra()
        self.assertFalse(self.ficha.esta_en_tablero())
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

        self.ficha.sacar_de_barra()
        self.assertTrue(self.ficha.esta_en_tablero())
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

        self.ficha.mandar_a_meta()
        self.assertFalse(self.ficha.esta_en_tablero())
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertTrue(self.ficha.esta_en_meta())

    def test_repr(self):
        repr_tablero = repr(self.ficha)
        self.assertIn("Checker", repr_tablero)
        self.assertIn("jugador=1", repr_tablero)
        self.assertIn("estado=tablero", repr_tablero)
        self.assertEqual(repr_tablero, "<Checker jugador=1, estado=tablero>")

        self.ficha.mandar_a_barra()
        repr_barra = repr(self.ficha)
        self.assertIn("estado=barra", repr_barra)

        self.ficha.mandar_a_meta()
        repr_meta = repr(self.ficha)
        self.assertIn("estado=meta", repr_meta)



if __name__ == "__main__":
    unittest.main()