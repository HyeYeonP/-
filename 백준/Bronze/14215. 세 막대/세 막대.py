a, b, c = map(int, input().split())
list_tri = [a, b, c]

while True:
  max_tri = max(list_tri)
  sum_tri = sum(list_tri) - max_tri

  if max_tri >= sum_tri:
    list_tri[list_tri.index(max_tri)] -= 1
  
  else:
    results = sum(list_tri)
    break

print(results)