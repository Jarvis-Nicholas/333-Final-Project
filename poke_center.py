"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk

class PokemonCenter:
    def __init__(self):
        self.inventory = []


def heal_team(self, owner):
    for i in range (0, len(owner.team)):
        owner.team[i].health = owner.team[i].max_health


