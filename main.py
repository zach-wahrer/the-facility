from helpers.room import Room, create_room


def main():
    room_blueprints = [
        {'name': 'Kitchen',
         'desc': 'A dank and dirty room buzzing with flies.',
         'doors': [{'direction': 'south', 'room': 'Dining Hall'}]
         },
        {'name': 'Ballroom',
         'desc': 'An elegant space that has obviously seen better days.',
         'doors': [{'direction': 'east', 'room': 'Dining Hall'}]
         },
        {'name': 'Dining Hall',
         'desc': 'Broken and mismatched chairs sit around a dusty table.',
         'doors': [{'direction': 'west', 'room': 'Ballroom'},
                   {'direction': 'north', 'room': 'Kitchen'}]
         }
    ]

    locations = {}

    for room in room_blueprints:
        create_room(room, locations)

    locations["Dining Hall"].get_details()


if __name__ == "__main__":
    main()
