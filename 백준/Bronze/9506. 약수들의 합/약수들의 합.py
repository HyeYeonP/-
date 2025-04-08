def perfect_num(a):
  results = []

  for i in range(1, a):
    if a % i == 0:
      results.append(i)
    else:
      continue

  if sum(results) == a:
    return True, results
  
  else:
    return False, []

while True:
  n = int(input())

  if n == -1:
    break
  
  is_perfect, results = perfect_num(n)

  if is_perfect:
    print(n, '=', end=" ")
    print(*results, sep=' + ')

  else:
    print(n, 'is NOT perfect.')