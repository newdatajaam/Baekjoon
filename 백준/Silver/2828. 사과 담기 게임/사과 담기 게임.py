n, m = map(int, input().split())
tot_apple = int(input())
bucket = [1, m]
total_move = 0

for i in range(tot_apple):
  pos = int(input())
  if bucket[0] <= pos <= bucket[1]:
    move = 0
  elif pos < bucket[0]:
    move = (bucket[0] - pos)
    bucket[0] -= move
    bucket[1] -= move  
  elif pos > bucket[1]:
    move = (pos - bucket[1])
    bucket[0] += move
    bucket[1] += move
  total_move += move

print(total_move)