# elke class heeft een UpperCamelCase ClasName
# dus start met Capital Letter
# je kan hier zetten: class Rectangle(object): maar dat laat je weg want default
class Rectangle:
    # Docstring to document the purpose
    """
    This class is an example
    """

    # Constructor
    # Starts with Double Underscore -> dunder methods
    # Mandatory
    def __init__(self, widthArg, heightArg, colorArg='black'):
        self.width = widthArg
        self.height = heightArg
        self.color = colorArg

    def getWidth(self):
        pass

    def setWidth(self):
        pass

    # def area(self)-> float:
    #     return round(self.width * self.height)
    
    # variant:
    def getArea(self)-> float:
        self.area = round(self.width * self.height)
        return self.area
    # vervolgens kan je self.area = round(self.width * self.height) ook bij de __init__ zetten.

    def getColor(self):
        return self.color
    
# Each class inherits from Rectangle
class Box(Rectangle):

    def __init__(self, widthArg, heightArg, depthArg):
        super().__init__(widthArg, heightArg)
        self.depth = depthArg
        self.areabox = 4*widthArg*heightArg + 2*heightArg*depthArg

    def getDepth(self):
        return self.depth
    
    def getAreaBox(self):
        return self.areabox

#class inherits from Rectangle
class Triangle(Rectangle):
    def __init__(self, widthArg, heightArg, thirdSideArg):
        super().__init__(widthArg, heightArg)
        self.thirdSide = thirdSideArg

    
