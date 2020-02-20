"""Testing for the GameMap class."""

from models.game_map import GameMap
from models.room import Room
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


class TestMap(unittest.TestCase):

    def test_creating_rooms(self):
        test_map = GameMap(room_blueprints)
        self.assertEqual(test_map.location['Kitchen'].get_name(), 'Kitchen')
        self.assertEqual(test_map.location['Dungeon'].get_name(), 'Dungeon')
