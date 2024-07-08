n = int(input())
body = []
ranks = [1]*n

for i in range(n):
  body.append(list(map(int,input().split())))

for i in range(n-1):
  for j in range(i+1,n):
    if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
      ranks[i] += 1
    elif body[i][0] > body[j][0] and body[i][1] > body[j][1]:
      ranks[j] += 1
print(*ranks)