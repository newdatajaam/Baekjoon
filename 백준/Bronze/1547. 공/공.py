times = int(input())
ball = 1

for i in range(times):
  num1, num2 = map(int, input().split())
  if num1 == ball:
    ball = num2
  elif num2 == ball:
    ball = num1

print(ball)