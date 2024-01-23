s, e = map(int, input().split())

num_str = ''
num_list = []
i = 1
while True:
  for _ in range(i):
    num_list.append(i)
  if len(num_list) >= e:
    break 
  else:
    i += 1

num_sum = 0
for j in range(s-1, e, 1):
  num_sum += int(num_list[j])

print(num_sum)