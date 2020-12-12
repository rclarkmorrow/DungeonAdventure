from room_feature import RoomFeature


# Main Class
class Pit(RoomFeature):
    def __init__(self):
        super().__init__(f'Pit({self.__hit_points})', 'Item')
        self.__hit_points = randomint(-1, -20)

    def effect(self):
        return f'The pit takes away {self.__hit_points} hit points.'

    @property
    def hit_points(self):
        return self.__hit_points
