from dungeon_adventure_controller import DungeonAdventureController

WELCOME = ('Welcome to the Dungeon, it\'s got fun and games.')
INTRO = ('\nYou descend a staircase into the dungeon of objects.'
         '\nThe door slams closed behind you.\nTo escape you'
         ' must find the four treasures that conquer\nobjects'
         ' and reach the exit.\nGOOD LUCK!')


class DungeonAdventure:
    @staticmethod
    def init_game(play_game: bool):
        if play_game:
            print(WELCOME)
            adventurer_name = str(input('\nEnter your adventurer\'s name or'
                                        ' press enter for a default name'
                                        ' >>> '))

            DungeonAdventure.__play_game(adventurer_name)
        else:
            print('Thank you for playing. See you next time!')

    @staticmethod
    def __play_game(adventurer_name):
        game = DungeonAdventureController(adventurer_name)
        play = True
        print(INTRO)
        while play:
            user_input = str(input('\nEnter your command (\'h\' or \'help\''
                                   ' for help) >>> '))
            result, play = game.user_input(user_input)
            print(f'\n{result}')
            # result, play = game.user_input(user_input)
            # print(result)
        user_input = (str(input('\nEnter \'y\' or \'yes\' to play again >>> '))
                      .lower())
        if user_input == 'y' or user_input == 'yes':
            DungeonAdventure.init_game(True)
        else:
            DungeonAdventure.init_game(False)


if __name__ == '__main__':
    DungeonAdventure.init_game(True)
