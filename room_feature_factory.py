from random import choice, randint
from factory import Factory
from healing_potion import HealingPotion
from vision_potion import VisionPotion
from obstacle import Obstacle

# Configuration
HEALING_POTION = randint(5, 15)   # 5 - 15 per rubric
OBSTACLE_DAMAGE = randint(1, 20)  # 1 - 20 per rubric
OBSTACLES = {
  'Pit': 'You fall into a pit filled with spikes.',

  'Trip-wire': ('You trip a trip wire and are shot with a'
                ' baker\'s dozen arrows.'),

  'Quicksand': 'You fell into a quicksand and are trapped.',
}


class RoomFeatureFactory:
    """
      This factory creates items an adventurer might run into or use.
    """
    @staticmethod
    def create_healing_potion(heal_points=HEALING_POTION):
        """
          Creates and returns a healing potion object.
          :: takes an HP as argument.
        """
        return HealingPotion(Factory.to_integer(heal_points))

    @staticmethod
    def create_vision_potion():
        """
        Creates and returns a vision object.
        """
        return VisionPotion()

    @staticmethod
    def create_obstacle(damage_points=OBSTACLE_DAMAGE):
        """
        Creates and returns an obstacle object.
        :: takes damage point as argument.
        """
        name, effect = choice(list(OBSTACLES.items()))
        return Obstacle(name, effect, Factory.to_integer(damage_points))
