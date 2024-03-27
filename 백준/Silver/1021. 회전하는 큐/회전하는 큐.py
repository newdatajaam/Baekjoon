n, m = map(int, input().split())
num_list = [i for i in range(1,n+1)]
select_list = list(map(int, input().split()))

cnt = 0
for finding in select_list:
  if num_list[0] == finding:
    num_list.pop(0)
  else:
    position = num_list.index(finding)
    temp1, temp2 = position, len(num_list)-(position+1)
    #print(temp1, temp2)
    if temp1 <= temp2:
      cnt += (temp1)
      num_list = num_list[position+1:] + num_list[:position]
      #print(num_list)
    else:
      cnt += (temp2+1)
      num_list = num_list[position+1:] + num_list[:position]
      #print(num_list)
print(cnt) 