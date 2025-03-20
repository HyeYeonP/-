sum = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
num = []

for i in range(6):
  num.append(sum[i] - a[i])

print(*num)