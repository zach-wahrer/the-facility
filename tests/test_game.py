from models.game import Game
from models.game_map import GameMap
from models.player import Player
from tests.test_configs.test_config1 import ROOM_BLUEPRINTS, START_LOCATION
import unittest


class TestGame(unittest.TestCase):
    def test_game_setup_start_location(self):
        g = Game(ROOM_BLUEPRINTS, START_LOCATION)
        self.assertEqual(g._player_start_location, START_LOCATION)

    def test_game_setup_game_map(self):
        g = Game(ROOM_BLUEPRINTS, START_LOCATION)
        self.assertIsInstance(g._gm, GameMap)

    def test_setup_player(self):
        g = Game(ROOM_BLUEPRINTS, START_LOCATION)
        g.setup_player()
        self.assertIsInstance(g._player, Player)
