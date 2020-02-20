class Player():
    def __init__(self, name, start_location):
        self._name = name
        self._location = start_location

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def move(self, to_location, game_map):
        if to_location in self._location.linked_rooms:
            self._location = game_map.location[self._location.linked_rooms[to_location]]
        else:
            print("\nThere is no door in that direction.")
        return self._location
