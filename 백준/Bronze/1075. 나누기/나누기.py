number_N = input()
divide_F = input()

min_num = number_N[0:-2] + "00"
max_num = number_N[0:-2] + "99"

for num in range(int(min_num),int(max_num)+1):
  if num % int(divide_F) == 0:
    str_num = str(num)
    print(str_num[-2]+str_num[-1])
    break
  else: 
    pass