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


def create_room(room: dict, locations: dict):
    locations[room['name']] = Room(room['name'])
    locations[room['name']].set_description(room['desc'])
    for door in room['doors']:
        create_door_to_other_room(locations[room['name']],
                                  door['room'],
                                  door['direction'])


def create_door_to_other_room(from_room: Room,
                              to_room: str,
                              in_which_direction: str):
    from_room.link_room(to_room, in_which_direction)
