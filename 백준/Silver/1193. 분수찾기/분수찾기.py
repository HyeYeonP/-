x = int(input())
count = 0
n_line = 0

while count < x:
    n_line += 1
    count += n_line

diff = count - x

if n_line % 2 == 0:
    a = n_line - diff
    b = 1 + diff
else:
    a = 1 + diff
    b = n_line - diff

print(f'{a}/{b}')