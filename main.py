"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import pokemon_owner as po


def main():
    print("**************************************************")
    print("                  ---------------\n                 | POKEMON FUN!! |\n                  ---------------\n") 
    user_name = str(input("-Welcome to your Pokemon adventure!! What is your name?\n"))

    # Create Owner
    player = po.PokemonOwner(user_name)
    player.create_team()

    # Menu
    print("\nBegin your journey!")
    while True:
        print("1: Poke Center\n" + "2: View Pokemon\n" + "3: Battle Stadium\n" + "4: Exit")
        user_input = int(input())

        if (user_input == 1):
            pass
        elif (user_input == 2):
            player.display_team()
        elif (user_input == 3):
            pass
        elif (user_input == 0):
            exit()
        else:
            print("Please enter a valid input!")

main()