def find_num(a):
  results = []

  for i in range(1, a+1):
    if a % i == 0:
      results.append(i)

      if len(results) > 2:
        continue

  return results

n = int(input())
list_num = find_num(n)

for result in list_num[1::]:
  if n == result:
    print(result)
    break

  while n % result == 0:
    n /= result
    print(result)