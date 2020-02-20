class Room():
    def __init__(self, name=None, description=None):
        self._name = name
        self._description = description
        self.linked_rooms = {}

    def get_name(self):
        return self._name

    def set_name(self, room_name):
        self._name = room_name

    def get_description(self):
        return self._description

    def set_description(self, room_description):
        self._description = room_description

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def describe(self):
        print(self.get_description())


def create_room(room, locations):
    locations[room['name']] = Room(room['name'])
    locations[room['name']].set_description(room['desc'])
    locations[room['name']].link_room(room['door']['room'],
                                      room['door']['direction'])
