class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.sz = length
        self.sz2 = width

    def area(self):
        return self.sz * self.sz2

x, y = input().split()
x = int(x)
y = int(y)
ans = Rectangle(x, y)

print(ans.area())