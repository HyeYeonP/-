a = input()
list_cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in list_cro:
  a = a.replace(i, '*')

print(len(a))