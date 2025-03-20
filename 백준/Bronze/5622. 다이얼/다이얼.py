num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = str(input())
sum = 0

for i in range(len(a)):
    for j in num:
        if a[i] in j:
            sum += num.index(j) + 3
            
print(sum)