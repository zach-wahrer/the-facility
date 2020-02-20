"""Testing for the Player class."""

from models.player import Player
from models.room import Room, create_room
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
        locations = {}
        for room in room_blueprints:
            create_room(room, locations)
        explorer = Player("Buzz", locations['Dungeon'])
        self.assertEqual(explorer._location, locations['Dungeon'])

    def test_move(self):
        locations = {}
        for room in room_blueprints:
            create_room(room, locations)
        explorer = Player("Buzz", locations['Kitchen'])
        explorer.move("down", locations)
        self.assertEqual(explorer._location, locations['Dungeon'])
