num = int(input())

for _ in range(num):
  money = int(input())
  result = [0, 0, 0, 0]

  while money > 0:
    if money >= 25:
      money -= 25
      result[0] += 1

    elif money >= 10:
      money -= 10
      result[1] += 1

    elif money >= 5:
      money -= 5
      result[2] += 1

    else:
      money -= 1
      result[3] += 1

  print(*result)