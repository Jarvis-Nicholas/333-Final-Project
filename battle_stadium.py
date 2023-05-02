"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

# Battle Stadium Utility Fucntions
 



def play_round(player1, player2):
    # Get input
    print("\n1: Attack\n" + "2:Exit")
    battle_choice = int(input)

    # Attack
    if (battle_choice == 1):
        # Find first alive pokemon
        #alive_index = bs.get_index(player1)

        # Pokemon Attack
        player2.team[get_index(player2)].decrease_health(player1.team[get_index(player1)].attack())
    elif (battle_choice == 2):
        return True

    return check_game_over(player1, player2)

# Check player who is getting attacked if their team is dead
# Integrate 2
def check_game_over(attacking_owner, victim_owner):
    # Victim died
    if (victim_owner.team_is_dead()):

        # Change stats
        attacking_owner.wins = attacking_owner.wins + 1
        victim_owner.losses = victim_owner.losses + 1

        # End loop boolean
        return True
    return False

# Doesn't execute unless teams are still alive (selection in main.py)
def get_index(owner):
    index = 0
    for i in range (0, len(owner.team)):
        if (owner.team[i].is_dead() == False):
            index = i
    return index