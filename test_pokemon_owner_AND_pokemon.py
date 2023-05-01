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

# Integration
class testPokemonOwnerPokemon(unittest.TestCase):
    def setUp(self):
        self.owner = po.PokemonOwner()
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.owner.add_pokmeon(self.pokemon)

    # Default name is same
    def test_pokemon_name_default(self):
       self.assertEqual(self.owner.team[0].name, self.pokemon.name)
    
    # Default type is same  
    def test_pokmeon_type_default(self):
        self.assertEqual(self.owner.team[0].type, self.pokemon.type)

    # Default health is same
    def test_pokemon_health_default(self):
        self.assertEqual(self.owner.team[0].health, self.pokemon.health)

    # Changing pokemon class updates into owner class
    def test_pokemon_name_change(self):
        old_name = self.pokemon.name
        self.pokemon.name = "new name"

        # Update is correct
        self.assertEqual(self.owner.team[0].name, self.pokemon.name)
        self.assertNotEqual(self.owner.team[0].name, old_name)

    # Changing pokemon class updates into owner class   
    def test_pokmeon_type_change(self):
        old_type = self.pokemon.type
        self.pokemon.name = "new type"

        # Update is correct
        self.assertEqual(self.owner.team[0].type, self.pokemon.type)
        self.assertNotEqual(self.owner.team[0].name, old_type)

    # Changing pokemon class updates into owner class
    def test_pokemon_health_change(self):
        old_health = self.pokemon.health
        self.pokemon.name = "new health"

        # Update is correct
        self.assertEqual(self.owner.team[0].health, self.pokemon.health)
        self.assertNotEqual(self.owner.team[0].name, old_health)

if __name__ == '__main__':
    unittest.main()