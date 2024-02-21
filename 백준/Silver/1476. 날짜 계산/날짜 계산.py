E, S, M = map(int, input().split())
n = 1

if E == 15: E = 0
if S == 28: S = 0
if M == 19: M = 0

while True: 
  if n % 15 == E and n % 28 == S and n % 19 == M:
    print(n)
    break
  else:
    n += 1