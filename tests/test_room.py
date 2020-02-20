"""Testing for the Room class."""

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


class TestRoom(unittest.TestCase):

    def test_room_name(self):
        test_map = GameMap(room_blueprints)
        self.assertEqual(test_map.location['Kitchen'].get_name(), 'Kitchen')

    def test_room_desc(self):
        test_desc = GameMap(room_blueprints).location['Kitchen'].get_description()
        description = 'A dank and dirty room buzzing with flies.'
        self.assertEqual(test_desc, description)

    def test_door_linking_kitchen(self):
        test_map = GameMap(room_blueprints)
        direction, room = 'south', 'Dining Hall'
        self.assertEqual(test_map.location['Kitchen'].linked_rooms[direction], room)
        direction, room = 'down', 'Dungeon'
        self.assertEqual(test_map.location['Kitchen'].linked_rooms[direction], room)

    def test_door_linking_dungeon(self):
        test_map = GameMap(room_blueprints)
        direction, room = 'up', 'Kitchen'
        self.assertEqual(test_map.location['Dungeon'].linked_rooms[direction], room)
