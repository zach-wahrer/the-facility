from models.room import Room


class GameMap():

    def __init__(self, room_blueprints):
        self.location = {}
        self.initialize_rooms(room_blueprints)

    def initialize_rooms(self, room_blueprints):
        for room in room_blueprints:
            self.location[room['name']] = self.create_room(room['name'],
                                                           room['desc'])
            self.create_doors(self.location[room['name']], room['doors'])

    def create_room(self, name: str, desc: str) -> Room:
        new_room = Room(name)
        new_room.set_description(desc)
        return new_room

    def create_doors(self, from_room, doors):
        for door in doors:
            from_room.link_room(door['room'], door['direction'])
