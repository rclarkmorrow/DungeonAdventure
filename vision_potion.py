from room_feature import RoomFeature


# Main Class
class VisionPotion(RoomFeature):
    def __init__(self, vision=bool):
        """
        Vision potion class creates a subclass of room feature.
        """
        super().__init__(f'Vision Potion ({self.__vision})', 'Item')
        self.__vision = vision

    @property
    def description(self):
        """
        Returns a string that is a description of what the potion will do.
        """
        return 'A potion that reveals the rooms surrounding the current room.'

    @property
    def effect(self):
        """
        Returns a string describing the use of hte potion
        """
        return ('You use the vision potion, and mystical forces allow you to'
                'see the surrounding area.')
