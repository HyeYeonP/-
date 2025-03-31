num = int(input())
paper = [[0] * 100 for _ in range(100)] 

for _ in range(num):
  a, b = map(int, input().split())

  for i in range(a, a+10):

    for j in range(b, b+10):
      paper[i][j] = 1

paper_extent = sum(sum(k) for k in paper)
print(paper_extent)