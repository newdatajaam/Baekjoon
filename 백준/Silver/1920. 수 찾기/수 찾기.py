n = int(input())
num_list = list(map(int,input().split()))
dict_list = {}
for i in num_list:
  dict_list[i] = 1

m = int(input())
find_num = list(map(int,input().split()))

for num in find_num:
  if num in dict_list:
    print(dict_list[num])
  else:
    print(0)