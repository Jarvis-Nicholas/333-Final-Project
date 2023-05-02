"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon as pk
import pokemon_owner as po

# Battle Stadium Utility Fucntions

   
# Integration 1    
def swap_pokemon(owner, current_index, swap_index):
    # Swap
    owner.team[swap_index], owner.team[current_index] = owner.team[current_index], owner.team[swap_index]

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
# Integration 3
def get_index(owner):
    index = 0
    for i in range (0, len(owner.team)):
        if (owner.team[i].is_dead() == False):
            index = i
    return index