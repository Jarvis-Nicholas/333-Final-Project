"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as po

class PokemonOwner:
    def __init__(self, n):
        self.name = n
        self.team = []
        self.wins = 0
        self.losses = 0

    def remove_pokemon(self, p):
        self.team.remove(p)

    def add_pokmeon(self, p):
        self.team.append(p)

    def increase_wins(self):
        self.wins = self.wins + 1

    def increase_losses(self):
        self.losses = self.losses + 1

    def display_team(self):
        # Print with alignment
        print('{:>12}  {:>12}  {:>12}'.format("NAME:", "TYPE:", "HEALTH:"), "\n")
        for i in range(0, len(self.team)):
            self.team[i].display_pokemon()