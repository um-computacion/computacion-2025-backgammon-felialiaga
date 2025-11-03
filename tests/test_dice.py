import unittest
from core.Dice import Dice

class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_roll_devuelve_lista_no_vacia(self):
        valores = self.dice.roll()
        self.assertTrue(len(valores) >= 2)

    def test_roll_valores_en_rango_correcto(self):
        valores = self.dice.roll()
        for v in valores:
            self.assertTrue(1 <= v <= 6)

    def test_tirada_doble_devuelve_cuatro_valores(self):
        while True:
            valores = self.dice.roll()
            if valores[0] == valores[1]:
                self.assertEqual(len(valores), 4)
                self.assertTrue(self.dice.tirada_doble())
                break

    def test_tirada_no_doble_devuelve_dos_valores(self):
        while True:
            valores = self.dice.roll()
            if valores[0] != valores[1]:
                self.assertEqual(len(valores), 2)
                self.assertFalse(self.dice.tirada_doble())
                break

    def test_individual_values_devuelve_dos_valores(self):
        self.dice.roll()
        valores = self.dice.individual_values()
        self.assertEqual(len(valores), 2)

    def test_usar_valor_disponible_devuelve_true(self):
        valores = self.dice.roll()
        valor = valores[0]
        resultado = self.dice.usar_valor(valor)
        self.assertTrue(resultado)
        self.assertIn(valor, self.dice.valores_usados())

    def test_usar_valor_no_disponible_devuelve_false(self):
        self.dice.roll()
        resultado = self.dice.usar_valor(7)  # valor imposible
        self.assertFalse(resultado)

    def test_valores_usados_devuelve_lista_correcta(self):
        valores = self.dice.roll()
        valor = valores[0]
        self.dice.usar_valor(valor)
        usados = self.dice.valores_usados()
        self.assertIn(valor, usados)



if __name__ == "__main__":
    unittest.main()