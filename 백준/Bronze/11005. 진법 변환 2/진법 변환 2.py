a, num = map(int, input().split())
result = ''

while a > 0:
  a, b = divmod(a, num)

  if b >= 10:
    result += str(chr(b + ord('A') - 10))
  
  else:
    result += str(b)

print(result[::-1])