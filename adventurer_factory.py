from random import randint, choice
from adventurer import Adventurer

# Configuration
MIN_HP = 50
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
    def create_adventurer(game, name=choice(DEFAULT_NAMES)):
        return Adventurer(game, name, randint(MIN_HP, MAX_HP))
