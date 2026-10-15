import math
def distance(x2: int, y2: int, x1: int, y1: int) -> int:
    d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return d
print(distance(5, 4, 1, 1))

