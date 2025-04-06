class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move_point(self, x = 0, y = 0):
        self.x = x
        self.y = y

p1 = Point(3,5)
p2 = Point(4,6)
p3 = Point()

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y)

p1.x = 10
p1.y = 20
print(p1.x, p1.y)


p1.move_point(12,4)
print(p1.x, p1.y)