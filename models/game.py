from config.room_blueprints import ROOM_BLUEPRINTS, START_LOCATION
from models.game_map import GameMap
from models.player import Player


class Game():
    def __init__(self):
        self._gm = GameMap(ROOM_BLUEPRINTS)
        self._player = None
        self._player_start_location = START_LOCATION

    def start(self):
        self.setup_player()
        self.greet_player()
        self.player_exploring()
        exit()

    def player_exploring(self):
        while True:
            print("\n")
            self.describe_room()
            self.ask_and_execute_command()

    def setup_player(self):
        self._player = Player(self.ask_for_name(),
                              self._gm.location[self._player_start_location])

    def ask_and_execute_command(self):
        print("What would you like to do?")
        command = input("> ").lower()
        self._player.move(command, self._gm)

    def ask_for_name(self):
        return input('Please enter your name: ')

    def greet_player(self):
        print(f"\nHello {self._player.get_name()}.")

    def describe_room(self):
        location = self._player.get_location()
        return location.get_details()
