"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""
# Command line executables:
# python3 -m coverage run test_poke_center.py -v -b
# python3 -m coverage report 

import unittest
import pokemon_trainer as pt
import pokemon as pk
import poke_center as pc

# Integration
class testPokemonTrainer(unittest.TestCase):
    def setUp(self):
        self.center = pc.PokemonCenter()
        self.trainer = pt.PokemonTrainer("trainer name")

        # Save pokemon to teams
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.pokemon2 = pk.Pokemon("name2", "type2", 15)
        self.center.add_pokemon(self.pokemon)
        self.trainer.add_pokemon(self.pokemon2)

        # Indexing
        self.bad_index = -1
        self.good_index = 1

    def test_give_pokemon_bad_index(self):
        self.center.give_pokemon(self.bad_index, self.trainer)

        # Pokemon not given
        self.assertNotEqual(self.pokemon, self.trainer.team[0])
        self.assertEqual(self.center.team[0], self.pokemon)
        self.assertEqual(len(self.center.team), 1)
        self.assertEqual(len(self.trainer.team), 1)

    def test_give_pokemon_good_index(self):
        self.center.give_pokemon(self.good_index, self.trainer)

        # Pokemon given
        # First pokemon not erased from trainer
        self.assertEqual(self.trainer.team[0], self.pokemon1)
        self.assertEqual(self.trainer.team[1], self.pokemon)
        self.assertEqual(len(self.center.team), 0)
        self.assertEqual(len(self.trainer.team), 2)


if __name__ == '__main__':
    unittest.main()