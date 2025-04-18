results = []

while True:
  a, b, c = map(int, input().split())
  list_line = []
  list_line.extend([a, b, c])

  if a == 0 and b == 0 and c == 0:
    break

  elif max(list_line) >= (sum(list_line) - max(list_line)):
    results.append('Invalid')

  elif len(set(list_line)) == 1:
    results.append('Equilateral')

  elif len(set(list_line)) == 2:
    results.append('Isosceles')

  else:
    results.append('Scalene')

for result in results:
  print(result, sep='\n')