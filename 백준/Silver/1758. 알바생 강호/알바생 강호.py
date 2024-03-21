N = int(input())
tip = sorted([int(input()) for _ in range(N) ], reverse=True)
sum = 0

for i in range(len(tip)):
  temp = tip[i] - i
  if temp >= 0:
    sum += temp
  else:
    break
print(sum)