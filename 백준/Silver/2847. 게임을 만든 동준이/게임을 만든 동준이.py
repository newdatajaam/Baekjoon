import sys
input = sys.stdin.readline
n = int(input())
score_list = []
cnt = 0

for _ in range(n):
  score = int(input())
  score_list.append(score)

score_list.reverse()

for i in range(1,n):
  if score_list[i] >= score_list[i-1]:
    cnt += score_list[i] - score_list[i-1] + 1
    score_list[i] = score_list[i-1] - 1
print(cnt)