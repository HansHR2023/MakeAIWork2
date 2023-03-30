"""
Uitleg in de aantekeningen Makeaiwork2
"""

# ------------------------------------------

class Shape:

    def __init__(self):
        self.width = 0
        self.height = 0

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

btn2 = Button(255, 'White')

btn1.click()
btn2.click()

# Add a breakpoint
print('')

# -----------------------------------------