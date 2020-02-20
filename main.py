from room import Room


def main():
    room_blueprints = [
        {'name': 'Kitchen',
         'desc': 'A dank and dirty room buzzing with flies.',
         'door': {'direction': 'South', 'room': 'Dining Hall'}},
        {'name': 'Ballroom',
         'desc': 'An elegant space that has obviously seen better days.',
         'door': {'direction': 'East', 'room': 'Dining Hall'}},
        {'name': 'Dining Hall',
         'desc': 'Broken and mismatched chairs sit around a dusty table.',
         'door': {'direction': 'West', 'room': 'Ballroom'}}
    ]

    locations = {}

    for room in room_blueprints:
        create_room(room, locations)


def create_room(room, locations):
    locations[room['name']] = Room(room['name'])
    locations[room['name']].set_description(room['desc'])
    locations[room['name']].link_room(room['door']['room'],
                                      room['door']['direction'])


if __name__ == "__main__":
    main()
