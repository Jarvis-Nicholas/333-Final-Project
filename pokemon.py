"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import random


class Pokemon:

    def __init__(self, n: str, t: str, h: int):
        self.name = n
        self.type = t
        self.health = h
        self.kills = 0.0
        self.deaths = 0.0

    def attack(self):
        nums = []
        for i in range(0, 20):
            nums.append(i)

        return random.choice(nums)
    
    def gain_health(self, h):
        self.health = self.health + h

    def lose_health(self, h):
        self.health = self.health - h

    def is_dead(self):
        if (self.health <= 0):
            return True
        return False

    def increase_kills(self):
        self.kills = self.kills + 1

    def increase_deaths(self):
        self.deaths = self.deaths + 1

    def get_kd(self):
        if self.deaths == 0:
            return self.kills
        else:
            return self.kills / self.deaths

    def display_pokemon(self):
        # Print with alignment
        print('{:>12}  {:>12}  {:>12}'.format(self.name, self.type, self.health), end = "")