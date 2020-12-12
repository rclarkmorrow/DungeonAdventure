import random
from roomfeature import RoomFeature
from healing_potion import HealthPotion
from vision_potion import VisionPotion
from pit import Pit
from roomfactory import RoomFactory


class Room:

    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = None  # A I P E
        self.__pit = False
        self.__entrance = False
        self.__exit = False
        self.__impassable = False
        self.__visited = False
        self.__items = []  # objects can be Potion (Vision or Health), Pit

    def __str__(self):
        print("* _ *" + "\n" + "|")
        if self.__pit:
            print(" P ")
        elif len(self.__items) > 1 or len(self.__items) > 0 and self._pillar is not None:
            print(" M ")
        elif self.healthpotion:
            print(" H ")
        elif self.visionpotion:
            print(" V ")
        elif self.pillars is not None:
            print(str(self.__pillar))
        else:
            print("  " + "|" + "\n" + "* _ *")
        if self.__entrance:
            return "Start"
        elif self.__exit:
            return "Exit"
        elif self.__impassable:
            return "Blocked"
        else:
            return "Room"

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, value: bool):
        self.__visited = value

    def set_entrance(self, value: bool):
        self.__entrance = value

    def set_exit(self, value: bool):
        self.__exit = value
