import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from core.Dice import Dice

class TestDice(unittest.TestCase):


    def test_throw_dice(self):

        dice = Dice()


        dice.set_dice1(5)
        dice.set_dice2(3)

        self.assertEqual(dice.get_dice1(), 5)
        self.assertEqual(dice.get_dice2(), 3)
    
    def test_total_dice(self):

        dice = Dice()

        dice.set_dice1(5)
        dice.set_dice2(4)

        dice.set_total(dice.get_dice1(), dice.get_dice2())

        self.assertEqual(dice.get_total() , 9)

    def test_total_duplicate(self):

        dice = Dice()

        dice.set_dice1(2)
        dice.set_dice2(2)  

        dice.set_total(dice.get_dice1(), dice.get_dice2())

        self.assertEqual(dice.get_total() , 8)


if __name__ == "__main__":
    unittest.main()