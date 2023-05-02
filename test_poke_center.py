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
import pokemon as pk
import poke_center as pc

# Integration
class testPokemonTrainer(unittest.TestCase):
    def setUp(self):
        self.center = pc.PokemonCenter()
        self.trainer = pt.PokemonTrainer()
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.pokemon2 = pk.Pokemon("name2", "type2", 15)
 
    def test_give_pokemon(self):
