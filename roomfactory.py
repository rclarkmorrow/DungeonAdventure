import random
from roomfeature import RoomFeature
from healing_potion import HealthPotion
from vision_potion import VisionPotion
from pit import Pit
from roomfactory import RoomFactory


class RoomFactory():

    @staticmethod
    def place_health(room):
        """
        Places Health potion in the room at 10% chance
        """
        if random.ranint(0, 100) < 10:
            room.add_items(HealingPotion())
            room.add_features(HealingPotion())

    @staticmethod
    def place_vision(room):
        """
        Places vision potion in the room at 10% chance
        """
        if random.ranint(0, 100) < 10:
            room.add_items(VisionPotion())
            room.add_features(VisionPotion())

    @staticmethod
    def place_obstacle(room):
        """
        Places obstacle in the room at 10% chance
        """
        if random.ranint(0, 100) < 10:
            room.add_obstacles(Obstacle())
            room.add_features(Obstacle())
