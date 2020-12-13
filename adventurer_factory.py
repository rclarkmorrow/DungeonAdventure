from random import randint, choice
from adventurer import Adventurer

# Configuration
MIN_HP = 75
MAX_HP = 100
DEFAULT_NAMES = [
    'Brunhilda',
    'Mighty Thor',
    'Leonidas',
    'Boudica'
]


# Factory
class AdventurerFactory:
    @staticmethod
    def to_integer(number):
        if int(str(number)):
            return int(str(number))
        else:
            raise ValueError('value must be an integer or convertable to'
                             ' an integer')

    @staticmethod
    def is_string(some_input):
        if isinstance(some_input, str):
            return some_input
        else:
            raise ValueError('value must be a string')

    @staticmethod
    def create_adventurer(name=choice(DEFAULT_NAMES),
                          hit_points=randint(MIN_HP, MAX_HP)):
        return Adventurer(AdventurerFactory.is_string(name),
                          AdventurerFactory.to_integer(hit_points))
