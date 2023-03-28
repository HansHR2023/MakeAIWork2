import numpy as np
from random import randrange

"""
Classnames always UpperCamelCase
test
"""


class Figure:
    # Constructor method
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    # Returns attribute color
    def getColor(self):
        get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))
        return self.color

    # Returns Shape (Numpy Array)
    def getShape(self):
        figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

        return self.shape

    # Change shape by multiplying with Numpy Array
    # self.shape gets new shape
    # self.shape = np.rot90(self.shape, 1 , axes=(1,0)
    def rotate(self):
        center = figure[0]
        figure_old = deepcopy(figure)
        if rotate:
            for i in range(4):
                x = figure[i].y - center.y
                y = figure[i].x - center.x
                figure[i].x = center.x - x
                figure[i].y = center.y + y
                if not check_borders():
                    figure = deepcopy(figure_old)
                    break
        return rotate
# 