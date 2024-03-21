test = int(input())
for i in range(test):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = (x1-x2)**2 + (y1-y2)**2

  # 무한 경우의 수
  if x1 == x2 and y1 == y2 and r1 == r2:
    print(-1)
  # 외접하는 경우 or 내접하는 경우
  elif distance > (r1+r2)**2 or distance < (r1-r2)**2:
    print(0)
  elif distance == (r1+r2)**2 or distance == (r1-r2)**2 : 
    print(1)
  elif distance < (r1+r2)**2 or distance > (r1-r2)**2:
    print(2)