import unittest

from vision_potion import VisionPotion
from healing_potion import HealingPotion
from obstacle import Obstacle
from adventurer_factory import AdventurerFactory, DEFAULT_NAMES, MIN_HP, MAX_HP
from room_feature_factory import (RoomFeatureFactory, HEALING_MIN, HEALING_MAX,
                                  OBSTACLE_MIN, OBSTACLE_MAX, OBSTACLES)

CUSTOM_HEAL = 50
HP_STRING = '15'
CUSTOM_OBSTACLE = ['Dragon', 'You are engulfed in fiery fire!', 25]
NOT_STRING = VisionPotion()


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

    def test_create_healing_potion_default(self):
        healing_potion = RoomFeatureFactory.create_healing_potion()

        self.assertEqual(type(healing_potion), HealingPotion, 'should return'
                         ' object of type Healing_Potion')
        self.assertLessEqual(healing_potion.hit_points, HEALING_MAX,
                             'healing potion hit points less than'
                             ' default max setting')
        self.assertGreaterEqual(healing_potion.hit_points, HEALING_MIN,
                                'healing potion hit points greater than'
                                ' default min setting')
        self.assertEqual(f'Healing Potion ({healing_potion.hit_points})',
                         healing_potion.name, 'healing potion default name'
                         ' is incorrect')
        self.assertEqual(f'A potion that heals {healing_potion.hit_points}'
                         ' hit points', healing_potion.description)
        self.assertEqual('You take a healing potion and gain'
                         f' {healing_potion.hit_points} hit points.',
                         healing_potion.effect)

    def test_create_healing_potion_custom(self):
        healing_potion = RoomFeatureFactory.create_healing_potion(CUSTOM_HEAL)

        self.assertEqual(type(healing_potion), HealingPotion, 'should return'
                         ' object of type Healing_Potion')
        self.assertEqual(CUSTOM_HEAL, healing_potion.hit_points,
                         'healing potion hit point does not match'
                         ' default setting')
        self.assertEqual(f'Healing Potion ({CUSTOM_HEAL})',
                         healing_potion.name, 'healing potion default name'
                                              ' is incorrect')
        self.assertEqual(f'A potion that heals {CUSTOM_HEAL} hit points',
                         healing_potion.description)
        self.assertEqual('You take a healing potion and gain'
                         f' {CUSTOM_HEAL} hit points.',
                         healing_potion.effect)

    def test_bad_string_input_healing(self):
        """
          String can't be converted to integer should raise ValueError
        """
        try:
            RoomFeatureFactory.create_healing_potion('dg')
            self.assertEqual(True, False, 'should not have got here,'
                             ' healing potion created with hit points not'
                             ' convertable to integer')
        except ValueError:
            self.assertEqual(True, True)

    def test_int_string_converts_healing_potion(self):
        """
          Strings convert to floats returns healing potion object
        """
        healing_potion = RoomFeatureFactory.create_healing_potion(HP_STRING)

        self.assertEqual(type(healing_potion), HealingPotion, 'should return'
                         ' object of type Healing_Potion')
        self.assertEqual(int(HP_STRING), healing_potion.hit_points,
                         'healing potion hit point does not match'
                         ' default setting')
        self.assertEqual(f'Healing Potion ({int(HP_STRING)})',
                         healing_potion.name, 'healing potion default name'
                                              ' is incorrect')
        self.assertEqual(f'A potion that heals {int(HP_STRING)} hit points',
                         healing_potion.description)
        self.assertEqual('You take a healing potion and gain'
                         f' {int(HP_STRING)} hit points.',
                         healing_potion.effect)

    def test_create_vision_potion_default(self):
        """
          Vision potion created
        """
        vision_potion = RoomFeatureFactory.create_vision_potion()

        self.assertEqual(type(vision_potion), VisionPotion, 'should return'
                         ' object of type VisionPotion')

    def test_create_vision_potion_argument(self):
        """
          Error if argument passed to vision potion
        """
        try:
            RoomFeatureFactory.create_vision_potion('argument')
            self.assertEqual(True, False, 'should not have got here,'
                             ' vision potion created with argument')
        except TypeError:
            self.assertEqual(True, True)

    def test_create_obstacle_default(self):
        """
          Create default obstacle
        """
        obstacle = RoomFeatureFactory.create_obstacle()

        self.assertEqual(type(obstacle), Obstacle, 'should return'
                         ' object of type Obstacle')
        self.assertLessEqual(obstacle.hit_points, OBSTACLE_MAX,
                             'hit points should be less or equal to'
                             'default max')
        self.assertGreaterEqual(obstacle.hit_points, OBSTACLE_MIN,
                                'hit points should be greater or equal to'
                                'default max')
        self.assertTrue(obstacle.name in OBSTACLES.keys(),
                        'obstacle should have string name')
        self.assertEqual(obstacle.description, f'An obstacle ({obstacle.name})'
                         f' that deals {obstacle.hit_points} damage.')
        self.assertTrue(isinstance(obstacle.effect, str),
                        'obstacle should have string effect')

    def test_create_obstacle_custom(self):
        """
          Create custom obstacle
        """
        obstacle = RoomFeatureFactory.create_obstacle(
            name=CUSTOM_OBSTACLE[0],
            effect=CUSTOM_OBSTACLE[1],
            hit_points=CUSTOM_OBSTACLE[2]
        )

        self.assertEqual(type(obstacle), Obstacle, 'should return'
                         ' object of type Obstacle')
        self.assertEqual(obstacle.hit_points, CUSTOM_OBSTACLE[2],
                         'hit points should match')
        self.assertEqual(obstacle.name, CUSTOM_OBSTACLE[0],
                         'nameshould match')
        self.assertEqual(obstacle.description, f'An obstacle'
                         f' ({CUSTOM_OBSTACLE[0]})'
                         f' that deals {CUSTOM_OBSTACLE[2]} damage.')
        self.assertTrue(CUSTOM_OBSTACLE[1] in obstacle.effect,
                        'effect should match')

    def test_int_string_converts_obstacle(self):
        """
          String converts to int for hit_points
        """
        obstacle = RoomFeatureFactory.create_obstacle(hit_points=HP_STRING)

        self.assertEqual(type(obstacle), Obstacle, 'should return'
                         ' object of type Obstacle')
        self.assertEqual(obstacle.hit_points, int(HP_STRING),
                         'hit points should match')
        self.assertTrue(obstacle.name in OBSTACLES.keys(),
                        'name should match')
        self.assertTrue(isinstance(obstacle.description, str),
                        'obstacle should have string description')
        self.assertTrue(isinstance(obstacle.effect, str),
                        'effect should be string')

    def test_bad_string_input_obstacle(self):
        """
          String can't be converted to int should raise ValueError
        """
        try:
            RoomFeatureFactory.create_obstacle(hit_points='dg')
            self.assertEqual(True, False, 'should not have got here'
                             ' hit points created with string')
        except ValueError:
            self.assertEqual(True, True)

    def test_bad_name_effect_input_obstacle(self):
        """
          Non-string should raise ValueError
        """
        try:
            RoomFeatureFactory.create_obstacle(name=NOT_STRING, effect=NOT_STRING)
            self.assertEqual(True, False, 'should not have got here'
                             ' obstacle created with non-string values')
        except ValueError:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
