class Shape:
    def __init__(self, color):
        self.color = color

    def show_color(self):
        return f"color : {self.color}"


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def area(self):
        return f"Area : {self.side * self.side}"


shape1 = Square(4, "blue")
print(shape1.show_color())
print(shape1.area())
