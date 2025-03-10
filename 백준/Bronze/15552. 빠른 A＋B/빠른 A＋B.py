import sys

num = int(sys.stdin.readline())
answer = []

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    answer.append(a + b)

sys.stdout.write('\n'.join(map(str, answer)) + '\n')