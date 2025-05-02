n, k = map(int, input().split())
list_a = []

list_a = list(map(int, input().split()))

if len(list_a) != n:
  print('error')

else:
  list_a.sort()
  print(list_a[n-k])