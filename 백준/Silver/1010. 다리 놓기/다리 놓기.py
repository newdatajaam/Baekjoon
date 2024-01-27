test_case = int(input())

for _ in range(test_case):
  left, right = map(int, input().split())
  temp = right - left

  r_fac, l_fac, minus_fac = 1,1,1
  for i in range(right,0,-1):
    r_fac *= i
  for j in range(left,0,-1):
    l_fac *= j
  for k in range(temp,0,-1):
    minus_fac *= k

  ans = r_fac / (l_fac * minus_fac)

  print(int(ans))