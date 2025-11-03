import unittest
from core.Player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player(1, "X")
        self.player2 = Player(2, "O")

    def test_get_numero(self):
        self.assertEqual(self.player1.get_numero(), 1)
        self.assertEqual(self.player2.get_numero(), 2)

    def test_get_ficha(self):
        self.assertEqual(self.player1.get_ficha(), "X")
        self.assertEqual(self.player2.get_ficha(), "O")

    def test_jugadores_distintos(self):
        self.assertFalse(self.player1.get_numero() == self.player2.get_numero())
        self.assertFalse(self.player1.get_ficha() == self.player2.get_ficha())

    def test_reutilizacion_numero_y_ficha(self):
        numero_inicial = self.player1.get_numero()
        ficha_inicial = self.player1.get_ficha()

        # Se consulta varias veces para confirmar consistencia
        self.assertEqual(self.player1.get_numero(), numero_inicial)
        self.assertEqual(self.player1.get_ficha(), ficha_inicial)
        self.assertEqual(self.player1.get_numero(), 1)
        self.assertEqual(self.player1.get_ficha(), "X")


if __name__ == "__main__":
    unittest.main()