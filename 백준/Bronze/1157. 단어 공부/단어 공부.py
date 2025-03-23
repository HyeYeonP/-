a = input().upper()
list_a = list(a)
set_a = set(list_a)
list_max = []
max = 0

for i in set_a:

  if list_a.count(i) > max:
    max = list_a.count(i)
    list_max.clear()
    list_max.append(i)

  elif list_a.count(i) == max:
    max = list_a.count(i)
    list_max.append(i)

  else:
    continue

if len(list_max) == 1:
  print(*list_max)
else:
  print('?')