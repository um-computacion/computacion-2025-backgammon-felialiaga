import unittest
from core.Dice import Dice

class TestDice(unittest.TestCase):


    def test_throw_dice(self):

        dice = Dice

        dice1 = 5
        dice2 = 2

        self.assertEqual(dice.get_dice1 , 5)
        self.assertEqual(dice.get_dice2 , 2)
    
    def test_total_dice(self):

        dice = Dice

        dice1 = 4
        dice2 = 5

        self.assertEqual(dice.get_total , 9)

    def test_total_duplicate(self):

        dice = Dice

        dice1 = 4
        dice2 = 4 

        self.assertEqual(dice.get_total , 16)


if __name__ == "__main__":
    unittest.main()