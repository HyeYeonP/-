import math

a, b, v = map(int, input().split())

if a >= v:
    print(1)
else:
    day = (v - a) / (a - b)
    print(math.ceil(day) + 1)