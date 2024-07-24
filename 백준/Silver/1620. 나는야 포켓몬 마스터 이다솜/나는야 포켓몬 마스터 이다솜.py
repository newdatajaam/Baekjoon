import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
  pokemon[str(i)] = input().rstrip()
  pokemon[pokemon[str(i)]] = i

ans = []
for _ in range(M):
  quiz = str(input().rstrip())
  ans.append(pokemon[quiz])

for a in ans:
  print(a)