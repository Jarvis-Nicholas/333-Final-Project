"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import random

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
            print(i + 1, end="")
            self.team[i].display_pokemon()
    
    def swap_pokemon(self, current_index, new_index):
        #user_input = int(input("Switch with which number Pokemon?"))
        # In sizing
        if ((current_index >= 0 and current_index <= len(self.team) - 1) and (new_index >= 0 and new_index <= len(self.team) - 1)):
            self.team[current_index], self.team[new_index] = self.team[new_index], self.team[current_index]

    def team_is_dead(self):
        dead_counter = 0

        # Check every Pokemon
        for i in range (0, len(self.team)):
            if (self.team[i].is_dead() == True):
                counter = counter + 1
        # All Dead
        if (dead_counter == len(self.team)):
            return True
        # Not all dead
        else:
            return False

    def create_team(self):
        # Read input file
        for i in range(0, 6):
            input_line = random.choice(list(open('pokemon_list.txt')))
            parsed_line = input_line.split(" ")
            pokemon = pk.Pokemon(parsed_line[0], parsed_line[1], parsed_line[2])
            self.team.append(pokemon)