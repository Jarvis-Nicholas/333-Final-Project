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

        self.player1.add_pokemon(self.pokemon1)
        self.player2.add_pokemon(self.pokemon2)

    def test_play_round_exit_choice(self):
        # battle_choice == 2
        self.assertTrue(bs.play_round(self.player1, self.player2, 2))

    def test_play_round_attack(self):
        bs.play_round(self.player1, self.player2, 1)

        # Health same and changed
        self.assertEqual(self.player1.team[0].health, self.player1.team[0].max_health)
        self.assertLess(self.player2.team[0].health, self.player2.team[0].max_health)

    def test_get_index_single_pokemon(self):
        # First pokemon alive = index 0
        self.assertEqual(bs.get_index(self.player1), 0)

    def test_get_index_multiple_pokemon(self):
        # Add new pokemon
        self.player1.add_pokemon(self.pokemon2)

        # Kill first pokeon
        self.player1.team[0].health = 0

        # First pokemon alive = index 1
        self.assertEqual(bs.get_index(self.player1), 1)

    def test_check_game_over_false(self):
        # No win
        self.assertFalse(bs.check_game_over(self.player1, self.player2))

        # Wins and losses the same
        self.assertEqual(self.player1.wins, 0)
        self.assertEqual(self.player1.losses, 0)
        self.assertEqual(self.player2.wins, 0)
        self.assertEqual(self.player2.losses, 0)

    def test_check_game_over_true(self):
        # Player 2 dead team
        self.player2.team[0].health = 0

        # Player 1 win
        self.assertTrue(bs.check_game_over(self.player1, self.player2))

        # Wins and losses increment
        self.assertEqual(self.player1.wins, 1)
        self.assertEqual(self.player1.losses, 0)
        self.assertEqual(self.player2.wins, 0)
        self.assertEqual(self.player2.losses, 1)

if __name__ == '__main__':
    unittest.main()