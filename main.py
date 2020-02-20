from models.room import Room, create_room
from models.player import Player


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

    player_name = input('Please enter your name: ')
    current_room = locations['Ballroom']
    explorer = Player(player_name, current_room)

    print(f"\nHello {explorer.get_name()}.")

    while True:
        print("\n")
        current_room.get_details()
        print("What would you like to do?")
        command = input("> ").lower()
        current_room = explorer.move(command, locations)


if __name__ == "__main__":
    main()
