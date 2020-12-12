from room_feature import RoomFeature
import random


# Main Class
class HealingPotion(RoomFeature):
    def __init__(self):
        super().__init__(f'Healing Potion ({self.__hit_points})', 'Item')
        self.__hit_points = randomint(5, 15)

    def effect(self):
        return f'A potion that heals {self.__hit_points} hit points.'

    @property
    def hit_points(self):
        return self.__hit_points
