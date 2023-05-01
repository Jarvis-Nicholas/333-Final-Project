"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

# Command line executables:
# python3 -m coverage run test_pokemon_owner_AND_pokemon.py -v -b
# python3 -m coverage report 

import unittest
import pokemon as pk
import pokemon_owner as po

class testPokemonOwnerPokemon(unittest.TestCase):
    def setUp(self):
        self.owner = po.PokemonOwner("name")
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.owner.add_pokmeon(self.pokemon)

    def test_pokemon_name(self):
       self.assertEqual(self.owner.team[0].name, self.pokemon.name)
    
    def test_pokmeon_type(self):
        self.assertEqual(self.owner.team[0].type, self.pokemon.type)

    def test_pokemon_health(self):
        self.assertEqual(self.owner.team[0].health, self.pokemon.health)

if __name__ == '__main__':
    unittest.main()