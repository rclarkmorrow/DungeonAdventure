class Adventurer:
    def __init__(self, name, hit_points):
        self.__name = name
        self.__hit_points = hit_points
        self.__treasures_found = []
        self.__inventory = []

    def __str__(self):
        return (f'Adventurer: {self.name}\n'
                f'Hit Points: {self.hit_points}\n'
                f'Treasures Found: {self.treasures_found}\n'
                f'Inventory: {self.inventory}')

    @property
    def name(self):
        return self.__name

    @property
    def hit_points(self):
        return self.__hit_points

    @property
    def treasures_found(self):
        return self.__treasures_found

    @property
    def inventory(self):
        return self.__inventory

    def add_item(self, item):
        """ Adds vision potion to adventurer's utility belt """
        self.__inventory.append(item)

    def remove_item(self, item):
        """ Removes vision potion from adventurer's utility belt """
        if item in self.__inventory:
            self.__inventory.remove(item)

    def use_healing_potion(self, potion):
        """
          This method is called when the adventurer encounters a
          healing potion. For now it only adds HP value of the potion
          to the adventurer, but it is a separate method so that we can
          add other logic (such as adventurer inventory) later if we want.
        """
        self.__add_health(potion.hit_points)
        self.remove_item(potion)

    def encounter_obstacle(self, obstacle):
        """
          This method is called when the adventurer encounters an obstacle.
          For now it only removes HP value of the obstacle from the adventurer,
          but it is a separate method so that we can add obstacles with other
          effects later if we want to.
        """
        self.__remove_health(obstacle.hit_points)

    def find_treasure(self, treasure):
        """ Method adds a pillar to adventurer's found pillars list. """
        self.__treasires_found.append(treasure)

    def __add_health(self, number):
        """ Adds specified value to adventurer's hit points. """
        self.__hit_points += number

    def __remove_health(self, number):
        """ Removes specified value from adventurer's hit points. """
        self.__hit_points -= number
