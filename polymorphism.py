import math


class TrianglePerimeter:
    def perimeter(self, *args):
        per = 0
        j = 0
        while j < 3:
            per += args[j]
            j += 1
        return per

class QuadrilateralPerimeter:
    def perimeter(self, *args):
        per = 0
        j = 0
        while j < 4:
            per += args[j]
            j += 1
        return per

class CirclePerimeter:
    def perimeter(self, *args):
        per = 0
        for i in args:
            per += i
        return per

triangle = TrianglePerimeter()
quadrilateral = QuadrilateralPerimeter()
circle = CirclePerimeter()

array = [triangle, quadrilateral, circle]

for i in array:
    print(i.perimeter(1,2,3,4,5,6,7))

