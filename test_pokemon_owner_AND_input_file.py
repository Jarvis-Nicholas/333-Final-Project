"""
Author: Nicholas Jarvis
CS 333 Final Project: Pokemon
Date: 4/25/2023
"""
# Command line executables:
# python3 -m coverage run test_pokemon_owner_AND_input_file.py -v -b
# python3 -m coverage report 

import unittest
from unittest.mock import patch, mock_open
import pokemon_owner as po

# Integration
class testPokemonOwnerANDInputFile(unittest.TestCase):
    def setUp(self):
        owner = po.PokemonOwner()
    """
    def test_create_team(self):
        file_content_mock = "Bulbasaur Grass 95"
        file_path = ''
    
    def test_create_team(self):
        # Tests opening the input file in read mode
        with patch('__main__.open', mock_open(read_data='bibble')) as m:
            with open('pokemon_list.txt') as h:
                result = h.read()

        m.assert_called_once_with('pokemon_list.txt')
        assert result == 'bibble'

    """
if __name__ == '__main__':
    unittest.main()