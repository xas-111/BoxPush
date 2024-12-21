import numpy as np

class GameMap:
    def __init__(self, height, width, box_location, hole_location, starting_position, obsticle_location):
        self.map = np.zeros((height, width))
        for hole_point in hole_location:
            self.map[hole_point[0], hole_point[1]] = 1
        for ob_point in obsticle_location:
            self.map[ob_point[0], ob_point[1]] = -1
        self.start = starting_position
        self.now = starting_position
        self.width = width
        self.height = height
        self.win = hole_location
        self.boxes = box_location
        
    def moveUp(self):
        target_position = (self.now[0], self.now[1]-1)
        # outside bound
        if (target_position[0] < 0 or target_position[0] > self.width - 1):
            #invalid move
            return
        
        # hits a wall
        if (self.map[target_position[0], target_position[1]] == -1):
            #invalid move
            return
        
        # hits a box
        for index, value in self.boxes:
            if (target_position == value):
                # check if the box can be pushed
                if (self.map[value[0], value[1]+1] != -1):
                    if (value[0], value[1]+1) not in self.boxes:
                        self.boxes[index] = (value[0], value[0+1])
                        break
        self.now = target_position