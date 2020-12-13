class Room:

    def __init__(self):
        self.items = []
        self.obstacles = []
        self.__pillar = None  # A I P E
        self.__entrance = False
        self.__exit = False
        self.__impassable = False
        self.__visited = False

    def __str__(self):
        print("* _ *" + "\n" + "|")
        if self.__obstacles:
            print(" O ")
        elif len(self.__items) > 1:
            print(" M ")
        elif self.h:
            print(" H ")
        elif self.visionpotion:
            print(" V ")
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
