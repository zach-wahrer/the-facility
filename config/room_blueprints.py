ROOM_BLUEPRINTS = [
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

START_LOCATION = 'Ballroom'
