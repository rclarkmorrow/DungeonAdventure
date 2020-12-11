from room_feature import RoomFeature


# Main Class
class Obstacle(RoomFeature):
    def __init__(self, name, effect, hit_points):
        super().__init__(name, 'Obstacle')
        self.__effect = effect
        self.__hit_points = hit_points

    def effect(self):
        return self.__effect

    @property
    def hit_points(self):
        return self.__hit_points
