from healing_potion import HealingPotion
from vision_potion import VisionPotion

class Adventurer:
    def __init__(self, name, hit_points):
        self.__name = name
        self.__hit_points = hit_points
        self.__inventory = []
        self.__treasure_found = []

    def __str__(self):
        return_string =  f'Adventurer: {self.name}\nHit Points: {self.hit_points}\n'
        return_string += 'Inventory:\n'
        for item in self.__inventory:
            return_string += f'  {item.description}\n'
        return_string += 'Treasure Found:\n'
        for treasure in self.treasure_found:
            return_string += f'  {treasure}'
        return return_string
        # return (f'Adventurer: {self.name}\n'
        #         f'Hit Points: {self.hit_points}\n'
        #         f'Inventory: {self.inventory}\n'
        #         f'Treasure Found: {self.treasure_found}')

    @property
    def name(self):
        return self.__name

    @property
    def hit_points(self):
        return self.__hit_points

    @property
    def inventory(self):
        return self.__inventory

    @property
    def treasure_found(self):
        return self.__treasure_found

    def use_healing_potion(self):
        """
          This method is called when the adventurer uses a
          healing potion. It grabs the first available healing
          potion and adds it to the adventurer's hit point total
          and then removes it from inventory or returns false if
          there are none.
        """
        for item in self.__inventory:
            if type(item) == HealingPotion:
                self.__add_health(item.hit_points)
                self.__inventory.remove(item)
                return item
        return False

    def use_vision_potion(self):
        """
          This method is called when the adventurer uses a
          vision potion. It removes the first vision potion
          from inventory or returns false if there are none.
        """
        for item in self.__inventory:
            if type(item) == VisionPotion:
                self.__inventory.remove(item)
                return item
        return False

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
        self.__treasure_found.append(treasure)

    def add_item(self, item):
        self.__inventory.append(item)

    def remove_item(self, item):
        self.__inventory.remove(item)

    def __add_health(self, number):
        """ Adds specified value to adventurer's hit points. """
        self.__hit_points += number

    def __remove_health(self, number):
        """ Remvoes specified value from adventurer's hit points. """
        self.__hit_points -= number
