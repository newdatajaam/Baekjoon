n, m = map(int, input().split())

if n > 2:
  if m > 5: # 오른쪽이 더 적게 가야할 경우 : 최소 위로 2칸은 있어야 함
    res = m - 6 + 4 # 최소조건 -6칸+4번 / 나머지 칸 = 횟수
    print(res)
  elif m == 5: # 최소조건 불가능 = 결과가 5이상 나오면 안됨
    print(4)
  elif m < 5: # 그 외에는 m칸 = m번
    print(m)
elif n == 2: # 위로 1칸 밖에 못움직여서 오른쪽을 무조건 2칸씩
  if m % 2 == 1:
    res = m//2+1
  else:
    res = m//2
  if res > 4:
    print(4)
  else:
    print(res)
elif n == 1:
  print(1)  # 처음 칸 밖에 안됨