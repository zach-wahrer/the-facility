"""Testing for the GameMap class."""

from models.game_map import GameMap
from models.room import Room
from tests.test_configs.test_config1 import ROOM_BLUEPRINTS
import unittest


class TestMap(unittest.TestCase):

    def test_creating_rooms(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        self.assertEqual(test_map.location['Kitchen'].get_name(), 'Kitchen')
        self.assertEqual(test_map.location['Dungeon'].get_name(), 'Dungeon')
