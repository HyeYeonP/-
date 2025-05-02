import sys

n = int(sys.stdin.readline())
list_n = []

for _ in range(n):
    a = int(sys.stdin.readline())
    list_n.append(a)

list_n.sort()

for i in list_n:
    print(i)