import unittest
from dungeon_adventure_controller import DungeonAdventureController
from adventurer_factory import DEFAULT_NAMES

ADVENTURER_NAME = 'Tom'
GAME_COMMANDS = ['n', 'North',
                 's', 'South',
                 'e', 'East',
                 'w', 'West',
                 'i', 'Info',
                 'R', 'Room',
                 'm', 'Map',
                 'p', 'Potion'
                 'V', 'Vision'
                 'c', 'Cheat'
]
CHEAT_COMMANDS = ['t', 'Treasure',
                  'g', 'god',
                  'u', 'Unveil']


class ControllerTests(unittest.TestCase):
    """ These are unittests for the Dungeon Adventure Controller class. """

    """--------------------------------------------------#
    # Tests for Game Creation
    #--------------------------------------------------"""

    def test_create_game_with_name(self):
        """ Create a dungeon adventure with dungeon adventurer name """
        game = DungeonAdventureController(ADVENTURER_NAME)
        adventurer_info, play = game.user_input('i')
        self.assertTrue(game, 'a game should be created')
        self.assertTrue(play, 'should be true')
        self.assertTrue(ADVENTURER_NAME in adventurer_info,
                        'name should be set')

    def test_create_game_with_default_name(self):
        """ Create a dungeon adventure with dungeon adventurer name """
        game = DungeonAdventureController(None)
        adventurer_info, play = game.user_input('i')
        is_default = False
        for name in DEFAULT_NAMES:
            if name in adventurer_info:
                is_default = True
                break
        self.assertTrue(game, 'a game should be created')
        self.assertTrue(play, 'should be true')
        self.assertTrue(is_default, 'should have default name')

    def test_create_game_without_name(self):
        """ Create a dungeon adventure with no argument passed """
        try:
            game = DungeonAdventureController()
            adventurer_info, play = game.user_input('i')
            self.assertEqual(True, False, 'should not have got here,'
                             ' game should not start without argument.')
        except TypeError:
            self.assertEqual(True, True)

    """--------------------------------------------------#
    # Tests for User Input
    #--------------------------------------------------"""

    def test_game_commands_valid(self):
        game = DungeonAdventureController(ADVENTURER_NAME)
        passed = True
        for command in GAME_COMMANDS:
            response, play = game.user_input(command)
            if not isinstance(response, str) or not play:
                passed = False
        self.assertTrue(game, 'a game should be created')
        self.assertTrue(play, 'should be true')
        self.assertTrue(passed, 'all commands should pass loop')

    def test_game_command_cheat_toggle(self):
        game = DungeonAdventureController(ADVENTURER_NAME)
        passed = True
        game.user_input('c')
        for command in CHEAT_COMMANDS:
            response, play = game.user_input(command)
            if not isinstance(response, str) or not play:
                passed = False
        self.assertTrue(game, 'a game should be created')
        self.assertTrue(play, 'should be true')
        self.assertTrue(passed, 'all cheat commands should pass loop')

    def test_game_command_quit(self):
        game = DungeonAdventureController(ADVENTURER_NAME)
        response, play = game.user_input('q')
        self.assertTrue(game, 'a game should be created')
        self.assertFalse(play, 'should be true')



if __name__ == '__main__':
    unittest.main()
