Num = int(input())
Answer = ''
Sum = 0

for i in range(1, Num+1):
    a, b = map(int, input().split())
    Sum += 1
    Line = '%d + %d = %d' % (a, b, a+b)
    
    Answer += 'Case #%d: ' % Sum + Line + '\n'

print(Answer)