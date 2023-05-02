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
    print("                  ---------------\n                 | POKEMON FUN!! |") 
    print("                  ---------------\n")
    user_name = str(input("-Welcome to your Pokemon adventure!! What is your name?\n"))

    # Create trainer
    player = pt.PokemonTrainer(user_name)
    player.create_team()

    # Create Rival
    rival = pt.PokemonTrainer("Gary")
    rival.create_team()

    # Create Poke Center
    center = pc.PokemonCenter()

    # Make large inventory
    center.create_team()
    center.create_team()

    # Menu
    print("\nBegin your journey!")
    
    while True:
        print("\n1: View Pokemon\n" + "2: Poke Center\n", end="")
        print("3: Battle Stadium\n" + "4: Exit")
        user_input = int(input())

        if (user_input == 1):
            player.display_team()

            # Swap choice
            print("Switch Pokemon around?\n" +  "Yes: 1\n" +  "No: 2  ")
            switch_choice = int(input())

            if(switch_choice == 1):
                # Get input
                switch_input1 = int(input("First Pokemon "))
                switch_input2 = int(input("Second Pokemon "))

                # Make swap
                player.swap_pokemon_team_members(switch_input1 - 1, switch_input2 - 1)
                player.display_team()
        elif (user_input == 2):
                while True:
                    center.display_team()
                    
                    # Get input
                    print("\n1: Buy Pokemon\n" + "2: Sell Pokemon\n", end ="")
                    print("3: Trade Pokemon\n" + "4: Exit")
                    center_input = int(input())
                    
                    
                    # Buy
                    if (center_input == 1 ):
                        buy_input = int(input("Which Pokemon would you like to buy?  ")) - 1
                        
                        # Remove from center and give to trainer
                        center.give_pokemon(buy_input + 1, player)

                    # Trade or sell BUT inventory is empty
                    elif (center_input != 1 and len(center.team) == 0):
                        print("We are all out of Pokemon! ", end= "")
                        print("Please come back another time or sell us Pokemon!")
                    
                    # Sell
                    elif (center_input == 2):
                        sell_input = int(input("Which Pokemon would you like to sell?  ")) - 1

                        # Remove from trainer and give to center 
                        center.take_pokemon(sell_input + 1, player)

                    # Trade
                    elif (center_input == 3):
                        trade_input1 = int(input("Your Pokemon "))
                        trade_input2 = int(input("Center Pokemon "))

                        # Trade
                        center.trade_pokemon(trade_input1 + 1, trade_input2 + 1, player)
                    else:
                        break
        elif (user_input == 3):


            if (player.team_is_dead()):
                print("All your Pokemon are DEAD!! Please visit the Research Lab ASAP!!!")
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