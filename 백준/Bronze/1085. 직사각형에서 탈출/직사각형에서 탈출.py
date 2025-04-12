x, y, w, h = map(int, input().split())
list_dot = [x, y, w-x, h-y]

print(min(list_dot))