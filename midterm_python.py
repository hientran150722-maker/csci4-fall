import math
def distance(x2: float, y2: float, x1: float, y1: float) -> float:
    d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return d
print(distance(5, 4, 1, 1))

