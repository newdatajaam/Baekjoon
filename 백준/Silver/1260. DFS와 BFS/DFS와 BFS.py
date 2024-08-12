from collections import deque

max_num, lines, start = map(int, input().split())
relations = [[] for _ in range(max_num)]

# 관계 정리 및 정렬
for _ in range(lines):
  a, b = map(int, input().split())
  relations[a-1].append(b)
  relations[b-1].append(a)

for rel in relations:
  rel.sort()

# dfs
def dfs(st):
  stack = [st]
  visited = []

  while stack:
    v = stack.pop()
    if v not in visited:
      visited.append(v)
      stack.extend(reversed(relations[v-1]))
  print(*visited)

# bfs
def bfs(st):
  queue = [st]
  visited = []

  while queue:
    v = queue.pop(0)
    if v not in visited:
      visited.append(v)
      queue.extend(relations[v-1])
  print(*visited)

dfs(start)
bfs(start)