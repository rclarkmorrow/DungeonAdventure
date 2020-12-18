import unittest
from adventurer_factory import AdventurerFactory, DEFAULT_NAMES, MIN_HP, MAX_HP
from room_feature_factory import (RoomFeatureFactory, HEALING_POTION,
                                  OBSTACLE_DAMAGE, OBSTACLES)


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

    def test_create_adventurer_name_not_string(self):
        try:
            AdventurerFactory.create_adventurer(
                name=3.1415926535)
            self.assertEqual(True, False, 'should not have got here,'
                             ' adventurer created with name that is'
                             ' not a string')
        except ValueError:
            self.assertEqual(True, True)

    def test_create_adventurer_string_converts_int(self):
        adventurer = AdventurerFactory.create_adventurer('Tom', '120')
        self.assertEqual('Tom', adventurer.name,
                         'adventurer name does not match input name')
        self.assertEqual(120, adventurer.hit_points)

    def test_create_adventurer_hit_points_not_int(self):
        try:
            AdventurerFactory.create_adventurer(
                hit_points='not a number')
            self.assertEqual(True, False, 'should not have got here,'
                             ' adventurer created with hit points not'
                             ' convertable to integer')
        except ValueError:
            self.assertEqual(True, True)

    """--------------------------------------------------#
    # Tests for Room Feature Factory
    #--------------------------------------------------"""

    def test_create__healing_potion_default(self):
        healing_potion = RoomFeatureFactory.create_healing_potion()
        self.assertEqual(HEALING_POTION, healing_potion.hit_points,
                         'healing potion hit point does not match'
                         ' default setting')
        self.assertEqual(f'Healing Potion ({HEALING_POTION})',
                         healing_potion.name, 'healing potion default name'
                         ' is incorrect')
        self.assertEqual(f'A potion that heals {HEALING_POTION} hit points.',
                         healing_potion.effect)

    def test_create__healing_potion_default(self):
        healing_potion = RoomFeatureFactory.create_healing_potion()
        self.assertEqual(HEALING_POTION, healing_potion.hit_points,
                         'healing potion hit point does not match'
                         ' default setting')
        self.assertEqual(f'Healing Potion ({HEALING_POTION})',
                         healing_potion.name, 'healing potion default name'
                                              ' is incorrect')
        self.assertEqual(f'A potion that heals {HEALING_POTION} hit points.',
                         healing_potion.effect)


    def test_bad_string_input_healing(self):
        """
          String can't be converted to float should raise ValueError
        """
        try:
            RoomFeatureFactory.create_healing_potion('dg')
            self.assertEqual(True, False)
        except ValueError:
            self.assertEqual(True, True)

    def test_int_string_converts_healing_potion(self):
        """
          Strings convert to floats returns healing potion object
        """
        healing_potion = RoomFeatureFactory.create_healing_potion('5')
        self.assertEqual(type(healing_potion), HEALING_POTION, 'should return object of '
                         'type Healing_Potion')


    def test_bad_string_input_obstacle(self):
        """
          String can't be converted to float should raise ValueError
        """
        try:
            RoomFeatureFactory.create_obstacle('dg')
            self.assertEqual(True, False)
        except ValueError:
            self.assertEqual(True, True)

    def test_int_string_converts_obstacle(self):
        """
          Strings convert to floats returns obstacle potion object
        """
        obstacle = RoomFeatureFactory.create_obstacle('5')
        self.assertEqual(type(obstacle), OBSTACLES, 'should return object of '
                                                             'type obstacle')

if __name__ == '__main__':
    unittest.main()
