list_n = []

for _ in range(5):
  n = int(input())
  list_n.append(n)

average_n = sum(list_n) // 5
median_n = sorted(list_n)[2]

print(average_n)
print(median_n)