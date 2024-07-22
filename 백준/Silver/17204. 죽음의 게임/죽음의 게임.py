n, k = map(int, input().split())
game = {}

for i in range(n):
  game[i] = int(input())

path = []
cnt = 0 
pick = 0
while k not in path:
  path.append(pick)
  pick = game[pick]
  cnt += 1

  if cnt > n:
    cnt = 0
    break

print(cnt-1)