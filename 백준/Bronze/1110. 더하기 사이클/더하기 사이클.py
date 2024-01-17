num = first_num = input()
cnt = 0

while True:
  if int(num) < 10:
    num = num[-1]*2
    cnt += 1
  else:
    temp = str(int(num[0])+int(num[1]))
    num = num[1]+ temp[-1]
    cnt += 1

  if int(num) == int(first_num):
    break

print(cnt)