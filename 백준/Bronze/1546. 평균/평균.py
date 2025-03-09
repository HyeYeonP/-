a = int(input())
b = list(map(int, input().split()))
b1 = max(b)

for i in range(a):
  b[i] = b[i]/b1*100

b2 = sum(b)/a

print(b2)