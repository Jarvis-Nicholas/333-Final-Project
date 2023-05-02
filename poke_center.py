"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon_owner as po

class PokemonCenter (po.PokemonOwner):

    def heal_team(owner):
        for i in range (0, len(owner.team)):
            owner.team[i].health = owner.team[i].max_health



  

    def give_pokemon(self, input_index, trainer):
        # In sizing
        #if (input_index >= 0 and input_index <= len(self.team)):
        if (self.index_in_range(input_index)):
            # Add to trainer
            trainer.team.add_pokemon(self.team[input_index])

            # Remove from poke center
            self.team.remove_pokemon(self.team[input_index])


    def take_pokemon(self, input_index, trainer):
        # In sizing
        #if (input_index >= 0 and input_index <= len(self.team)):
        if (self.index_in_range(input_index)):
            # Add to center
            self.team.add_pokemon(trainer.team[input_index])

            # Remove from trainer
            trainer.remove_pokemon(trainer.team[input_index])

    def trade_pokemon(self, trainer_index, center_index, trainer):
        # In sizing
        #if ((trainer_index >= 0 and trainer_index <= len(trainer.team) - 1) and (center_index >= 0 and center_index <= len(self.team) - 1)):
        if (trainer.index_is_in_range(trainer_index) and self.index_in_range(center_index)): 
            trainer.team[trainer_index], self.team[center_index] = self.team[center_index], trainer.team[trainer_index]
            """
def rename_pokemon(pokemon, new_name: str):
    pokemon.name = new_name
"""