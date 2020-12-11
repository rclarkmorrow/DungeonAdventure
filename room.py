from random import randint

class Room:

    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = None
        self.__pit = False
        self.__exit = False
        self.__eastDoor = True
        self.__westDoor = True
        self.__northDoor = True
        self.__southDoor = True
        self.__impassable = False
        self.__visited = False
        self.__items = []  # objects can be Potion (Vision or Health), Pit

    def __str__(self):
        if self.northDoor:
            print("* * *" + "\n")
        else:
            print("* _ *" + "\n")

        if self.eastDoor:
            print("*")
            if self.__pit:
                print(" P ")
            elif count(self.items) > 2:
                print(" M ")
            elif self.healthpotion:
                print(" H ")
            elif self.visionpotion:
                print(" V ")
            elif self.pillars is not None:
                print(str(self.__pillar))
            else:
                print("  ")
        else:
            print("|")
            if self.__pit:
                print(" P ")
            elif count(self.items) > 2:
                print(" M ")
            elif self.healthpotion:
                print(" H ")
            elif self.visionpotion:
                print(" V ")
            elif self.pillars is not None:
                print(str(self.__pillar))
            else:
                print("  ")

        if self.westDoor:
            print("x" + "\n")
        else:
            print("|" + "\n")

        if self.southDoor:
            print("* * *")
        else:
            print("* _ *")

    # the Dungeon should manage the random value
    # that places in the room
    def set_health(self, heath_potion: Potion):
        self.__healthPotion = True
        self.__items.append(heath_potion)

    def set_vision(self, vision_potion: int):
        self.__visionPotion = True
        self.__items.append(vision_potion)

    def set_pit(self, pit: Pit):
        self.__pit = True
        self.__items.append(pit)

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, value: bool):
        self.__visited = value

    def set_entrance(self, value: bool):
        self.__entrance: value

    def set_exit(self, value: bool):
        self.__exit: value


class Potion:  # vision or health
    def __init__(self, point):
        self.point = point


class Pit:  # pit
    def __init__(self, damage):
        self.damage = damage
