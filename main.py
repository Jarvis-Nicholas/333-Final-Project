"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

# coverage run -m unittest discover
# coverage report


import pokemon_trainer as pt
import battle_stadium as bs
import poke_center as pc

def main():
    print("**************************************************")
    print("                  ---------------\n                 | POKEMON FUN!! |\n                  ---------------\n") 
    user_name = str(input("-Welcome to your Pokemon adventure!! What is your name?\n"))

    # Create trainer
    player = pt.PokemonTrainer(user_name)
    player.create_team()

    # Create Rival
    rival = pt.PokemonTrainer("Gary")
    rival.create_team()

    # Create Poke Center
    center = pc.PokemonCenter()
    center.create_inventory()


    # Menu
    print("\nBegin your journey!")
    
    while True:
        print("1: View Pokemon\n" + "2: Poke Center\n" + "3: Battle Stadium\n" + "4: Exit")
        user_input = int(input())

        if (user_input == 1):
            player.display_team()
            switch_choice = int(input("Switch Pokemon around?  Yes:1  No: 2  "))
            if(switch_choice == 1):
                switch_input1 = int(input("Which Pokemon would you like to switch? "))
                switch_input2 = int(input("Who do you want to switch with? "))
                player.swap_pokemon_team_members(switch_input1 - 1, switch_input2 - 1)
                player.display_team()
        elif (user_input == 2):
            if (len(center.inventory) == 0):
                print("We are all out of Pokemon! Please come back another time!")
            else:
                center.display_inventory()
                center_input = int("Buy Pokemon: 1  Sell Pokemon: 2  Trade Pokemon: 3  ")
                if (center_input == 1 and len(center.inventory) != 1):
                    input = int("Which Pokemon would you like to buy?  ")

                elif (center_input == 2):

                        input = int("")
        elif (user_input == 3):


            if (player.team_is_dead()):
                print("All your Pokemon are DEAD!! Please visit the Poke Center ASAP!!!")
                exit()

            # First round
            player1 = player
            player2 = rival
            game_over = False
            """
            while game_over == False:
                    # Dont want to get index unless sure that team has atleast 1 Pokemon alive
                    if (player)

                # Play with alive Pokemon
                player_index = bs.get_index(player)
                rival_index = bs.get_index(rival)
            """

            # Heal rival
            
        elif (user_input == 4):
            exit()
        
        else:
            print("Please enter a valid input!\n")
    
main()