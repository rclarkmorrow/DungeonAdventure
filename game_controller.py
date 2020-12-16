from healing_potion import HealingPotion
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
        self.__dungeon = Dungeon()
        self.__adventurer = (AdventurerFactory
                             .create_adventurer(adventurer_name))
        self.__current_room = None
        print(self.__dungeon)

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
                self.__current_room = self.__dungeon.update_adv_pos(-1, 0)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return 'You cannot go north here.', True
            elif user_input == 's' or user_input == 'south':
                # Do move south
                self.__current_room = self.__dungeon.update_adv_pos(1, 0)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return 'You cannot go south here.', True
            elif user_input == 'e' or user_input == 'east':
                # Do move east
                self.__current_room = self.__dungeon.update_adv_pos(0, 1)
                if self.__current_room:
                    return self.__enter_room()
                else:
                    return 'You cannot go east here.', True
            elif user_input == 'w' or user_input == 'west':
                # Do move west
                self.__current_room = self.__dungeon.update_adv_pos(0, -1)
                if self.__current_room:
                   return self.__enter_room()
                else:
                    return 'You cannot go west here.', True

            # Status commands
            elif user_input == 'i' or user_input == 'info':
                # Show adventurer status
                return str(self.__adventurer), True
            elif user_input == 'r' or user_input == 'room':
                # Show room
                return self.__dungeon.display_curr_room(), True

            # Use item commands
            elif user_input == 'p' or user_input == 'potion':
                result = self.__adventurer.use_healing_potion()
                if result:
                    return result.effect, True
                else:
                    return 'You do not have any healing potions', True

            elif user_input == 'v' or user_input == 'vision':
                # Do vision
                result = self.__adventurer.use_vision_potion()
                if result:
                    map_string = result.effect
                    map_dictionary = self.__dungeon.use_vision_potion()
                    for key, value in map_dictionary.items():
                        map_string += f'\n{key}:\n{value}'
                    return map_string, True
                else:
                    return 'You do not have any vision potions', True
                # for key,value in d.items():
                #     print(key, ":\n", value)

            # Game commands
            elif user_input == 'h' or user_input == 'help':
                return INPUT_HELP, True
            elif user_input == 'q' or user_input == 'quit':
                # Exit the dungeon
                return 'Exiting the dungeon', False
            else:
                return 'Something went wrong', True
        else:
            return f'{user_input} is not a valid command.', True

    def __enter_room(self):
        print("WE ARE IN A ROOM!")
        print(self.__current_room.features)
        room_string = ''
        if not self.__current_room.features:
            print("EMPTY ROOM")
            room_string += 'There is nothing in this room!'
        for feature in self.__current_room.features:
            if feature.category == 'Item':
                print("ROOM HAS ITEM")
                print(feature.name)
                print(feature.effect)
                self.__adventurer.add_item(feature)
                room_string += f'You have picked up a {feature.name}\n'
                self.__current_room.remove_feature(feature)
            if feature.category == 'Obstacle':
                print("ROOM HAS OBSTACLE")
                self.__adventurer.encounter_obstacle(feature)
                room_string += f'{feature.effect}\n'
                print('Room string!')
            else:
                room_string += 'There is nothing in this room!'
        if self.__adventurer.hit_points < 1:
            room_string += 'Oh noes, you have died! :\'('
            return room_string, False
        print("BEFORE RETURN")
        play = True
        # print(room_string, True)
        return room_string, play
