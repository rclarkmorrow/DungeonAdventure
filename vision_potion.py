from room_feature import RoomFeature


# Main Class
class VisionPotion(RoomFeature):
    def __init__(self, vision=bool):
        """
        Vision potion class creates a subclass of room feature.
        """
        super().__init__(f'Vision Potion ({self.__vision})', 'Item')
        self.__vision = vision

    def effect(self):
        """
        Returns a string of stating that the potion reveals the surrounding rooms
        """
        return f'A potion that reveals the surrounding rooms of current'

    @property
    def vision(self):
        """
        Returns vision potion
        """
        return self.__vision
