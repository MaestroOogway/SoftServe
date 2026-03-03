class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__("rectangle")  # name
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(5, 3)
print("Area:", rect.area())