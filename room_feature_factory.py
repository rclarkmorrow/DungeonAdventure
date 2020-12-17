from random import choice

from healing_potion import HealingPotion
from vision_potion import VisionPotion
from obstacle import Obstacle

# Configuration
HEALING_POTION = 20   # 5 - 15 per rubric
OBSTACLE_DAMAGE = 50  # 1 - 20 per rubric
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
    def create_healing_potion(hit_points=HEALING_POTION):
        return HealingPotion(hit_points)

    @staticmethod
    def create_vision_potion():
        return VisionPotion()

    @staticmethod
    def create_obstacle(hit_points=OBSTACLE_DAMAGE):
        name, effect = choice(list(OBSTACLES.items()))
        return Obstacle(name, effect, hit_points)
