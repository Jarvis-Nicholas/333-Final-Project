"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""
# Command line executables:
# python3 -m coverage run test_battle_stadium.py -v -b
# python3 -m coverage report 

import unittest
import pokemon_trainer as pt
import pokemon as pk
import battle_stadium as bs

# Integration
class testBattleStadium(unittest.TestCase):
    def setUp(self):
        self.player1 = pt.PokemonTrainer("player1")
        self.player2 = pt.PokemonTrainer("player2")

        self.pokemon1 = pk.Pokemon("pokemon1", "type1", 10)
        self.pokemon2 = pk.Pokemon("pokemon2", "type2", 11)
        #self.pokemon2 = pk.Pokemon("pokemon3", "type3", 12)
        #self.pokemon3 = pk.Pokemon("pokemon4", "type4", 13)

        self.player1.add_pokemon(self.pokemon1)
        self.player2.add_pokemon(self.pokemon2)



    