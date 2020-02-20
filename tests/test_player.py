"""Testing for the Player class."""

from models.player import Player
from models.game_map import GameMap
import unittest

room_blueprints = [
    {'name': 'Kitchen',
     'desc': 'A dank and dirty room buzzing with flies.',
     'doors': [{'direction': 'south', 'room': 'Dining Hall'},
               {'direction': 'down', 'room': 'Dungeon'}]
     },
    {'name': 'Dungeon',
     'desc': 'Darkness.',
     'doors': [{'direction': 'up', 'room': 'Kitchen'}]
     }
]


class TestPlayer(unittest.TestCase):

    def test_name(self):
        self.assertEqual(Player("Buzz", None).get_name(), "Buzz")

    def test_start_loc(self):
        test_map = GameMap(room_blueprints)
        explorer = Player("Buzz", test_map.location['Dungeon'])
        self.assertEqual(explorer._location, test_map.location['Dungeon'])

    def test_move_valid(self):
        test_map = GameMap(room_blueprints)
        explorer = Player("Buzz", test_map.location['Kitchen'])
        explorer.move("down", test_map)
        self.assertEqual(explorer._location, test_map.location['Dungeon'])

    def test_move_invalid(self):
        test_map = GameMap(room_blueprints)
        explorer = Player("Buzz", test_map.location['Kitchen'])
        explorer.move("north", test_map)
        self.assertEqual(explorer._location, test_map.location['Kitchen'])
