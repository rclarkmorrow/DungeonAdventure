class Adventurer:
    def __init__(self, name, hit_points):
        self.__name = name
        self.__hit_points = hit_points
        self.__pillars_found = []
        self.__vision = count

    def __str__(self):
        return (f'Adventurer: {self.__name}\n'
                f'Hit Points: {self.hit_points}\n'
                f'Inventory: {self.inventory}')

    @property
    def name(self):
        return self.__name

    @property
    def hit_points(self):
        return self.__hit_points

    @property
    def pillars_found(self):
        return self.__pillars_found

    def use_healing_potion(self, potion):
        """
          This method is called when the adventurer encounters a
          healing potion. For now it only adds HP value of the potion
          to the adventurer, but it is a separate method so that we can
          add other logic (such as adventurer inventory) later if we want.
        """
        self.__add_health(potion.hit_points)

    def encounter_obstacle(self, obstacle):
        """
          This method is called when the adventurer encounters an obstacle.
          For now it only removes HP value of the obstacle from the adventurer,
          but it is a separate method so that we can add obstacles with other
          effects later if we want to.
        """
        self.__remove_health(obstacle.hit_points)

    def find_pillar(self, pillar):
        """ Method adds a pillar to adventurer's found pillars list. """
        self.__pillars_found.append(pillar)

    def __add_health(self, number):
        """ Adds specified value to adventurer's hit points. """
        self.__hit_points += number

    def __remove_health(self, number):
        """ Removes specified value from adventurer's hit points. """
        self.__hit_points -= number

    def __add_vision(self):
        """ Adds vision potion to adventurer's utility belt """
        self.__vision += 1

    def __remove_vision(self):
        """ Removes vision potion from adventurer's utility belt """
        self.__hit_points -= 1
