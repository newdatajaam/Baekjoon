a, k = map(int, input().split())

dq = []
dq.append([k,0])

while dq:
  now, level = dq.pop()
  if now == a:
    print(level)
    break

  if now % 2 == 0:
    if now / 2 < a:
      dq.append([now-1, level+1])
    else:
      dq.append([int(now/2), level+1])
  else:
    dq.append([now-1, level+1])