import sys
from itertools import combinations

n, m = map(int, input().split())
list_num = list(map(int, input().split()))
max_sum = 0

for i in combinations(list_num, 3):
  num_sum = sum(i)

  if num_sum <= m:
    max_sum = max(max_sum, num_sum)

print(max_sum)