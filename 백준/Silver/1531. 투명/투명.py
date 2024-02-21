n, m = map(int, input().split())

picture = [] 
for i in range(100):
  picture.append([0]*100)

cnt = 0

for _ in range(n):
  x1, y1, x2, y2 = map(int, input().split())
  for row in range(x1-1, x2):
    for col in range(y1-1, y2):
      picture[row][col] += 1

for row in range(100):
  for col in range(100):
    if picture[row][col] > m:
      cnt+=1
print(cnt)