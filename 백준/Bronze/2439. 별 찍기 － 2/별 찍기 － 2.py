a = int(input())
Num = 0

for i in range(1, a+1):
    Num += 1
    Answer = "%{0}s".format(a) % ('*' * Num)
    print(Answer)