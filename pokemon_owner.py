"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import random

class PokemonOwner:
    def __init__(self):
        self.team = []

    def remove_pokemon(self, p):
        self.team.remove(p)

    def add_pokemon(self, p):
        self.team.append(p)

    def index_in_range(self, input_index):
        index = input_index - 1
        #if (index >= 0 and index <= len(self.team) - 1 and len(self.team) != 0):
        if ((index >= 0) and (index <= len(self.team) - 1) and (len(self.team) != 0)):
            return True
        else:
            return False

    def display_team(self):
        # Print with alignment
        print('{:>12}  {:>12}  {:>12}'.format("NAME:", "TYPE:", "HEALTH:"), "\n")
        for i in range(0, len(self.team)):
            print(i + 1, end="")
            self.team[i].display_pokemon()
        print()

    def swap_pokemon_team_members(self, current_index, new_index):
        # In sizing
        if ((current_index >= 0 and current_index <= len(self.team) - 1) and (new_index >= 0 and new_index <= len(self.team) - 1)):
            self.team[current_index], self.team[new_index] = self.team[new_index], self.team[current_index]



    def create_team(self):
        # Read input file
        for i in range(0, 6):
            input_line = random.choice(list(open('pokemon_list.txt')))
            parsed_line = input_line.split(" ")
            pokemon = pk.Pokemon(parsed_line[0], parsed_line[1], parsed_line[2])
            self.team.append(pokemon)

    def team_is_dead(self):
        dead_counter = 0

        # Check every Pokemon
        for i in range (0, len(self.team)):
            if (self.team[i].is_dead() == True):
                dead_counter = dead_counter + 1
        # All Dead
        if (dead_counter == len(self.team)):
            return True
        # Not all dead
        else:
            return False