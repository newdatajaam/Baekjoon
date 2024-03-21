# 1388번 바닥장식
vert, hori  = map(int, input().split())
floor = []
for _ in range(vert):
  floor.append(list(input()))

cnt = 0

for i in range(vert):
  for j in range(hori-1):
    if floor[i][j] == '-' and floor[i][j+1] == '|':
      cnt += 1
  if floor[i][-1] == '-':
    cnt += 1

for i in range(hori):
  for j in range(vert-1):
    if floor[j][i] == '|' and floor[j+1][i] == '-':
        cnt += 1
  if floor[-1][i] == '|':
    cnt += 1

print(cnt)
