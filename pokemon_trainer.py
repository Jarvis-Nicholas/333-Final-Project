"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon_owner as po

# Inheritance
class PokemonTrainer (po.PokemonOwner):
    def __init__(self, n):
        self.name = n
        self.wins = 0
        self.losses = 0

        # Inherit parent's attributes and methods (owner)
        super().__init__()

    def increase_wins(self):
        self.wins = self.wins + 1

    def increase_losses(self):
        self.losses = self.losses + 1 
    