matrix_a, matrix_b = [], []
n, m = map(int, input().split())

for i in range(n):
  i = list(map(int, input().split()))
  matrix_a.append(i)

for i in range(n):
  i = list(map(int, input().split()))
  matrix_b.append(i)

for i in range(n):
  for j in range(m):
    print(matrix_a[i][j] + matrix_b[i][j], end=' ')
  print()