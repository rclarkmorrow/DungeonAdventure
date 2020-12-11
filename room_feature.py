from abc import ABC, abstractmethod

class RoomFeature(ABC):
    """
       Abstract base class for an item, should not be
       used for a concrete object.
    """
    def __init__(self, name="", category=""):
        self.__name = name
        self.__category = category

    @property
    def name(self):
        """
           Returns the shapes name as a property.
        """
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    @abstractmethod
    def effect(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is RoomFeature:
            attrs = set(dir(subclass))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
