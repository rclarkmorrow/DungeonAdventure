from obstacle import Obstacle
from vision_potion import VisionPotion
from healing_potion import HealingPotion


class Room:

    def __init__(self):
        """
        Abstract base class for a room, should not be
        used for a concrete object.
        """
        self.__features = []
        self.__treasure = None  # A I P E
        self.__is_entrance = False
        self.__is_exit = False
        self.__is_impassable = False
        self.__visited = False

    def __str__(self):
        """
        Returns string representation of the current room and features
        """
        if self.__is_entrance:
            return "S: Start"
        elif self.__is_exit:
            return "X: Exit"
        elif self.__is_impassable:
            return "B: No Room (Blocked)"
        elif self.__treasure:
            return str(self.__treasure[0])
        elif len(self.__features) > 1:
            return "M: Multiple Features"
        elif len(self.__features):
            if type(self.__features[0]) == HealingPotion:
                return "H: Healing Potion"
            elif type(self.__features[0]) == VisionPotion:
                return "V: Vision Potion"
            elif type(self.__features[0]) == Obstacle:
                return f"O: Obstacle ({self.__features[0].name})"
        else:
            return " : Empty Room"

        # return_string = ''
        # return_string += ("* — *" + "\n" + "|")
        # if len(self.__features) > 1:
        #     return_string += (" M ")
        # elif len(self.__features):
        #     print(type(self.features[0]))
        #     # if type(self.__features[0]) == HealingPotion
        #     #     return_string += (" H ")
        #     if self.__features[0].name == "Vision Potion":
        #         return_string += (" V ")
        #     elif self.__features[0].category == "Obstacle":
        #         return_string += (" O ")
        # elif self.treasure is not None:
        #     return_string += f" {(str(self.__treasure[0]))} "
        # else:
        #     return_string += ("   ")
        # return_string += ("|" + "\n" + "* _ *\n")
        # return return_string

    @property
    def can_enter(self):
        return not self.__is_impassable and not self.__visited

    @property
    def is_empty(self):
        return not(self.__features or self.__treasure)

    @property
    def is_impassable(self):
        return self.__is_impassable

    @is_impassable.setter
    def is_impassable(self, value: bool):
        self.__is_impassable = value

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, value: bool):
        self.__visited = value

    @property
    def is_entrance(self):
        return self.__is_entrance

    @is_entrance.setter
    def is_entrance(self, value: bool):
        self.__is_entrance = value

    @property
    def is_exit(self):
        return self.__is_exit

    @is_exit.setter
    def is_exit(self, value: bool):
        self.__is_exit = value

    @property
    def features(self):
        return self.__features

    def add_feature(self, feature):
        self.__features.append(feature)

    def remove_feature(self, feature):
        self.__features.remove(feature)

    @property
    def treasure(self):
        return self.__treasure

    @treasure.setter
    def treasure(self, treasure_string):
        self.__treasure = treasure_string
