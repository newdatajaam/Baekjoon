quiz_num = int(input())
ans = []
for i in range(quiz_num):
  quiz = input()
  score = 0
  total_score = 0
  for j in quiz:
    if j == 'O':
      score += 1
      total_score += score
    else:
      score = 0
  ans.append(total_score)

for a in ans:
  print(a)