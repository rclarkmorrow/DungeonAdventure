import random
import numpy as np

class Room():
    """
      creates a room.
    """
    def __init__(self):
        #corresponds to the four doors North, South, West and East.
        #initially all doors are open and so set to true.
        self.doors = [True, True, True, True]

    def __str__(self):
        return "room"

class RoomFactory():
    def create_rooms(r,c):
        """
        Returns a list of lists consisting of rooms with the doors in the outer edges set to False(closed).
        :param r: the number of rows
        :param c: the number of columns
        :return: list of lists of rows
        """
        rooms = []
        for num in range(r):
            rows = []
            for num in range(c):
                rows.append(Room())
            rooms.append(rows)
        #establishing the closed doors for the rooms in the outer borders.
        for room in rooms[0]:
            #setting north to False for rooms in first row
            room.doors[0] = False
        for room in rooms[r-1]:
            #setting south to False for rooms in last row
            room.doors[1] = False
        for num in range(r-1):
            #setting west to False for rooms in first column
            rooms[num][0].doors[2] = False
        for num in range(r-1):
            #setting east to False for rooms in last column
            rooms[num][c-1].doors[3] = False
        return rooms

class Dungeon():
    """
      builds a dungeon
    """
    def __init__(self,r,c):
        self.rows = r
        self.columns = c
        self.grid = RoomFactory.create_rooms(self.rows,self.columns)
        self.entrance = self.grid[0][0]
        self.exit = self.grid[r-1][c-1]

    def __str__(self):
        out_li = []
        for elem in self.grid:
            out = []
            for item in elem:
                out.append(item.__str__())
            out_li.append(",".join(out))
        return "\n".join(out_li)

    def gen_maze(self):
        count =0
        while count < 5:
            random_row = random.choice(range(0,self.rows))
            random_col = random.choice(range(0,self.columns))
            random_room = self.grid[random_row][random_col]
            random_door = random.choice(range(0,4))
            if not random_room.doors[random_door]:
                break
            else:
                random.choice(range(0,self.columns))
                print(random_row,random_col)
                random_room.doors[random_door] = False
                count += 1
            print("deleted",random_room.doors)


d1 = Dungeon(5,5)
print(d1.__str__())
print(d1.entrance)
print(d1.exit)
d1.gen_maze()
