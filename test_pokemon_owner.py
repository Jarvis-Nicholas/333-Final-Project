"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

# Command line executables:
# python3 -m coverage run test_pokemon_owner.py -v -b
# python3 -m coverage report 

import unittest
import pokemon as pk
import pokemon_owner as po

class testPokemonOwner(unittest.TestCase):
    def setUp(self):
        self.owner = po.PokemonOwner("name")
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.pokemon2 = pk.Pokemon("name2", "type2", 15)

    def test_constructor(self):
        self.assertEqual(self.owner.name, "name")
        self.assertEqual(len(self.owner.team), 0)
        self.assertEqual(self.owner.wins, 0)
        self.assertEqual(self.owner.losses, 0)

    def test_remove_pokemon(self):
        self.owner.team.append(self.pokemon)
        self.owner.remove_pokemon(self.pokemon)
        self.assertEqual(len(self.owner.team), 0)
    
    def test_add_pokemon(self):
        self.owner.add_pokmeon(self.pokemon)
        self.assertEqual(len(self.owner.team), 1)

    def test_increase_wins(self):
        old_wins = self.owner.wins
        self.owner.increase_wins()

        self.assertEqual(old_wins + 1, self.owner.wins)

    def test_increase_losses(self):
        old_losses = self.owner.losses
        self.owner.increase_losses()

        self.assertEqual(old_losses + 1, self.owner.losses)

    def test_swap_pokemon_correct_indices(self):
        self.owner.add_pokmeon(self.pokemon)
        self.owner.add_pokmeon(self.pokemon2)

        # swap
        self.owner.swap_pokemon(0, 1)
        self.assertEqual(self.owner.team[0], self.pokemon2)
        self.assertEqual(self.owner.team[1], self.pokemon)

    # Pokemon do not swap
    def test_swap_pokemon_incorrect_indices(self):
        self.owner.add_pokmeon(self.pokemon)
        self.owner.add_pokmeon(self.pokemon2)

        small_index = -1
        large_index = 2
        good_lower = 0
        good_higher = 1


        # Current too small
        self.owner.swap_pokemon(small_index , good_higher)
        self.assertEqual(self.owner.team[0], self.pokemon)
        self.assertEqual(self.owner.team[1], self.pokemon2)

        # Current too large
        self.owner.swap_pokemon(good_lower, large_index)
        self.assertEqual(self.owner.team[0], self.pokemon)
        self.assertEqual(self.owner.team[1], self.pokemon2)

        # New too small
        self.owner.swap_pokemon(small_index , good_higher)
        self.assertEqual(self.owner.team[0], self.pokemon)
        self.assertEqual(self.owner.team[1], self.pokemon2)

        # New too large
        self.owner.swap_pokemon(good_lower, large_index)
        self.assertEqual(self.owner.team[0], self.pokemon)
        self.assertEqual(self.owner.team[1], self.pokemon2)

if __name__ == '__main__':
    unittest.main()
