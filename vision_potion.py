from room_feature import RoomFeature


# Main Class
class VisionPotion(RoomFeature):
    def __init__(self, vision=bool):
        super().__init__(f'Vision Potion ({self.__vision})', 'Item')
        self.__vision = vision

    def effect(self):
        return f'A potion that reveals the surrounding rooms of current'

    @property
    def vision(self):
        return self.__vision
