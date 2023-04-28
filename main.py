"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import pokemon_owner as po
import battle_stadium as bs

def main():
    print("**************************************************")
    print("                  ---------------\n                 | POKEMON FUN!! |\n                  ---------------\n") 
    user_name = str(input("-Welcome to your Pokemon adventure!! What is your name?\n"))

    # Create Owner
    player = po.PokemonOwner(user_name)
    player.create_team()

    # Create Rival
    rival = po.PokemonOwner("Gary")
    rival.create_team()

    # Menu
    print("\nBegin your journey!")
    while True:
        print("1: View Pokemon\n" + "2: Poke Center\n" + "3: Battle Stadium\n" + "4: Exit")
        user_input = int(input())

        if (user_input == 1):
            player.display_team()
        elif (user_input == 2):
            pass
        elif (user_input == 3):
            game_over = False
            while game_over == False:
                    # Dont want to get index unless sure that team has atleast 1 Pokemon alive
                    if (player)

                # Play with alive Pokemon
                player_index = bs.get_index(player)
                rival_index = bs.get_index(rival)
        elif (user_input == 4):
            exit()
        else:
            print("Please enter a valid input!\n")

main()