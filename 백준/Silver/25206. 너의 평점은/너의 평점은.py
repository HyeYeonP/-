sum_mark = 0
sum_score = 0

for i in range(20):
  name, mark, grade = input().split()

  grade_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
  }

  score = grade_score.get(grade)

  if grade == 'P':
    continue
  
  else:
    sum_score += float(mark) * float(score)
    sum_mark += float(mark)

print(sum_score / sum_mark)