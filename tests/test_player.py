"""Testing for the Player class."""

from models.player import Player
from models.game_map import GameMap
from tests.test_configs.test_config1 import ROOM_BLUEPRINTS
import unittest


class TestPlayer(unittest.TestCase):

    def test_name(self):
        self.assertEqual(Player("Buzz", None).get_name(), "Buzz")

    def test_start_loc(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        explorer = Player("Buzz", test_map.location['Dungeon'])
        self.assertEqual(explorer._location, test_map.location['Dungeon'])

    def test_move_valid(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        explorer = Player("Buzz", test_map.location['Kitchen'])
        explorer.move("down", test_map)
        self.assertEqual(explorer._location, test_map.location['Dungeon'])

    def test_move_invalid(self):
        test_map = GameMap(ROOM_BLUEPRINTS)
        explorer = Player("Buzz", test_map.location['Kitchen'])
        explorer.move("north", test_map)
        self.assertEqual(explorer._location, test_map.location['Kitchen'])
