import unittest
from core.Dice import Dice

class TestDice(unittest.TestCase):

    def test_throw_dice(self):
        dice1 = 5
        dice2 = 2

        self.assertEqual(self.__dice1, 5)
        self.assertEqual(self.__dice2, 2)
    
    def test_total_dice(self):
        dice1 = 4
        dice2 = 5

        self.assertEqual(self.__total, 9)

    def test_total_duplicate(self):
        dice1 = 4
        dice2 = 4

        self.assertEqual(self.__total, 16)


if __name__ == "__main__":
    unittest.main()