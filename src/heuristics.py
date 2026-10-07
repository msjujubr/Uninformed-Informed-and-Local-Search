import math
from typing import Tuple

Pos = Tuple[int, int]

def manhattan(a: Pos, b: Pos) -> float:
    x1, y1 = a
    x2, y2 = b
    dx = x1 - x2 if x1 >= x2 else x2 - x1
    dy = y1 - y2 if y1 >= y2 else y2 - y1
    return dx + dy


def euclidean(a: Pos, b: Pos) -> float:
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5