from typing import List
import math


class Vector:
    '''Класс реализует N-мерный вектор'''

    def __init__(self, coordinats: List[int]):
        self.coordinats = coordinats

    def __len__(self):
        return len(self.coordinats)

    def __str__(self):
        return f'{self.coordinats}'

    def __getitem__(self, i: int):
        return self.coordinats[i]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError(f"left != right: {len(self)} != {len(other)}")
        else:
            return Vector([self[i] + other[i] for i in range(len(self))])

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError(f"left != right: {len(self)} != {len(other)}")
        else:
            return Vector([self[i] * other[i] for i in range(len(self))])
    
    def __eq__(self, other):
        if self.coordinats == other.coordinats:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.coordinats != other.coordinats:
            return True
        else:
            return False

    def __abs__(self):
        r = 0
        for i in self.coordinats:
            r += i**2
        return math.sqrt(r)
    
    def __lt__(self,other):
        if abs(self) < abs(other):
            return True
        else:
            return False

    def __gt__(self,other):
        if abs(self) > abs(other):
            return True
        else:
            return False

    def __le__(self,other):
        if abs(self) <= abs(other):
            return True
        else:
            return False

    def __ge__(self,other):
        if abs(self) >= abs(other):
            return True
        else:
            return False

v1 = Vector([1, 2, 3])
v2 = Vector([3, 2, 1])


print(v1 + v2)
print(v1 * v2)
print(v1 == v2, v1 >= v2)

