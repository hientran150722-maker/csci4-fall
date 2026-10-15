import math


def distance (x: int, y: int) -> float:
    d = math.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)
    return d
print(distance((2, 3), (3, 4)))



