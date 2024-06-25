nums = list(map(int, input().split()))

if nums[0] == 1:
  temp = 0
  for num in nums:
    if nums[num-1] == num:
      temp += 1
      continue
    else:
      print('mixed')
      break
  if temp == 8:
    print('ascending')
elif nums[0] == 8:
  temp = 0
  for num in nums:
    if nums[num-1] == (9-num):
      temp += 1
      continue
    else:
      print('mixed')
      break
  if temp == 8:
    print('descending')
else:
  print('mixed')