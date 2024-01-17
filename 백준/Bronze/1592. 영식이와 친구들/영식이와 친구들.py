n, m, l = map(int,input().split())

member = [0]*n

i = 0
cnt = 0

while True:
  member[i] += 1

  if member[i] == m:
    break

  if member[i] % 2 == 1:
    i += l
    if i >= n:
      i -= n
  elif member[i] % 2 == 0:
    i -= l
    if i < 0:
        i += n
  cnt += 1

print(cnt)