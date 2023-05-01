"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

# Command line executables:
# python3 -m coverage run test_pokemon.py -v -b
# python3 -m coverage report 

import unittest
import pokemon as pk

class testPokmeon(unittest.TestCase):
    def setUp(self):
        self.pokemon = pk.Pokemon("name", "type", 10)
        self.new_health = 0

    def test_constructor(self):
        self.assertEqual(self.pokemon.name, "name")
        self.assertEqual(self.pokemon.type, "type")
        self.assertEqual(self.pokemon.health, 10) 

    def test_attack(self):
        # 0 <= health <= 20
        self.assertGreaterEqual(self.pokemon.attack(), 0)
        self.assertLessEqual(self.pokemon.attack(), 20)

    def test_gain_health(self):
        # Mark new health
        self.new_health = self.pokemon.health + 1

        # Increase health
        self.pokemon.gain_health(1)
        self.assertEqual(self.new_health, self.pokemon.health)

    def test_lose_health_decrement(self):
        # Mark new health
        self.new_health = self.pokemon.health - 1

        # Lose health
        self.pokemon.lose_health(1)
        self.assertEqual(self.new_health, self.pokemon.health)

    def test_is_dead_not_dead(self):
        # Not Dead
        self.pokemon.health = 1
        self.assertFalse(self.pokemon.is_dead())

    def test_is_dead_negative_health(self):
        # Negative
        self.pokemon.health = -1
        self.assertTrue(self.pokemon.is_dead())

    def test_is_dead_zero(self):
        # Zero
        self.pokemon.health = 0
        self.assertTrue(self.pokemon.is_dead())

    def test_increase_kills(self):
        old_kills = self.pokemon.kills
        self.pokemon.increase_kills()
        self.assertEqual(self.pokemon.kills, old_kills + 1)

    def test_increase_deaths(self):
        old_deaths = self.pokemon.deaths
        self.pokemon.increase_deaths()
        self.assertEqual(self.pokemon.deaths, old_deaths + 1)

    def test_get_kd_zero_deaths(self):
        self.pokemon.deaths = 0
        self.pokemon.kills = 1
        self.assertEqual(self.pokemon.get_kd(), self.pokemon.kills)

    def test_get_kd_whole_number(self):
        self.pokemon.deaths = 1
        self.pokemon.kills = 5
        self.assertEqual(self.pokemon.get_kd(), self.pokemon.kills)

    def test_kd_frational(self):
        self.pokemon.deaths = 2
        self.pokemon.kills = 5
        self.assertEqual(self.pokemon.get_kd(), 5.0 / 2.0)

if __name__ == '__main__':
    unittest.main()