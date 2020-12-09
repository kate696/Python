class Shape:
    def __init__(self, a=None, b=None, c=None):
        self.set_params(a, b, c)

    def set_params(self, a, b, c):
        self._a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self._a

    def __repr__(self):
        result = self.__class__.__name__
        result += "["
        if self._a!=None:
           result+= str(self._a)
        if self.b!=None:
            result += ", " + str(self.b)
        if self.c!=None:
            result += ", " + str(self.c)
        result+= "] at " + str(hex(id(self)))
        return result




class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b


import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2


r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())


c = Circle(7)
print(c)
print(c.calc_surface())



class Triangle(Shape):
    def calc_perim(self):
        return self._a+self.b+self.c


class EquilateralTriangle(Shape):
    def calc_perim(self):
        return self._a+self.b+self.c


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


t = Triangle(3, 6, 6)
print(t, "Perimeter =", t.calc_perim())

Et = EquilateralTriangle(6, 6, 6)
print(Et, "Perimeter =", Et.calc_perim())

s = Square(3)

print(s, "Surface = ", s.calc_surface())

# some code that tests the new functionality and structures
t = Triangle(5, 4, 4)
print(t, "Perimeter =", t.calc_perim())


Et = EquilateralTriangle(5, 5, 5)
print(Et, "Perimeter =", Et.calc_perim())


s = Square(8)

print(s, "Surface = ", s.calc_surface())