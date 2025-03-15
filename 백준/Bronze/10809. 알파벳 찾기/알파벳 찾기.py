a = str(input())
list_a = [chr(i) for i in range(ord('a'),ord('z')+1)]

for i in list_a:
  print(a.find(i), end = ' ')