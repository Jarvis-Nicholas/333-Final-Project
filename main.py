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
import research_lab as rl

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
        print("3: Battle Stadium\n" +  "4: Lab  " + "5: Exit")
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
                        print("Which Pokemon would you like to buy?  ")
                        buy_input = int(input) - 1
                        # Remove from center and give to trainer
                        center.give_pokemon(buy_input + 1, player)

                    # Trade or sell BUT inventory is empty
                    elif (center_input != 1 and len(center.team) == 0):
                        print("We are all out of Pokemon! ", end= "")
                        print("Please come back another time or sell us Pokemon!")
                    
                    # Sell
                    elif (center_input == 2):
                        print("Which Pokemon would you like to sell?  ")
                        sell_input = int(input) - 1

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
            # Heal rival
            rl.heal_team(rival)

            # All dead
            if (player.team_is_dead()):
                print("All your Pokemon are DEAD! Please visit the Research Lab ASAP!")
            else:

                # First round
                player1 = player
                player2 = rival
                game_over = False
                
                while game_over is False:
                    # Get input
                    print("\n1: Attack\n" + "2:Exit")
                    battle_choice = int(input)

                    game_over = bs.play_round(player1, player2, battle_choice)
                    #game_over = bs.check_game_over(player1, player2)

                    # Swap turns
                    if (game_over is False):
                        # Temp variables
                        temp_trainer = pt.PokemonTrainer("temp")
                        temp_trainer = player1

                        player1 = player2
                        player2 = temp_trainer
                
        elif (user_input == 4):
            # Get input
            print("\n1: Heal Team\n" + "2: Change Pokemon name\n", end ="")
            print("3: Change Pokemon Type\n" + "4: Change Pokemon Health\n", end="")
            print("5: Change Pokemon Max Health\n" + "6: Exit")
            lab_input = int(input())
            
            if (lab_input == 1):
                rl.heal_team(player)

            elif (lab_input == 2):
                # Get input
                print("Which Pokemon would you like to rename?  ")
                index = int(input) - 1

                print("What is their new name?  ")
                choice = str(input)  

                # Rename
                rl.change_pokemon_name(player, index, choice)              
            
            elif (lab_input == 3):
                # Get input
                print("Which Pokemon would you like to change type?  ")
                index = int(input) - 1

                print("What is their new type?  ")
                choice = str(input)  

                # Rename
                rl.change_pokemon_type(player, index, choice)                   
            elif (lab_input == 4):
                # Get input
                print("Which Pokemon would you like to change health?  ")
                index = int(input) - 1

                print("What is their new health?  ")
                choice = int(input)  

                # Rename
                rl.change_pokemon_health(player, index, choice)                 
            elif (lab_input == 5):
                # Get input
                print("Which Pokemon would you like to change max health?  ")
                index = int(input) - 1

                print("What is their new max health?  ")
                choice = int(input)  

                # Rename
                rl.change_pokemon_max_health(player, index, choice)                  
            elif (lab_input == 6):
                break
                
                                                                  
        elif (user_input == 5):
            exit()
        
        else:
            print("Please enter a valid input!\n")
    
main()