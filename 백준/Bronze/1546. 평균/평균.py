n = int(input())
scores = list(map(int, input().split()))

max_sc = max(scores)

for i in range(len(scores)):
  scores[i] = scores[i] / max_sc * 100

print(sum(scores)/len(scores))