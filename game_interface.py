from game_controller import GameController

WELCOME = ('Welcome to the Dungeon, it\'s got fun and games.')


class GameInterface:
    @staticmethod
    def init_game(play_game: bool):
        if play_game:
            print(WELCOME)
            adventurer_name = str(input('Enter your adventurer\'s name or'
                                        ' press enter for a default name'
                                        ' >>> '))
            GameInterface.__play_game(adventurer_name)
        else:
            print('Thank you for playing. See you next time!')

    @staticmethod
    def __play_game(adventurer_name):
        game = GameController(adventurer_name)
        play = True
        while play:
            user_input = str(input('Enter your command (\'h\' or \'help\''
                                   ' for help) >>> '))
            result, play = game.user_input(user_input)
            print(result)
            # result, play = game.user_input(user_input)
            # print(result)
        user_input = (str(input('Enter \'y\' or \'yes\' to play again >>> '))
                      .lower())
        if user_input == 'y' or user_input == 'yes':
            GameInterface.init_game(True)
        else:
            GameInterface.init_game(False)


if __name__ == '__main__':
    GameInterface.init_game(True)