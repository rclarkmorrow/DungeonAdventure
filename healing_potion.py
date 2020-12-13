from room_feature import RoomFeature


# Main Class
class HealingPotion(RoomFeature):
    def __init__(self, hit_points):
        super().__init__(f'Healing Potion ({hit_points})', 'Item')
        self.__hit_points = hit_points

    def effect(self):
        return f'A potion that heals {self.__hit_points} hit points.'

    @property
    def hit_points(self):
        return self.__hit_points
