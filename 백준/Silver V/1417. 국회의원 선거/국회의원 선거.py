n = int(input())
vote = []
cnt = 0
for i in range(n):
  if i == 0:
    dasom = int(input())
  else:
    vote_num = int(input())
    vote.append(vote_num)

if vote == []:
  print(0)
else:
  while dasom <= max(vote):
    max_idx = vote.index(max(vote))
    vote[max_idx] -= 1
    dasom += 1
    cnt += 1
  print(cnt)