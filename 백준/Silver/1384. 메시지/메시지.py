answer = []

while True:
  people_num = int(input())
  name_list = []
  result_list = []
  nasty_list = []

  if people_num == 0:
    break
  else:
    for _ in range(people_num):
      name, *result = input().split()
      name_list.append(name)
      result_list.append(result)
    
    for idx1, each_list in enumerate(result_list):
      for idx2, message in enumerate(each_list):
        if message == 'N':
          nasty_list.append([name_list[idx1], name_list[idx1-(idx2+1)]])
    answer.append(nasty_list)

for idx, group in enumerate(answer):
  print(f"Group {idx+1}")
  if group == []:
    print("Nobody was nasty")
  else:
    for name in group:
      print(f"{name[1]} was nasty about {name[0]}")
  print()