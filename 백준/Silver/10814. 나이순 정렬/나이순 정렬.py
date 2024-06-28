import sys
input = sys.stdin.readline
member = []

n = int(input())
for i in range(n):
  a, b = map(str, input().split())
  member.append([int(a), b])

member.sort(key= lambda x: x[0])

for x in member:
  key, value = x
  print(key, value)