from config.room_blueprints import ROOM_BLUEPRINTS, START_LOCATION
from config.npc_config import NPC_CONFIG
from models.game_map import GameMap
from models.npc import Enemy, Friend
from models.npc_controller import NPCController
from models.player import Player


class Game():
    def __init__(self, rooms=ROOM_BLUEPRINTS, start=START_LOCATION):
        self._gm = GameMap(rooms)
        self._player = None
        self._player_start_location = start
        self._npc_controller = NPCController()

    def start(self):
        self.generate_NPCs()
        self.setup_player()
        self.greet_player()
        self.player_exploring()
        exit()

    def player_exploring(self):
        while True:
            print("\n")
            self.describe_room()
            self.ask_and_execute_command()

    def generate_NPCs(self):
        for npc in NPC_CONFIG:
            if npc['type'] == 'enemy':
                self._npc_controller.add_npc(npc['name'], Enemy(npc['name'],
                                                                npc['description']))
            else:
                self._npc_controller.add_npc(npc['name'], Friend(npc['name'],
                                                                 npc['description']))
            self.randomize_character_location(self._npc_controller.get_npc(npc['name']))

    def randomize_character_location(self, character):
        character.set_location(self._gm.get_random_location())

    def setup_player(self):
        self._player = Player(self.ask_for_name(),
                              self._gm.location[self._player_start_location])

    def ask_and_execute_command(self):
        print("What would you like to do?")
        command = input("> ").lower()
        self.run_command(command)

    def run_command(self, command):
        move_directions = ['north', 'south', 'east', 'west', 'up', 'down']
        quit_commands = ['exit', 'quit']

        if command in move_directions:
            self._player.move(command, self._gm)

        elif command in quit_commands:
            self.print_quit_confirmation()
        else:
            print("\nCommand not recognized. Please try again.")

    def print_quit_confirmation(self):
        confirm = input("\nAre you sure you want to quit? ").lower()
        if confirm == 'y' or confirm == 'yes':
            print(f"Thanks for playing, {self._player.get_name()}!")
            quit()

    def ask_for_name(self):
        return input('Please enter your name: ')

    def greet_player(self):
        print(f"\nHello {self._player.get_name()}.")

    def describe_room(self):
        location = self._player.get_location()
        return location.get_details()
