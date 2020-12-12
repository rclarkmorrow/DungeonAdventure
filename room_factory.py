from random import randint
from healing_potion import HealingPotion
from vision_potion import VisionPotion
from obstacle import Obstacle
from room import Room


class RoomFactory():
    @staticmethod
    def create_room():
        room = Room


    @staticmethod
    def place_health(room):
        if randint(0, 100) < 10:
            room.__items.append(HealingPotion())

    @staticmethod
    def place_vision(room):
        if randint(0, 100) < 10:
            room.__items.append(VisionPotion(True))

    @staticmethod  # Needs to be created with the obstacle factory
    def place_obstacle(room):
        if randint(0, 100) < 10:
            room.__items.append(Obstacle())
