n = int(input())
dot = 2

for _ in range(n):
  dot_num = (2*dot - 1)**2
  dot += dot - 1

print(dot_num)