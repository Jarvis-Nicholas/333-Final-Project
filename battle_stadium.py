"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

# Battle Stadium Utility Functions

def play_round(player1, player2, battle_choice):

    # Attack
    if (battle_choice == 1):
        # Find first alive pokemon
        # Pokemon Attack
        health_loss: int = player1.team[get_index(player1)].attack()
        player2.team[get_index(player2)].lose_health(health_loss)

        # Display Health
        print("\n" + player2.name + " Team:")
        player2.display_team()
    elif (battle_choice == 2):
        return True

    return check_game_over(player1, player2)

# Check player who is getting attacked if their team is dead
def check_game_over(attacking_owner, victim_owner):
    # Victim died
    if (victim_owner.team_is_dead()):

        # Change stats
        attacking_owner.increase_wins()
        victim_owner.increase_losses()

        # End loop boolean
        return True
    return False

# Doesn't execute unless teams are still alive (selection in main.py)
def get_index(owner):
    index: int = 0
    for i in range (0, len(owner.team)):
        if (owner.team[i].is_dead() is False):
            return i
    return index