from helpers.room import Room, create_room


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


if __name__ == "__main__":
    main()
