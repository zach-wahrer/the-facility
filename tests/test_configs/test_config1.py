ROOM_BLUEPRINTS = [
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

START_LOCATION = 'Dungeon'

STORY_BLUEPRINTS = ['I ran out of the house.', 'I forgot to lock the door.']
