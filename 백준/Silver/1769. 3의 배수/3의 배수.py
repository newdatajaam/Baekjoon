num = input()
cnt = 0
while len(num) > 1:
  temp = 0
  for i in range(len(num)):
    temp += int(num[i])
  num = str(temp)
  cnt += 1
print(cnt)

if int(num) % 3 == 0:
  print('YES')
else:
  print('NO')