"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""
# Command line executables:
# python3 -m coverage run test_research_lab.py -v -b
# python3 -m coverage report 

import unittest
import pokemon_owner as po
import pokemon as pk
import research_lab as rl


# Integration
class testResearchLab(unittest.TestCase):
    def setUp(self):
        self.owner = po.PokemonOwner()
        self.bad_index = -1
        self.good_index = 1

        # Save pokemon to team
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.owner.add_pokemon(self.pokemon)

    def test_heal_team(self):
        self.owner.team[0].health = 1

        # Heal
        rl.heal_team(self.owner)
        self.assertEqual(self.owner.team[0].health, self.owner.team[0].max_health)

    def test_change_pokemon_name_no_change(self):
        # No change
        rl.change_pokemon_name(self.owner, self.bad_index, "new")

        self.assertEqual(self.owner.team[0].name, self.pokemon.name)
        self.assertNotEqual(self.owner.team[0].name, "new")

    def test_change_pokemon_name_change(self):
        # Change
        old_data = self.pokemon.name
        rl.change_pokemon_name(self.owner, self.good_index, "new")
        
        self.assertEqual(self.owner.team[0].name, "new")
        self.assertNotEqual(self.owner.team[0].name, old_data)

    def test_change_pokemon_type_no_change(self):
        # No change
        rl.change_pokemon_type(self.owner, self.bad_index, "new")

        self.assertEqual(self.owner.team[0].type, self.pokemon.type)
        self.assertNotEqual(self.owner.team[0].type, "new")
    
    def test_change_pokemon_type_change(self):
        # Change
        old_data = self.pokemon.type
        rl.change_pokemon_type(self.owner, self.good_index, "new")

        self.assertEqual(self.owner.team[0].type, "new")
        self.assertNotEqual(self.owner.team[0].type, old_data)

    def test_change_pokemon_health_no_change(self):
        # No change
        rl.change_pokemon_health(self.owner, self.bad_index, 100)

        self.assertEqual(self.owner.team[0].health, self.pokemon.health)
        self.assertNotEqual(self.owner.team[0].health, 100)

    def test_change_pokemon_health_change(self):
        # Change
        old_data = self.pokemon.health
        rl.change_pokemon_health(self.owner, self.good_index, 100)

        self.assertEqual(self.owner.team[0].health, 100)
        self.assertNotEqual(self.owner.team[0].health, old_data)

    def test_change_pokemon_max_health_no_change(self):
        # No change
        rl.change_pokemon_max_health(self.owner, self.bad_index, 100)

        self.assertEqual(self.owner.team[0].max_health, self.pokemon.max_health)
        self.assertNotEqual(self.owner.team[0].max_health, 100)

    def test_change_pokemon_max_health_change(self):
        # Change
        old_data = self.pokemon.max_health
        rl.change_pokemon_max_health(self.owner, self.good_index, 100)

        self.assertEqual(self.owner.team[0].max_health, 100)
        self.assertNotEqual(self.owner.team[0].max_health, old_data)

if __name__ == '__main__':
    unittest.main()