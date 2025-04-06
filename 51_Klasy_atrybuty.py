class Point:

    points_counter = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points_counter += 1
    
    def move_point(self, x = 0, y = 0):
        self.x = x
        self.y = y

p1 = Point(1,2)
p2 = Point(3,4)
P3 = Point(4,5)



print(Point.points_counter)
print(p1.points_counter)