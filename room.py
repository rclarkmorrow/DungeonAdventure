class Room:

    def __init__(self):
        """
        Abstract base class for a room, should not be
        used for a concrete object.
        """
        self.features = []
        self.items = []
        self.obstacles = []
        self.__pillar = None  # A I P E
        self.__entrance = False
        self.__exit = False
        self.__impassable = False
        self.__visited = False

    def __str__(self):
        """
        Returns string representation of the current room and features
        """
        print("* _ *" + "\n" + "|")
        if len(self.__features)>1:
            print(" M ")
        elif len(self.items)>1:
            print(" M ")
        elif HealthPotion() in self.items:
            print(" H ")
        elif VisionPotion() in self.items:
            print(" V ")
        elif self.obstacles:
            print(" O ")
        elif self.pillars is not None:
            print(str(self.__pillar))
        else:
            print("  " + "|" + "\n" + "* _ *")

    @property
    def can_enter(self):
        return self.__impassable  # and not self.__visited

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, value: bool):
        self.__visited = value

    @property
    def is_entrance(self):
        return self.__entrance

    @is_entrance.setter
    def is_entrance(self, value: bool):
        self.__entrance = value

    @property
    def is_exit(self):
        return self.__exit

    @is_exit.setter
    def is_exit(self, value: bool):
        self.__exit = value

    @property
    def g_items(self, item):
        return self.items.pop(item)

    @add_items.setter
    def add_items(self, item):
        self.items.append(item)

    @property
    def g_features(self, feature):
        return self.features.pop(feature)

    @add_features.setter
    def add_features(self, features):
        self.features.append(features)

    @property
    def g_obstacles(self, obstacle):
        return self.obstacles.pop(obstacle)

    @add_features.setter
    def add_obstacles(self, obstacles):
        self.obstacles.append(obstacles)
