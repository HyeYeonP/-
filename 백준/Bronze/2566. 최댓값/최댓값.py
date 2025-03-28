int_max = 0
list_index = []

for i in range(9):
  n = list(map(int, input().split()))

  if max(n) >= int_max:
    int_max = max(n)
    list_index.clear()
    list_index.append(i + 1)
    list_index.append(n.index(max(n)) + 1)
  
  else:
    continue

print(int_max)
print(*list_index)