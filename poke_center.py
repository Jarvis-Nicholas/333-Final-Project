"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""

import pokemon_trainer as pt
import pokemon_owner as po

class PokemonCenter (po.PokemonOwner):

    def give_pokemon(self, input_index, trainer):
        # In sizing
        if (self.index_in_range(input_index)):
            # Add to trainer
            trainer.add_pokemon(self.team[input_index - 1])

            # Remove from poke center
            self.remove_pokemon(self.team[input_index - 1])

    def take_pokemon(self, input_index, trainer):
        # In sizing
        if (self.index_in_range(input_index)):
            # Add to center
            self.add_pokemon(trainer.team[input_index - 1])

            # Remove from trainer
            trainer.remove_pokemon(trainer.team[input_index - 1])

    def trade_pokemon(self, trainer_index, center_index, trainer):
        # In sizing
        if ((trainer.index_in_range(trainer_index))
            and (self.index_in_range(center_index))): 

            # Temp
            temp_trainer = pt.PokemonTrainer("temp")
            temp_trainer.add_pokemon(trainer.team[trainer_index - 1])

            #Swap
            trainer.team[trainer_index - 1] = self.team[center_index - 1]
            self.team[center_index - 1] = temp_trainer.team[0] 