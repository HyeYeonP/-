n, m = map(int, input().split())
a = list(range(1, n+1))

for _ in range(m):
  i, j = map(int, input().split())
  a[i-1:j] = reversed(a[i-1:j])

for b in range(n):
  print(a[b], end = ' ') 