import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from core.Player import Player

class TestPlayer(unittest.TestCase):

    def test_get_name(self):
        player = Player("Felipe Aliaga", 1)

        self.assertEqual(player.name ,"Felipe Aliaga")


    def test_set_name(self):
        player = Player("Felipe Aliaga", 1)

        newName = "Marcos"

        player.name = newName

        self.assertEqual(player.name, "Marcos")

    def test_get_player_number(self):
        player = Player("Felipe Aliaga", 1)

        self.assertEqual(player.number, 1)

    def test_set_player_number(self):
        player = Player("Felipe Aliaga", 1)

        player.number = 2

        self.assertEqual(player.number, 2)

    def test_get_token(self):
        player = Player("Felipe Aliaga", 1)

        self.assertEqual(player.token, "X")


    def test_get_token_advanced(self):
        player = Player("Felipe Aliaga", 1)

        player.number = 2

        self.assertEqual(player.token, "O")


if __name__ == "__main__":
    unittest.main()