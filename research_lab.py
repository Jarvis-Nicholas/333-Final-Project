"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""



def heal_team(owner):
    for i in range (0, len(owner.team)):
        owner.team[i].health = owner.team[i].max_health

def change_pokemon_name(owner, index, new_name: str):
    if (owner.index_in_range(index)):
        owner.team[index - 1].name = new_name

def change_pokemon_type(owner, index, new_type: str):
    if (owner.index_in_range(index)):
        owner.team[index - 1].type = new_type

def change_pokemon_health(owner, index, new_health):
    if (owner.index_in_range(index)):
        owner.team[index - 1].health = new_health

def change_pokemon_max_health(owner, index, new_health):
    if (owner.index_in_range(index)):
        owner.team[index - 1].max_health = new_health

