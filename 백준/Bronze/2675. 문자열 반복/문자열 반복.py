a = int(input())

for _ in range(a):
  r, s = input().split()
  p = ''

  for i in s:
    p += i * int(r)
  
  print(p, end = '\n')