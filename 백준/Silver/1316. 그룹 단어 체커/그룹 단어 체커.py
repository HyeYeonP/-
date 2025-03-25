def check_word(word):
  used_word = []

  for j in range(len(word)):
    alpha = word[j]

    if alpha in used_word and alpha != word[j - 1]:
      return False

    used_word.append(alpha)
  
  return True
      


num = int(input())
num_word = 0

for i in range(num):
  word = str(input())

  if check_word(word):
    num_word += 1

print(num_word)