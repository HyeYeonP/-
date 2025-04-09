def find_num(a):
  results = []

  for i in range(1, a+1):
    if a % i == 0:
      results.append(i)

      if len(results) > 2:
        return False

  return len(results) == 2

n = int(input())
list_num = list(map(int, input().split()))

if len(list_num) != n:
  print('wrong input')

else:
  num = 0

  for i in list_num:
    if find_num(i):
      num += 1
    
  print(num)