bird = int(input())
total_sec = 0
bird_cnt = 0
sec = 1

while True:
  if bird_cnt == bird:
    break
  if bird_cnt + sec <= bird:
    bird_cnt += sec
    sec += 1
    total_sec += 1
  else:
    sec = 1

print(total_sec)