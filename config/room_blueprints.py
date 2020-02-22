ROOM_BLUEPRINTS = [
    {'name': 'Airlock',
     'desc': 'A cramped space the allows you to access the rest of the ship.',
     'doors': [{'direction': 'north', 'room': 'Engine Room'}]
     },
    {'name': 'Engine Room',
     'desc': 'A large space, dark and dingy. It is full of complicated machinery and equipment.',
     'doors': [{'direction': 'south', 'room': 'Airlock'},
               {'direction': 'north', 'room': 'Bridge'}]
     },
    {'name': 'Bridge',
     'desc': 'A few run-down command chairs sit before black screens.',
     'doors': [{'direction': 'south', 'room': 'Engine Room'}]
     }
]

START_LOCATION = 'Airlock'
