from BaseFigure import BaseFigure


class Triangle(BaseFigure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    @classmethod
    def n_dots(cls) -> int:
        return 3

    def area(self) -> float:
        p = (self.a + self.b + self.c)/2  # полупериметр

        # формула
        return p * (p - self.a) * (p - self.b) * (p - self.c)

    def validate(self):
        if not ((self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)):
            raise ValueError("sides are wrong")


class Rectangle(BaseFigure):
    def __init__(self,a: float, b: float, c: float, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        super().__init__()
    
    @classmethod
    def n_dots(cls) -> int:
        return 4

    def area(self) -> float:
        return self.a*self.b 

    def validate(self):
        if (self.a != self.c) or (self.b != self.d):
            raise ValueError("Not a rectangle. Check equality of opposite sides")

class Circle(BaseFigure):
    def __init__(self, r: int):
        self.r = r
        super().__init__()

    @classmethod
    def n_dots(cls) -> float:
        return float('inf')
    
    def area(self) -> float:
        return 3.14 * self.r

    def validate(self):
        pass



tri = Triangle(3, 4, 5)
rec = Rectangle(3, 4, 3, 4)
cir = Circle(5)
print(rec.n_dots(), rec.area())
print(tri.n_dots(), tri.area())
print(cir.n_dots(), cir.area())
