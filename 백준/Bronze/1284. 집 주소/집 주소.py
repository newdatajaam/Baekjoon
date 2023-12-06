while True:
  # 변수 입력
  address = input()
  length = 0
  if address == '0':
    break
  else:
    # 각 숫자별 길이
    for i in range(len(address)):
      if address[i] == '1':
        length += 2
      elif address[i] == '0':
        length += 4
      else:
        length += 3

    # 숫자간 간격 길이 + 양 옆
    length = length + (len(address)-1) + 2

    print(length)