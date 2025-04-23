def sum_m(num):
    return sum(map(int, str(num)))

n = int(input())

for i in range(n):
  if n == i + sum_m(i):
    print(i)
    break
    
  elif i == n - 1:
    print(0)
  
  else:
    continue