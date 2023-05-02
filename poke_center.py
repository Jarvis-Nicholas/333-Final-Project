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
            trainer.add_pokemon(self.team[input_index - 1])

            # Remove from poke center
            self.team.remove_pokemon(self.team[input_index - 1])


    def take_pokemon(self, input_index, trainer):
        # In sizing
        #if (input_index >= 0 and input_index <= len(self.team)):
        if (self.index_in_range(input_index - 1)):
            # Add to center
            self.team.add_pokemon(trainer.team[input_index - 1])

            # Remove from trainer
            trainer.remove_pokemon(trainer.team[input_index])

    def trade_pokemon(self, trainer_index, center_index, trainer):
        # In sizing
        #if ((trainer_index >= 0 and trainer_index <= len(trainer.team) - 1) and (center_index >= 0 and center_index <= len(self.team) - 1)):
        if (trainer.index_is_in_range(trainer_index) and self.index_in_range(center_index)): 
            trainer.team[trainer_index - 1], self.team[center_index - 1] = self.team[center_index - 1], trainer.team[trainer_index - 1]
            """
def rename_pokemon(pokemon, new_name: str):
    pokemon.name = new_name
"""