def find_num(a):
  results = []

  for i in range(1, a+1):
    if a % i == 0:
      results.append(i)

      if len(results) > 2:
        return False

  return len(results) == 2

m = int(input())
n = int(input())
sum_num = 0
list_num = []

for i in range(m, n+1):
  if find_num(i):
    sum_num += i
    list_num.append(i)

if list_num:
  print(sum_num)
  print(list_num[0])

else:
  print(-1)