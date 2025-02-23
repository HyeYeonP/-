a, b, c = map(int, input().split())
s1 = set([a, b, c])
l1 = [a, b, c]
l1.sort()

if len(s1) == 1:
    print(10000+a*1000)
elif len(s1) == 2:
    print(1000+l1[1]*100)
else:
    print(l1[-1]*100)