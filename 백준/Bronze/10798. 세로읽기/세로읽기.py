list_a = []

for _ in range(5):
  list_a.append(list(str(input()))) 

max_len = max(len(word) for word in list_a)
result = [[] for _ in range(max_len)]

for i in range(max_len):
  for word in list_a:
    if i < len(word):
      result[i].append(word[i])

answer = ''
for i in result:
  for alpha in i:
    answer += alpha

print(answer)