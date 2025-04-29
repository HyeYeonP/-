n = int(input())

count = 0
num = 666
str_num = "666"

while True:
    if str_num in str(num):
        count += 1
            
        if count == n:
            print(num)
            break
                
    num += 1