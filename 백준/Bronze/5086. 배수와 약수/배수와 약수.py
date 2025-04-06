def num(x,y):
  if x % y == 0:
    return 'multiple'

  elif y % x == 0:
    return 'factor'

  else:
    return 'neither'
    
results = []

while True:
  a, b = map(int, input().split())

  if a == 0 and b == 0:
    break

  else:
    results.append(num(a,b))

for result in results:
  print(result, sep='\n')