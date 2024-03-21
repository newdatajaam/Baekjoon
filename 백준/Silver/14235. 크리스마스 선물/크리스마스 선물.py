n = int(input())
present = []
for _ in range(n):
  a, *a_list = map(int, input().split())
  if a == 0:
    if len(present) == 0:
      print(-1)
    else:
      res = present.pop(0)
      print(res)
  else:
    present.extend(a_list)
    present.sort(reverse=True)