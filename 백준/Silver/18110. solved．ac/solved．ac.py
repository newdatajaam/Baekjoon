import sys
input = sys.stdin.readline

n = int(input())
score = []

if n==0:
  print(0)
else:
  trim_score = int(n * 0.15 + 0.5)

  for i in range(n):
    score.append(int(input()))
  score.sort()
  score = score[trim_score:(len(score) - trim_score)]
  
  print(int(sum(score)/len(score)+0.5))