import random
from roomfeature import RoomFeature
from healing_potion import HealthPotion
from vision_potion import VisionPotion
from pit import Pit
from roomfactory import RoomFactory


class RoomFactory():

    @staticmethod
    def place_health(room):
        if random.ranint(0, 100) < 10:
            room.__healthPotion = True
            room.__items.append(HealingPotion())

    @staticmethod
    def place_vision(room):
        if random.ranint(0, 100) < 10:
            room.__visionPotion = True
            room.__items.append(VisionPotion(True))

    @staticmethod
    def place_pit(room):
        if random.ranint(0, 100) < 10:
            room.__pit = True
            room.__items.append(Pit())
