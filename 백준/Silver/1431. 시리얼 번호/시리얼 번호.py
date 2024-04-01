testcase = int(input())
serial_dict = {}
for _ in range(testcase):
  numbers = input()
  len_num = len(numbers)
  sum_num = 0
  for i in numbers:
    if i.isdigit():
      sum_num += int(i)
  
  serial_dict[numbers] = [len_num, sum_num]

answer = sorted(serial_dict.items(), key = lambda item: [item[1][0],item[1][1],item[0]])

for key, value in answer:
  print(key)