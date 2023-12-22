N, m, M, T, R = map(int,input().split())

excercise_T = 0          
min_T = 0

X = m               # 영식이의 초기 맥박


while excercise_T < N: 
  if m + T > M:
    min_T = -1
    break   
  if X + T <= M:
    X += T
    excercise_T += 1
    min_T += 1
  else:
    X -= R
    min_T += 1
    if X < m:
      X = m

print(min_T)