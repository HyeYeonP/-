n = int(input())
list_n = []

for _ in range(n):
  a = int(input())
  list_n.append(a)

for i in sorted(list_n):
  print(i, sep= '\n')