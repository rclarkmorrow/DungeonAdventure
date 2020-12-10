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

        return "Health potion: " + str(self.__healthPotion) + "\n" \
               + "Vision potion: " + str(self.__visionPotion) + "\n" \
               + "Pillar: " + str(self.__pillar) + "\n" \
               + "Pit: " + str(self.__pit) + "\n" \
               + "Entrance: " + str(self.__entrance) + "\n" \
               + "Exit: " + str(self.__exit) + "\n" \
               + "Impassable: " + str(self.__impassable) + "\n\n"



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
    def __init__(self, row_count = 5, col_count = 5, block = 5):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count
        self.__block = block
        # Adding rooms to the maze (Default 2D grid of rooms)
        for r in range(0, self.__rowCount):
            self.__maze.append([Room() for c in range(0, self.__colCount)])
        # To set entrance, exit, blocks and additional features to the maze:
        self.build_maze()

    def build_maze(self):
        # To randomly set an entrance and exit
        rand_row = random.choice(range(0,self.__rowCount))
        rand_col = random.choice(range(0,self.__colCount))
        self.__maze[rand_row][rand_col].set_entrance()
        print(f"entrance:[{rand_row}][{rand_col}]")
        count = 0
        while count == 0:
            rand_row = random.choice(range(0,self.__rowCount))
            rand_col = random.choice(range(0,self.__colCount))
            if not self.__maze[rand_row][rand_col].is_entrance():
                self.__maze[rand_row][rand_col].set_exit()
                print(f"exit:[{rand_row}][{rand_col}]")
                count += 1
        # make some rooms impassible (making 5 rooms impassable)
        block = 0
        while block < self.__block:
            rand_row = random.choice(range(0,self.__rowCount))
            rand_col = random.choice(range(0,self.__colCount))
            if not self.__maze[rand_row][rand_col].is_entrance() and \
                    not self.__maze[rand_row][rand_col].is_exit() and \
                    not self.__maze[rand_row][rand_col].is_impassable():
                self.__maze[rand_row][rand_col].set_impassable()
                block += 1
                print(f"blocked room at [{rand_row}][{rand_col}]")


    def __str__(self):
        out_li = []
        for elem in self.__maze:
            out = []
            for item in elem:
                out.append(item.__str__())
            out_li.append(",".join(out))
        return "\n".join(out_li)

    def print_maze(self):
        # print(self.__maze)
        for row in range(0, self.__rowCount):
            print("row ", row)
            for col in range(0, self.__colCount):
                print(self.__maze[row][col].__str__())
            print()

    def traversable_bfs(self):
        queue = deque()
        queue.append(self.__maze[0][0])
        while len(queue)>0:
            node = queue.popleft()
            if node == self.exit:
                return True
            if node.doors[0]:
                queue.append(self.grid[node.row-1][node.col])
            if node.doors[1]:
                queue.append(self.grid[node.row+1][node.col])
            if node.doors[2]:
                queue.append(self.grid[node.row][node.col-1])
            if node.doors[3]:
                queue.append(self.grid[node.row][node.col+1])
        return False

d1 = Dungeon(5,5)
d1.print_maze()
print("printing",d1)
#d1.gen_maze()
#print("Traversable:",d1.traversable_bfs())
