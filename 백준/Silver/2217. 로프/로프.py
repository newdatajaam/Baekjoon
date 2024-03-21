# 2217번 로프
import sys
N = int(input())
rope = []
for i in range(N):
  rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)
max_w = 0

for k in range(len(rope)):
  temp =rope[k] * (k+1)
  if temp >= max_w:
    max_w = temp

print(max_w)