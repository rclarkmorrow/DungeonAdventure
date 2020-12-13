import unittest
from adventurer_factory import AdventurerFactory, DEFAULT_NAMES, MIN_HP, MAX_HP
from room_feature_factory import RoomFeatureFactory


class FactoryTests(unittest.TestCase):
    """ These are unittests for the Dungeon adventure factory classes. """

    """--------------------------------------------------#
    # Tests for Adventurer Factory
    #--------------------------------------------------"""

    def test_create_adventurer_default_name(self):
        """ Adventurer is created with default values """
        adventurer = AdventurerFactory.create_adventurer()
        self.assertTrue(adventurer.name in DEFAULT_NAMES,
                        'adventurer name is not in default names list')
        self.assertGreaterEqual(adventurer.hit_points, MIN_HP,
                                'adventurer hit points are less than'
                                ' the minimum setting')
        self.assertLessEqual(adventurer.hit_points, MAX_HP,
                             'adventurer hit points are greater than')

    def test_create_adventurer_custom(self):
        """ Adventurer is created with custom values """
        adventurer = AdventurerFactory.create_adventurer('Tom', 120)
        self.assertEqual('Tom', adventurer.name,
                         'adventurer name does not match input name')
        self.assertEqual(120, adventurer.hit_points)

    def test_create_adventurer_string_converts_int(self):
        adventurer = AdventurerFactory.create_adventurer('Tom', '120')
        self.assertEqual('Tom', adventurer.name,
                         'adventurer name does not match input name')
        self.assertEqual(120, adventurer.hit_points)

    def test_create_adventurer_bad_int(self):
        try:
            AdventurerFactory.create_adventurer(
                hit_points='not a number')
            self.assertEqual(True, False, 'should not have got here,'
                             ' adventurer created with hit points not'
                             ' convertable to integer')
        except ValueError:
            self.assertEqual(True, True)

        # obstacle = RoomFeatureFactory.create_obstacle()
        # adventurer.encounter_obstace(obstacle)
        # potion = RoomFeatureFactory.create_healing_potion()
        # adventurer.use_healing_potion(potion)


if __name__ == '__main__':
    unittest.main()
