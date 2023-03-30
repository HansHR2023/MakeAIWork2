"""
Uitleg in de aantekeningen Makeaiwork2
"""

# ------------------------------------------

from Shape_v2 import Shape

# ------------------------------------------

class Button:

    def __init__(self, bgColor, text):
        self.backgroundColor = bgColor
        self.text = text

        self.shape = Shape()

    def click(self):
        print(f"Press button {self.text}.")

# ------------------------------------------

# Create a button
btn1 = Button(0, 'Black')

btn1.shape.width = 100
btn1.shape.height = 100

btn2 = Button(255, 'White')

btn2.shape.width = 100
btn2.shape.height = 100

btn1.click()
btn2.click()

# Add a breakpoint
print('')

# -----------------------------------------