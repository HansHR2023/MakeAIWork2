from tetris_objects import Figure
import numpy as np

# Create block object from class Figure
blockShape = np.array([])
block = Figure(blockShape, "blue")
print(block.getColor)
