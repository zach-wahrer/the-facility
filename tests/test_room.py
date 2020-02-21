"""Testing for the Room class."""

from models.game_map import GameMap
from models.room import Room
from tests.test_configs.test_config1 import ROOM_BLUEPRINTS
import unittest


class TestRoom(unittest.TestCase):

    def test_room_name(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        self.assertEqual(test_map.location['Kitchen'].get_name(), 'Kitchen')

    def test_room_desc(self):
        test_desc = GameMap(ROOM_BLUEPRINTS).location['Kitchen'].get_description()
        description = 'A dank and dirty room buzzing with flies.'
        self.assertEqual(test_desc, description)

    def test_door_linking_kitchen(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        direction, room = 'south', 'Dining Hall'
        self.assertEqual(test_map.location['Kitchen'].linked_rooms[direction], room)
        direction, room = 'down', 'Dungeon'
        self.assertEqual(test_map.location['Kitchen'].linked_rooms[direction], room)

    def test_door_linking_dungeon(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        direction, room = 'up', 'Kitchen'
        self.assertEqual(test_map.location['Dungeon'].linked_rooms[direction], room)
