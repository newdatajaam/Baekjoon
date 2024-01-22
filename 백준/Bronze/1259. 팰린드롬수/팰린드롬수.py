while True:
  num = int(input())
  num = str(num)
  if num == '0':
    break

  if len(num) == 1:
    answer = 'yes'
  else:
    for i in range(int(len(num)/2)):
      if num[i] == num[len(num)-i-1]:
        answer = 'yes'
      else:
        answer = 'no'
        break

  print(answer)