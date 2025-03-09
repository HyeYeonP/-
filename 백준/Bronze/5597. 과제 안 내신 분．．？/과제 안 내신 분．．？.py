a = []
b = set(range(1, 31))

for i in range(28):
  a.append(int(input()))

a1 = set(a)
b1 = list(b - a1)
b1.sort()

print(b1[0], b1[1], sep = '\n')