import math

a, b, c, d, e, f = map(int, input().split())

determinant = a * e - b * d

if abs(determinant) > 1e-9:
    x = (c * e - b * f) / determinant
    y = (a * f - c * d) / determinant
    print(int(x), int(y))