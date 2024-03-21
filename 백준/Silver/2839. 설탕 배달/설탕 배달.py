n_kilo = int(input())
ans = []

if n_kilo == 4 or n_kilo == 7:
  ans.append(-1)
else:
  for i in range(5):
    cal = n_kilo - (3 * i)
    if cal % 5 == 0:
      j = cal // 5
      ans.append(i + j)
print(min(ans))