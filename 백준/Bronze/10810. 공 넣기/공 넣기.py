n, m = map(int, input().split())
a = [0] * (n+1)

for _ in range(m):
  i, j, k = map(int, input().split())
  for h in range(i, j+1):
    a[h] = k

for b in range(1, n+1):
  print(a[b], end = ' ')