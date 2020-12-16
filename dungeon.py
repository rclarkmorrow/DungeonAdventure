import random
from collections import deque
from room_factory import RoomFactory

    # def set_treasure(self, value):
    #     self.__treasure = value

    # def get_treasure(self):
    #     return self.__treasure

class Dungeon():
    """
      builds a dungeon
    """
    def __init__(self, row_count = 5, col_count = 5, block = 0.2):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count
        self.__blockFactor = block
        self.__entrance_pos = None
        self.__exit_pos = None
        self.build_maze()
        self.__adventurer_pos = self.__entrance_pos

    def pick_random_empty_room(self):
        """
          Randomly selects an empty room in the maze
          that is not an entrance and not an exit
          and is not blocked.
          :return: tuple - co-ord of the random room in the maze.
        """
        while True:
            rand_row = random.randrange(0, self.__rowCount)
            rand_col = random.randrange(0, self.__colCount)
            rand_room = self.__maze[rand_row][rand_col]
            if rand_room.is_empty and not rand_room.is_entrance \
                    and not rand_room.is_exit and not rand_room.is_impassable:
                return rand_row, rand_col

    def pick_random_room(self):
        """
          Randomly selects a room in the maze
          that is not an entrance and not an exit
          and is not blocked.
          :return: tuple - co-ord of the random room in the maze.
        """
        while True:
            rand_row = random.randrange(0,self.__rowCount)
            rand_col = random.randrange(0,self.__colCount)
            rand_room = self.__maze[rand_row][rand_col]
            if (not rand_room.is_entrance and
                    not rand_room.is_exit and
                    not rand_room.is_impassable and
                    not rand_room.treasure):
                return rand_row, rand_col

    def set_entrance(self):
        """
          To randomly set an empty room as the entrance
        """
        self.__entrance_pos = self.pick_random_empty_room()
        self.__maze[self.__entrance_pos[0]][self.__entrance_pos[1]].is_entrance = True
        print(f"entrance: {self.__entrance_pos}")

    def set_exit(self):
        """
          To randomly set an empty room as the exit
        """
        self.__exit_pos = self.pick_random_empty_room()
        self.__maze[self.__exit_pos[0]][self.__exit_pos[1]].is_exit = True
        print(f"exit: {self.__exit_pos}")

    def block_rooms(self):
        """
          Make some empty rooms impassible (making 5 rooms impassable)
        """
        block = 0
        while block < self.__blockFactor*self.__rowCount*self.__colCount:
            rand_pos = self.pick_random_empty_room()
            self.__maze[rand_pos[0]][rand_pos[1]].is_impassable = True
            block += 1
            print(f"blocked room: {rand_pos}")

    def set_treasures(self):
        """
          Set the pillars(randomly pick rooms that are traverse-able)
        """
        treasure_count = 0
        treasures = ["ABSTRACTION", "ENCAPSULATION",
                     "INHERITANCE", "POLYMORPHISM"]
        while treasure_count < len(treasures):
            rand_pos = self.pick_random_room()
            if self.__maze[rand_pos[0]][rand_pos[1]].visited:
                self.__maze[rand_pos[0]][rand_pos[1]].treasure = treasures[treasure_count]
                print(f"{treasures[treasure_count]} at: {rand_pos}")
                treasure_count += 1

    def build_maze(self):
        """
          Creates a 2D grid (list of lists) of rooms.
          Sets a random unblocked empty room as the entrance, exit
          and randomly blocks a specific number of rooms
          depending on the blockFactor.
          Ensures exit is reachable from the entrance and updates
          visited field of all traverse-able rooms in the maze.
        """
        self.__maze = []
        # Adding rooms to the maze (Default 2D grid of rooms)
        for r in range(0, self.__rowCount):
            self.__maze.append([RoomFactory.create_room() 
                                for c in range(0, self.__colCount)])
        # Setting entrance and exit of the maze
        self.set_entrance()
        self.set_exit()
        # Making some rooms impassable
        self.block_rooms()
        # Check maze is traverse-able from entrance to exit and a list of rooms that can be reached.
        reachable_exit_rooms = self.bfs_reachable_exit_rooms(self.__entrance_pos[0],self.__entrance_pos[1])
        print("traversable", reachable_exit_rooms)
        if not reachable_exit_rooms:  #exit is not reachable
            self.build_maze()
        # Placing the four pillars
        self.set_treasures()

    def __str__(self):
        line_string = ''
        for row in self.__maze:

            def build_wall(row):
                wall_string = ''
                for room in row:
                    if room is not row[-1]:
                        wall_string += '* _ '
                    else:
                        wall_string += '* _ *\n'
                return wall_string
            if row is self.__maze[0]:
                line_string += build_wall(row)
            for room in row:
                if room is not row[-1]:
                    line_string += f'| {str(room)} '
                else:
                    line_string += f'| {str(room)} |\n'
            line_string += build_wall(row)
        return line_string

    def bfs_reachable_exit_rooms(self, row, col):
        """
          Performs a BFS of the maze and checks exit is reachable from entrance
          and updates the visited field of all rooms that can reached.
        :param row: Int index
        :param col: Int index
        :return: Bool (if exit is reachable)
        """
        queue = deque()
        queue.append((row, col))
        found_Exit = False
        while len(queue) > 0:
            node = queue.popleft()
            if self.__maze[node[0]][node[1]].is_exit:
                found_Exit = True
            if self.is_valid_room(node[0]-1,node[1]):
                self.__maze[node[0]-1][node[1]].visited = True
                queue.append((node[0]-1,node[1]))
            if self.is_valid_room(node[0]+1,node[1]):
                self.__maze[node[0]+1][node[1]].visited = True
                queue.append((node[0]+1,node[1]))
            if self.is_valid_room(node[0],node[1]-1):
                self.__maze[node[0]][node[1]-1].visited = True
                queue.append((node[0],node[1]-1))
            if self.is_valid_room(node[0],node[1]+1):
                self.__maze[node[0]][node[1]+1].visited = True
                queue.append((node[0],node[1]+1))
        return found_Exit

    def is_valid_room(self, row, col):
        """
          Helper function to check maze traversal.
          Returns true if row,col is a valid room in the maze and if it can be entered.
          (not blocked and not visited)
        :param row: Int index
        :param col: Int index
        :return: Bool
        """
        return 0 <= row < self.__rowCount and 0 <= col < self.__colCount and self.__maze[row][col].can_enter

    def update_adv_pos(self, r_data, c_data):
        """
          Updates the position of the adventurer in the maze depending on the user input
        :return: Updated(current) position of the adventurer after the move.
        """
        if self.check_room(self.__adventurer_pos[0]+r_data, self.__adventurer_pos[1]+c_data):
            self.__adventurer_pos = (self.__adventurer_pos[0]+r_data, self.__adventurer_pos[1]+c_data)
            return self.__maze[self.__adventurer_pos[0]][self.__adventurer_pos[1]]
        else:
            return False

    # def update_room(self):
    #     curr_room = self.__maze[self.__adventurer_pos[0]][self.__adventurer_pos[1]]
    #     temp = {}
    #     if curr_room.get_treasure():
    #         temp["treasure"] = curr_room.get_treasure
    #         curr_room.set_treasure = False
    #     if curr_room.healing_potion:
    #         temp["healing_potion"] = curr_room.healing_potion
    #         curr_room.healing_potion = False
    #     if curr_room.vision_potion:
    #         temp["vision_potion"] = curr_room.vision_potion
    #     if curr_room.obstacle:
    #         temp["obstacle"] = curr_room.obstacle
    #     if curr_room.is_exit():
    #         temp["exit"] = curr_room.is_exit()
    #     return temp

    def check_room(self, row, col):
        """
          Helper function to see room exists and can be entered by the adventurer.
          Returns true if row,col is a valid room in the maze and if it can be entered.
          (not blocked)
        :param row: Int index
        :param col: Int index
        :return: Bool
        """
        return self.check_room_exists(row,col) and not self.__maze[row][col].is_impassable

    def display_curr_room(self):
        """
          Returns the string representation of the current room
        :return: String representation of the current room
        """
        return str(self.__maze[self.__adventurer_pos[0]][self.__adventurer_pos[1]])

    def check_room_exists(self, row, col):
        """
          Helper function to check a room exists at the (row,col) location in the maze.
        :param row: Int - row:location in the maze
        :param col: Int - col:location in the maze
        :return: Bool
        """
        return 0 <= row < self.__rowCount and 0 <= col < self.__colCount

    def use_vision_potion(self):
        """
          Returns a dictionary with the string representation of the adventurer's current room
          and its surrounding rooms.
        :return: Dictionary
        """
        dict_map = {}
        #Room - NW
        if self.check_room_exists(self.__adventurer_pos[0]-1,self.__adventurer_pos[1]-1):
            dict_map["NorthWest Location:"] = str(self.__maze[self.__adventurer_pos[0]-1][self.__adventurer_pos[1]-1])
        else:
                dict_map["NorthWest Location:"] = "No room"
        #Room - N
        if self.check_room_exists(self.__adventurer_pos[0]-1,self.__adventurer_pos[1]):
            dict_map["North Location:"] = str(self.__maze[self.__adventurer_pos[0]-1][self.__adventurer_pos[1]])
        else:
            dict_map["North Location:"] = "No room"
        #Room - NE
        if self.check_room_exists(self.__adventurer_pos[0]-1,self.__adventurer_pos[1]+1):
            dict_map["NorthEast Location:"] = str(self.__maze[self.__adventurer_pos[0]-1][self.__adventurer_pos[1]+1])
        else:
            dict_map["NorthEast Location:"] = "No room"
        #Room - W
        if self.check_room_exists(self.__adventurer_pos[0],self.__adventurer_pos[1]-1):
            dict_map["West Location:"] = str(self.__maze[self.__adventurer_pos[0]][self.__adventurer_pos[1]-1])
        else:
            dict_map["West Location:"] = "No room"
        #Room - C
        if self.check_room_exists(self.__adventurer_pos[0],self.__adventurer_pos[1]):
            dict_map["Current Location:"] = str(self.__maze[self.__adventurer_pos[0]][self.__adventurer_pos[1]])
        else:
            dict_map["Current Location:"] = "No room"
        #Room - E
        if self.check_room_exists(self.__adventurer_pos[0],self.__adventurer_pos[1]+1):
            dict_map["East Location:"] = str(self.__maze[self.__adventurer_pos[0]][self.__adventurer_pos[1]+1])
        else:
            dict_map["East Location:"] = "No room"
        #Room - SW
        if self.check_room_exists(self.__adventurer_pos[0]+1,self.__adventurer_pos[1]-1):
            dict_map["SouthhWest Location:"] = str(self.__maze[self.__adventurer_pos[0]+1][self.__adventurer_pos[1]-1])
        else:
            dict_map["SouthWest Location:"] = "No room"
        #Room - S
        if self.check_room_exists(self.__adventurer_pos[0]+1,self.__adventurer_pos[1]):
            dict_map["South Location:"] = str(self.__maze[self.__adventurer_pos[0]+1][self.__adventurer_pos[1]])
        else:
            dict_map["South Location:"] = "No room"
        #Room - SE
        if self.check_room_exists(self.__adventurer_pos[0]+1,self.__adventurer_pos[1]+1):
            dict_map["SouthEast Location:"] = str(self.__maze[self.__adventurer_pos[0]+1][self.__adventurer_pos[1]+1])
        else:
            dict_map["SouthEast Location:"] = "No room"
        return dict_map

# d = Dungeon()
# print(d)
