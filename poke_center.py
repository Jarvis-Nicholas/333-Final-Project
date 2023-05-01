"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import random

class PokemonCenter:
    def __init__(self):
        self.inventory = []


def heal_team(owner):
    for i in range (0, len(owner.team)):
        owner.team[i].health = owner.team[i].max_health

def rename_pokemon(pokemon, new_name: str):
    pokemon.name = new_name

def create_inventory(self):
    # Read input file
    for i in range(0, 15):
        input_line = random.choice(list(open('pokemon_list.txt')))
        parsed_line = input_line.split(" ")
        pokemon = pk.Pokemon(parsed_line[0], parsed_line[1], parsed_line[2])
        self.inventory.append(pokemon)

def display_inventory(self):
    # Print with alignment
    print('{:>12}  {:>12}  {:>12}'.format("NAME:", "TYPE:", "HEALTH:"), "\n")
    for i in range(0, len(self.team)):
        print(i + 1, end="")
        self.inventory[i].display_pokemon()
    print()

def give_pokemon(self, input):
    if (len(self.inventory) == 0):

    if (input >= 0 and input <= len(inventory - 1)):




    return pokemon

def take_pokemon(self, pokemon):
    self.inventory.append(pokemon)