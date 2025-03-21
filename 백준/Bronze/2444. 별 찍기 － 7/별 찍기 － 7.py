a = int(input())

for i in range(1, 2*a):
  if i <= a:
    star = "{0:>{width}}".format("*"*(2*i-1), width = (a+i-1))
    print(star)
  else:
    star = "{0:>{width}}".format("*"*((2*a-1)-2*(i-a)), width = ((2*a)-(i-a)-1))
    print(star)