import math

def solve_quadratic(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D < 0:
        return None
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
    return x1, x2

def viet_quadratic(x1, x2):
    p = -1 * (x1 + x2)
    q = x1 * x2
    return p, q
