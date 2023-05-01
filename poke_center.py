"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon_owner as po


class PokemonCenter (po):

def heal_team(owner):
    for i in range (0, len(owner.team)):
        owner.team[i].health = owner.team[i].max_health

def rename_pokemon(pokemon, new_name: str):
    pokemon.name = new_name

def give_pokemon(self, input):
    if (len(self.inventory) == 0):

    if (input >= 0 and input <= len(inventory - 1)):




    return pokemon

def take_pokemon(self, pokemon):
    self.inventory.append(pokemon)