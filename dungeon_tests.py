import unittest
from dungeon import Dungeon
from unittest.mock import patch

traversable_li = [(2, 2), (2, 3), (4, 4), (0, 4),(1, 1), (1, 2), (1, 0)]
non_traversable_li = [(2, 2), (2, 0), (1, 1), (0, 1), (0, 0), (1, 2), (1, 0)]


class DungeonTests(unittest.TestCase):
    """
      Instantiating a dungeon calls the build_maze recursively until we have a
      traversable dungeon. Build_maze calls the pick_random_empty_room
      to set an entrance, exit and block rooms.
      This test mocks the pick_random_empty_room method in the Dungeon class to
      return a value from a specific list each time the method is called.
      When the dungeon is not traversable it tries to call the mocked method
      again but since the return list is now empty, we get an index error.

    """
    @patch.object(Dungeon, 'pick_random_empty_room')
    def test_dungeon_traversable(self, mock_rand_empty):
        try:
            mock_rand_empty.side_effect = lambda: traversable_li.pop()
            dungeon = Dungeon()
            self.assertEqual(True, True)
        except IndexError:
            self.assertEqual(True, False,
                             "Shouldn't have got here! "
                             "Traversable dungeon is non traversable.")

    @patch.object(Dungeon, 'pick_random_empty_room')
    def test_dungeon_not_traversable(self, mock_rand_empty):
        try:
            mock_rand_empty.side_effect = lambda: non_traversable_li.pop()
            dungeon = Dungeon()
            self.assertEqual(True, False,
                             "Shouldn't have got here. "
                             "Non traversable dungeon is traversable.")
        except IndexError:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
