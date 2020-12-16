from dungeon import Dungeon
from adventurer_factory import AdventurerFactory

VALID_INPUT = [
    'n', 'north',  # move north
    's', 'south',  # move south
    'e', 'east',  # move east
    'w', 'west',  # move west
    'i', 'info',  # get adventurer status
    'r', 'room',  # show current room
    'h', 'help',  # get help
    'p', 'potion',  # use healing potion
    'v', 'vision',  # use vision potion
    'q', 'quit',  # exit the dungeon
]

INPUT_HELP = """
GAME HELP

Movement commands:
  n, north to move the character north.
  s, south to move the character south.
  e, east to move the  character east.
  w, west to move the characer west.
Status commands:
  i, info to show adventurer status.
  r, room to show the current room.
Use item commands:
  p, potion to use a healing potion.
  v, vision to use a vision potion.
Game commands:
  q, quit to leave the dungeon.
"""

class GameController:
    def __init__(self, adventurer_name=''):
        self.__dungeon = Dungeon
        self.__adventurer = (AdventurerFactory
                             .create_adventurer(adventurer_name))

    def user_input(self, user_input):
        """
          This static method determines whether a user command is
          in the list of valid input. Calls appropriate methods if so,
          returns an error message if not.
        """

        # Convert user input to lower case.
        user_input = user_input.lower()
        if user_input in VALID_INPUT:
            # Move commands
            if user_input == 'n' or user_input == 'north':
                # Do move north
                self.__dungeon.update_adv_pos(-1,0)
            elif user_input == 's' or user_input == 'south':
                # Do move south
                self.__dungeon.update_adv_pos(1,0)
            elif user_input == 'e' or user_input == 'east':
                # Do move east
                self.__dungeon.update_adv_pos(0,1)
            elif user_input == 'w' or user_input == 'west':
                # Do move west
                self.__dungeon.update_adv_pos(0,-1)

            # Status commands
            elif user_input == 'i' or user_input == 'info':
                # Show adventurer status
                print(str(self.__adventurer))
            elif user_input == 'r' or user_input == 'room':
                # Show room
                print(self.__dungeon.display_curr_room())

            # Use item commands
            elif user_input == 'p' or user_input == 'potion':
                # Use healing potion
                pass
            elif user_input == 'v' or user_input == 'vision':
                # Do vision
                self.__adventurer.remove_item('Vision Potion')
                d = self.__dungeon.use_vision_potion()
                for key,value in d.items():
                    print(key, ":\n", value)

            # Game commands
            elif user_input == 'q' or user_input == 'quit':
                # Exit the dungeon
                return 'Exiting the dungeon', False
            else:
                return 'Something went wrong', True
        else:
            return f'{user_input} is not a valid command.', True
