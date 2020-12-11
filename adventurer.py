from observer import Observer


class Adventurer(Observer):
    def __init__(self, observable, name, hit_points):
        super().__init__(observable)
        self.__name = name
        self.__hit_points = hit_points
        self.__inventory = []

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
    def inventory(self):
        return self.__inventory

    def use_healing_potion(self, potion):
        self.__add_health(potion.hit_points)
        self.__remove_item(potion)

    def __add_health(self, number):
        self.__hit_points += number

    def __remove_health(self, obstacle):
        self.__hit_points -= obstacle.hit_points

    def __add_item(self, item):
        self.__inventory.append(item)

    def __remove_item(self, item):
        self.__inventory.remove(item)

    def notify(self, **kwargs):
        for key, value in kwargs:
            if key == 'Item':
                self.__add_item(value)
            if key = 'Obstacle':
                self.__remove_health(value)

        # Placeholder for possible notification from game.
