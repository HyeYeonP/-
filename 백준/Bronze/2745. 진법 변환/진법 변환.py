alpha, num = input().split()
num = int(num)
result = 0

for i, j in enumerate(reversed(alpha)):
  if '0' <= j <= '9':
    result += int(j)*(num**i)
  
  else:
    result += (ord(j) - ord('A') + 10)*(num**i)

print(result)