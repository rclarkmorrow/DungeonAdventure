ffrom random import randint


class Room:

    def _init__(self):
        self.__items = []  # Pillars (A, I, E, P) or Potion (V, H)
        self.__doors = []  # N, S, E, W
        self.__entrance = False  # indicate if the room has an entrance
        self.__exit = False  # indicate if the room has an exit

        # set the potion
        # if randint(0, 1) == 1:
        #     self.__items.append()

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items

    def __str__(self):
        return "@"  # need to determine the letter to put here


# abstract class for Pillar, Potion
class Item:
    def __init__(self):
        pass


class Pillar(Item):
    def __init__(self, four=None):
        self.__four = four  # A, I, E, P

    @property
    def four(self):
        return self.__four

    @four.setter
    def four(self, four):
        self.__four = four

    def __str__(self):
        if self.four is None:
            return " "
        else:
            return self.four


class Potion(Item):
    def __init__(self, elixir=None, point=0):
        if elixir not in ['H', 'V']:
            raise Exception("The potion elixir must be one of two letters H, V")
        self.__elixir = elixir  # Healing or Vision

        if point <= 0:
            raise Exception("The potion point must be positive")
        self.__point = point

    @property
    def elixir(self):
        return self.__elixir

    @elixir.setter
    def elixir(self, four):
        if side not in ['H', 'V']:
            raise Exception("The potion elixir must be one of two letters H, V")
        self.__elixir = elixir

    @property
    def point(self):
        if point <= 0:
            raise Exception("The potion point must be positive")
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point

    def __str__(self):
        if self.__elixir is None:
            return None
        else:
            return "{}({})".format(self.__elixir, self.__point)


class Door(Item):
    def __init__(self, side=None):
        if side not in ['N', 'S', 'W', 'E']:
            raise Exception("The door side must be one of four letters N, S, W, E")
        self.__side = side  # N S W E

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if side not in ['N', 'S', 'W', 'E']:
            raise Exception("The door side must be one of four letters N, S, W, E")
        self.__side = side

    def __str__(self):
        if self.side is None:
            return " "
        else:
            return self.side


class Dungeon:
    def __init__(self, size=5):
        if size != 5:
            raise Exception("The size of the dungeon must be 5 by 5")
        self.__size = size

        self.__rooms = []
        for col_index in range(0, self.__size):
            rows = []
            for row_index in range(0, self.__size):
                rows.append(Room())
            self.__rooms.append(rows)

        self.__MAX_VISION_POTION = 8

    @property
    def size(self):
        return self.__size

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    def __str__(self):
        for col_index in range(0, self.size):
            for row_index in range(0, self.size):
                pass

    def place_potion(self, col_index, row_index, item, possibility=10):
        if randint(0, 100) < possibility:  # generate a random number from 0-100 if we get less than 10
            self.rooms[col_index][row_index].items.append(item)
        # JUST FOR TESTING PURPOSE
        print(len(self.rooms[col_index][row_index].items[0]))

test = Room()
print(test)

healing_potion = Potion(elixir='H', point=5)
print(healing_potion)

test = Door(side='N')
print(test)

dungeon = Dungeon(size=5)
dungeon.place_potion(0, 0, healing_potion, 10)

print("")

    # def potion(self):
    #     return randomint(5,15)
    #
    # def pit(self):
    #     return randomint(1,20)
    #
    # def entrance(self):
    #
    # def exit(self):
    #
    # def pillar(self):
    #
    # def door(self):
    #
    # def Vision(self):
