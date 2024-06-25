# 2562번
max_num = 0
loc = 0
for i in range(9):
  num = int(input())
  if num > max_num:
    max_num = num
    loc = i+1
print(max_num)
print(loc)