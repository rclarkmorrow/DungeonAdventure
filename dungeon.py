import random
from collections import deque


class Room():
    """
      creates a room.
    """
    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = False
        self.__pit = False
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False
        self.__healthChance = 10

    def get_health_chance(self):
        return self.__healthChance

    def __str__(self):
        item_count = 0;
        if self.__healthPotion:
            item_count += 1
        if self.__visionPotion:
            item_count += 1


        if item_count > 1:
            return "M"

        """
        return "Health potion: " + str(self.__healthPotion) + "\n" \
               + "Vision potion: " + str(self.__visionPotion) + "\n" \
               + "Pillar: " + str(self.__pillar) + "\n" \
               + "Pit: " + str(self.__pit) + "\n" \
               + "Entrance: " + str(self.__entrance) + "\n" \
               + "Exit: " + str(self.__exit) + "\n" \
               + "Impassable: " + str(self.__impassable) + "\n\n"
        """
        if self.__entrance:
            return "strt"
        elif self.__exit:
            return "exit"
        elif self.__impassable:
            return "bloc"
        elif self.__pillar:
            return "pill"
        else:
            return "room"


    def set_health(self, add_potion):
        self.__healthPotion = add_potion

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_entrance(self):
        return self.__entrance

    def is_exit(self):
        return self.__exit

    def is_impassable(self):
        return self.__impassable

    def is_visited(self):
        return self.__visited

    def set_visited(self, visited):
        self.__visited = visited

    def set_entrance(self):
        self.__entrance = True

    def set_exit(self):
        self.__exit = True

    def set_impassable(self):
        self.__impassable = True

    def is_empty(self):
        return not (self.__healthPotion or self.__visionPotion or self.__pillar)

    def set_pillar(self, value):
        self.__pillar = value

class Dungeon():
    """
      builds a dungeon
    """
    def __init__(self, row_count = 5, col_count = 5, block = 0.2):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count
        self.__blockFactor = block
        self.entrance_pos = None
        self.exit_pos = None
        self.build_maze()

    def pick_random_empty_room(self):
        """
          Randomly selects an empty room in the maze
          that is not an entrance and not an exit
          and is not blocked.
          :return: tuple - co-ord of the random room in the maze.
        """
        while True:
            rand_row = random.randrange(0,self.__rowCount)
            rand_col = random.randrange(0,self.__colCount)
            rand_room = self.__maze[rand_row][rand_col]
            if rand_room.is_empty() and not rand_room.is_entrance() \
                    and not rand_room.is_exit() and not rand_room.is_impassable():
                return rand_row,rand_col

    def set_entrance(self):
        """
          To randomly set an empty room as the entrance
        """
        self.entrance_pos = self.pick_random_empty_room()
        self.__maze[self.entrance_pos[0]][self.entrance_pos[1]].set_entrance()
        print(f"entrance: {self.entrance_pos}")

    def set_exit(self):
        """
          To randomly set an empty room as the exit
        """
        self.exit_pos = self.pick_random_empty_room()
        self.__maze[self.exit_pos[0]][self.exit_pos[1]].set_exit()
        print(f"exit: {self.exit_pos}")

    def block_rooms(self):
        """
          Make some empty rooms impassible (making 5 rooms impassable)
        """
        block = 0
        while block < self.__blockFactor*self.__rowCount*self.__colCount:
            rand_pos = self.pick_random_empty_room()
            self.__maze[rand_pos[0]][rand_pos[1]].set_impassable()
            block += 1
            print(f"blocked room: {rand_pos}")

    def set_pillars(self):
        """
          Set the pillars(randomly pick empty rooms that are traverse-able)
        """
        pillar_count = 0
        pillars = ["ABST","ENCA","INHE","POLY"]
        while pillar_count < len(pillars):
            rand_pos = self.pick_random_empty_room()
            if self.__maze[rand_pos[0]][rand_pos[1]].is_visited:
                self.__maze[rand_pos[0]][rand_pos[1]].set_pillar(pillars[pillar_count])
                print(f"{pillars[pillar_count]} at: {rand_pos}")
                pillar_count += 1

    def build_maze(self):
        """
          Creates a 2D grid (list of lists) of rooms.
          Sets a random unblocked empty room as the entrance, exit
          and randomly blocks a specific number of rooms
          depending on the blockFactor.
          Ensures exit is reachable from the entrance and updates
          visited field of all traverse-able rooms in the maze.
        """
        # Adding rooms to the maze (Default 2D grid of rooms)
        for r in range(0, self.__rowCount):
            self.__maze.append([Room() for c in range(0, self.__colCount)])
        # Setting entrance and exit of the maze
        self.set_entrance()
        self.set_exit()
        # Making some rooms impassable
        self.block_rooms()
        # Check maze is traverse-able from entrance to exit and a list of rooms that can be reached.
        reachable_exit_rooms = self.bfs_reachable_exit_rooms(self.entrance_pos[0],self.entrance_pos[1])
        print("traversable",reachable_exit_rooms)
        if not reachable_exit_rooms:  #exit is not reachable
            self.build_maze()
        # Placing the four pillars
        self.set_pillars()

    def __str__(self):
        out_li = []
        for row in self.__maze:
            out_li.append(",".join([item.__str__() for item in row]))
        return "\n".join(out_li)

    def bfs_reachable_exit_rooms(self,row,col):
        """
          Performs a BFS of the maze and checks exit is reachable from entrance
          and updates the visited field of all rooms that can reached.
        :param row: Int index
        :param col: Int index
        :return: Bool (if exit is reachable)
        """
        queue = deque()
        queue.append((row,col))
        found_Exit = False
        while len(queue)>0:
            node = queue.popleft()
            if self.__maze[node[0]][node[1]].is_exit():
                found_Exit = True
            if self.is_valid_room(node[0]-1,node[1]):
                self.__maze[node[0]-1][node[1]].set_visited(True)
                queue.append((node[0]-1,node[1]))
            if self.is_valid_room(node[0]+1,node[1]):
                self.__maze[node[0]+1][node[1]].set_visited(True)
                queue.append((node[0]+1,node[1]))
            if self.is_valid_room(node[0],node[1]-1):
                self.__maze[node[0]][node[1]-1].set_visited(True)
                queue.append((node[0],node[1]-1))
            if self.is_valid_room(node[0],node[1]+1):
                self.__maze[node[0]][node[1]+1].set_visited(True)
                queue.append((node[0],node[1]+1))
        return found_Exit

    def is_valid_room(self, row, col):
        """
          Returns true if row,col is a valid room in the maze and if it can be entered.
          (not blocked and not visited)
        :param row: Int index
        :param col: Int index
        :return: Bool
        """
        return 0 <= row < self.__rowCount and 0 <= col < self.__colCount and self.__maze[row][col].can_enter()


d1 = Dungeon(5,5)
print(d1)