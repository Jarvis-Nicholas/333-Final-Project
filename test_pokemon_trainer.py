"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""
# Command line executables:
# python3 -m coverage run test_pokemon_trainer.py -v -b
# python3 -m coverage report 

import unittest
import pokemon_trainer as pt

class testPokemonTrainer(unittest.TestCase):

    def setUp(self):
        self.trainer = pt.PokemonTrainer("name")

    def test_constructor(self):
        self.assertEqual(self.trainer.name, "name")
        self.assertEqual(self.trainer.wins, 0)
        self.assertEqual(self.trainer.losses, 0)

    def test_increase_wins(self):
        old_wins = self.trainer.wins
        self.trainer.increase_wins()

        self.assertEqual(old_wins + 1, self.trainer.wins)

    def test_increase_losses(self):
        old_losses = self.trainer.losses
        self.trainer.increase_losses()

        self.assertEqual(old_losses + 1, self.trainer.losses)

if __name__ == '__main__':
    unittest.main()