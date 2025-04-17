list_angle = []

for _ in range(3):
  num = int(input())
  list_angle.append(num)

set_angle = set(list_angle)

if sum(list_angle) != 180:
  print('Error')

elif len(set_angle) == 1 and sum(list_angle) == 180:
  print('Equilateral')

elif len(set_angle) == 2 and sum(list_angle) == 180:
  print('Isosceles')

else:
  print('Scalene')