n, l, d = map(int, input().split())

time = l
bell = d

for i in range(1,n+1):   # 노래 곡 수 만큼 돌아
  if bell >= time-l and bell < time:
    while bell < time:
      bell += d
    time += 5+l
  elif bell >= time and bell < time+5:
    break
  else:
    time += 5+l
print(bell)