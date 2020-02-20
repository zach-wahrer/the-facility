"""Testing for the Room class."""

from helpers.room import Room, create_room
import unittest

room_blueprint = {'name': 'Kitchen',
                  'desc': 'A dank and dirty room buzzing with flies.',
                  'doors': [{'direction': 'South', 'room': 'Dining Hall'},
                            {'direction': 'Down', 'room': 'Dungeon'}]
                  }


class TestRoom(unittest.TestCase):

    def test_room_name(self):
        location = {}
        create_room(room_blueprint, location)
        self.assertEqual(location['Kitchen'].get_name(), 'Kitchen')

    def test_room_desc(self):
        location = {}
        create_room(room_blueprint, location)
        description = 'A dank and dirty room buzzing with flies.'
        self.assertEqual(location['Kitchen'].get_description(), description)

    def test_door_linking(self):
        location = {}
        create_room(room_blueprint, location)
        direction = 'South'
        room = 'Dining Hall'
        self.assertEqual(location['Kitchen'].linked_rooms[direction], room)
        direction = 'Down'
        room = 'Dungeon'
        self.assertEqual(location['Kitchen'].linked_rooms[direction], room)


if __name__ == "__main__":
    unittest.main()