s1,s2,s3 = map(int,input().split())
dice_list = []

for i in range(1,s1+1):
  for j in range(1, s2+1):
    for k in range(1,s3+1):
      dice_list.append(i+j+k)

max_count = 0
max_num = dice_list[-1]
num_list = list(set(dice_list))
num_list.reverse()

for num in num_list:
  if dice_list.count(num) >= max_count:
    max_count = dice_list.count(num)
    if num < max_num:
      max_num = num

print(max_num)