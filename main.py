"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import pokemon_owner as po
import random


def main():
    print("**************************************************")
    print("                  ---------------\n                 | POKEMON FUN!! |\n                  ---------------\n") 
    user_name = str(input("-Welcome to your Pokemon adventure!! What is your name?\n"))

    # Create Owner
    player = po.PokemonOwner(user_name)


    #lines = open('pokemon_list.txt').read().splitlines()
    #my_line = random.choice(lines)

    for i in range(0, 6):
        input_line = random.choice(list(open('pokemon_list.txt')))
        parsed_line = input_line.split(" ")
        pokemon = pk.Pokemon(parsed_line[0], parsed_line[1], parsed_line[2])
        player.team.append(pokemon)
    player.display_team()

    #while True:


main()