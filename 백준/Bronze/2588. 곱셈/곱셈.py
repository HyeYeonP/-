a = int(input())
b = int(input())

b_1 = b%10
b_2 = b//10%10
b_3 = b//100

print(a*b_1, a*b_2, a*b_3, a*b, sep='\n')