missing = []
while True:
  student = int(input())
  stu_list = []
  if student == 0:
    break
  else:
    for _ in range(student):
      name = input()
      stu_list.append([name])

    for _ in range(student*2-1):
      num, AB = input().split()
      stu_list[int(num)-1].append(AB)

    for info in stu_list:
      if len(info) == 2:
        missing.append(info[0])

for idx, name in enumerate(missing):
  print(idx+1, name)