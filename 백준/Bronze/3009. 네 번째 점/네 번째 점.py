list_x = []
list_y = []

for _ in range(3):
  a, b = map(int, input().split())

  list_x.append(a)
  list_y.append(b)

x4 = 0
y4 = 0

for i in range(3):
  if list_x.count(list_x[i]) == 1:
    x4 = list_x[i]

  if list_y.count(list_y[i]) == 1:
    y4 = list_y[i]

print(x4, y4)