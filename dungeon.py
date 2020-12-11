import random
from collections import deque

class Room():
    """
      creates a room.
    """
    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = "No pillar"
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

    def set_visited(self, visited):
        self.__visited = visited

    def set_entrance(self):
        self.__entrance = True

    def set_exit(self):
        self.__exit = True

    def set_impassable(self):
        self.__impassable = True


class Dungeon():
    """
      builds a dungeon
    """
    def __init__(self, row_count = 5, col_count = 5, block = 0.2):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count
        self.__block = block
        self.entrance_pos = None
        self.exit_pos = None
        self.build_maze()

    def build_maze(self):
        # Adding rooms to the maze (Default 2D grid of rooms)
        for r in range(0, self.__rowCount):
            self.__maze.append([Room() for c in range(0, self.__colCount)])
        # To randomly set an entrance and exit
        rand_row = random.randrange(0,self.__rowCount)
        rand_col = random.randrange(0,self.__colCount)
        self.__maze[rand_row][rand_col].set_entrance()
        self.entrance_pos = [rand_row, rand_col]
        print(f"entrance:[{rand_row}][{rand_col}]")
        count = 0
        while count == 0:
            rand_row = random.randrange(0,self.__rowCount)
            rand_col = random.randrange(0,self.__colCount)
            if not self.__maze[rand_row][rand_col].is_entrance():
                self.__maze[rand_row][rand_col].set_exit()
                self.exit_pos = [rand_row, rand_col]
                print(f"exit:[{rand_row}][{rand_col}]")
                count += 1
        # make some rooms impassible (making 5 rooms impassable)
        block = 0
        while block < self.__block*self.__rowCount*self.__colCount:
            rand_row = random.randrange(0,self.__rowCount)
            rand_col = random.randrange(0,self.__colCount)
            if not self.__maze[rand_row][rand_col].is_entrance() and \
                    not self.__maze[rand_row][rand_col].is_exit() and \
                    not self.__maze[rand_row][rand_col].is_impassable():
                self.__maze[rand_row][rand_col].set_impassable()
                block += 1
                print(f"blocked room at [{rand_row}][{rand_col}]")
        #Check maze is traversable from entrance to exit and get a list of rooms that can be reached.
        reachable_exit_rooms = self.bfs_reachable_exit_rooms(self.entrance_pos[0],self.entrance_pos[1])
        print("test",reachable_exit_rooms)
        if not reachable_exit_rooms:  #exit is not reachable
            self.build_maze()

    def __str__(self):
        out_li = []
        for row in self.__maze:
            out_li.append(",".join([item.__str__() for item in row]))
        return "\n".join(out_li)

    def print_maze(self):
        # print(self.__maze)
        for row in range(0, self.__rowCount):
            print("row ", row)
            for col in range(0, self.__colCount):
                print(self.__maze[row][col].__str__())
            print()

    def bfs_reachable_exit_rooms(self,row,col):
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

    #initial call if you know entrance is 0,0 would be traverse(0, 0)
    def traverse(self, row, col):
        print(row,col)
        found_exit = False
        if self.is_valid_room(row, col):
            self.__maze[row][col].set_visited(True)
            # check for exit
            if self.__maze[row][col].is_exit():
                return True
            # not at exit so try another room: south, east, north, west
            found_exit = self.traverse(row + 1, col)#south
            if not found_exit:
                found_exit = self.traverse(row, col + 1)#east
            if not found_exit:
                found_exit = self.traverse(row - 1, col)#north
            if not found_exit:
                found_exit = self.traverse(row, col - 1)#west

            # if we did not reach the exit from this room we need mark it as visited to
            # avoid going into the room again
            if not found_exit:
                self.__maze[row][col].set_visited(True)

        else:  # tried to move into a room that is not valid
            return False
        return found_exit

    def is_valid_room(self, row, col):
        return 0 <= row < self.__rowCount and 0 <= col < self.__colCount and self.__maze[row][col].can_enter()


d1 = Dungeon(5,5)
#d1.print_maze()
print(d1)
#print("Traversable:",d1.traversable_bfs(d1.entrance_pos[0],d1.entrance_pos[1]))
"""
if d1.traverse(d1.entrance_pos[0],d1.entrance_pos[1]):
    print("whoo hoo, we reached the exit")
else:
    print("exit not reachable")
"""